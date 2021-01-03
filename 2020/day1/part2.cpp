#include <bits/stdc++.h>

#define MAX_LENGTH 128000
 
uint64_t solve(std::vector<int> vec){
    //check list for occurs of item
    std::vector<bool>visited(2021, false);
  
    for(auto &v: vec){ 
        if(visited[v])
            std::cout << "hello";
        visited[v] = true;
    }
    uint64_t result = 1;
      
          
    for(int i=0; i<vec.size()-1; i++){
        for(int j=i+1; j<vec.size(); j++){
            if (vec[i]+vec[j] < 2020 && visited[2020-vec[i]-vec[j]] && visited[vec[i]] && visited[vec[j]]){
                result*=(vec[i]*vec[j]*(2020-vec[i]-vec[j]));
                visited[vec[i]] = false;
                visited[vec[j]] = false;
                visited[2020-vec[i]-vec[j]] = false;
            }
        }
     }
  
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
  
