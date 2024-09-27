# https://leetcode.com/problems/my-calendar-ii/description/

# solution - 
class MyCalendarTwo:

    def __init__(self):
        self.bookings = set()
        self.overlappings = set()

    def book(self, start: int, end: int) -> bool:
        def overlap(a, b) -> bool:
            return max(a[0],b[0]) < min(a[1],b[1])
        
        def get_overlap(a,b):
            return (max(a[0],b[0]),min(a[1],b[1]))

        request = (start, end)
        for item in self.overlappings:
            if(overlap(item, request)):
                return False
        
        for item in self.bookings:
            if(overlap(item, request)):
                self.overlappings.add(get_overlap(item, request))
        
        self.bookings.add(request)
        return True