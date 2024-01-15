class Solution {
public:
    bool judgeSquareSum(int c) {
        long long int i=0;
        long long int j=sqrt(c);
        while (i<=j){
            long long int ans = i*i + j*j;
            if (ans < c){
                i++;
            }
            else if (ans == c) return true;
            else j--;
        }
        return false;
        
    }
};