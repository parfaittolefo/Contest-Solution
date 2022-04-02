#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{

    int n,cA=0,cB=0;

    vector<char> l = {'A'};
    cin>>n;

    for(int i=0; i<n; i++)
    {
        cA=count(l.begin(), l.end(),'A');
        cB=count(l.begin(), l.end(),'B');
        l.clear();
        for(int j=0; j<cA; j++)
        {
            l.push_back('B');
        }
        for(int j=0; j<cB; j++)
        {
            l.push_back('A');
            l.push_back('B');
        }

    }

cA=count(l.begin(), l.end(),'A');
cB=count(l.begin(), l.end(),'B');
cout <<cA<<" "<<cB;
    return 0;
}
