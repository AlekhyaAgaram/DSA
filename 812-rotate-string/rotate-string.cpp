class Solution {
public:
    bool rotateString(string s, string goal) {
        int n = s.length();

        // if lengths of s and goal not equal , rot not possible
        if(s.length()!= goal.length()){
            return false;
        }

        int i =0;

        //rotate s for all possible comb
        while(i<n){
            string temp = s;
            for(int j=0;j<n;j++){
                temp[(j+i)%n] = s[j];
            }
            //if any rot is equal to goal
            if(temp == goal){
                return true;
            }
            else{
                i++;
            }
        }
        return false;
    }
};