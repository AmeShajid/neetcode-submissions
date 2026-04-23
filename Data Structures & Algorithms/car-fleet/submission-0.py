class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine each car's position and speed into a single pair (tuple)
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        # Sort the cars by their starting position, from farthest to closest to the destination
        # We use reverse=True so we sort from closest to target to farthest
        cars.sort(reverse=True)
        
        # Create a stack to keep track of fleet arrival times
        stack = []
        
        # Loop through each car, starting from the one closest to the destination
        for pos, spd in cars:
            # Calculate time needed for this car to reach the target
            time = (target - pos) / spd
            
            # If the stack is empty, or this car needs more time than the car in front, 
            # it starts a new fleet (push its time onto the stack)
            if not stack or time > stack[-1]:
                stack.append(time)
            # If time <= stack[-1], it means this car will catch up and join the current fleet, so do nothing
        
        # The number of fleets is the number of times on the stack
        return len(stack)
        