class Solution {
  private:
  bool is_palindrom(string s,int i ,int j){
     
      while(i<j){
          if(s[i]==s[j]){
              i+=1;
              j-=1;
          }
          else{
              return false;
          }
      }
      return true;
  }
    
    
public:
    bool validPalindrome(string s) {
        int i = 0;
        int j = s.size()-1;
        // bool ans;
        while(i<=j){
            if(s[i]==s[j]){
                i+=1;
                j-=1;
            }
            else{
                return (is_palindrom(s,i,j-1)||is_palindrom(s,i+1,j));
            }  
           
        }
        return true;
        
        
    }
};