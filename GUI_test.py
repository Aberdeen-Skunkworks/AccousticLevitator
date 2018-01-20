## GUI testing

import sys
from PyQt5 import QtWidgets, QtGui


def window1(): ### Trial 1
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)
    b.setText('Push me')
    l.setText('Look at me')
    w.setWindowTitle('GUI Testing')
    w.setGeometry(100, 100, 300, 200)
    b.move(100, 50)
    l.move(110, 100)
    w.show()
    sys.exit(app.exec_())
    
    
    
    
    
    
def window2(): ### Trial 2
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton('Push me')
    l = QtWidgets.QLabel('Look at me')
    
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch() 
    
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)
    v_box.addLayout(h_box)
    
    w.setLayout(v_box)
    w.setWindowTitle('GUI Testing')
    w.setGeometry(100, 100, 300, 200)
    w.show()
    sys.exit(app.exec_())


    
class Window(QtWidgets.QWidget):
        x = 0    
        y = 0
        z = 0
        
        def __init__(self):
            
            super().__init__()
            
            self.init_ui()
        
        def init_ui(self):
            self.forward = QtWidgets.QPushButton('Forward')
            self.backward = QtWidgets.QPushButton('Backwards')
            self.right = QtWidgets.QPushButton('Right')
            self.left = QtWidgets.QPushButton('Left')
            self.up = QtWidgets.QPushButton('Up')
            self.down = QtWidgets.QPushButton('Down')


            h_box = QtWidgets.QHBoxLayout()
            h_box.addWidget(self.down)
            h_box.addWidget(self.forward)
            h_box.addWidget(self.up) 
        
            h_box2 = QtWidgets.QHBoxLayout()
            h_box2.addWidget(self.left)
            h_box2.addWidget(self.backward)
            h_box2.addWidget(self.right) 
        
            v_box = QtWidgets.QVBoxLayout()
            v_box.addLayout(h_box)
            v_box.addLayout(h_box2)
            
            
            self.setLayout(v_box)
            self.setWindowTitle('GUI Testing')
            
            self.forward.clicked.connect(self.forward_click)
            self.backward.clicked.connect(self.backward_click)
            self.left.clicked.connect(self.left_click)
            self.right.clicked.connect(self.right_click)
            self.up.clicked.connect(self.up_click)
            self.down.clicked.connect(self.down_click)
            
            self.show()
    
        def forward_click(self):
            self.x += 1
            print('x = ', self.x)
        
        def backward_click(self):
            self.x -= 1
            print('x = ', self.x)
            
        def left_click(self):
            self.z += 1
            print('z = ', self.z)
            
        def right_click(self):
            self.z -= 1
            print('z = ', self.z)
            
        def up_click(self):
            self.y += 1
            print('y = ', self.y)
        
        def down_click(self):
            self.y -= 1
            print('y = ', self.y)


# test
 
""" 
app = QtWidgets.QApplication(sys.argv)
app.aboutToQuit.connect(app.deleteLater)
a_window = Window()
sys.exit(app.exec_())

"""







