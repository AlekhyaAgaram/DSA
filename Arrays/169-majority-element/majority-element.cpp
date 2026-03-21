class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int,int> freq;
        for(int x: nums){
            freq[x]++;
        }
        int res = 0;
        for (auto it : freq){
            if(it.second > n/2){
                res =  it.first;
            }
        }
        return res;

    }
};