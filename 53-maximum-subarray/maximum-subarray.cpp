class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();

        int max = INT_MIN;
        int sum = 0;

        for(int i=0;i<n;i++){
            sum += nums[i];
            if(sum < 0){
                sum = 0;
            }
            if (sum>max){
                max = sum;
            }
        }
        if(max == 0){
            int k = 0;
            int max1 = nums[0];
            while(k<n){
                if(nums[k] > max1){
                    max1 = nums[k];
                }
                k++;
            }
            max = max1;
        }
        return max;
    }
};