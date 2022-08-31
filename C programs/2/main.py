'''Monocarp wrote down two numbers on a whiteboard. Both numbers follow a specific format: a positive integer x with p zeros appended to its end.

Now Monocarp asks you to compare these two numbers. Can you help him?

Input
The first line contains a single integer t (1≤t≤104) — the number of testcases.

The first line of each testcase contains two integers x1 and p1 (1≤x1≤106;0≤p1≤106) — the description of the first number.

The second line of each testcase contains two integers x2 and p2 (1≤x2≤106;0≤p2≤106) — the description of the second number.

Output
For each testcase print the result of the comparison of the given two numbers. If the first number is smaller than the second one, print '<'. If the first number is greater than the second one, print '>'. If they are equal, print '='.'''

# include<bits/stdc++.h>
using
namespace
std;

# define ll long long
# define all(x) x.begin(),x.end()
# define endl "\n";
# define ss(x) x.size()

void
solve()
{
    int
p1, p2;
string
x1, x2;
cin >> x1 >> p1 >> x2 >> p2;
if (x1.size() + p1 > x2.size() + p2)
cout << ">";
else if (x1.size() + p1 < x2.size() + p2) cout << "<";
else {
int mx = max(ss(x1), ss(x2));
for (int i=ss(x1);i <= mx;i++) x1 += "0";
for (int i=ss(x2);i <= mx;i++) x2 += "0";
if (x1 > x2) cout << ">";
else if (x1 < x2) cout << "<";
else cout << "=";
}

}

int
main()
{
    ios_base:: sync_with_stdio(false);
cin.tie(NULL);
int
t = 1;
cin >> t;
while (t - -){
solve();
cout << endl;
}
return 0;
}