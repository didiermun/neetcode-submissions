class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        left = 0
        right = len(self.store[key]) - 1

        result = ""

        while left <= right:
            mid = left + (right-left)//2

            mid_val, mid_stamp = self.store[key][mid]

            if mid_stamp <= timestamp:
                result = mid_val
                left = mid + 1
            else:
                right = mid - 1

        return result
        
