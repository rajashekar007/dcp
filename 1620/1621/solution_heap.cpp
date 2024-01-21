#include <queue>
#include <vector>
#include <unordered_set>
#include <iostream>
#include <initializer_list>

using namespace std;


vector<int> generateRegularNumbers(int n) {
  vector<int> regularNumbers;
  unordered_set<int> seen;
  priority_queue<int, vector<int>, std::greater<int> > minHeap;
  minHeap.push(1);
  seen.insert(1);

  while(regularNumbers.size() < n) {
    int cur = minHeap.top();
    minHeap.pop();
    regularNumbers.push_back(cur);
    for(auto f : {2, 3, 5}){
      int newf = cur * f;
      if(seen.find(newf) == seen.end()){
        minHeap.push(newf);
        seen.insert(newf);
      }
    }
  }
  return regularNumbers;
}


int main() {
  int n;
  cin>>n;
  vector<int> rn = generateRegularNumbers(n);
  for(auto e : rn){
    cout<<e<<", ";
  }
  cout<<endl;
  return 0;
}