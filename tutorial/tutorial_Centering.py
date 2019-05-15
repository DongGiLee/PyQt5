import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class MyApp8(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("화면 가운데")
        self.resize(500,350)
        self.center()
        self.show()

    def center(self):
        # frameGeometry 메서드로 창의 위치와 크기정보가져옴
        qr = self.frameGeometry()
        # 사용하는 모니터 화면의 가운데 위치를 파악
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        #self.move(qr.topLeft()) 현재창을 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킨다는데
        #결과적으론 같음 근데 topLeft를 사용한이유를 모르겠음.
if __name__== '__main__':
    app = QApplication(sys.argv)
    ex = MyApp8()
    sys.exit(app.exec_())