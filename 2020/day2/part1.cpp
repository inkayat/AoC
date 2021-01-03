#include <bits/stdc++.h>

bool validate_password(int _min, int _max, char ch, std::string text){
    int freq = 0;
    int i = 0;
    while(i < text.length()){
        if(text[i]==ch)
            freq++;
        if (freq>_max)
            return false;
        i++;
    }
    return freq>=_min;
}

int solve(std::vector<std::string> vec) {
    int valid_password = 0;
    int result = 0;
    for(int i=0; i<vec.size(); i++){
        int x = vec[i].find('-');
        int y = vec[i].find(':');
        int _min = std::stoi(vec[i].substr(0, x));
        int _max = std::stoi(vec[i].substr(x+1, y-2));
        char ch = vec[i].at(y-1);
        std::string ss = vec[i].substr(y+2, vec[i].length());
        if(validate_password(_min, _max, ch, ss))
            result++;
    }
    return result; 
}

int main(int argc, char *argv[]){
    std::ifstream file("input.txt");
    std::vector<std::string> ss;
    std::string s;
    while(std::getline(file, s))
        ss.push_back(s);
    
    std::cout << solve(ss) << std::endl;
}
