import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class MyApp11(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        okButton = QPushButton('OK')
        cancelButton = QPushButton('취소')

        # 수평박스를 하나만들고 두개의 버튼과 양쪽에 빈공간을 추가합니다.
        # addStretch() 메서드는 신축성있는 빈공간을 제공합니다.
        # 두버튼의 양쪽의 stretch factor가 1로 같기떄문에 두빈공간의 크기는 창의크기가 변해도 항상같음
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        # 수평박스(hbox)를 수직박스(vbox)에 넣어줍니다.
        # 수직박스의 stretch factor는 수평박스를 아래쪽으로 밀어내서 두개의 버튼을 장의 아래쪽에 위치하도록 합니다.
        # 수평 박스 위와 아래의 빈공간의 크기는 항상 3:1을 유지합니다.
        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        # 최종적으로 수직박스를 창의 메인레이아웃으로 설정합니다.
        self.setLayout(vbox)

        self.setWindowTitle('box Layout')
        self.setGeometry(300,300,300,200)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp11()
    sys.exit(app.exec_())

# 창의 크기를 변경해도 가운데에있다.




#QHBoxLayout은 여러 위젯을 수평으로 정렬하는 레이아웃 클래스 입니다.
# QHBoxLayout 생성자는 수평의 박스를 하나 만드는데, 다른 레이아웃 박스를 넣을 수도 있고 위젯을 배치할 수도 있습니다.

#QVBoxLayout은 여러 위젯을 수직으로 정렬하는 레이아웃 클래스입니다.
# QVBoxLayout 생성자는 수직의 박스를 하나 만드는데, 다른 레이아웃 박스를 넣을 수도 있고 위젯을 배치할 수도 있습니다.


