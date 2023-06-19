import sys
import math
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication, QWidget

class Corkscrew(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(1820, 1030, 100, 100)
        
        
        self.angle1 = 0
        self.angle2 = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_angles)
        self.timer.start(10)
    
    def center(self):
        frame_geometry = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        center_point = QApplication.desktop().screenGeometry(screen).center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())
    
    def update_angles(self):
        self.angle1 += 2
        self.angle2 -= 3
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)

        num_turns = 20
        num_points = 50
        spacing = 4
        radius1 = 50
        radius2=45
        radius3 = 40
        radius4 =35
        radius5 =30
        radius6 =25
        radius7 =20
        radius8 =15
        radius9 =10
        radius10 =5
        
        # Draw first corkscrew
        painter.rotate(self.angle1)
        pen1 = QPen(QColor('#5E2B73'))
        pen1.setWidth(2)
        painter.setPen(pen1)
        
        for i in range(num_turns):
            for j in range(num_points):
                theta = j * 2 * math.pi / num_points + i * spacing * 2 * math.pi / num_turns
                x = radius1 * math.cos(theta)
                y = radius1 * math.sin(theta)
                painter.drawPoint(int(x), int(y))
        
        # Draw second corkscrew

        painter.rotate(self.angle2)
        pen2 = QPen(QColor('#7E327D'))
        pen2.setWidth(2)
        painter.setPen(pen2)
        
        for i in range(num_turns):
            for j in range(num_points):
                theta = j * 2 * math.pi / num_points + i * spacing * 2 * math.pi / num_turns
                x = radius2 * math.cos(theta)
                y = radius2 * math.sin(theta)
                painter.drawPoint(int(x), int(y))

        painter.rotate(self.angle1)
        pen3 = QPen(QColor('#9F3D88'))
        pen3.setWidth(2)
        painter.setPen(pen3)
        
        for i in range(num_turns):
            for j in range(num_points):
                theta = j * 2 * math.pi / num_points + i * spacing * 2 * math.pi / num_turns
                x = radius3 * math.cos(theta)
                y = radius3 * math.sin(theta)
                painter.drawPoint(int(x), int(y))

        painter.rotate(self.angle2)
        pen4 = QPen(QColor('#BF4893'))
        pen4.setWidth(2)
        painter.setPen(pen4)
        
        for i in range(num_turns):
            for j in range(num_points):
                theta = j * 2 * math.pi / num_points + i * spacing * 2 * math.pi / num_turns
                x = radius4 * math.cos(theta)
                y = radius4 * math.sin(theta)
                painter.drawPoint(int(x), int(y))

        painter.rotate(self.angle1)
        pen5 = QPen(QColor('#DF539E'))
        pen5.setWidth(2)
        painter.setPen(pen5)
        
        for i in range(num_turns):
            for j in range(num_points):
                theta = j * 2 * math.pi / num_points + i * spacing * 2 * math.pi / num_turns
                x = radius5 * math.cos(theta)
                y = radius5 * math.sin(theta)
                painter.drawPoint(int(x), int(y))
        
        # Draw second corkscrew

        painter.rotate(self.angle2)
        pen6 = QPen(QColor('#FF5FA9'))
        pen6.setWidth(2)
        painter.setPen(pen6)
        
        for i in range(num_turns):
            for j in range(num_points):
                theta = j * 2 * math.pi / num_points + i * spacing * 2 * math.pi / num_turns
                x = radius6 * math.cos(theta)
                y = radius6 * math.sin(theta)
                painter.drawPoint(int(x), int(y))

        painter.rotate(self.angle1)
        pen7 = QPen(QColor('#FF73B1'))
        pen7.setWidth(2)
        painter.setPen(pen7)
        
        for i in range(num_turns):
            for j in range(num_points):
                theta = j * 2 * math.pi / num_points + i * spacing * 2 * math.pi / num_turns
                x = radius7 * math.cos(theta)
                y = radius7 * math.sin(theta)
                painter.drawPoint(int(x), int(y))

        painter.rotate(self.angle2)
        pen8 = QPen(QColor('#FF87BA'))
        pen8.setWidth(2)
        painter.setPen(pen8)
        
        for i in range(num_turns):
            for j in range(num_points):
                theta = j * 2 * math.pi / num_points + i * spacing * 2 * math.pi / num_turns
                x = radius8 * math.cos(theta)
                y = radius8 * math.sin(theta)
                painter.drawPoint(int(x), int(y))

        painter.rotate(self.angle1)
        pen9 = QPen(QColor('#FF9BC3'))
        pen9.setWidth(2)
        painter.setPen(pen9)
        
        for i in range(num_turns):
            for j in range(num_points):
                theta = j * 2 * math.pi / num_points + i * spacing * 2 * math.pi / num_turns
                x = radius9 * math.cos(theta)
                y = radius9 * math.sin(theta)
                painter.drawPoint(int(x), int(y))

        painter.rotate(self.angle2)
        pen10 = QPen(QColor('#FFAFCC'))
        pen10.setWidth(2)
        painter.setPen(pen10)
        
        for i in range(num_turns):
            for j in range(num_points):
                theta = j * 2 * math.pi / num_points + i * spacing * 2 * math.pi / num_turns
                x = radius10 * math.cos(theta)
                y = radius10 * math.sin(theta)
                painter.drawPoint(int(x), int(y))

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    corkscrew = Corkscrew()
    corkscrew.show()
    sys.exit(app.exec_())
