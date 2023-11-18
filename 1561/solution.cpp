#include <iostream>
using namespace std;

struct node {
  int val;
  node *left;
  node *right;
  node(v) : val(v), left(NULL), right(NULL) {}
}

void bfs(node *root, vector<int> &level_order, int cur_level) {
  
}

void solve() {
  node *root;
  int max_level = height(root);
  vector<int> level_order[max_level];
  int cur_level;
  queue<node*> q;
  q.push(root);
  while(q.size()){
    node *n = q.pop();
    if(n->left) q.push(n->left);
    if(n->right) q.push(q->right);
    if(n!=root) cout<<", ";
    cout<<n->val;
  }
  cout<<endl;
}

int main() {
  solve();
  return 0;
}