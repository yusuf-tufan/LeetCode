class Solution {
public:
    int searchInsert(vector<int>& nums, int target){
        bool find = false;
        for (int i : nums) {
            if (i == target) {
                find = true;
                break;
            }
        }
        if (find == true) {
            for (int i = 0;i < nums.size();i++) {
                if (nums[i] == target) {
                    return i;
                }
            }
        }
        else {
            nums.push_back(target);
            sort(nums.begin(), nums.end());
            for (int i = 0;i < nums.size();i++) {
                if (nums[i] == target) {
                    return i;
                }
            }
        }
        return 0;
    }
};