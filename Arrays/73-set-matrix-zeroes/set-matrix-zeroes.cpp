class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        unordered_set <int> setR;        
        unordered_set <int> setC;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(matrix[i][j] == 0){
                    setR.insert(i);
                    setC.insert(j);
                }
            }
        }

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(setR.find(i)!=setR.end() || setC.find(j)!=setC.end()){
                    matrix[i][j] = 0;
                }
            }
        
        }


    }
};