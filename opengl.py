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

    # head section
    draw_head()
    draw_upper_jaw()
    draw_lower_jaw()
    draw_horn()

    # tail section
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

def draw_head():
    x = 0
    y = 0
    glBegin(GL_TRIANGLE_STRIP);

    glVertex2f(508, 445);
    glVertex2f(594, 445);
    glVertex2f(503, 465);
    glVertex2f(563, 468);
    glVertex2f(503, 465);
    glVertex2f(548, 485);
    glVertex2f(500, 476);
    glVertex2f(544, 494);
    glVertex2f(498, 496);
    glVertex2f(555, 500);
    glVertex2f(502, 515);
    glVertex2f(566, 504);
    glVertex2f(514, 527);
    glVertex2f(574, 505);
    glVertex2f(528, 540);
    glVertex2f(580, 505);
    glVertex2f(541, 550);
    glVertex2f(587, 498);
    glVertex2f(562, 555);
    glVertex2f(596, 496);
    glVertex2f(583, 563);
    glVertex2f(609, 495);
    glVertex2f(603, 561);
    glVertex2f(616, 489);
    glVertex2f(622, 551);
    glVertex2f(619, 485);
    glVertex2f(636, 539);


    glEnd();

def draw_upper_jaw():
    x = 0
    y = 0
    glBegin(GL_TRIANGLE_STRIP);
    glVertex2f(636, 539);
    glVertex2f(628, 514);
    glVertex2f(646, 532);
    glVertex2f(637, 511);
    glVertex2f(654, 528);
    glVertex2f(644, 510);
    glVertex2f(661, 521);
    glVertex2f(649, 504);
    glVertex2f(667, 514);
    glVertex2f(653, 494);
    glVertex2f(671, 504);


    glEnd();

def draw_lower_jaw():
    x = 0
    y = 0
    glBegin(GL_TRIANGLE_STRIP);

    glVertex2f(620, 485);
    glVertex2f(620, 504);
    glVertex2f(623, 480);
    glVertex2f(634, 499);
    glVertex2f(631, 479);
    glVertex2f(642, 490);
    glVertex2f(642, 478);
    glVertex2f(648, 481);

    glEnd();

def draw_horn():
    x = 0
    y = 0
    glBegin(GL_TRIANGLE_STRIP);

    glVertex2f(562, 555);
    glVertex2f(584, 560);
    glVertex2f(556, 564);
    glVertex2f(565, 574);
    glVertex2f(549, 574);
    glVertex2f(552, 584);
    glVertex2f(540, 581);
    glVertex2f(543, 592);
    glVertex2f(527, 591);
    glVertex2f(530, 603);


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
