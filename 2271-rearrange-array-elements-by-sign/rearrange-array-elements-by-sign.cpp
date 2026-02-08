class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        vector <int> pos;
        vector <int> neg;
        for(int i=0;i<n;i++){
            if(nums[i]>0){
                pos.push_back(nums[i]);
            }
            if(nums[i]<0){
                neg.push_back(nums[i]);
            }
        }

        int i = 0;
        int j=0;

        while(i<n){
            nums[i] = pos[j];            
            nums[i+1] = neg[j];
            j++;
            i=i+2;
        }
        return nums;
    }
};