CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra
TARGET = Assembler

all: $(TARGET)

$(TARGET): assembler.o
	$(CXX) $(CXXFLAGS) -o $(TARGET) assembler.o

assembler.o: assembler.cpp
	$(CXX) $(CXXFLAGS) -c assembler.cpp

clean:
	rm -f *.o $(TARGET)