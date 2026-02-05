class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int count_0 = 0;
        int count_1 = 0;
        int count_2 = 0;
        for(int i=0;i<n;i++){
            if(nums[i]==0){
                count_0++;
            }
            else if(nums[i]==1){
                count_1++;
            }
            if(nums[i]==2){
                count_2++;
            }
        }
        
        int j=0;
        while(count_0 > 0){
            nums[j++] = 0;
            count_0--;
        }
        while(count_1 > 0){
            nums[j++] = 1;
            count_1--;
        }
        while(count_2 > 0){
            nums[j++] = 2;
            count_2--;
        }
    }
};