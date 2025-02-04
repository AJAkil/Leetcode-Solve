class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, [])
        l, r = 0, len(values) - 1
        m = 0
        res = ""
        while l <= r:
            m = (l+r)//2

            if values[m][0] <= timestamp:
                # look in the right half
                res = values[m][1] # update the result to have largest timestamp we have seen so far
                l = m + 1
                
            else:
                # look in the left half
                r = m - 1
            
        
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)