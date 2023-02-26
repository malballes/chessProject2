# hello.py

"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
    QLabel,
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
# hello.py
# ...

# 2. Create an instance of QApplication
app = QApplication([])
# hello.py
# ...

# 3. Create your application's GUI
rows = ['a','b','c','d','e','f','g','h']
cols = ['8','7','6','5','4','3','2','1']
window = QWidget()
window.setWindowTitle("Chess Project")
window.setGeometry(100, 100, 800,800)
layout = QGridLayout()
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            color = 'black'
        else:
            color = 'green'
        widget = QLabel(rows[i]+cols[j])
        widget.setAutoFillBackground(True)
        palette = widget.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        widget.setPalette(palette)
        widget.setStyleSheet("QLabel {color: white; vertical-align: bottom;}")
        widget.setAlignment(Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(widget, j, i)
window.setLayout(layout)

window.show()
sys.exit(app.exec())