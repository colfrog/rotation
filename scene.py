from rotation import vector
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ipywidgets as widgets
import numpy as np

class scene:
	def __init__(self):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111, projection = "3d", xlim = (-3, 3), ylim = (-3, 3), zlim = (-3, 3))
		plt.ion()

	def xunit(self, v: vector):
		return vector([1.0, 0, 0], v.orig)
	def yunit(self, v: vector):
		return vector([0, 1.0, 0], v.orig)
	def zunit(self, v: vector):
		return vector([0, 0, 1.0], v.orig)

	def make_angle_slider(self):
		return widgets.IntSlider(min = 0, max = 360, step = 1)

	def quiver(self, v: vector, col = "black"):
		o = v.orig
		d = v.dest
		q = self.ax.quiver(o[0], o[1], o[2], d[0], d[1], d[2], color = col)
		return q


class scene1(scene):
	def __init__(self):
		super(scene1, self).__init__()
		self.Q = self.quiver(vector([0, 0, 0]))

	def draw_2D_rotation(self, dir: vector, v: vector, angle):
		Vrot = v.rotate(dir, angle, True)
		self.ax.collections.remove(self.Q)
		self.Q = self.quiver(Vrot)
		self.fig.canvas.draw()

class scene2(scene1):
	def draw_3D_rotation(self, v: vector, angleX, angleY, angleZ):
		Vrot = v.rotate(self.xunit(v), angleX) \
			.rotate(self.yunit(v), angleY) \
			.rotate(self.zunit(v), angleZ)
		self.ax.collections.remove(self.Q)
		self.Q = self.quiver(Vrot)
		self.fig.canvas.draw()

class scene3(scene):
	def generate_cube_vectors(self):
		vectors = []
		for i in range(-2, 2):
			for j in range(-2, 2):
				for k in range(-2, 2):
					vectors.append(vector([i, j, k]))

		return vectors

	def draw_cube_scatter(self, vectors):
		x = y = z = []
		for v in vectors:
			v.show()
			x.append(v[0])
			y.append(v[1])
			z.append(v[2])

		self.S = self.ax.scatter(x, y, z)

	def rotate_cube(self, dir, vectors, angle, marker = 'o'):
		vectors_rot = []
		for v in vectors:
			vectors_rot.append(v.rotate(dir.unit(), angle, True))

		self.ax.collections.remove(self.S)
		draw_cube_scatter(vectors_rot)
