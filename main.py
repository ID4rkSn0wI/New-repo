import random
import sys

from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QColor

from UI import UI
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyWidget(QMainWindow, UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createButton.clicked.connect(self.create)
        self.paint = False

    def create(self):
        self.paint = True
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.paint:
            self.drawing(qp)
            self.paint = False
        qp.end()

    def drawing(self, qp):
        size = random.randint(20, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(QPointF(random.randint(0, self.width()), random.randint(0, self.height())), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
