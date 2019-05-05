from rotation import vector
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ipywidgets as widgets

class scene:
	def __init__(self):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111, projection = "3d", xlim = (-3, 3), ylim = (-3, 3), zlim = (-3, 3))
		self.Q = self.ax.quiver(0, 0, 0, 0, 0, 0)
		plt.ion()

	def xunit(self, v: vector):
		return vector([1, 0, 0], v.orig)
	def yunit(self, v: vector):
		return vector([0, 1, 0], v.orig)
	def zunit(self, v: vector):
		return vector([0, 0, 1], v.orig)

	def make_angle_slider(self):
		return widgets.IntSlider(min = 0, max = 360, step = 1)
	
	def quiver(self, v: vector, col = "black"):
		o = v.orig
		d = v.dest
		q = self.ax.quiver(o[0], o[1], o[2], d[0], d[1], d[2], color = col)
		return q

	
	def draw_2D_rotation(self, dir: vector, v: vector, angle):
		Vrot = v.rotate(dir, angle, True)
		self.ax.collections.remove(self.Q)
		self.Q = self.quiver(Vrot)
		self.fig.canvas.draw()

	def draw_3D_rotation(self, v: vector, angleX, angleY):
		Vrot = v.rotate(self.xunit(v), angleX, True) \
			.rotate(self.yunit(v), angleY, True)
		self.ax.collections.remove(self.Q)
		self.Q = self.quiver(Vrot)
		self.fig.canvas.draw()
