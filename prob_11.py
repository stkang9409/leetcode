class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=[]
        idxs=[0,len(height)-1]
        
        for i in range(len(height)-1):
            if height[idxs[0]]<=height[idxs[1]]:
                area.append(height[idxs[0]]*(idxs[1]-idxs[0]))
                idxs[0]+=1
            else:
                area.append(height[idxs[1]]*(idxs[1]-idxs[0]))
                idxs[1]-=1
            
        return max(area)