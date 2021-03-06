import sys

from PySide import QtGui

try:
    from OpenGL.GL import *
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "OpenGL grabber",
                               "PyOpenGL must be installed to run this example.")
    sys.exit(1)


class Triangle:
    def __init__(self, center_x, center_y, width):
        self.centerX = center_x
        self.centerY = center_y
        self.width = width

    def render(self):
        glBegin(GL_TRIANGLES)
        self.centerX +=1.0
        x1 = self.centerX
        x2 = self.centerX - self.width / 2
        x3 = self.centerX + self.width / 2
        y1 = self.centerY + self.width / 2
        y2 = self.centerY - self.width / 2
        y3 = self.centerY - self.width / 2

        glColor3f(100, 122, 0.3)

        glVertex3f(x1, y1, 0);
        glVertex3f(x2, y2, 0);
        glVertex3f(x3, y3, 0);
        glEnd()
