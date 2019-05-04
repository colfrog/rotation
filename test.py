#!/usr/bin/python3
from vector3d import vector

v = vector([1, 2, 3])
dir = vector([1, 1, 0])
vrot = v.rotate(dir, 60, True)
vrot.show()
