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
std::unordered_map<std::string, int> labels;

int pc;

//vector to store all commands
std::vector<std::string> commands;

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
            if(command[0] == '('){ // found label - there might be a better way than just looking at first char
                std::string label = std::regex_replace(command, labelFormat, "$1");
                labels[label] = pc; // store the pc for each label
            }else{
                commands.push_back(command);
                pc++;
            }
        }
    }   
}

std::string translate_A(std::string command){
    return "A";
}

std::string translate_R(std::string command){

    return "R";
}

std::string translate(std::string command){
    std::regex whitespaces("\\s+");
    command = std::regex_replace(command, whitespaces, "");

    if (command[0]=='@'){
        return translate_A(command);
    }else{
        return translate_R(command);
    }
}

void second_pass(std::ofstream& outfile){
    std::string binary_command;
    // somewhere, variable mem location needs to be change
    for (const std::string& command : commands){ //iterate through commands
        binary_command = translate(command);
        outfile << binary_command << std::endl; // write binary to output file
    }
}

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

    std::string output_file = input_file;
    size_t pos = output_file.find(".asm");
    if (pos != std::string::npos) {
        output_file.replace(pos, 4, ".hack");
    } else {
        output_file += ".hack";
    }
    std::ofstream outfile(output_file);
    
    first_pass(infile, pc);
    second_pass(outfile);

    infile.close();
    return 0;
}
