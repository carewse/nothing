#!/usr/bin/env python
from enum import Enum, unique

@unique
class Colour(Enum):
    black=0
    red=1

class Postion():
    def __init__(self,xAxis,yAxis):
        self.xAxis = xAxis
        self.yAxis = yAxis

class Chess():

    def __init__(self,colour,xAxis,yAxis):
        self.colour = colour
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.postion = Postion(xAxis,yAxis)

    def __str__(self):
        return "x:%s y:%s colour:%s " % (self.xAxis,self.yAxis,self.colour)

class Chessboard():
    """

    """

    #longNum make the num of x, latNum make the num of y
    def __init__(self,xAxis,yAxis,gobangNum=5):
        if xAxis<3 or yAxis<2 :
            raise ValueError("chessboard's xAxis or yAxis lt 10")
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.points = [[None for _ in range(xAxis)] for _ in range(yAxis)]
        self.gobangNum = gobangNum

    def move(self,chess):
        if chess.xAxis < 0 or chess.xAxis > self.xAxis - 1:
            raise ValueError("chess's x-axis postion is wrong")
        if chess.yAxis < 0 or chess.yAxis > self.yAxis - 1:
            raise ValueError("chess's y-axis postion is wrong")
        point = self.points[chess.yAxis][chess.xAxis]
        if not point is None:
            raise ValueError("this postion already exists a chess already")
        self.points[chess.yAxis][chess.xAxis] = chess
        return self.__checkWin(chess)

    def getChess(self,postion):
        if postion.xAxis < 0 or postion.yAxis < 0:
            return None
        if postion.xAxis > self.longNum - 1 or postion.yAxis > self.latNum - 1:
            return None
        return self.points[postion.yAxis][postion.xAxis]


    def __checkWin(self,chess):
        xpoint = chess.xAxis
        ypoint = chess.yAxis
        xlinkedBeads = 0
        _xlinkedBeads = 0
        ylinkedBeads = 0
        _ylinkedBeads = 0
        xylinkedBeads = 0
        _xylinkedBeads = 0
        x_ylinkedBeads = 0
        _x_ylinkedBeads = 0

        xlinkedBeadsFlag = True
        _xlinkedBeadsFlag = True
        ylinkedBeadsFlag = True
        _ylinkedBeadsFlag = True
        xylinkedBeadsFlag = True
        _xylinkedBeadsFlag = True
        x_ylinkedBeadsFlag = True
        _x_ylinkedBeadsFlag = True
        for i in range(1,self.gobangNum):
            xltZ = xpoint - i < 0
            xgtM = xpoint + i > len(self.points[0]) - 1
            yltZ = ypoint - i < 0
            ygtM = ypoint + i > len(self.points) - 1

            XpointChess = None if xgtM else self.points[ypoint][xpoint + i]
            _XpointChess = None if xltZ else self.points[ypoint][xpoint - i]
            YpointChess = None if ygtM else self.points[ypoint + i][xpoint]
            _YpointChess = None if yltZ else self.points[ypoint - i][xpoint]
            XYpointChess = None if xgtM or ygtM else self.points[ypoint + i][xpoint + i]
            _XYpointChess = None if xltZ or ygtM else self.points[ypoint + i][xpoint - i]
            X_YpointChess = None if xgtM or yltZ else self.points[ypoint - i][xpoint + i]
            _X_YpointChess = None if xltZ or yltZ else self.points[ypoint - i][xpoint - i]
            # x
            if (XpointChess != None and XpointChess.colour == chess.colour)  and xlinkedBeadsFlag:
                xlinkedBeads = xlinkedBeads + 1
            else:
                xlinkedBeadsFlag = False

            if (_XpointChess != None and _XpointChess.colour == chess.colour) and _xlinkedBeadsFlag:
                _xlinkedBeads = _xlinkedBeads + 1
            else:
                _xlinkedBeadsFlag = False

            # y
            if (YpointChess != None and YpointChess.colour == chess.colour) and ylinkedBeadsFlag:
                ylinkedBeads = ylinkedBeads + 1
            else:
                ylinkedBeadsFlag = False

            if (_YpointChess != None and _YpointChess.colour == chess.colour) and _ylinkedBeadsFlag:
                _ylinkedBeads = _ylinkedBeads + 1
            else:
                _ylinkedBeadsFlag = False;

            # xy
            if (_X_YpointChess != None and _X_YpointChess.colour == chess.colour) and _x_ylinkedBeadsFlag:
                _x_ylinkedBeads = _x_ylinkedBeads +1
            else:
                _x_ylinkedBeadsFlag = False

            if (XYpointChess != None and XYpointChess.colour == chess.colour) and xylinkedBeadsFlag:
                xylinkedBeads = xylinkedBeads + 1
            else:
                xylinkedBeadsFlag = False

            # x_y
            if (_XYpointChess != None and _XYpointChess.colour == chess.colour) and _xylinkedBeadsFlag:
                _xylinkedBeads = _xylinkedBeads + 1
            else:
                _xylinkedBeadsFlag = False;

            if (X_YpointChess != None and X_YpointChess.colour == chess.colour) and x_ylinkedBeadsFlag:
                x_ylinkedBeads = x_ylinkedBeads + 1
            else:
                x_ylinkedBeadsFlag = False
            if xlinkedBeads + _xlinkedBeads >= self.gobangNum - 1 or ylinkedBeads + _ylinkedBeads >= self.gobangNum - 1 or _x_ylinkedBeads + xylinkedBeads >= self.gobangNum - 1 or _xylinkedBeads + x_ylinkedBeads >= self.gobangNum - 1:
                return True
        return False

    def __str__(self):
        boardStr = ''
        for xpoints in self.points[::-1]:
            for point in xpoints:
                if not point is None:
                    boardStr = boardStr + str(point.colour.value) + ' '
                else:
                    boardStr = boardStr + 'x '
            boardStr = boardStr + '\n'
        return boardStr


try:
    chessboard = Chessboard(5,5,3)
    chess0 = Chess(Colour.black,0,0)
    chess1 = Chess(Colour.black,0,1)
    chess2 = Chess(Colour.black,2,2)
    chess3 = Chess(Colour.black,3,3)
    chess4 = Chess(Colour.black,4,4)
    chess5 = Chess(Colour.black,5,5)
    chessboard.move(chess0)
    chessboard.move(chess1)
    chessboard.move(chess2)
    chessboard.move(chess3)
    #chessboard.move(chess5)
    #chessboard.move(chess4)
    if chessboard.move(chess4):
        print("win!!!")
    print(chessboard)
except ValueError as ve:
    print(str(ve))
