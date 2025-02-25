#include <iostream>
#include <string>
#include <unordered_map>

std::unordered_map<std::string, int> symbolTable;

int main (int argc, char** argv){
    if (argc != 2) {
        std::cout << "usage: assembler prog.asm" << std::endl;

        char* input_file = argv[1];

        first_pass(input_file);
        

    }
}

void first_pass(char* inputs){

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