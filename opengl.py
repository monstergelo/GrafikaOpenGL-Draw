from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time
from PIL import Image

window = 0  # glut window number

width, height = 1200, 768   # window size
anglePyramid = 0.0          # Rotational angle for pyramid [NEW]
angleCube = 0.0             # Rotational angle for cube [NEW]
refreshMills = 15           # refresh interval in milliseconds [NEW]


# ascii codes for various special keys
ESCAPE = 27
PAGE_UP = 73
PAGE_DOWN = 81
UP_ARROW = 72
DOWN_ARROW = 80
LEFT_ARROW = 75
RIGHT_ARROW = 77

# lighting on/off (1 = on, 0 = off)
light = 0


xrot = 0   # x rotation
yrot = 0   # y rotation
xspeed = 0  # x rotation speed
yspeed = 0  # y rotation speed

z = -5.0  # depth into the screen.


# white ambient light at half intensity (rgba)
LightAmbient = [0.5, 0.5, 0.5, 1.0]

# super bright, full intensity diffuse light.
LightDiffuse = [1.0, 1.0, 1.0, 1.0]

# position of light (x, y, z, (position of light))
LightPosition = [0.0, 0.0, 2.0, 1.0]


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d
    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    draw_sky_background(0, 0.746, 1, 0, 0.746, 1)
    # draw_light(1, 1, 1, 0.4, 1, 1, 1, 0.4)
    draw_hill(0, 0, width, 300)
    draw_circle(600, -500, 100, 850, 0.16, 0.22, 0.09, 1, 0.16, 0.22, 0.09, 1)
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

def initGL():
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    # Set background color to black and opaque
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)                   # Set background depth to farthest
    glEnable(GL_DEPTH_TEST)   # Enable depth testing for z-culling
    glDepthFunc(GL_LEQUAL)    # Set the type of depth-test
    glShadeModel(GL_SMOOTH)   # Enable smooth shading
    # Nice perspective correctionss
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    # set up light number 1.
    glLightfv(GL_LIGHT1, GL_AMBIENT, LightAmbient)  # add lighting. (ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, LightDiffuse)  # add lighting. (diffuse).
    glLightfv(GL_LIGHT1, GL_POSITION, LightPosition)  # set light position.
    glEnable(GL_LIGHT1)                             # turn light 1 on.


def LoadTextures():
    #global texture
    image = Image.open("texture.png")
    ix = image.size[0]
    iy = image.size[1]
    image = image.convert(mode='RGBA').tobytes("raw", "RGBA", 0, -1)
    # Create Texture
    # 2d texture (x and y size)
    glBindTexture(GL_TEXTURE_2D, glGenTextures(1))

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def display():
    global angleCube
    global anglePyramid
    global xrot, yrot

    # Clear color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)     # To operate on model-view matrix

    # Render a color-cube consisting of 6 quads with different colors
    glLoadIdentity()                 # Reset the model-view matrix
    glTranslatef(1.5, 0.0, -7.0)  # Move right and into the screen

    # move z units out from the screen.
    glTranslatef(0.0, 0.0, z)

    glRotatef(xrot, 1.0, 0.0, 0.0)         # Rotate On The X Axis
    glRotatef(yrot, 0.0, 1.0, 0.0)         # Rotate On The Y Axis
    # Begin drawing the color cube with 6 quads
    glBegin(GL_QUADS)
    # Top face (y = 1.0)
    # Define vertices in counter-clockwise (CCW) order with normal pointing out
    glColor3f(0.0, 1.0, 0.0)     # Green
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0.6, 1.0, -0.05)
    glTexCoord2f(0.473, 0.0)
    glVertex3f(-0.6, 1.0, -0.05)
    glTexCoord2f(0.473, 0.05)
    glVertex3f(-0.6, 1.0,  0.05)
    glTexCoord2f(0.0, 0.05)
    glVertex3f(0.6, 1.0,  0.05)

    # Bottom face (y = -1.0)
    glColor3f(1.0, 0.5, 0.0)     # Orange
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0.6, -1.0,  0.05)
    glTexCoord2f(0.473, 0.0)
    glVertex3f(-0.6, -1.0,  0.05)
    glTexCoord2f(0.473, 0.05)
    glVertex3f(-0.6, -1.0, -0.05)
    glTexCoord2f(0.0, 0.05)
    glVertex3f(0.6, -1.0, -0.05)

    # Front face  (z = 1.0)
    glColor3f(1.0, 0.0, 0.0)     # Red
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0.6,  1.0, 0.05)
    glTexCoord2f(0.473, 0.0)
    glVertex3f(-0.6,  1.0, 0.05)
    glTexCoord2f(0.473, 1.0)
    glVertex3f(-0.6, -1.0, 0.05)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(0.6, -1.0, 0.05)

    # Back face (z = -1.0)
    glColor3f(1.0, 1.0, 0.0)     # Yellow
    glTexCoord2f(0.519, 1.0)
    glVertex3f(0.6, -1.0, -0.05)
    glTexCoord2f(0.955, 1.0)
    glVertex3f(-0.6, -1.0, -0.05)
    glTexCoord2f(0.955, 0.0)
    glVertex3f(-0.6,  1.0, -0.05)
    glTexCoord2f(0.519, 0.0)
    glVertex3f(0.6,  1.0, -0.05)

    # Left face (x = -1.0)
    glColor3f(0.0, 0.0, 1.0)     # Blue
    glTexCoord2f(0.473, 0.0)
    glVertex3f(-0.6,  1.0,  0.05)
    glTexCoord2f(0.517, 0.0)
    glVertex3f(-0.6,  1.0, -0.05)
    glTexCoord2f(0.517, 1.0)
    glVertex3f(-0.6, -1.0, -0.05)
    glTexCoord2f(0.473, 1.0)
    glVertex3f(-0.6, -1.0,  0.05)

    # Right face (x = 1.0)
    glColor3f(1.0, 0.0, 1.0)     # Magenta
    glTexCoord2f(0.957, 0.0)
    glVertex3f(0.6,  1.0, -0.05)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.6,  1.0,  0.05)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.6, -1.0,  0.05)
    glTexCoord2f(0.957, 1.0)
    glVertex3f(0.6, -1.0, -0.05)
    glEnd()  # End of drawing color-cube

    xrot += xspeed                       # X Axis Rotation
    yrot += yspeed  # Y Axis Rotation

    glutSwapBuffers()  # Swap the front and back frame buffers (double buffering)


