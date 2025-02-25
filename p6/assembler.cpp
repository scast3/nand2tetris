#include <iostream>
#include <string>
#include <unordered_map>
#include <fstream>
#include <sstream>

std::unordered_map<std::string, std::string> comp;
std::unordered_map<std::string, std::string> dest;
std::unordered_map<std::string, std::string> jump;

void load_map(const std::string& filename, std::unordered_map<std::string, std::string>& comp) {
    std::ifstream infile(filename);
    std::string line;

    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        std::string key, value;

        if (std::getline(iss, key, ',') && std::getline(iss, value)) {
            comp[key] = value;
        }
    }

    infile.close();
}

int main (int argc, char** argv){

    if (argc != 2) {
        std::cout << "usage: assembler prog.asm" << std::endl;
    }
    load_map("comp.txt", comp);
    load_map("dest.txt", dest);
    load_map("jump.txt", jump);

    int pc = -1;

    char* input_file = argv[1];

    first_pass(input_file, pc);

}

void first_pass(char* inputs, int pc){

}

void second_pass(){
    
}

void next_command(){

}

void translate(){

}

void translate_A(){

}

void translate_B(){

}