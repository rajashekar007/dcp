#include <iostream>
using namespace std;

struct ll {
  int val;
  ll* next;
  ll(int v) : val(v), next(nullptr) {}
};

ll* add(ll *a, ll *b) {
  int carry = 0;
  ll *an = a;
  ll *bn = b;
  ll *res = nullptr, *ans = new ll(0);
  while(an || bn || carry) {
    int sum = carry;
    if(an) {
      sum += an->val;
      an = an->next;
    }
    if(bn) {
      sum += bn->val;
      bn = bn->next;
    }
    carry = sum/10;
    sum = sum % 10;
    ans->next = new ll(sum);
    ans = ans->next;
    if(res == nullptr) {
      res = ans;
    }
  }
  return res;
}

int main() {
  ll *a;
  a = new ll(9);
  a->next = new ll(9);
  ll *b;
  b = new ll(5);
  b->next = new ll(2);
  ll *res = add(a, b);
  while(res) {
    cout<<res->val;
    res = res->next;
  }
  return 0;
}