import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp7(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #아이콘,라벨설정
        exitAction = QAction(QIcon('../Image/exit.png'),'종료',self)
        #단축키
        exitAction.setShortcut("Ctrl+Q")
        #상태바 메세지에 띄워준다.
        exitAction.setStatusTip("어플리케이션을 종료")
        #리마인드! 클릭시 생성되는 시그널을 qApp에 quit()메서드에 연결!
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        #아래두줄이 툴바를 생성, 종료액션을 추가하는란
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('툴툴바바')
        self.setGeometry(300,300,300,200)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp7()
    sys.exit(app.exec_())