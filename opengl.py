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
    draw_rainbow(600, 100, 100, 600, 1.5)
    # draw_sun_light(600, 500, 20, 100)
    glColor3f(1.0, 1.0, 1.0)
    draw_sun(600, 500, 20, 100)

    # # head section
    # draw_head()
    # draw_upper_jaw()
    # draw_lower_jaw()
    # draw_horn()
    # draw_wing_triangle_strip()

    # # body section
    # draw_body()
    # draw_front()
    # draw_front_leg()
    # draw_back_leg()

    # # tail section
    # draw_tail()

    # glColor3f(255.0, 255.0, 255.0)
    # draw_eye()

    # important for double buffering
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


def draw_body():
    glBegin(GL_POLYGON)

    glVertex2f(508, 445)
    glVertex2f(594, 445)
    glVertex2f(585, 352)
    glVertex2f(472, 325)
    glVertex2f(388, 305)
    glVertex2f(388, 385)

    glEnd()


def draw_front():
    glBegin(GL_TRIANGLE_STRIP)

    glVertex2f(594, 445)
    glVertex2f(585, 352)
    glVertex2f(610, 397)
    glVertex2f(606, 379)

    glEnd()


def draw_front_leg():
    glBegin(GL_TRIANGLE_STRIP)

    glVertex2f(585, 352)
    glVertex2f(534, 345)
    glVertex2f(594, 340)
    glVertex2f(529, 312)
    glVertex2f(588, 308)
    glVertex2f(584, 264)
    glVertex2f(606, 280)
    glVertex2f(585, 273)
    glVertex2f(529, 345)
    glVertex2f(606, 272)
    glVertex2f(599, 254)
    glVertex2f(619, 255)
    glVertex2f(585, 239)
    glVertex2f(650, 249)

    glEnd()


def draw_back_leg():
    glBegin(GL_TRIANGLE_STRIP)

    glVertex2f(388, 305)
    glVertex2f(458, 340)
    glVertex2f(398, 273)
    glVertex2f(500, 280)
    glVertex2f(420, 250)
    glVertex2f(470, 250)
    glVertex2f(430, 234)
    glVertex2f(450, 235)
    glVertex2f(398, 220)
    glVertex2f(500, 230)

    glEnd()


def draw_wing_triangle_strip():
    x = 0
    y = 768
    glBegin(GL_TRIANGLE_STRIP)

    glVertex2f(61, 627)
    glVertex2f(171, 579)
    glVertex2f(195, 661)
    glVertex2f(376, 669)
    glVertex2f(148, 508)
    glVertex2f(453, 626)
    glVertex2f(220, 493)
    glVertex2f(447, 548)
    glVertex2f(213, 434)
    glVertex2f(427, 483)
    glVertex2f(347, 443)
    glVertex2f(450, 463)
    glVertex2f(337, 391)
    glVertex2f(508, 445)
    glVertex2f(388, 383)

    glEnd()


def draw_rainbow(offset_x, offset_y, width, radius, curve_factor):
	segment_width = float(width/6)
	true_r = radius
	cx = offset_x
	cy = offset_y
	for ii in range(0, 51):
		glBegin(GL_QUAD_STRIP);
		r = 600
		for i  in range(0,6):
			if(i == 0) : glColor3f(1.0,0.0,1.0);
			elif(i == 1) : glColor3f(0.0,0.0,1.0);
			elif(i == 2) : glColor3f(0.0,1.0,1.0);
			elif(i == 3) : glColor3f(0.0,1.0,0.0);
			elif(i == 4) : glColor3f(1.0,1.0,0.0);
			elif(i == 5) : glColor3f(1.0,0.0,0.0);
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

def draw_sun(x, y, slices, radius):
	twicePi = 2.0 * math.pi
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x, y)
	for i in range (0, slices+1):
		glColor3f(1.0, 0.72, 0.07)
		cx = x + (radius * math.cos(i * twicePi / slices))
		cy = y + (radius * math.sin(i * twicePi / slices))
		glVertex2f(cx, cy)
	glEnd()

