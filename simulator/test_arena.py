from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

def init():
    global m, r, a, v, rad, colr, colg, colb
    glClearColor(0.0, 0.0, 0.0, 1.0)
    # Enable depth testing for true 3D effects

    glEnable(GL_DEPTH_TEST)

    # Add lighting and shading effects
    glShadeModel(GL_SMOOTH)
    lightdiffuse = [1.0, 1.0, 1.0, 1.0]
    lightposition = [1.0, 1.0, 1.0, 0.0]
    lightambient = [0.0, 0.0, 0.0, 1.0]
    lightspecular = [1.0, 1.0, 1.0, 1.0]

    # Turn on the light
    glLightfv(GL_LIGHT1, GL_DIFFUSE, lightdiffuse)
    glLightfv(GL_LIGHT1, GL_POSITION, lightposition)
    glLightfv(GL_LIGHT1, GL_AMBIENT, lightambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, lightdiffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, lightspecular)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)


def keyboard(key, x, y):
    # Allows us to quit by pressing 'Esc' or 'q'
    if key == chr(27):
        sys.exit()
    if key == "q":
        sys.exit()


def plotfunc():
    alpha = 0
    beta = 0
    gamma = 0
    screen_X = 600
    screen_Y = 600
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(45, 1, 0.1, 4000)
    glViewport(0, 0, screen_X, screen_Y)
    glPushMatrix()
    glTranslatef(0, 0, -2)
    glRotatef(alpha, 1, 0, 0)
    glRotatef(beta, 0, 1, 0)
    glRotatef(gamma, 0, 0, 1)

    # glLoadIdentity()
    glutWireCube(0.5)
    glPopMatrix()
    glFlush()


def main():
    width = 600
    height = 600
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Test Arena")
    glutDisplayFunc(plotfunc)
    glutKeyboardFunc(keyboard)

    # init()
    glutMainLoop()

main()
