class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int left = 0, right = 0;
        vector<int> arr;

        while (left < nums1.size() && right < nums2.size()) {
            if (nums1[left] <= nums2[right]) {
                arr.push_back(nums1[left]);
                left++;
            } else {
                arr.push_back(nums2[right]);
                right++;
            }
        }

        while (left < nums1.size()) {
            arr.push_back(nums1[left]);
            left++;
        }

         while (right < nums2.size()) {
            arr.push_back(nums2[right]);
            right++;
        }

        int nearMid = arr.size() / 2;
        if (arr.size() % 2 == 0) {
            return (double)(arr[nearMid-1] + arr[nearMid]) / 2;
        } else {
            return (double)arr[nearMid];
        }
    }
};