# def draw_sun_light(x, y, slices, radius):
# 	twicePi = 2.0 * math.pi
# 	glColor3f(0.0, 0.0, 0.0)
# 	glBegin(GL_TRIANGLE_FAN)
# 	glVertex2f(x, y)
# 	for i in range (0, slices+1):
# 		glColor3f(0.0, 0.0, 0.0)
# 		cx = x + (radius * math.cos(i * twicePi / slices))
# 		cy = y + (radius * math.sin(i * twicePi / slices))
# 		glVertex2f(cx, cy)
# 	glColor3f(1.0, 0.72, 0.07)
# 	glVertex2f(cx, cy)
# 	for i in range (slices+1, 50):
# 		glColor3f(0.0, 0.0, 0.0)
# 		cx = x + (radius * math.cos(i * twicePi / slices))
# 		cy = y + (radius * math.sin(i * twicePi / slices))
# 		glVertex2f(cx, cy)
# 	glEnd()


def draw_head():
    x = 0
    y = 0
    glBegin(GL_TRIANGLE_STRIP)

    glVertex2f(508, 445)
    glVertex2f(594, 445)
    glVertex2f(503, 465)
    glVertex2f(563, 468)
    glVertex2f(503, 465)
    glVertex2f(548, 485)
    glVertex2f(500, 476)
    glVertex2f(544, 494)
    glVertex2f(498, 496)
    glVertex2f(555, 500)
    glVertex2f(502, 515)
    glVertex2f(566, 504)
    glVertex2f(514, 527)
    glVertex2f(574, 505)
    glVertex2f(528, 540)
    glVertex2f(580, 505)
    glVertex2f(541, 550)
    glVertex2f(587, 498)
    glVertex2f(562, 555)
    glVertex2f(596, 496)
    glVertex2f(583, 563)
    glVertex2f(609, 495)
    glVertex2f(603, 561)
    glVertex2f(616, 489)
    glVertex2f(622, 551)
    glVertex2f(619, 485)
    glVertex2f(636, 539)

    glEnd()

def draw_test():
	glBegin(GL_QUADS)
	glColor3f(1.0,0.0,0.0);
	glVertex2f(100.0, 200.0);
	#blue color
	glColor3f(0.0,0.0,1.0);
	glVertex2f(100.0,100.0);
	
	glVertex2f(200.0,100.0);
	glVertex2f(200.0, 200.0);
	glEnd();

def draw_upper_jaw():
    x = 0
    y = 0
    glBegin(GL_TRIANGLE_STRIP)

    glVertex2f(636, 539)
    glVertex2f(628, 514)
    glVertex2f(646, 532)
    glVertex2f(637, 511)
    glVertex2f(654, 528)
    glVertex2f(644, 510)
    glVertex2f(661, 521)
    glVertex2f(649, 504)
    glVertex2f(667, 514)
    glVertex2f(653, 494)
    glVertex2f(671, 504)

    glEnd()


def draw_lower_jaw():
    x = 0
    y = 0
    glBegin(GL_TRIANGLE_STRIP)

    glVertex2f(620, 485)
    glVertex2f(620, 504)
    glVertex2f(623, 480)
    glVertex2f(634, 499)
    glVertex2f(631, 479)
    glVertex2f(642, 490)
    glVertex2f(642, 478)
    glVertex2f(648, 481)

    glEnd()


def draw_horn():
    x = 0
    y = 0
    glBegin(GL_TRIANGLE_STRIP)

    glVertex2f(562, 555)
    glVertex2f(584, 560)
    glVertex2f(556, 564)
    glVertex2f(565, 574)
    glVertex2f(549, 574)
    glVertex2f(552, 584)
    glVertex2f(540, 581)
    glVertex2f(543, 592)
    glVertex2f(527, 591)
    glVertex2f(530, 603)

    glEnd()


def draw_eye():
    x = 0
    y = 0
    glBegin(GL_POLYGON)

    glVertex2f(599, 546)
    glVertex2f(622, 532)
    glVertex2f(623, 521)
    glVertex2f(602, 529)

    glEnd()


def draw_tail():
    x = 0
    y = 768
    glBegin(GL_TRIANGLE_STRIP)

    glVertex2f(175 - x, y - 529)
    glVertex2f(115 - x, y - 600)
    glVertex2f(135 - x, y - 600)
    glVertex2f(120 - x, y - 665)
    glVertex2f(155 - x, y - 667)
    glVertex2f(176 - x, y - 700)
    glVertex2f(220 - x, y - 660)
    glVertex2f(268 - x, y - 663)
    glVertex2f(280 - x, y - 583)
    glVertex2f(362 - x, y - 476)
    glVertex2f(325 - x, y - 430)
    glVertex2f(395 - x, y - 463)
    glVertex2f(388 - x, y - 383)

    glEnd()

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
# create window with title
window = glutCreateWindow(b'Dragon')
# set draw function callback
glutDisplayFunc(draw)
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()
