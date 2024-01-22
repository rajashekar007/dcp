#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int lengthLongestSubstringKUnique(string &s, int k) {
  int cnt[256] = {};
  int n = s.length();
  int left = 0, right = 0;
  int unique_cnt = 0;
  int max_len = 0;
  while(right < n) {
    if(cnt[s[right]] == 0) {
      unique_cnt++;
    }
    cnt[s[right]]++;
    while(unique_cnt>k && left<=right){
      cnt[s[left]]--;
      if(cnt[s[left]] == 0){
        unique_cnt--;
      }
      left++;
    }
    max_len = max(max_len, right - left + 1);
    right++;
  } 
  return max_len;
}


int main() {
  string s = "abcba";
  cout<<lengthLongestSubstringKUnique(s, 2);
  return 0;
}