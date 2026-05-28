class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new = set()

        for x in nums:
            if x in new:
                return True
        
        
            new.add(x)

            
        return False    

        
         

            

            

            
