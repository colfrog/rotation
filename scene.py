from rotation import vector
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ipywidgets as widgets
import numpy as np

def xunit(v: vector = vector()):
       	return vector([1.0, 0, 0], v.orig)
def yunit(v: vector = vector()):
	return vector([0, 1.0, 0], v.orig)
def zunit(v: vector = vector()):
	return vector([0, 0, 1.0], v.orig)


def make_angle_slider(self):
	return widgets.IntSlider(min = 0, max = 360, step = 1)

class scene:
	def __init__(self, v, d = xunit()):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111, projection = "3d", xlim = (-3, 3), ylim = (-3, 3), zlim = (-3, 3))

		self.vangle = 0
		self.dangle = 0
		self.vi = self.v = v
		self.di = self.d = d
		self.Qv = self.quiver(v)
		self.Qd = self.quiver(d, "green")
		
		plt.ion()
		plt.show()

	def make_angle_slider(self):
		return widgets.IntSlider(min = 0, max = 360, step = 1)

	def quiver(self, v: vector, col = "black"):
		o = v.orig
		d = v.dest
		q = self.ax.quiver(o[0], o[1], o[2], d[0], d[1], d[2], color = col)
		return q
	
	def rotate_vector(self, angle_vecteur):
		self.vangle = angle_vecteur
		self.v = self.vi.rotate(self.d, self.vangle, True)
		self.ax.collections.remove(self.Qv)
		self.Qv = self.quiver(self.v)
		self.fig.canvas.draw()

	def rotate_dir(self, d, angle_direction):
		self.dangle = angle_direction
		self.d = self.di.rotate(d, self.dangle, True)
		
		self.vi = self.v.rotate(self.d, -self.vangle, True)
		self.ax.collections.remove(self.Qd)
		self.Qd = self.quiver(self.d, "green")
		self.fig.canvas.draw()

#class scene3(scene1):
#	def draw_3D_rotation(self, v: vector, angleX, angleY, angleZ):
#		Vrot = v.rotate(self.xunit(v), angleX) \
#			.rotate(self.yunit(v), angleY) \
#			.rotate(self.zunit(v), angleZ)
#		self.ax.collections.remove(self.Q)
#		self.Q = self.quiver(Vrot)
#		self.fig.canvas.draw()
