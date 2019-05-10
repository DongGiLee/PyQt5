import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp4(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        #툴팁에 사용될 폰트설정, SansSerif폰트와 크기는 10
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('이것은 <b>QWidget</b> 위젯입니다.')

        btn = QPushButton('버튼', self)
        btn.setToolTip('이것은 <b>QPushButton</b> 위젯입니다.')
        btn.move(50, 50)
        #sizeHint() 메서드는 버튼을 적절한크기로 만들어줌
        btn.resize(btn.sizeHint())

        self.setWindowTitle("툴팁")
        self.setGeometry(300,300,300,200)
        self.show()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = MyApp4()
    sys.exit(app.exec_())