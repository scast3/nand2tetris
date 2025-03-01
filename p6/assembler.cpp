#include <iostream>
#include <string>
#include <unordered_map>
#include <fstream>
#include <sstream>
#include <regex>

// global maps (bad design?)
std::unordered_map<std::string, std::string> comp;
std::unordered_map<std::string, std::string> dest;
std::unordered_map<std::string, std::string> jump;

std::unordered_map<std::string, int> symbols;

int pc;

// load maps from the textfile
void load_map(const std::string& filename, std::unordered_map<std::string, std::string>& my_map) {
    std::ifstream infile(filename);
    std::string line;

    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        std::string key, value;

        if (std::getline(iss, key, ',') && std::getline(iss, value)) {
            my_map[key] = value;
        }
    }

    infile.close();
}

std::string next_command(std::ifstream& infile) {
    std::string line;
    std::regex comments("//.*");
    std::regex whitespaces("\\s+");

    if (std::getline(infile, line)){
        line = std::regex_replace(line, comments, "");
        line = std::regex_replace(line, whitespaces, "");
        return line;
    }return "~"; //EOF marker - might need to change????

    // use this to test
    // while (std::getline(infile, line)) {
    //     line = std::regex_replace(line, comments, "");
    //     line = std::regex_replace(line, whitespaces, "");
    //     // Process the line (for now, just print it)
    //     std::cout << line << std::endl;
    // }
}

void first_pass(std::ifstream& infile, int& pc){
    pc = 0;
    std::string command;
    std::regex labelFormat("^\\((.*)\\)$");
    for (;;){
        command = next_command(infile);
        if (command == "~") break; // break if file end
        
        if (!(command == "")){
            if(command[0] == '('){ // found label
                std::string label = std::regex_replace(command, labelFormat, "$1");
                symbols[label] = pc; // store the pc for each label
            }else{
                std::cout << "PC: "  << pc << ", Command: " << command << std::endl;
                pc++;
            }
        }
    }   

}

// void second_pass(){
    
// }

// void translate(){

// }

// void translate_A(){

// }

// void translate_R(){

// }


// input will be in the format: ./Assembler <filename.asm>

int main (int argc, char** argv){

    if (argc != 2) {
        std::cout << "usage: assembler prog.asm" << std::endl;
    }
    load_map("comp.txt", comp);
    load_map("dest.txt", dest);
    load_map("jump.txt", jump);

    std::string input_file = argv[1];
    std::ifstream infile(input_file);

    if (!infile.is_open()) {
        std::cerr << "Error opening file: " << input_file << std::endl;
        return 1;
    }
    
    
    first_pass(infile, pc);
    infile.close();
    return 0;
}
