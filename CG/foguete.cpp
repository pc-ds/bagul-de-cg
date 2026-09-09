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

void DrawTip() {
    glBegin(GL_TRIANGLES);
        glColor3f(0.0, 1.0, 0.0);
        glVertex3f(3.0,6.0,0);
        glVertex3f(4.0, 8.0,0);
        glVertex3f(5.0,6.0,0);
    glEnd();
}

void DrawBody(){
    glBegin(GL_QUADS);
        glColor3f(0.99, 0.05, 0.55);
        glVertex3f(3.0,1.0,0);
        glVertex3f(5.0, 1.0,0);
        glVertex3f(5.0,6.0,0);
        glVertex3f(3.0,6.0,0);
    glEnd();
}

void DrawLWing(){
    glBegin(GL_TRIANGLES);glRotatef(angle, 4.0f, 4.0f, 0.0f);
        glColor3f(1,0,0);
        glVertex3f(1.5,1.0,0);
        glVertex3f(3.0, 1.0,0);
        glVertex3f(3.0,3.0,0);
    glEnd();
}

void DrawRWing(){
    glBegin(GL_TRIANGLES);
        glColor3f(1,0,0);
        glVertex3f(5.0,1.0,0);
        glVertex3f(6.5, 1.0,0);
        glVertex3f(5.0,3.0,0);
    glEnd();
}
void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glLoadIdentity();
    
    gluLookAt(
        0, 0, 20, // objeto 
        0, 0, 0, // camera
        0, 1.0, 0  // rotação
    );

    glRotatef(angle, 0.0f, 1.0f, 0.0f);
    glTranslatef(-2.0f, -2.0f, 0.0f);
    glScalef(0.5f,0.5f,0.5f);    
    DrawTip();
    DrawBody();
    DrawLWing();
    DrawRWing();

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

    DrawTip();
    glTranslatef(0.0f, 0.0f, 0.0f);
    DrawCube();
    glutSwapBuffers();
}

void update(int value) {
    angle += 1.0f;
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
    glutInitWindowSize(1024, 800);
    glutCreateWindow("OpenGL Rocket");

    glEnable(GL_DEPTH_TEST);
    glClearColor(0.1f, 0.1f, 0.1f, 1.0f);

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutTimerFunc(0, update, 0);

    glutMainLoop();
    return 0;
}