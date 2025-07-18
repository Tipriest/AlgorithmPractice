#include <algorithm>
#include <iostream>
#include <limits.h>
#include <math.h>
#include <unordered_set>
#include <vector>
using namespace std;
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};
class Solution {
public:
  long long minCost(int m, int n, vector<vector<int>> &waitCost) {
    vector<vector<int>> dp(m, vector<int>(n, 0));
    dp[0][0] = 1;
    for (int j = 1; j < n; j++) {
      dp[0][j] = dp[0][j - 1] + waitCost[0][j - 1] + 1 * (j + 1);
    }
    for (int i = 1; i < m; i++) {
      dp[i][0] = dp[i - 1][0] + waitCost[i - 1][0] + (i + 1) * 1;
    }
    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        dp[i][j] = min(dp[i - 1][j] + waitCost[i - 1][j] + (i + 1) * (j + 1),
                       dp[i][j - 1] + waitCost[i][j - 1] + (i + 1) * (j + 1));
      }
    }
    return dp[m - 1][n - 1] - waitCost[0][0];
  }
};
int main() {
  // 示例二叉树
  Solution solution;
  vector<vector<int>> nums = {{6, 1, 4}, {3, 2, 5}};
  long long result = solution.minCost(2, 3, nums);
  std::cout << "result: " << result << std::endl;
}