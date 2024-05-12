import matplotlib.pyplot as plt
import math
import itertools
from Vector import Vector

# TODO:
#* - Add collision detection
#* - Add more objects
#* - Remove Sun if Planet collides with it
#* - Add more complex interactions (e.g. black holes, moons, etc.)

class SolarSystem:
    
    def __init__(self, size, projection_2d=False):
        self.size = size
        self.objects = []
        self.projection_2d = projection_2d
        self.fig, self.ax = plt.subplots(1, 1, subplot_kw={'projection': '3d'}, figsize=(self.size/50, self.size/50))
        self.fig.tight_layout()
        if self.projection_2d:
            self.ax.view_init(10,0)
        else:
            self.ax.view_init(0,0)
        
    def add_object(self, obj):
        self.objects.append(obj)
        
    def update_all(self):
        self.objects.sort(key=lambda item: item.position[0])
        for obj in self.objects:
            obj.move()
            obj.draw()
            
    def draw_all(self):
        self.ax.set_xlim((-self.size/2, self.size/2))
        self.ax.set_ylim((-self.size/2, self.size/2))
        self.ax.set_zlim((-self.size/2, self.size/2))
        if self.projection_2d:
            self.ax.xaxis.set_ticklabels([])
            self.ax.yaxis.set_ticklabels([])
            self.ax.zaxis.set_ticklabels([])
        else:
            self.ax.axis(False)
        plt.pause(0.01)
        self.ax.clear()
            
        
    def calculate_all_interactions(self):
        bodies = self.objects.copy()
        for idx, body in enumerate(bodies):
            for other_body in bodies[idx + 1:]:
                body.gravity_acceleartion(other_body)
        
class SolarSystemObject:
    min_display_size = 10
    display_log_base = 1.3
    
    def __init__(self, solar_system, mass, position=(0, 0, 0), velocity=(0, 0, 0)):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.display_size = max(math.log(self.mass, self.display_log_base), self.min_display_size)
        self.color = "black"
        self.solar_system.add_object(self)
        
    def move(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1], self.position[2] + self.velocity[2])
    
    def draw(self):
        self.solar_system.ax.plot(*self.position, 'o', markersize=self.display_size + self.position[0] / 30, color=self.color)
        if self.solar_system.projection_2d:
            self.solar_system.ax.plot(self.position[0], self.position[1], -self.solar_system.size/2, 'o', markersize=self.display_size/2, color=(.5, .5, .5))
        
    def gravity_acceleartion(self, other):
        G = 6.67430e-11
        distance = Vector(*other.position) - Vector(*self.position)
        magnitude = distance.get_magnitude()
        
        force_magnitude = self.mass * other.mass / magnitude**2
        force = distance.normalize() * force_magnitude
        
        reverse = 1
        for body in self, other:
            acceleration = force / body.mass
            body.velocity += acceleration * reverse
            reverse *= -1
            
class Sun(SolarSystemObject):
    def __init__(self, solar_system, mass=10000, position=(0, 0, 0), velocity=(0, 0, 0)):
        super(Sun, self).__init__(solar_system, mass, position, velocity)
        self.color = "yellow"
        
class Planet(SolarSystemObject):
    colors = itertools.cycle([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)])
    def __init__(self, solar_system, mass=10, position=(0, 0, 0), velocity=(0, 0, 0)):
        super(Planet, self).__init__(solar_system, mass, position, velocity)
        self.color = next(Planet.colors)