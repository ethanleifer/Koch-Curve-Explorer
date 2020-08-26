"""
File Name: kochCurveExplorerFinal
Project: Koch Curve Explorer
Made By: Ethan Leifer
Orginal Dependences: DEgraphics.py, fractUtils.py (both in this directory)
Description: This project creates a koch curve and a koch polygon.

Note:
    1 Error I found that if you click draw, clear, change point, draw
    it draws both the old curve (the one you just cleared) and the new curve (with the updated center point)
"""


# imports
from DEgraphics import *
from fractUtils import *
from NLDUtils import *
from math import cos, tan, atan, sin, sqrt, acos, degrees, log, radians, pow
import time
from tkinter import colorchooser

# CONSTANTS

# font used on gui's
FONT = "arial"

# list of colors for polygon coloring
COLORS = [color_rgb(0, 255, 0), color_rgb(255, 0, 0), color_rgb(125, 0 , 125), color_rgb(0, 0, 255), color_rgb(255, 255, 0), color_rgb(255, 0, 255), color_rgb(0, 255, 255), color_rgb(125, 125, 125), color_rgb(0, 125, 0)]


# list of koch polygon objects
kochPolygons = []

# create graph windows
win = DEGraphWin(title='Koch Curve Explorer Window', hBGColor='black', width=400, height=400)
gui = DEGraphWin(title='GUI', width=600, height=400, offsets=[win.width, 0], defCoords=[0, 0, 10, 6], hBGColor='black')
gui.displayGrid()

# create gui

# title text object
txtTitle = Text(Point(4, 5.5), "Koch Curve Explorer")
txtTitle.setFace(FONT)
txtTitle.setSize(30)
txtTitle.draw(gui)

# main buttons
btnExit = SimpleButton(win=gui, topLeft=Point(.1, .9), width=3.8, height=.8, label='EXIT', font=(FONT, 35),
                       buttonColor='red', )
btnDraw = SimpleButton(win=gui, topLeft=Point(4.1, .9), width=3.8, height=.8, label="DRAW", font=(FONT, 35),
                       buttonColor='blue', textColor='white')
btnClear = SimpleButton(win=gui, topLeft=Point(2.1, 1.9), width=1.8, height=.8, label="CLEAR", font=(FONT, 25),
                        buttonColor='blue', textColor='white')
btnPolygons = SimpleButton(win=gui, topLeft=Point(.1, 1.9), width=1.8, height=.8, label="SHOW\nPOLYGONS",
                              font=(FONT, 20), buttonColor='blue', textColor='white')
btnZoomIn = SimpleButton(win=gui, topLeft=Point(.1, 2.9), width=1.8, height=.8, label="ZOOM\nIN", font=(FONT, 20),
                         buttonColor='blue', textColor='white')
btnZoomOut = SimpleButton(win=gui, topLeft=Point(2.1, 2.9), width=1.8, height=.8, label="ZOOM\nOUT", font=(FONT, 20),
                          buttonColor='blue', textColor='white')


# text boxes without direct entry to display information about the Koch Curve
txtLength = Text(Point(2, 4.8), "Length of each Koch Curve = ")
txtLength.draw(gui)
txtDistanceComparision = Text(Point(2, 4.5), "")
txtDistanceComparision.draw(gui)
txtSimilarityDimension = Text(Point(2, 4.2), "Similarity Dimension = ")
txtSimilarityDimension.draw(gui)

