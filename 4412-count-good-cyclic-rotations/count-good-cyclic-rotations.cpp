class Solution {
public:
    int countGoodRotations(vector<int>& nums) {
        int n = nums.size();
        long long left = accumulate(nums.begin(), nums.begin() + (n / 2), 0LL);
        long long right = accumulate(nums.begin() + (n / 2), nums.end(), 0LL);
        int mid = n / 2;
        int good = 0;
        int l = 0, r = n - 1;

        for(int i = 0; i < n; i++)
            {
                if(left > right)
                    good++;
                left -= nums[l], right += nums[l];
                left += nums[mid];
                right -= nums[mid];
                r--;
                l++;
                mid = (mid +1) % n;
            }
            return good;
    }
};