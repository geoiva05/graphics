# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_painter


class drawer(QMainWindow, Ui_painter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
ex = drawer()


def flexing(x, a, b, c):
    return a * x * x + b * x + c


def running():
    try:
        left, rigth = int(ex.left.text()), int(ex.right.text())
    except:
        left, rigth = -1000, 1000

    try:
        a, b, c = int(ex.koff_a.text()), int(ex.koff_b.text()), int(ex.koff_c.text())
    except:
        a, b, c = 1, 1, 1

    ex.graphicsView.clear()
    ex.graphicsView.plot([i for i in range(left, rigth + 1)], [flexing(j, a, b, c) for j in range(left, rigth + 1)],
                         pen='r')


ex.draw_graphics.clicked.connect(running)
ex.show()
sys.exit(app.exec_())
