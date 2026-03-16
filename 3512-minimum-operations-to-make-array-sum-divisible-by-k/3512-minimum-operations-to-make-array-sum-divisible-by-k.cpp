class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int sumList = 0,count=0;
        for (int i = 0;i < nums.size();i++) {
            sumList += nums[i];
        }
        while (sumList%k!=0) {
            sumList -= 1;
            count += 1;
        }
        return count;
    }
};