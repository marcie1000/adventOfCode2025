#include <fstream>
#include <iostream>
#include <string>
#include <vector>

struct range {
    size_t min;
    size_t max;
};

size_t sumP1 { 0 };
size_t sumP2 { 0 };

std::vector<range> ranges;

std::string input { "" };

void readFile() {
    std::ifstream f { "input.txt" };
    std::string s { "" };

    while (std::getline(f, s)) {
        input = input + s;
    }
}

void parse() {
    size_t posStart { 0 }, posEnd { 0 };
    bool end { false };
    while (!end) {
        posEnd = input.find(",", posStart);
        std::string rangeString { input.substr (posStart, posEnd - posStart) };
        posStart = posEnd + 1;

        size_t posH { 0 }; // position of hyphen
        struct range r;
        posH = rangeString.find("-", 0);

        r.min = std::stoll(rangeString.substr(0, posH));
        r.max = std::stoll(rangeString.substr(posH + 1, std::string::npos));

        if(posEnd == std::string::npos){
            end = true;
        }

        ranges.push_back(r);
    }
}

void findInvalids(struct range r) {

    // iterate through numbers in range
    for (size_t i {r.min}; i <= r.max; i++) {

        std::string s { std::to_string(i) };

        // test if we have patterns that repeats 2 to size(s) times
        for (size_t times {2}; times <= std::size(s); times++) {

            if (std::size(s) % times != 0) {
                continue;
            }

            std::string sub { s.substr(0, std::size(s) / times) };

            std::string sToCompare { "" };
            for (size_t x = 0; x < times; x++) {
                sToCompare = sToCompare + sub;
            }

            if(s == sToCompare) {
                if(times == 2) {
                    sumP1 += i;
                }
                sumP2 += i;
                break;
            }
        }
    }
}

auto main(int argc, char *argv[]) -> int {

    readFile();
    parse();

    for(const auto r : ranges) {
        findInvalids(r);
    }

    std::cout << "Part 1: " << sumP1 << std::endl;
    std::cout << "Part 2: " << sumP2 << std::endl;

    return 0;
}
