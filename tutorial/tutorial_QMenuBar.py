import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp6(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon("../Image/exit.png"),'종료',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip("어플리케이션 종료")
        #이동작을 선택했을때 생성된(triggered)시그널이 QApplication 위젯에 quit()메서드에 연결된다.
        exitAction.triggered.connect(qApp.quit)
        """
        이네줄의 코드를 통해 아이콘과 동작을만들고 단축키를 정의한다.
        메뉴에 마우스를 올렸을때 상태바에 나타날 상태팁을 setStatusTip으로 설정
        """
        self.statusBar()

        menubar = self.menuBar()
        # macOS에서는 메뉴바를 다르게 다루는데, 아래 예제에서 볼 수 있듯이 한 줄의 코드(menubar.setNativeMenuBar(False))를 추가함으로써 macOS에서도 Windows 환경과 동일한 결과를 얻을 수 있습니다.
        menubar.setNativeMenuBar(False)
        #&는 앰퍼샌드는 간편하게 단축키를 설정하게해줌 F앞에 &가있으므로 'Alt+F'가 메뉴의 단축기가됨
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        """
        menuBar() 메서드는 메뉴바를 생성합니다. 이어서 'File' 메뉴를 하나 만들고, 거기에 'exitAction' 동작을 추가합니다.
        '&File'의 앰퍼샌드(ampersand, &)는 간편하게 단축키를 설정하도록 해줍니다.
        'F' 앞에 앰퍼샌드가 있으므로 'Alt+F'가 File 메뉴의 단축키가 됩니다.
        만약 'i'의 앞에 앰퍼샌드를 넣으면 'Alt+I'가 단축키가 됩니다.
        """
        self.setWindowTitle("메뉴바")
        self.setGeometry(300,300,300,200)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp6()
    sys.exit(app.exec_())