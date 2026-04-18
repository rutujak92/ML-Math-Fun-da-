class Vector:
    def __init__(self,components):
        self.components = list(components)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.components,other.components)])
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.components,other.components)])
    def dot(self,other):
        return sum(a+b for a,b in zip(self.components,other.components))
    def magnitude(self):
        return sum(a**2 for a in self.components) ** 0.5
    def cosine_similarity(self,other):
        return self.dot(other) / (self.magnitude() * other.magnitude())
    def __repr__(self):
        return f"{self.components}"
    
    
a = Vector([1,2,3])
b = Vector([4,5,6])

print(f"vector addition:{a+b}")
print(f"vector subtraction:{a-b}")
print(f"vector dot product:{a.dot(b)}")
print(f"vector magnitude:{a.magnitude()}")
print(f"vector cosine similarity to other:{a.cosine_similarity(b)}")
