import math

class Vector:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __str__(self):
        return f"({self.x}i + {self.y}j + {self.z}k)"
    
    def __getitem__(self, item) -> float:
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        if item == 2:
            return self.z
        raise IndexError("Index out of range")

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector): # dot product
            return Vector(self.x * other.x + self.y * other.y + self.z * other.z)
        if isinstance(other, (int, float)): # scalar multiplication
            return Vector(self.x * other, self.y * other, self.z * other)
        raise TypeError("Unsupported operand type(s) for *: 'Vector' and 'Vector'")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other, self.z / other)
        raise TypeError("Unsupported operand type(s) for /: 'Vector' and 'Vector'")

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(self.x / magnitude, self.y / magnitude, self.z / magnitude)