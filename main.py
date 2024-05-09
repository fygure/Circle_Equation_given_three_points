"""
Program to calculate equation of circle

[Goal] => (Equation of the circle given three points)

    - With three given points A B C, 
        find midpoints of two lines (ex: AC & AC)
        then take the intersection of both line's 
        perpendicular gradient which returns the
        center coordinates.
    - The center coordinates allow us to find
        radius by comparing the center and any
        of the three points (ex: center & B)
        and using Pythagorean Theorem to obtain
        r^2 for the equation of the circle where
        x and y are found through midpoint and
        gradient calculations.

"""



class PointStorage:
    
    # Data members
    storage = {}
    
    # Constructor
    def __init__(self) -> None:
        pass
    
    # Methods
    def add_coordinate_pair(self, point_char: chr, x: int, y: int) -> None:
        self.storage[point_char] = (x, y)
    
    def display_full_storage(self) -> None:
        print(self.storage)
    
    def get_coordinates(self, point_char: chr) -> tuple:
        if point_char in self.storage:
            return self.storage[point_char]
        else:
            return ('$', '$')
         
    def check_edge_cases(self) -> bool:
        #TODO 1) Collinear Points (all points lying on a single straight line)
        
        #2) Identical Points
        seen = set()
        for coord in self.storage.values():
            if coord in seen:
                return True
            seen.add(coord)
        return False        
        
        #TODO 3) Numerical Stability
        
        #TODO 4) Floating Point Precision
        
    def get_midpoint(self, p1_chr: chr, p2_chr: chr) -> tuple:
        #Add both x or y coords then divide by 2
        p1 = self.storage[p1_chr]
        p2 = self.storage[p2_chr]
        
        x = (p1[0] + p2[0]) / 2
        y = (p1[1] + p2[1]) / 2
        
        return (x, y)
        

def main():
    points = ['A', 'B', 'C']
    
    p = PointStorage()
    
    # Take inputs for each (x, y)
    for i in points:
        x = int(input(f"Point{i} x: "))
        y = int(input(f"Point{i} y: "))
        # initialize points
        p.add_coordinate_pair(point_char=i, x=x, y=y)
    
    # Check edge cases
    if p.check_edge_cases():
        print("edge case detected, terminating program with exit code -1.")
        return -1
    
    p.display_full_storage()
    #print(p.get_coordinates('D'))
    #print(p.check_edge_cases())
    
    print(p.get_midpoint('A', 'B'))
    
    #TODO: implement get gradient and also to get perpendicular gradient.
    #TODO: store center coordinates.
    #TODO: use center coordinates and another to obtain r^2.
    #TODO: complete and output circle equation.
    
    return 0
    
    

if __name__ == "__main__":
    main()