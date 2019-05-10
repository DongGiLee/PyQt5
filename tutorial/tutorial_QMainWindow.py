import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyApp5(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        #statusBar를 만드려면 QMainWindow에서 상속받아야한다.
        self.statusBar().showMessage("하단부분")
        self.setWindowTitle('상태바')
        self.setGeometry(300,300,300,200)
        self.show()

if __name__=='__main__':

    app = QApplication(sys.argv)
    ex = MyApp5()
    sys.exit(app.exec_())