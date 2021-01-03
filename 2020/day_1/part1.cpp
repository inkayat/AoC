#include <bits/stdc++.h>

#define MAX_LENGTH 128000

// Part1
// solution in O(n) time-complexity & O(n) memory
uint64_t solve(std::vector<int> vec){
    const int target = 2020;
    std::vector<int> mmap(target+1, 0);
    uint64_t result = 1;

    //O(n)
    for(auto &v: vec)
        mmap[v] += 1;

    //O(n)
    for(int i=0; i<=target/2; i++)
        result *= std::pow(i*(target-i), std::min(mmap[i], mmap[target-i]));

    return result;
}


int main(int argc, char *argv[]){

    std::ifstream fin;
    std::vector<int> entries;

    fin.open("input.txt");

    while(fin) {

        std::string a; 
        std::getline(fin, a);
        
        try {
            entries.push_back(std::stoi(a));
        } catch(const std::exception& e) {
            std::cout << e.what() << std::endl;
        }

    }

    // Print the solution (result)
    std::cout << solve(entries) << std::endl;

    return 0;
}


