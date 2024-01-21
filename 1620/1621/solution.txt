#include <iostream>
using namespace std;

bool is_regular(int n) {
  while(n%2 == 0) n/=2;
  while(n%3 == 0) n/=3;
  while(n%5 == 0) n/=5;
  return n==1;
}

vector<int> n_regular_numbers(int n){
  vector<int> rn;
  int cur = 2;
  while(rn.size() < n) {
    if(is_regular(cur)){
      rn.push_back(cur);
    }
    cur++;
  }
  return rn;
}


int main() {
  int n;
  cin>>n;
  vector<int> rn = n_regular_numbers(n);
  for(auto e : rn){
    cout<<e<<", ";
  }
  cout<<endl;
  return 0;
}