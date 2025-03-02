/*
Author: Santiago Castillo
Date: 3/1/2025
Course: CSCI410
Description: Created an assembler for translating hack assembly to binary
Note: Regular expressions are a pain in the ass
*/

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

// load maps from the textfile
void load_map2(const std::string& filename, std::unordered_map<std::string, int>& my_map) {
    std::ifstream infile(filename);
    std::string line;

    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        std::string key;
        int value;

        if (std::getline(iss, key, ',') && iss >> value) {
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
                symbols[label] = pc; // store the pc for each label
            }else{
                commands.push_back(command);
                pc++;
            }
        }
    }   
}

std::string translate_A(std::string command, int& ramAddr){
    std::regex a_command("^@(.+)$");
    std::smatch match;
    std::regex_match(command, match, a_command);
    std::string value = match[1];
    std::string a_header = "0";

    try { // value is int
        int intValue = std::stoi(value);  // Try to convert it to an integer
        std::string binary_value = std::bitset<15>(intValue).to_string(); // convert to binary
        return a_header + binary_value; // a instructions start with 0
    } catch (const std::invalid_argument& e) { // value is string
        if (symbols.find(value) != symbols.end()){ // if the string is in symbols
            int mem_val = symbols[value]; // extract mem value from symbol
            std::string binary_value = std::bitset<15>(mem_val).to_string();
            return a_header + binary_value;
        }else{ // if not in symbols, need to add it in memory
            symbols[value] = ramAddr;
            std::string binary_value = std::bitset<15>(ramAddr).to_string();
            ramAddr++;
            return a_header + binary_value;
        } 
    }

}

std::string translate_C(std::string command, int& ramAddr){
    std::string b_header = "111";
    std::regex c_pattern(R"(^([A-Z]+)?=?\s*([A-Za-z0-9+\-*/&|!<>=\s]+)(?:;\s*([JGT|JEQ|JGE|JLT|JNE|JLE|JMP]+))?$)");
    // std::regex c_pattern(R"(^((?:[ADM]{1,3})?)=?(.*?);?((?:JGT|JEQ|JGE|JLT|JNE|JLE|JMP)?)$)");
    std::smatch match;

    std::regex_match(command, match, c_pattern);
    std::string dest_str = match[1].str();  // First captured group (dest)
    std::string comp_str = match[2].str();  // Second captured group (comp)
    std::string jump_str = match[3].str();  // Third captured group (jump)

    if (dest_str.empty()) dest_str = "null";
    if (comp_str.empty()) comp_str = "null";
    if (jump_str.empty()) jump_str = "null";

    // search for appropriate binary in tables
    std::string dest_binary = dest[dest_str];
    std::string comp_binary = comp[comp_str];
    std::string jump_binary = jump[jump_str];

    // Use for debugging C commands
    // std::cout << "command: " << command << std::endl;
    // std::cout << "dest string: " << dest_str << " dest binary: " << dest_binary << std::endl;
    // std::cout << "comp string: " << comp_str << " comp binary: " << comp_binary << std::endl;
    // std::cout << "jump string: " << jump_str << " jump binary: " << jump_binary << "\n" << std::endl;

    return b_header+comp_binary+dest_binary+jump_binary;
}

std::string translate(std::string command, int& ramAddr){
    std::regex whitespaces("\\s+");
    command = std::regex_replace(command, whitespaces, "");

    if (command[0]=='@'){
        return translate_A(command, ramAddr);
    }else{
        return translate_C(command, ramAddr);
    }
}

void second_pass(std::ofstream& outfile){
    std::string binary_command;
    // variable mem location needs to start at 16
    int ramAddr = 16;
    for (const std::string& command : commands){ //iterate through commands
        binary_command = translate(command, ramAddr);
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
    load_map2("symbols.txt", symbols);

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
    outfile.close();
    return 0;
}
