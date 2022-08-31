'''Let's call a sequence of integers x1,x2,…,xk MEX-correct if for all i (1≤i≤k) |xi−MEX(x1,x2,…,xi)|≤1 holds. Where MEX(x1,…,xk) is the minimum non-negative integer that doesn't belong to the set x1,…,xk. For example, MEX(1,0,1,3)=2 and MEX(2,1,5)=0.

You are given an array a consisting of n non-negative integers. Calculate the number of non-empty MEX-correct subsequences of a given array. The number of subsequences can be very large, so print it modulo 998244353.

Note: a subsequence of an array a is a sequence [ai1,ai2,…,aim] meeting the constraints 1≤i1<i2<⋯<im≤n. If two different ways to choose the sequence of indices [i1,i2,…,im] yield the same subsequence, the resulting subsequence should be counted twice (i. e. two subsequences are different if their sequences of indices [i1,i2,…,im] are not the same).

Input
The first line contains a single integer t (1≤t≤105) — the number of test cases.

The first line of each test case contains a single integer n (1≤n≤5⋅105).

The second line contains n integers a1,a2,…,an (0≤ai≤n).

The sum of n over all test cases doesn't exceed 5⋅105.

Output
For each test case, print a single integer — the number of non-empty MEX-correct subsequences of a given array, taken modulo 998244353.'''

# include <bits/stdc++.h>

using
namespace
std;
# define int long long

const
int
N = 5e5 + 5, MOD = 998244353;
int
n, a[N], dp[N * 2][2];

void
solve()
{
    cin >> n;
for (int i = 1; i <= n; ++i)
{
    cin >> a[i];
}
for (int i = 0; i <= n * 2; ++i) {
    dp[i][0] = dp[i][1] = 0;
}
dp[0][0] = 1;
for (int i = 1; i <= n; ++i) {
if (a[i] - 1 >= 0) {
(dp[a[i] - 1][1] += dp[a[i] - 1][0] + dp[a[i] - 1][1]) %= MOD;
}
(dp[a[i] + 1][0] += dp[a[i] + 1][0]) %= MOD;
(dp[a[i] + 1][1] += dp[a[i] + 1][1]) %= MOD;
// (dp[a[i] + 2][0] += dp[a[i]][1]) %= MOD;
(dp[a[i] + 1][0] += dp[a[i]][0]) %= MOD;
}
int res = -1;
for (int i = 0; i <= n; ++i) {
res = (res + dp[i][0] + dp[i][1]) % MOD;
// cerr << i << ' ' << dp[i][0] << ' ' << dp[i][1] << endl;
}
cout << res << endl;
}

signed
main()
{
    ios_base:: sync_with_stdio(0);
cin.tie(0);

int
tc;
cin >> tc;
while (tc - -) {
solve();
}

return 0;
}