def reshape(width, height):
    # Compute aspect ratio of the new window
    if (height == 0):
        height = 1                # To prevent divide by 0
        
    aspect = float(width) / float(height)

    # Set the viewport to cover the new window
    glViewport(0, 0, width, height)

    # Set the aspect ratio of the clipping volume to match the viewport
    glMatrixMode(GL_PROJECTION)  # To operate on the Projection matrix
    glLoadIdentity()             # Reset
    # Enable perspective projection with fovy, aspect, zNear and zFar
    gluPerspective(45.0, aspect, 0.1, 100.0)


def timer(value):
    glutPostRedisplay()      # Post re-paint request to activate display()
    glutTimerFunc(refreshMills, timer, 0)  # next timer call milliseconds later

# The function called whenever a normal key is pressed.


def keyPressed(key, x, y):
    global light, filter, blend

    key = ord(key)

    # avoid thrashing this procedure
    time.sleep(0.01)

    if key == ESCAPE:
        # shut down our window
        glutDestroyWindow(window)
        # exit the program...normal termination.
        sys.exit()
    elif key == 108 or key == 76:  # switch the lighting.
        print("L/l pressed; light is: %d\n" % (light))

    if light == 0:
        light = 1
    else:
        light = 0      # switch the current value of light, between 0 and 1.
    print("Light is now: %d\n" % (light))
    if not(light):
        glDisable(GL_LIGHTING)
    else:
        glEnable(GL_LIGHTING)

# The function called whenever a normal key is pressed.


def specialKeyPressed(key, x, y):
    global z, xspeed, yspeed

    # avoid thrashing this procedure
    time.sleep(0.01)

    if key == GLUT_KEY_PAGE_UP:  # move the cube into the distance.
        z -= 0.2

    elif key == GLUT_KEY_PAGE_DOWN:  # move the cube closer.
        z += 0.2

    elif key == GLUT_KEY_UP:  # decrease x rotation speed;
        xspeed -= 0.1

    elif key == GLUT_KEY_DOWN:  # increase x rotation speed;
        xspeed += 0.1

    elif key == GLUT_KEY_LEFT:  # decrease y rotation speed;
        yspeed -= 0.1

    elif key == GLUT_KEY_RIGHT:  # increase y rotation speed;
        yspeed += 0.1


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_DOUBLE)  # Enable double buffered mode
glutInitWindowSize(640, 480)   # Set the window's initial width & height
glutInitWindowPosition(50, 50)  # Position the window's initial top-left corner

# Create window with the given title
glutCreateWindow(b'Handphone Model')

# Register callback handler for window re-paint event
glutDisplayFunc(display)

# Register callback handler for window re-size event
glutReshapeFunc(reshape)
glEnable(GL_BLEND)

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

glutIdleFunc(display)

# Register the function called when the keyboard is pressed.
glutKeyboardFunc(keyPressed)

# Register the function called when special keys (arrows, page down, etc)
# are pressed.
glutSpecialFunc(specialKeyPressed)

initGL()                       # Our own OpenGL initialization
glutMainLoop()                 # Enter the infinite event-processing loop
