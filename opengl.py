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
    draw_wing_triangle_strip()
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

def draw_wing_line():
    x = 0
    y = 768
    glBegin(GL_LINE_STRIP);
    glVertex2f(56-x,625);
    glVertex2f(129-x,607);
    glVertex2f(129-x,607);
    glVertex2f(158-x,593);
    glVertex2f(172-x,576);
    glVertex2f(151-x,511);
    glVertex2f(171-x,529);
    glVertex2f(166-x,492);
    glVertex2f(176-x,534);
    glVertex2f(191-x,536);
    glVertex2f(212-x,529);
    glVertex2f(222-x,514);
    glVertex2f(211-x,480);
    glVertex2f(205-x,462);
    glVertex2f(211-x,434);
    glVertex2f(214-x,461);
    glVertex2f(238-x,477);
    glVertex2f(290-x,490);
    glVertex2f(312-x,473);
    glVertex2f(324-x,453);
    glVertex2f(342-x,453);
    glVertex2f(333-x,403);
    glVertex2f(343-x,378);
    glVertex2f(388-x,383);
    glVertex2f(508-x,441);
    glVertex2f(433-x,475);
    glVertex2f(425-x,494);
    glVertex2f(454-x,581);
    glVertex2f(459-x,611);
    glVertex2f(420-x,648);
    glVertex2f(315-x,677);
    glVertex2f(56-x,625);
    glEnd();


def draw_wing_triangle_strip():
    x = 0
    y = 768
    glBegin(GL_TRIANGLE_STRIP);
    glVertex2f(61, 627);
    glVertex2f(171, 579);
    glVertex2f(195, 661);
    glVertex2f(376, 669);
    glVertex2f(148, 508);
    glVertex2f(453, 626);
    glVertex2f(220, 493);
    glVertex2f(447, 548);
    glVertex2f(213, 434);
    glVertex2f(427, 483);
    glVertex2f(347, 443);
    glVertex2f(450, 463);
    glVertex2f(337, 391);
    glVertex2f(483, 442);
    glVertex2f(388, 383);
    glEnd();

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
