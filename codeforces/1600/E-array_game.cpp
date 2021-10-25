#include <bits/stdc++.h>
using namespace std;
# define ll long long 
# define ar array
const int mxN = 2e5;
int n, nums[mxN] = {0};

int main(){
    // ios_base::sync_with_stdio(false);

    cin >> n;

    for (int i = 0; i < n; i++)
        cin >> nums[i];

    int l = 0, r = n - 1, last = -1;
    bool player = 1;

    while (l <= r)
    {
        if (r == l) {
            cout << ((player) ? "Alice" : "Bob");
            break;
        }
        if (nums[l] >= nums[r] && nums[l] > last) {
            int i = l+1;
            while (i <= r && nums[i] > nums[i-1]) {
                i++;
            }
            if ((i-l) & 1 ) { // we won or this is the only move
                cout << ((player) ? "Alice" : "Bob");
                break;
            }else if (nums[r] <= last) {
                cout << ((!player) ? "Alice" : "Bob");
                break;
            }
            last = nums[r];
            r--;
        }else if (nums[r] > last) {
            int i = r - 1;
            while (i >= 0 && nums[i] > nums[i+1]) {
                i--;
            }
            if ((r - i) & 1 )
            { // we won or this is the only move
                cout << ((player) ? "Alice" : "Bob");
                break;
            }else if (nums[l] <= last) {
                cout << ((!player) ? "Alice" : "Bob");
                break;
            }
            last = nums[l];
            l++;
        }
        else
        {
            cout << ((!player) ? "Alice" : "Bob");
            break;
        }
        
        player = !player;
    }


    return 0;
}
