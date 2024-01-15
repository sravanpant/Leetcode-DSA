class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort()
        i=0
        j=n-1
        boats=0
        while i<=j:
            weight = people[i]+people[j]
            if weight > limit:
                boats+=1
                j-=1
            else: 
                i+=1 
                j-=1
                boats+=1
        return boats