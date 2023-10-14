class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int expectedSum = ((0 + nums.size()) * (nums.size() + 1))/2;

        for(int i = 0; i < nums.size(); i++){

            expectedSum -= nums[i];
        }

        
        return expectedSum;

    }

};