# sides entry
entSides = IntEntry(Point(5, 2.25), width=10, span=[0, 500])
entSides.draw(gui)
entSides.setFace(FONT)
btnEnterSides = SimpleButton(gui, topLeft=Point(6.1, 2.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                             buttonColor='blue', textColor='white')
txtSides = Text(Point(5, 2.75), "# of Sides = ")
txtSides.setFace(FONT)
txtSides.draw(gui)

# levels entry
entLevels = IntEntry(Point(5, 1.25), width=10, span=[0, 8])
entLevels.draw(gui)
entLevels.setFace(FONT)
btnEnterLevels = SimpleButton(gui, topLeft=Point(6.1, 1.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                              buttonColor='blue', textColor='white')
txtLevels = Text(Point(5, 1.75), "# of Levels = ")
txtLevels.setFace(FONT)
txtLevels.draw(gui)

# change center point
btnChangeCenterPoint = SimpleButton(win=gui, topLeft=Point(0.1, 3.9), width=1.8, height=.8,
                                    label="CHANGE\nCENTER\nPOINT", font=(FONT, 15), buttonColor='blue',
                                    textColor='white')
txtCircleCenterTitle = Text(Point(3, 3.75), "( X  ,  Y )")
txtCircleCenterTitle.setFace(FONT)
txtCircleCenterTitle.setSize(20)
txtCircleCenterTitle.draw(gui)
txtCircleCenterPoint = Text(Point(3, 3.25), "")
txtCircleCenterPoint.setFace(FONT)
txtCircleCenterPoint.setSize(20)
txtCircleCenterPoint.draw(gui)

# radius entry
entRadius = IntEntry(Point(5, 3.25), width=10, span=[0, 10])
entRadius.draw(gui)
entRadius.setFace(FONT)
btnEnterRadius = SimpleButton(gui, topLeft=Point(6.1, 3.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                              buttonColor='blue', textColor='white')
txtRadius = Text(Point(5, 3.75), "Radius = ")
txtRadius.setFace(FONT)
txtRadius.draw(gui)

# KCangle entry
entKCAngle = IntEntry(Point(5, 4.25), width=10, span=[0, 90])
entKCAngle.draw(gui)
entKCAngle.setFace(FONT)
btnEnterKCAngle = SimpleButton(gui, topLeft=Point(6.1, 4.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                              buttonColor='blue', textColor='white')
txtKCAngle = Text(Point(5, 4.75), "KC Angle = ")
txtKCAngle.setFace(FONT)
txtKCAngle.draw(gui)

# line color options
txtLineColor = Text(Point(9, 5.5), "Line\nColor:")
txtLineColor.setFace(FONT)
txtLineColor.setSize(20)
txtLineColor.draw(gui)
btnLineColorBlack = SimpleButton(gui, topLeft=Point(8.1, 4.9), width=.8, height=.8, label="", buttonColor="Black",
                                 edgeColor="Light Green", edgeWidth=2)
btnLineColorBlue = SimpleButton(gui, topLeft=Point(9.1, 4.9), width=.8, height=.8, label="", buttonColor="Blue",
                                 edgeColor="Black", edgeWidth=2)
btnLineColorRed = SimpleButton(gui, topLeft=Point(8.1, 3.9), width=.8, height=.8, label="", buttonColor="Red",
                                 edgeColor="Black", edgeWidth=2)
btnLineColorWhite = SimpleButton(gui, topLeft=Point(9.1, 3.9), width=.8, height=.8, label="", buttonColor="White",
                                 edgeColor="Black", edgeWidth=2)

# background color options
txtBackgroundColor = Text(Point(9, 2.5), "Background\nColor:")
txtBackgroundColor.setFace(FONT)
txtBackgroundColor.setSize(20)
txtBackgroundColor.draw(gui)
btnBackgroundColorBlack = SimpleButton(gui, topLeft=Point(8.1, 1.9), width=.8, height=.8, label="", buttonColor="Black",
                                 edgeColor="Black", edgeWidth=2)
btnBackgroundColorBlue = SimpleButton(gui, topLeft=Point(9.1, 1.9), width=.8, height=.8, label="", buttonColor="Blue",
                                 edgeColor="Black", edgeWidth=2)
btnBackgroundColorRed = SimpleButton(gui, topLeft=Point(8.1, 0.9), width=.8, height=.8, label="", buttonColor="Red",
                                 edgeColor="Black", edgeWidth=2)
btnBackgroundColorWhite = SimpleButton(gui, topLeft=Point(9.1, 0.9), width=.8, height=.8, label="", buttonColor="White",
                                 edgeColor="Light Green", edgeWidth=2)


buttonsActive = False


class kochPolygon():

    def __init__(self, win, center, radius, sides, levels, KCangle):
        self.win = win
        self.center = center
        self.radius = radius
        self.circle = Circle(self.center, self.radius)
        self.sides = sides
        self.levels = levels
        self.isDrawn = False
        self.lines = []
        self.triangles = []
        self.showTriangles = True
        self.initialPoint = p = Point(0, radius)
        self.KCangle = KCangle
        self.length = 0
        self.area = None
        self.inclinationAngle = 0
        self.lineColor= "Black"

    def generateKochCurveManager(self):
        '''draws the koch curve polygon'''

        # if the sides = 1 or 2 draw either a straight line or two straight lines with one flipped
        if self.sides == 1:
            self.length = self.circle.radius * 2
            self.generateKochCurve(self.win, self.levels, self.inclinationAngle, self.KCangle,
                                   Point(self.circle.p1.getX(), self.circle.center.getY()), self.length)

        elif self.sides == 2:
            self.length = self.circle.radius * 2
            self.generateKochCurve(self.win, self.levels, self.inclinationAngle, self.KCangle,
                                   Point(self.circle.p1.getX(), self.circle.center.getY()), self.length)
            self.generateKochCurve(self.win, self.levels, self.inclinationAngle, -self.KCangle,
                                   Point(self.circle.p1.getX(), self.circle.center.getY()), self.length)
        # sides > 2
        else:
            # compute interior angle (This is a modified interior angle formula that I created)
            interiorAngle = ((self.sides - 2) * (180 / self.sides)) / 2

            # calculate the length of one side
            p0 = self.initialPoint
            changeAngle = radians(90 - 360 / self.sides)
            p1 = Point(self.circle.radius * cos(changeAngle), self.circle.radius * sin(changeAngle))
            self.length = sqrt((p0.getX() - p1.getX()) ** 2 + (p0.getY() - p1.getY()) ** 2)
            p = p0

            # if the number of sides is even
            if self.sides % 2 == 0:
                # I came up with this through trial and error and trying to line up
                # the end points of the curve onto a circle
                # (you can uncomment the draw circle lines in the (un)drawKochCurve functions if you want to see it)

                divider = (self.sides - 2) / 2

                sideNum, sideMult = 1, 1

                while sideNum <= self.sides:
                    self.generateKochCurve(self.win, self.levels,
                                           self.inclinationAngle - interiorAngle / divider * sideMult, self.KCangle, p,
                                           self.length)
                    sideNum += 1
                    sideMult += 2

            # if the number of sides is odd
            else:
                # again this is a formula I came up with while trying to line my points up on the circle
                exteriorAngle = 90 - interiorAngle

                sideNum, sideMult = 1, 1

                while sideNum <= self.sides:
                    self.generateKochCurve(self.win, self.levels, self.inclinationAngle - exteriorAngle * sideMult,
                                           self.KCangle, p, self.length)
                    sideNum += 1
                    sideMult += 2

    def generateKochCurve(self, win, levels, inclinationAngle, KCangle, p, length):
        '''recursive algorithm that draws a specific Koch Curve'''

        # base case: draw a straight line
        if levels == 0:
            self.lines.append(drawLine(win, p, inclinationAngle, length, lineColor=self.lineColor))

        else:
            # split the length into 4 segments
            newLength = length / (2 * (1 + cos(radians(KCangle))))

            # iterate the 4 segments
            self.generateKochCurve(win, levels - 1, inclinationAngle, KCangle, p, newLength)
            p3 = p.clone()
            self.generateKochCurve(win, levels - 1, inclinationAngle + KCangle, KCangle, p, newLength)
            p1 = p.clone()
            self.generateKochCurve(win, levels - 1, inclinationAngle - KCangle, KCangle, p, newLength)
            p2 = p.clone()
            self.generateKochCurve(win, levels - 1, inclinationAngle, KCangle, p, newLength)

            # create the triange on those segments
            poly = Polygon([p1, p2, p3])
            color = COLORS[levels]
            poly.setFill(color)
            poly.setWidth(0)
            self.triangles.append(poly)

    def drawKochCurve(self):
        for l in self.lines:
            if not (l.isDrawn()):
                l.draw(self.win)

        if self.showTriangles:
            for t in self.triangles:
                if not (t.isDrawn()):
                    t.setOutline(self.lineColor)
                    t.draw(self.win)
        # uncomment line below if you want to see the underlying circle (make sure you uncomment line in undrawKochCurve)
        # self.circle.draw(self.win)

        self.isDrawn = True

    def undrawKochCurve(self):
        for l in self.lines:
            l.undraw()
        if len(self.triangles) > 0:
            for t in self.triangles:
                t.undraw()

        # uncomment line below if you want to see the underlying circle (make sure you uncomment line in drawKochCurve)
        # self.circle.draw(self.win)
        
        self.isDrawn = False

    def resetKochCurveObjects(self):
        '''update the KochCurve Objects to a new curve'''
        self.lines = []
        self.triangles = []
        self.generateKochCurveManager()

    def setSides(self, sides):
        '''Set number of sides to sides'''
        self.sides = sides

    def setKCangle(self, KCangle):
        '''Set Koch Curve angle to KCangle'''
        self.KCangle = KCangle

    def setLevels(self, levels):
        '''Set number of levels to levels'''
        self.levels = levels

    def setInitialPoint(self, p):
        '''Set intial point to p'''
        self.initialPoint = p

    def setRadius(self, radius):
        '''Set radius to radius'''
        self.radius = radius
        self.circle = Circle(self.center, self.radius)

    def setCenter(self, center):
        '''Set center point to center'''
        self.center = center
        self.circle = Circle(self.center, self.radius)

    def setLineColor(self, lineColor):
        '''Set line color to lineColor'''
        self.lineColor = lineColor

    def getDistance(self):
        "returns the length of the koch curve"
        numberOfSides = self.sides * 3 * pow(4, self.levels)
        lengthOfSide = self.length * pow(3, self.levels)
        return numberOfSides * lengthOfSide


    def getSimilarityDimension(self):
        '''returns the similarity dimension of the last draw koch polygon'''
        return (2 * log(2))/(log(2 * (1+cos(radians(self.KCangle)))))

    def __repr__(self):
        '''returns a string representation of the KochPolygon Object'''
        return "KochPolygon(sides: " + str(self.sides) + ", levels: " + str(self.levels) + ", radius: " + str(
            self.radius) + ", center:" + str(self.center) + ", initial point: " + str(
            self.initialPoint) + ", area: " + str(self.getArea()) + ", length: " + str(
            self.length) + ", koch angle: " + str(self.KCangle) + ", is Drawn: " + str(self.isDrawn)

    def __str__(self):
        return self.__repr__()


def updateTextBoxes(kcPoly):
    ''' update the text boxes on gui to match the element of the kcPoly'''
    txtLength.setText("Length of each Koch Curve = " + str(round(convertToMeters(kcPoly.getDistance()), 3))+ " m")
    txtDistanceComparision.setText("This compares to: " + getDistanceConversion(convertToMeters(kcPoly.getDistance())))
    txtSides.setText("# of Sides = " + str(kcPoly.sides))
    txtLevels.setText("# of Levels = " + str(kcPoly.levels))
    txtRadius.setText("Radius = " + str(kcPoly.radius))
    center = kcPoly.center
    txtCircleCenterPoint.setText("( " + str(round(center.getX(), 2)) + ", " + str(round(center.getY(), 2)) + ")")
    txtSimilarityDimension.setText("Similarity Dimnension = " + str(round(kcPoly.getSimilarityDimension(),3)))
    txtKCAngle.setText("KC Angle = " + str(kcPoly.KCangle) + "°")


def activateButtons():
    '''manages activating and deactivating buttons'''
    global buttonsActive
    if buttonsActive:
        btnClear.deactivate()
        btnExit.deactivate()
        btnDraw.deactivate()
        btnPolygons.deactivate()
        btnEnterSides.deactivate()
        btnEnterLevels.deactivate()
        btnZoomIn.deactivate()
        btnZoomOut.deactivate()
        btnCreate.deactivate()
        btnEnterRadius.deactivate()
        btnChangeCenterPoint.deactivate()
        btnEnterKCAngle.deactivate()
        btnLineColorBlack.deactivate()
        btnLineColorBlue.deactivate()
        btnLineColorRed.deactivate()
        btnLineColorWhite.deactivate()
        btnBackgoundColorBlack.deactivate()
        btnBackgoundColorBlue.deactivate()
        btnBackgoundColorRed.deactivate()
        btnBackgoundColorWhite.deactivate()
    else:
        btnClear.activate()
        btnExit.activate()
        btnDraw.activate()
        btnPolygons.activate()
        btnEnterSides.activate()
        btnEnterLevels.activate()
        btnZoomIn.activate()
        btnZoomOut.activate()
        btnChangeCenterPoint.activate()
        btnEnterRadius.activate()
        btnEnterKCAngle.activate()
        btnLineColorBlack.activate()
        btnLineColorBlue.activate()
        btnLineColorRed.activate()
        btnLineColorWhite.activate()
        btnBackgroundColorBlack.activate()
        btnBackgroundColorBlue.activate()
        btnBackgroundColorRed.activate()
        btnBackgroundColorWhite.activate()

    buttonsActive = not (buttonsActive)


# decorater timer function that times the decorated function (not used by I was just messing around with)
def timer(f):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        rv = f(*args, **kwargs)
        total = time.time() - startTime
        print("Time: ", total)
        return rv

    return wrapper

def getDistanceConversion(length):
    '''returns a real world distance conversion of a meter.'''

    if length <= .11:
        return "The length of your finger"

    elif length <=  1.67:
        return "Smaller than Ethan"

    elif length <= 2.72:
        return "Around the tallest man in the world"

    elif length <= 4.5:
        return "average length of a car"

    elif length < 30.48:
        return "longest car in the world"

    elif length <= 50:
        return "Olympic Swimming Pool"

    elif length <= 100:
        return "Football Feild"

    elif length <= 1600:
        return "1 mile ish"

    elif length <= 4000:
        return "NYC to LA"

    elif length <= 6437.376:
        return "NYC to Alaska"

    elif length <= 9656.064:
        return "Length of Russia"

    elif length <= 40075:
        return "The perimeter of earth"

    elif length <= 408000:
        return "from earth to the ISS"

    elif length <= 384.4 * 10**7:
        return "from earth to the moon"

    elif length <= 25800000000:
        return "from earth to venus"

    elif length <= 48600000000:
        return "from earth to mars"

    elif length <= 57000000000:
        return "from earth to mercury"

    elif length <= 93000000000:
        return "from earth to the sun"

    elif length <= 390000000000:
        return "from earth to Jupiter"

    elif length <= 777000000000:
        return "distance from earth to saturn"

    elif length <= 1690000000000:
        return "from earth to uranus"

    elif length <= 2700000000000:
        return "from earth to neptune"

    elif length <= 150000000000:
        return "from sun to pluto"

    else:
        return "so big I didn't even write a comparision"

def convertToMeters(distance):
    '''appromimatly converts units on the screen to meters (This is probably not that accurate but close enough.
    I literally measured my screen....) '''
    return distance/500

def main():
    ''' main method'''
    global gui, win, p, circles

    # set default values create the intial koch curve
    activateButtons()
    levels = 4
    inclinationAngle = 0
    center = Point(0, 0)
    radius = 7
    KCangle = 60
    length = 16
    sides = 1
    currentBackgroundClicked = btnBackgroundColorWhite
    currentLineClicked = btnLineColorBlack

    # create the intial Koch Curve
    kcPoly = kochPolygon(win, center, radius, sides, levels, KCangle)
    kochPolygons.append(kcPoly)
    updateTextBoxes(kcPoly)
    clickPoint = gui.getMouse()


    while not (btnExit.clicked(clickPoint)):

        if btnDraw.clicked(clickPoint):
            # update and draw a koch curve
            kcPoly.generateKochCurveManager()
            kcPoly.drawKochCurve()
            txtLength.setText("Length of each Koch Curve:" + str(length))

        if btnClear.clicked(clickPoint):
            # undraw the koch curve and reset the objects
            kcPoly.undrawKochCurve()
            kcPoly.resetKochCurveObjects()

        if btnPolygons.clicked(clickPoint):
            # hide and show the shading of the polygons
            kcPoly.showTriangles = not(kcPoly.showTriangles)


        # setting new values below:
        if btnEnterSides.clicked(clickPoint):
            kcPoly.setSides(entSides.getValue())

        if btnEnterLevels.clicked(clickPoint):
            kcPoly.setLevels(entLevels.getValue())

        if btnEnterRadius.clicked(clickPoint):
            kcPoly.setRadius(entRadius.getValue())

        if btnChangeCenterPoint.clicked(clickPoint):
            kcPoly.setCenter(win.getMouse())

        if btnEnterKCAngle.clicked(clickPoint):
            kcPoly.setKCangle(entKCAngle.getValue())

        # let the user change the line color:
        if btnLineColorBlack.clicked(clickPoint):
            kcPoly.setLineColor("Black")
            btnLineColorBlack.setEdgeColor("Light Green")
            currentLineClicked.setEdgeColor("Black")
            currentLineClicked = btnLineColorBlack

        if btnLineColorBlue.clicked(clickPoint):
            kcPoly.setLineColor("Blue")
            btnLineColorBlue.setEdgeColor("Light Green")
            currentLineClicked.setEdgeColor("Black")
            currentLineClicked = btnLineColorBlue

        if btnLineColorRed.clicked(clickPoint):
            kcPoly.setLineColor("Red")
            btnLineColorRed.setEdgeColor("Light Green")
            currentLineClicked.setEdgeColor("Black")
            currentLineClicked = btnLineColorRed

        if btnLineColorWhite.clicked(clickPoint):
            kcPoly.setLineColor("White")
            btnLineColorWhite.setEdgeColor("Light Green")
            currentLineClicked.setEdgeColor("Black")
            currentLineClicked = btnLineColorWhite

        # let the user change the background color
        if btnBackgroundColorBlack.clicked(clickPoint):
            win.setBackground("black")
            btnBackgroundColorBlack.setEdgeColor("Light Green")
            currentBackgroundClicked.setEdgeColor("Black")
            currentBackgroundClicked = btnBackgroundColorBlack

        if btnBackgroundColorBlue.clicked(clickPoint):
            win.setBackground("Blue")
            btnBackgroundColorBlue.setEdgeColor("Light Green")
            currentBackgroundClicked.setEdgeColor("Black")
            currentBackgroundClicked = btnBackgroundColorBlue

        if btnBackgroundColorRed.clicked(clickPoint):
            win.setBackground("Red")
            btnBackgroundColorRed.setEdgeColor("Light Green")
            currentBackgroundClicked.setEdgeColor("Black")
            currentBackgroundClicked = btnBackgroundColorRed

        if btnBackgroundColorWhite.clicked(clickPoint):
            win.setBackground("white")
            btnBackgroundColorWhite.setEdgeColor("Light Green")
            currentBackgroundClicked.setEdgeColor("Black")
            currentBackgroundClicked = btnBackgroundColorWhite

        # let the user zoom in and out
        if btnZoomIn.clicked(clickPoint):
            win.zoom("in", keepRatio=True)

        if btnZoomOut.clicked(clickPoint):
            win.zoom("out", keepRatio=True)

        updateTextBoxes(kcPoly)
        clickPoint = gui.getMouse()

    win.close()
    gui.close()


if __name__ == "__main__":
    main()
