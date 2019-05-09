import numpy as np

class point:
	def __init__(self, l = [0, 0 ,0]):
		self.x = l[0]
		self.y = l[1]
		self.z = l[2]
		self.comp = l

	def __getitem__(self, key):
		if key < 0 or key > 2:
			return None
		else:
			return self.comp[key]

	def __iter__(self):
		return iter(self.comp)

class vector:
	def __init__(self, dest = [0, 0, 0], orig = [0, 0, 0]):
		self.orig = point(orig)
		self.dest = point(dest)
		self.comp = point([dest[i] - orig[i] for i in range(3)])
		self.norm = np.sqrt(sum(c**2 for c in self.comp))

	def __iter__(self):
		return iter(self.comp)

	def __getitem__(self, key):
		return self.comp[key]

	def __mul__(self, x = 1):
		return vector([c*x for c in self.comp], self.orig)
	def __div__(self, x = 1):
		return vector([c/x for c in self.comp], self.orig)
	def __add__(self, m = [0, 0, 0]):
		return vector([self[i]+m[i] for i in range(3)], self.orig)
	def __sub__(self, m = [0, 0 ,0]):
		return vector([self[i]-m[i] for i in range(3)], self.orig)

	def show(self):
		print("[{} {} {}]".format(self[0], self[1], self[2]))
		return self

	def unit(self):
		return vector([c/self.norm for c in self.comp], self.orig)

	def angle(self, v):
		return np.arccos(self.dot_product(v)/(self.norm*v.norm))

	def dot_product(self, v):
		return sum(self[i]*v[i] for i in range(3))

	def cross_product(self, v):
		a = self[1]*v[2] - self[2]*v[1]
		b = self[2]*v[0] - self[0]*v[2]
		c = self[0]*v[1] - self[1]*v[0]
		return vector([a, b, c])

	def projection(self, v):
		return v*(self.dot_product(v)/(v.norm**2))

	def rotate(self, dir, angle, degrees = True):
		th = angle*(np.pi/180) if degrees else angle
		u = dir.unit()
		p = quaternion(np.cos(th/2), u*np.sin(th/2))
		q = quaternion(0, self)
		return (p*q*p.inverse()).imag

class quaternion:
	def __init__(self, a = 0, v: vector = vector()):
		self.real = a
		self.imag = v

	def __mul__(self, q):
		a, u = self.real, self.imag
		b, v = q.real, q.imag
		c = a*b - u.dot_product(v)
		w = v*a + u*b + u.cross_product(v)
		return quaternion(c, w)

	def __add__(self, q):
		return quaternion(self.real + q.real, self.imag + q.imag)

	def __sub__(self, q):
		return quaternion(self.real - q.real, self.imag - q.imag)

	def show(self):
		print("({}, {}, {}, {})".format(self.real, self.imag[0], self.imag[1], self.imag[2]))
		return self

	def inverse(self):
		return quaternion(self.real, vector() - self.imag)
