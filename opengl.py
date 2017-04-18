from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

window = 0                                             # glut window number
width, height = 1200, 768                               # window size


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d
    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    draw_sky_background(0, 0.746, 1, 0, 0.746, 1)
    # draw_light(1, 1, 1, 0.4, 1, 1, 1, 0.4)
    draw_hill(0, 0, width, 300)
    draw_tree(50, 50)
    draw_tree(700, 50)
    draw_tree(350, 100)
    draw_tree(500, 200)
    draw_tree(200, 200)
    draw_tree(1100, 100)
    draw_tree(900, 200)
    draw_cloud(300, 475)
    draw_cloud(800, 475)
    draw_circle(600, 500, 20, 800, 1, 1, 1, 0.5, 1, 1, 1, 0)
    draw_circle(600, 500, 100, 100, 1, 1, 1, 1, 1, 0.72, 0.07, 0.6)
    draw_rainbow(600, 100, 100, 600, 1.5)

    glutSwapBuffers()

def drawPlane():
    glBegin(GL)

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_rainbow(offset_x, offset_y, width, radius, curve_factor):
	segment_width = float(width/6)
	true_r = radius
	cx = offset_x
	cy = offset_y
	for ii in range(0, 51):
		glBegin(GL_QUAD_STRIP);
		r = 600
		for i  in range(0,6):
			if(i == 0) : glColor4f(1.0,0.0,1.0,0.6);
			elif(i == 1) : glColor4f(0.0,0.0,1.0,0.6);
			elif(i == 2) : glColor4f(0.0,1.0,1.0,0.6);
			elif(i == 3) : glColor4f(0.0,1.0,0.0,0.6);
			elif(i == 4) : glColor4f(1.0,1.0,0.0,0.6);
			elif(i == 5) : glColor4f(1.0,0.0,0.0,0.6);
			#leftbound***********************************************************
			theta = 2.0 * 3.1415926 * float(ii) / float(100) #get the current angle 
			x = float(r * math.cos(theta) * curve_factor); #calculate the x component 
			y = float(r * math.sin(theta)); #calculate the y component 
			glVertex2f(x + cx, y + cy); #output vertex 
			
			#rightbound***********************************************************
			theta = 2.0 * 3.1415926 * float(ii+1) / float(100) #get the current angle 
			#upperbound----------------------------------------------------------
			x = float(r * math.cos(theta) * curve_factor); #calculate the x component 
			y = float(r * math.sin(theta)); #calculate the y component 
			glVertex2f(x + cx, y + cy); #output vertex 
			#lowerbound----------------------------------------------------------
			r -= segment_width
		glEnd();

def draw_circle(x, y, slices, radius, rin, bin, gin, ain, rout, bout, gout, aout):
	twicePi = 2.0 * math.pi
	glBegin(GL_TRIANGLE_FAN)
	glColor4f(rin, bin, gin, ain)
	glVertex2f(x, y)
	for i in range (0, slices+1):
		glColor4f(rout, bout, gout, aout)
		cx = x + (radius * math.cos(i * twicePi / slices))
		cy = y + (radius * math.sin(i * twicePi / slices))
		glVertex2f(cx, cy)
	glEnd()

def draw_sky_background(rtop, gtop, btop, rbot, gbot, bbot):
	glBegin(GL_QUADS)
	glColor3f(rtop, gtop, btop)
	glVertex2f(0, height)
	glVertex2f(width, height)
	glColor3f(rbot, gbot, bbot)
	glVertex2f(width, 0)
	glVertex2f(0, 0)
	glEnd()

def draw_hill(x, y, width, length):
	glBegin(GL_QUADS)
	glColor3f(0.16, 0.22, 0.09)
	glVertex2f(x, y)
	glVertex2f(x, y + length)
	glVertex2f(x + width, y + length)
	glVertex2f(x + width, y)
	glEnd()

def draw_tree(x, y):
	glBegin(GL_QUADS)
	glColor3f(0.4, 0.2, 0)
	glVertex2f(x, y)
	glVertex2f(x, y + 100)
	glVertex2f(x + 24, y + 100)
	glVertex2f(x + 24, y)
	glEnd()
	draw_circle(x + 12, y + 140, 10, 50, 0.273, 0.453, 0.03, 1, 0.15, 0.3, 0, 1)

def draw_cloud(x, y):
	draw_circle(x, y, 100, 35, 1, 1, 1, 1, 1, 1, 1, 0.5)
	draw_circle(x + 50, y, 100, 50, 1, 1, 1, 1, 1, 1, 1, 0.5)
	draw_circle(x + 100, y, 100, 35, 1, 1, 1, 1, 1, 1, 1, 0.5)


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
# create window with title
window = glutCreateWindow(b'Scenery')
# set draw function callback
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glutDisplayFunc(draw)
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()
