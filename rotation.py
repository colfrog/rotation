import numpy as np

class vector:
	def __init__(self, l = [0, 0, 0]):
		self.components = l
		self.norm = np.sqrt(l[0]**2 + l[1]**2 + l[2]**2)

	def show(self):
		print("[{} {} {}]".format(self[0], self[1], self[2]))
		return self

	def unit(self):
		l = [0, 0, 0]
		for i in range(3):
			l[i] = self[i]/self.norm
		return vector(l)

	def __getitem__(self, key):
		if key < 0 or key > 2:
			return None
		else:
			return self.components[key]

	def __mul__(self, x = 1):
		return vector([self[0]*x, self[1]*x, self[2]*x])
	def __div__(self, x = 1):
		return vector([self[0]/x, self[1]/x, self[2]/x])
	def __add__(self, m = [0, 0, 0]):
		return vector([self[0]+m[0], self[1]+m[1], self[2]+m[2]])
	def __sub__(self, m = [0, 0 ,0]):
		l = self.components
		return vector([self[0]-m[0], self[1]-m[1], self[2]-m[2]])

def vector_dot_product(self, v: vector):
	n = 0
	for i in range(3):
		n += self[i]*v[i]

	return n

def vector_cross_product(self, v: vector):
	a = self[1]*v[2] - self[2]*v[1]
	b = self[2]*v[0] - self[0]*v[2]
	c = self[0]*v[1] - self[1]*v[0]
	return vector([a, b, c])

def vector_projection(self, v: vector):
	return v*(self.dot_product(v)/(v.norm**2))

vector.dot_product = vector_dot_product
vector.cross_product = vector_cross_product
vector.projection = vector_projection

class quaternion:
	def __init__(self, a = 0, v: vector = vector()):
		self.real = a
		self.imag = v

	def show(self):
		print("({}, {}, {}, {})".format(self.real, self.imag[0], self.imag[1], self.imag[2]))
		return self

	def inverse(self):
		return quaternion(self.real, vector() - self.imag)
	
def quaternion_mul(self, q: quaternion):
	a, u = self.real, self.imag
	b, v = q.real, q.imag
	c = a*b - u.dot_product(v)
	w = v*a + u*b + u.cross_product(v)
	return quaternion(c, w)

def quaternion_add(self, q: quaternion):
	return quaternion(self.real + q.real, self.imag + q.imag)

def quaternion_sub(self, q: quaternion):
	return quaternion(self.real - q.real, self.imag - q.imag)

quaternion.__mul__ = quaternion_mul
quaternion.__add__ = quaternion_add
quaternion.__sub__ = quaternion_sub

def vector_rotate(self, dir: vector, angle, degrees = False):
	th = angle*(np.pi/180) if degrees else angle
	u = dir.unit()
	p = quaternion(np.cos(th/2), u*np.sin(th/2))
	q = quaternion(0, self)
	
	return (p*q*p.inverse()).imag

vector.rotate = vector_rotate
