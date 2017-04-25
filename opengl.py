from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

window = 0                                             # glut window number
width, height = 1200, 768                               # window size
anglePyramid = 0.0;  # Rotational angle for pyramid [NEW]
angleCube = 0.0;     # Rotational angle for cube [NEW]
refreshMills = 15;        # refresh interval in milliseconds [NEW]

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
	print "we"
	glClearColor(0.0, 0.0, 0.0, 1.0); # Set background color to black and opaque
	glClearDepth(1.0);                   # Set background depth to farthest
	glEnable(GL_DEPTH_TEST);   # Enable depth testing for z-culling
	glDepthFunc(GL_LEQUAL);    # Set the type of depth-test
	glShadeModel(GL_SMOOTH);   # Enable smooth shading
	glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);  # Nice perspective corrections

def display():
	global angleCube
	global anglePyramid
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); # Clear color and depth buffers
	glMatrixMode(GL_MODELVIEW);     # To operate on model-view matrix

	# Render a color-cube consisting of 6 quads with different colors
	glLoadIdentity();                 # Reset the model-view matrix
	glTranslatef(1.5, 0.0, -7.0);  # Move right and into the screen
	glRotatef(angleCube, 1.0, 1.0, 1.0);  # Rotate about (1,1,1)-axis [NEW]

	glBegin(GL_QUADS);                # Begin drawing the color cube with 6 quads
	# Top face (y = 1.0)
	# Define vertices in counter-clockwise (CCW) order with normal pointing out
	glColor3f(0.0, 1.0, 0.0);     # Green
	glVertex3f( 0.6, 1.0, -0.05);
	glVertex3f(-0.6, 1.0, -0.05);
	glVertex3f(-0.6, 1.0,  0.05);
	glVertex3f( 0.6, 1.0,  0.05);

	# Bottom face (y = -1.0)
	glColor3f(1.0, 0.5, 0.0);     # Orange
	glVertex3f( 0.6, -1.0,  0.05);
	glVertex3f(-0.6, -1.0,  0.05);
	glVertex3f(-0.6, -1.0, -0.05);
	glVertex3f( 0.6, -1.0, -0.05);

	# Front face  (z = 1.0)
	glColor3f(1.0, 0.0, 0.0);     # Red
	glVertex3f( 0.6,  1.0, 0.05);
	glVertex3f(-0.6,  1.0, 0.05);
	glVertex3f(-0.6, -1.0, 0.05);
	glVertex3f( 0.6, -1.0, 0.05);

	# Back face (z = -1.0)
	glColor3f(1.0, 1.0, 0.0);     # Yellow
	glVertex3f( 0.6, -1.0, -0.05);
	glVertex3f(-0.6, -1.0, -0.05);
	glVertex3f(-0.6,  1.0, -0.05);
	glVertex3f( 0.6,  1.0, -0.05);

	# Left face (x = -1.0)
	glColor3f(0.0, 0.0, 1.0);     # Blue
	glVertex3f(-0.6,  1.0,  0.05);
	glVertex3f(-0.6,  1.0, -0.05);
	glVertex3f(-0.6, -1.0, -0.05);
	glVertex3f(-0.6, -1.0,  0.05);

	# Right face (x = 1.0)
	glColor3f(1.0, 0.0, 1.0);     # Magenta
	glVertex3f(0.6,  1.0, -0.05);
	glVertex3f(0.6,  1.0,  0.05);
	glVertex3f(0.6, -1.0,  0.05);
	glVertex3f(0.6, -1.0, -0.05);
	glEnd();  # End of drawing color-cube

	glutSwapBuffers();  # Swap the front and back frame buffers (double buffering)

	# Update the rotational angle after each refresh [NEW]
	anglePyramid = anglePyramid + 0.2;
	angleCube = angleCube + 0.15;
	print "Wa"

def reshape(width, height):
	print "wi"
	# Compute aspect ratio of the new window
	if (height == 0): height = 1;                # To prevent divide by 0
	aspect = float(width) / float(height);

	# Set the viewport to cover the new window
	glViewport(0, 0, width, height);

	# Set the aspect ratio of the clipping volume to match the viewport
	glMatrixMode(GL_PROJECTION);  # To operate on the Projection matrix
	glLoadIdentity();             # Reset
	# Enable perspective projection with fovy, aspect, zNear and zFar
	gluPerspective(45.0, aspect, 0.1, 100.0);

def timer(value):
	glutPostRedisplay();      # Post re-paint request to activate display()
	glutTimerFunc(refreshMills, timer, 0); # next timer call milliseconds later

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_DOUBLE); # Enable double buffered mode
glutInitWindowSize(640, 480);   # Set the window's initial width & height
glutInitWindowPosition(50, 50); # Position the window's initial top-left corner
glutCreateWindow("waw");          # Create window with the given title
glutDisplayFunc(display);       # Register callback handler for window re-paint event
glutReshapeFunc(reshape);       # Register callback handler for window re-size event
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glutIdleFunc(display)    
initGL();                       # Our own OpenGL initialization
glutMainLoop();                 # Enter the infinite event-processing loop
