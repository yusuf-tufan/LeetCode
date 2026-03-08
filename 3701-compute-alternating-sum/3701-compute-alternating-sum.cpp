class Solution {
public:
    int alternatingSum(vector<int>& nums) {
        int sumNums = 0;

for (int i = 0;i < nums.size();i++) {
    if (i % 2 == 0) { sumNums += nums[i]; }

    else {
        sumNums -= nums[i];
    }

}
return sumNums;
    }
};