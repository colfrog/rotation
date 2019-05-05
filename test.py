#!/usr/bin/python3
from rotation import vector

v = vector([1, 2, 3])
dir = vector([1, 0, 0])
vrot = v.rotate(dir, 0, True)
vrot.show()
