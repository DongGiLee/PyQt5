import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp3(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #*PyQt5에서 이벤트처리는 시그널과 슬롯 메커니즘

        btn = QPushButton('종료',self)
        btn.move(50,50)
        btn.resize(btn.sizeHint())

        #instance()=현재인스턴스를 반환
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("종료 버튼")
        self.setGeometry(300,300,300,200)
        self.show()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = MyApp3()
    sys.exit(app.exec_())
