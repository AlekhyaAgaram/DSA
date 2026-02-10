class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        //Only count when the previous number doesn’t exist.
        //If a number is not a sequence start, it must not execute any counting logic
        // If I loop over a set, I must use the loop variable (x), not array indexing.

        int n = nums.size();
        int count = 0;
        unordered_set<int> set;

        // Store all numbers for quick lookup
        for(int i=0;i<n;i++){
            set.insert(nums[i]);
        }

        int i=0;
        for(auto x : set){
            // Skip non-starting elements
            // if prev ele exists ->it is in middle of seq, do not start counting form here
            if(set.find(x - 1) != set.end()){
                continue;
            }

            int temp = 1;
            int curr = x;

            //Only start counting when you find the beginning of a sequence.
            while(set.find(curr + 1) != set.end()){
                temp++;
                curr++;
            }
            count = max(temp,count);  //Update global maximum
        }
        return count;
    }
};