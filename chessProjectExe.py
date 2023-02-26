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
    QLayout,
    QLayoutItem,
    QVBoxLayout,
    QStackedLayout
)
from PyQt6.QtGui import QPalette, QColor, QPixmap
from PyQt6.QtCore import Qt, QRect, QSize
from ChessPieces import ChessPieces

whitePieces = ChessPieces(True)
blackPieces = ChessPieces(False)

# hello.py
# ...

# 2. Create an instance of QApplication
app = QApplication([])
# hello.py
# ...

# 3. Create your application's GUI
cols = ['a','b','c','d','e','f','g','h']
rows = ['8','7','6','5','4','3','2','1']
window = QWidget()
window.setWindowTitle("Chess Project")
window.setGeometry(50, 50, 800,800)
window.setAutoFillBackground(True)
backgroundColor = window.palette()
backgroundColor.setColor(QPalette.ColorRole.Window, QColor('gray'))
window.setPalette(backgroundColor)
layout = QVBoxLayout()
board = QGridLayout()
square = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            color = 'white'
        else:
            color = 'green'
            
        square = QStackedLayout()
        square.setGeometry(QRect(1,1,35,35))
        square.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        square.setStackingMode(QStackedLayout.StackingMode.StackAll)
        background = QLabel(rows[i]+cols[j])
        background.setAutoFillBackground(True)
        palette = background.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        background.setPalette(palette)
        background.setStyleSheet("QLabel {color: gray; vertical-align: bottom;}")
        background.setAlignment(Qt.AlignmentFlag.AlignBottom)
        background.setGeometry(QRect(1,1,35,35))
        square.addWidget(background)
        
        board.addLayout(square, i, j)
for i in whitePieces.pieces:
    imageName = 'imagesResized\white' + i.piece
    piece = QLabel()
    piecePic = QPixmap(imageName)
    piecePic.scaledToHeight(35)
    piece.setPixmap(piecePic)
    piece.setGeometry(QRect(1,1,35,35))
    piece.setAlignment(Qt.AlignmentFlag.AlignCenter)
    square = board.itemAtPosition(i.col,i.row).layout()
    square.addWidget(piece)
    square.setCurrentWidget(piece)
for i in blackPieces.pieces:
    imageName = 'imagesResized\\black' + i.piece
    print(imageName)
    piece = QLabel()
    piecePic = QPixmap(imageName)
    piecePic.scaledToHeight(35)
    piece.setPixmap(piecePic)
    piece.setGeometry(QRect(1,1,35,35))
    piece.setAlignment(Qt.AlignmentFlag.AlignCenter)
    square = board.itemAtPosition(i.col,i.row).layout()
    square.addWidget(piece)
    square.setCurrentWidget(piece)
layout.addLayout(board)
window.setLayout(layout)

window.show()
sys.exit(app.exec())

