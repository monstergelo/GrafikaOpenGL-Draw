from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 1200, 768                               # window size


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d
    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    draw_right_wing(365,210)                                  
    draw_dragon_head()
    glutSwapBuffers()                                  # important for double buffering


def drawPlane():
    glBegin(GL)


def draw_dragon_head():
    # start drawing a rectangle
    glBegin(GL_POLYGON)
    glVertex2f(295, 460)
    glVertex2f(295, 505)
    glVertex2f(240, 510)
    glVertex2f(160, 495)
    glVertex2f(80, 510)
    glVertex2f(75, 525)
    glVertex2f(40, 545)
    glVertex2f(30, 540)
    glVertex2f(50, 525)
    glVertex2f(45, 500)
    glVertex2f(25, 495)
    glVertex2f(23, 514)
    glVertex2f(18, 513)
    glVertex2f(11, 494)
    glVertex2f(42, 464)
    glVertex2f(16, 408)
    glVertex2f(53, 456)
    glVertex2f(77, 461)
    glVertex2f(96, 379)
    glVertex2f(99, 463)
    glVertex2f(163, 444)
    glVertex2f(238, 463)
    glEnd()

def draw_triangle(x, y, width, height):
    glBegin(GL_TRIANGLES)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point                       # top left point
    glEnd()

def draw_right_wing(x,y):
    glBegin(GL_TRIANGLE_FAN);
    glVertex2f(105+x, 380+y);    # A
    glVertex2f(11+x , 104+y);    # B
    glVertex2f(153+x,  12+y);    # C
    glVertex2f(295+x, 167+y);    # D
    glVertex2f(541+x, 339+y);    # E
    glEnd();    

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b'test')              # create window with title
# set draw function callback
glutDisplayFunc(draw)
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()
