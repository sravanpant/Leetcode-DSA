#User function Template for python3

class Solution:
    def longest(self, names, n):
    	# code here
    	l = 0
        for c in names:
            if l < len(c):
                l = len(c)
                name = c
        return name
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	n=int(input())
    	names = []
    	for i in range(n):
    		names.append(input())
    	ob = Solution()
    	print(ob.longest(names, n))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends