class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int length = nums.size();
        vector<int> temp(length);
        
        for(int i=0;i<length;i++){
            temp[(i+k)%length] = nums[i];
        }
        nums = temp;
    }
};