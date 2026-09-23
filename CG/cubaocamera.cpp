#include <GL/glut.h>
#include <math.h>

void desenharCubao(){
    glColor3f(1.0f, 0.7f, 0.0f);
    glutSolidCube(1);
}

double camy = 0, camx = 0;

void arrow_keys(int a_key, int x, int y){
    switch(a_key){
        case GLUT_KEY_UP:
            if(camy >= 90) camy = 0;    
            camy -= 0.5;
            break;
        case GLUT_KEY_DOWN:
            if(camy >= 90) camy = 0;
            camy += 0.5;
            break;
        case GLUT_KEY_LEFT:
            if(camx >= 90) camx = 0;
            camx -= 0.5;
            break;
        case GLUT_KEY_RIGHT:
            if(camx >= 90) camx = 0;
            camx += 0.5;
            break;
    }
    glutPostRedisplay();
}

void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, (double)w / h, 0.1, 100.0);
    glMatrixMode(GL_MODELVIEW);
}

void display(){
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    

    gluLookAt(
        camx, camy, 10.0,
        0.0, 0.0, 0.0,
        0.0, 1.0, 0.0
    );
    camx = sin(camx) * 5;
    camy = cos(camy) * 5;
    glutWireTeapot(2);
    glTranslatef(0.0f, 2.0f, 0.0f);
    desenharCubao();
    glutSwapBuffers();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Cubao");

    glEnable(GL_DEPTH_TEST);
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glutReshapeFunc(reshape);
    glutSpecialFunc(arrow_keys);
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
