import sys
from PyQt5.QtWidgets import QApplication, QWidget
#기본적인 UI 구성요소는 PyQt5.QtWidgets 모듈에 포함

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("첫번째 테스트")
        # 위젯을 스크린의 x=?px y=?px의 위치로 이동
        self.move(300,300)
        # 위젯의 크기
        self.resize(400,400)
        # 스크린에 호출
        self.show()

"""
__name__ : 현재 모듈의 이름이 저장되는 내장변수     'tutorial.py'를 import하면 __name__은 tutorial이 된다.
그렇지 않고 코드를 직접 실행하면 __name__==__main__이 된다.
 프로그램이 직접 실행되는지 혹은 모듈을 통해 실행되는지를 확인
"""
if __name__ == '__main__':

    app = QApplication(sys.argv)
    #모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야함
    ex = MyApp()
    sys.exit(app.exec())