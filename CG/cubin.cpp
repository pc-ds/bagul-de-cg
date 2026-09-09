#include <GL/glut.h>
#include <math.h>

float angle = 0.0f;

void DrawCube() {
    glBegin(GL_QUADS);
        // Front face (red)
        glColor3f(1, 0.3, 1);
        glVertex3f(-1, -1,  1); glVertex3f( 1, -1,  1);
        glVertex3f( 1,  1,  1); glVertex3f(-1,  1,  1);

        // Back face (green)
        glColor3f(1, 0.3, 1);
        glVertex3f(-1, -1, -1); glVertex3f(-1,  1, -1);
        glVertex3f( 1,  1, -1); glVertex3f( 1, -1, -1);

        // Top face (blue)
        glColor3f(1, 0.5, 0.0);
        glVertex3f(-1,  1, -1); glVertex3f(-1,  1,  1);
        glVertex3f( 1,  1,  1); glVertex3f( 1,  1, -1);

        // Bottom face (yellow)
        glColor3f(0, 0, 0);
        glVertex3f(-1, -1, -1); glVertex3f( 1, -1, -1);
        glVertex3f( 1, -1,  1); glVertex3f(-1, -1,  1);

        // Right face (magenta)
        glColor3f(1, 1, 1);
        glVertex3f( 1, -1, -1); glVertex3f( 1,  1, -1);
        glVertex3f( 1,  1,  1); glVertex3f( 1, -1,  1);

        // Left face (cyan)
        glColor3f(0, 0, 0);
        glVertex3f(-1, -1, -1); glVertex3f(-1, -1,  1);
        glVertex3f(-1,  1,  1); glVertex3f(-1,  1, -1);
    glEnd();
}


void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glLoadIdentity();
    

    glTranslatef(0.0f, 0.0f, -6.0f);
    glRotatef(angle, 0.0f, 0.0f, 0.0f);
    DrawCube();

    glutSwapBuffers();
}


void display2() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glLoadIdentity();
    
    float x = sin(angle) * 7;
    float y = cos(angle) * 7;

    
    gluLookAt(
        0, 0, 10, // objeto 
        0, 0, 0, // camera
        0, 1.0, 0.0  // rotação
    );

    DrawCube();
    glTranslatef(3.0f, 0.0f, 0.0f);
    DrawCube();
    glutSwapBuffers();
}

void update(int value) {
    angle += 0.1f;
    glutPostRedisplay();
    glutTimerFunc(16, update, 0); // ~60 fps
}

void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, (double)w / h, 0.1, 100.0);
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("OpenGL Cube");

    glEnable(GL_DEPTH_TEST);
    glClearColor(0.1f, 0.1f, 0.1f, 1.0f);

    glutDisplayFunc(display2);
    glutReshapeFunc(reshape);
    glutTimerFunc(0, update, 0);

    glutMainLoop();
    return 0;
}