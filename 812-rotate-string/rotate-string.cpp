class Solution {
public:
    bool rotateString(string s, string goal) {
        int n = s.length();

        if(s.length()!= goal.length()){
            return false;
        }

        int i =0;

        while(i<n){
            string temp = s;
            for(int j=0;j<n;j++){
                temp[(j+i)%n] = s[j];
            }
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