#include <iostream>
using namespace std;

int64_t nth_sevenish_number(int n){
  int64_t ans = 0;
  int pos = 0;
  while(n) {
    int bit = n&1;
    ans += pow(7, pos) * bit;
    pos++;
    n >>= 1;
  }
  return ans;
}


int main(){
  int n;
  cin>>n;
  cout << nth_sevenish_number(n);
}