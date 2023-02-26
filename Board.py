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
from functools import partial

class Board():
    def __init__(self, board, whitePieces, blackPieces):
        self.board = board
        self.whitePieces = whitePieces
        self.blackPieces = blackPieces
        self.rows = ['8','7','6','5','4','3','2','1']
        self.cols = ['a','b','c','d','e','f','g','h']

    def createBoard(self, isFlipped):
        for i in range(8):
            for j in range(8):
                row = i
                col = j
                if isFlipped:
                    row = 7-i
                    col = 7-j
                if (i + j) % 2 == 0:
                    color = 'white'
                else:
                    color = 'green' 
                square = QStackedLayout()
                square.setGeometry(QRect(1,1,35,35))
                square.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
                square.setStackingMode(QStackedLayout.StackingMode.StackAll)
                background = QLabel(self.rows[row]+self.cols[col])
                background.setAutoFillBackground(True)
                palette = background.palette()
                palette.setColor(QPalette.ColorRole.Window, QColor(color))
                background.setPalette(palette)
                background.setStyleSheet("QLabel {color: gray; vertical-align: bottom;}")
                background.setAlignment(Qt.AlignmentFlag.AlignBottom)
                background.setGeometry(QRect(1,1,35,35))
                square.addWidget(background)
                self.board.addLayout(square, i, j)
        
        for i in self.whitePieces.pieces:
            imageName = 'imagesResized\white' + i.piece
            piece = QLabel()
            piecePic = QPixmap(imageName)
            piecePic.scaledToHeight(35)
            piece.setPixmap(piecePic)
            piece.setGeometry(QRect(1,1,35,35))
            piece.setAlignment(Qt.AlignmentFlag.AlignCenter)
            piece.mousePressEvent = partial(self.selectPiece,i)
            col = i.col
            row = i.row
            if isFlipped:
                col = 7-i.col
                row = 7-i.row
            square = self.board.itemAtPosition(col,row).layout()
            square.addWidget(piece)
            square.setCurrentWidget(piece)
        for i in self.blackPieces.pieces:
            imageName = 'imagesResized\\black' + i.piece
            piece = QLabel()
            piecePic = QPixmap(imageName)
            piecePic.scaledToHeight(35)
            piece.setPixmap(piecePic)
            piece.setGeometry(QRect(1,1,35,35))
            piece.setAlignment(Qt.AlignmentFlag.AlignCenter)
            piece.mousePressEvent = partial(self.selectPiece,i)
            col = i.col
            row = i.row
            if isFlipped:
                col = 7-i.col
                row = 7-i.row
            square = self.board.itemAtPosition(col,row).layout()
            square.addWidget(piece)
            square.setCurrentWidget(piece)

    def selectPiece(self,chessPiece, event):
        print("Piece Clicked:")
        print(event)
        print(chessPiece.__str__())
         




