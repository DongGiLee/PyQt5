import sys
from PyQt5.QtCore import QDate, Qt, QTime, QDateTime

from PyQt5.QtWidgets import QApplication, QMainWindow

#현재날짜
now = QDate.currentDate()

#월 5 20 2019
print(now.toString())
#20.5.19
print(now.toString('d.M.yy'))
#20.05.2019
print(now.toString('dd.MM.yyyy'))
#월.5월.2019
print(now.toString('ddd.MMMM.yyyy'))
#2019-05-20
print(now.toString(Qt.ISODate))
#2019년 5월 20일 월요일
print(now.toString(Qt.DefaultLocaleLongDate))

#15,17번줄은 ISO표준형식 or 어플리케이션의 기본 설정에 맞게 출력할수있다.


#23:55:23
time = QTime.currentTime()
#23:55:23
print(time.toString())
#23:55:23
print(time.toString('h.m.s'))
#23:55:23
print(time.toString('hh.mm.ss'))
#23.55.23.934, z는 1000분의 1초를 나타냅니다.
print(time.toString('hh.mm.ss.zzz'))
#오후 11:55:23
print(time.toString(Qt.DefaultLocaleLongDate))
#오후 11:55
print(time.toString(Qt.DefaultLocaleShortDate))

#33,35도 15,17과 마찬가지로 시간을나타낼수있다.

datetime = QDateTime.currentDateTime()
print("\n",datetime.toString())

class MyApp9():

    def __init__(self):

        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):

        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300,300,400,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp9()
    sys.exit(app.exec_())