import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp2(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("아이콘테스트")
        #아이콘 설정
        self.setWindowIcon(QIcon("../Image/king.jpg"))
        #위치,사이즈 move+resize 합쳐놓은것과같다.
        self.setGeometry(300,300,300,200)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp2()
    sys.exit(app.exec_())