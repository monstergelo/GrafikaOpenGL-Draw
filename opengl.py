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
    draw_tail()
    glutSwapBuffers()                                  # important for double buffering


def drawPlane():
    glBegin(GL)



def draw_triangle(x, y, width, height):
    glBegin(GL_TRIANGLES)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point                       # top left point
    glEnd()


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_tail():
    x = 0
    y = 768
    glBegin(GL_TRIANGLE_STRIP);

    glVertex2f( 175-x, y-529);    #A
    glVertex2f( 115-x, y-600);    #B
    glVertex2f( 135-x, y-600);    #C
    glVertex2f( 120-x, y-665);    #D
    glVertex2f( 155-x, y-667);    #E
    glVertex2f( 176-x, y-700);    #F
    glVertex2f( 220-x, y-660);    #G
    glVertex2f( 268-x, y-663);    #A
    glVertex2f( 280-x, y-583);    #A
    glVertex2f( 362-x, y-476);    #A
    glVertex2f( 325-x, y-430);    #A
    glVertex2f( 395-x, y-463);    #A
    glVertex2f( 388-x, y-383);    #A



    glEnd();

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
