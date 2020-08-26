# some useful functions for fractal programs

from DEgraphics import *
from NLDUtils import *
from math import sin, cos, radians

def drawLine(win, startPt, dirDegrees, L, lineThickness=1, lineColor='black'):
    """ceate and daws on a win a line segment that stats at point pointPt with a length of L and a diection of dirDegrees, having a color and thickness specified by LineColor and lineThickness and moves startPt to the end of the segment when done"""

    dirRadians = radians(dirDegrees)

    dx = L * cos(dirRadians)
    dy = L * sin(dirRadians)
    endPt = Point(startPt.x + dx, startPt.y + dy)
    line = Line(startPt, endPt)
    line.setWidth(lineThickness)
    line.setOutline(lineColor)
    startPt.move(dx, dy)

    return line
