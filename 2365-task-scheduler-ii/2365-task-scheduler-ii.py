class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_loc = {}
        space += 1
        days = 0
        for i, t in enumerate(tasks):
            if t in last_loc:
                recent = last_loc[t]
                diff = days - recent
                if diff < space:
                    days += space - diff    
            last_loc[t] = days
            days += 1
        
        return days
            