#include <iostream>
#include <string>
#include <unordered_map>
#include <fstream>
#include <sstream>

// global maps (bad design?)
std::unordered_map<std::string, std::string> comp;
std::unordered_map<std::string, std::string> dest;
std::unordered_map<std::string, std::string> jump;

std::unordered_map<std::string, int> symbols;

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



void next_command(std::ifstream& infile) {
    std::string line;
    while (std::getline(infile, line)) {
        // Process the line (for now, just print it)
        std::cout << line << std::endl;
    }
}

// void first_pass(char* inputs, int pc){

// }

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

    int pc = -1;

    std::string input_file = argv[1];
    std::ifstream infile(input_file);

    if (!infile.is_open()) {
        std::cerr << "Error opening file: " << input_file << std::endl;
        return 1;
    }
    
    
    next_command(infile);
    infile.close();
    return 0;
}
