import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyApp10(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #QLabel 클래스로 세게의 라벨위젯을 만듦
        lbl_red = QLabel('빨강')
        lbl_green = QLabel('초록')
        lbl_blue = QLabel('파랑')

        #경계선 실선 : solid, 경계선두께 : width 경계선색 : color, 경계선의 모서리 둥글게 : radius
        lbl_red.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius: 3px;")
        lbl_green.setStyleSheet("color: green;"
                                "background-color: #7FFFD4")
        lbl_blue.setStyleSheet("color: blue;"
                               "background-color: #87CEFA;"
                               "border-style: dashed;"
                               "border-width: 3px;"
                               "border-color: #1E90FF")

        # QVBOxLayout: 수직박스레이아웃, vertical
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        # 다양한 스타일 항목 https://doc.qt.io/qt-5/stylesheet-reference.html 참고

        self.setLayout(vbox)
        self.setWindowTitle("스타일시트")
        self.setGeometry(300,300,300,200)
        self.show()

if __name__== '__main__':
    app = QApplication(sys.argv)
    ex = MyApp10()
    sys.exit(app.exec_())