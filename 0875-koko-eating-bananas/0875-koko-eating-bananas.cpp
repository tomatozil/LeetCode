#include <cmath>
#include <algorithm>

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(), piles.end());

        while (l < r) {
            int m = (l + r) / 2;
            if (total(piles, m) <= h){
                r = m;
            } else {
                l = m + 1;
            }
        }

        return l;
    }

    int total(vector<int>& piles, int k) { // k가 커질 수록 total이 작아짐
        int ret = 0;
        for (auto i: piles) {
            ret += ceil((double)i/k);
        }
        return ret;
    }
};