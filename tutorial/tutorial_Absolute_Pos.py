import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MyApp11(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        label1 = QLabel('라벨',self)
        label1.move(20,20)
        label2 = QLabel('라벨2',self)
        label2.move(20,60)

        btn1 = QPushButton('버튼1',self)
        btn2 = QPushButton('버튼2',self)

        btn1.move(80,13)
        btn2.move(80,53)

        self.setWindowTitle("절대 위치")
        self.setGeometry(300,300,400,200)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp11()
    sys.exit(app.exec_())