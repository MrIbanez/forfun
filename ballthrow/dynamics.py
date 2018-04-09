import numpy as np


class Point3D:
    def __init__(self, coord, vel=None, acc=None, mass=1.):
        self.crd = np.array(coord)
        self.vel = np.array(vel)
        self.acc = acc
        self.mass = mass

    def iterate(self, force, dt):
        # Velocity Verlet
        # x1 = x0 + v0 dt + 1/2 a dt^2
        a = force/self.mass
        self.crd += self.vel*dt + 0.5*a*dt*dt
        self.vel += (self.acc + a)*dt/2
        self.acc = a

class DynamicSystem:
