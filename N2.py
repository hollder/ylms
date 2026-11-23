import sys

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from random import randint


class Yellow_Circles(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('кружочки')

        self.btn = QPushButton('круг', self)
        self.btn.move(300, 20)
        self.btn.resize(120, 30)
        self.btn.clicked.connect(self.trigger_paint)

        self.do_paint = False

    def trigger_paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        center = QPoint(randint(10, 500), randint(10, 500))
        rad = randint(10, 50)
        qp.drawEllipse(center, rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow_Circles()
    ex.show()
    sys.exit(app.exec())