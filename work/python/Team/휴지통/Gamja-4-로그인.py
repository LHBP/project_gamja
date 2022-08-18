#Gamja-4-pyqt.py >>> 로그인창, 로그인 클릭시 메인창으로 이동

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QLineEdit
from PyQt5 import QtGui

#로그인창
class loginWindow(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('감자합니다')
        self.setGeometry(0, 0, 400, 400)
        
        # 아이디 입력
        self.label0 = QLabel('아이디', self)
        self.label0.move(100,50)
        self.edit0 = QLineEdit(self)
        self.edit0.setEchoMode(0)
        self.edit0.move(200,50)
        
        # 비밀번호 입력
        self.label1 = QLabel('비밀번호', self)
        self.label1.move(100,80)
        self.edit1 = QLineEdit(self)
        self.edit1.setEchoMode(2)
        self.edit1.move(200,80)
        
        # 로그인 버튼
        self.button0 = QPushButton('로그인', self)
        self.button0.move(100,120)
        self.button0.clicked.connect(self.button0_clicked)
        
        
    def button0_clicked(self) :
        self.hide() # 로그인창 숨김
        self.myWin = MainWindow() 
        self.myWin.show() # 메인창 띄움
    
        

'''
class MainWindow(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('감자합니다')
        self.setGeometry(0, 0, 400, 400)
            
        # 안내창
        self.labelA = QLabel(self)
        self.labelA.setText('어서 구해줘') # 텍스트 변경가능
        self.labelA.move(80, 40)
        self.labelA.resize(500, 50)
        
        
        # 총 마일리지
        global mileage
        mileage = 0
        self.labelB = QLabel(self)
        self.labelB.setText(f'마일리지 : {mileage}')
        self.labelB.move(120, 0)
        self.labelB.resize(500, 50)
        
        # 등급
        self.labelC = QLabel(self)
        self.labelC.setText('등급 : 알감자')
        self.labelC.move(0, 0)
        self.labelC.resize(500, 50)
        
        #등급별 그림
        self.label_imgA = QLabel(self)
        self.label_imgA.setPixmap(QtGui.QPixmap('C:\감자그림\감자1.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        self.label_imgA.move(150,150)
        self.label_imgA.resize(100,100)
        
        
        # 버튼 복붙으로 여러개 만들기 가능
        self.button1 = QPushButton(self)
        self.button1.setText('비료주기') # 텍스트 변경 가능
        self.button1.setCheckable(True)
        self.button1.move(100, 100) # 버튼 위치 변경
        self.button1.clicked.connect(self.button1_clicked)
        self.button1.clicked.connect(self.level)

    
      
    # 버튼 클릭시 마일리지 상승 복붙가능
    # 버튼 1
    def button1_clicked(self) :
        global mileage
        self.labelA.setText(f'{self.button1.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 # 마일리지 조정하기 
        self.labelB.setText(f'마일리지 : {mileage}')
        return mileage
    
    # 등급
    def level(self) :
        if mileage >= 300 and mileage < 400 :
            self.labelC.setText('등급 : 실버')                         
            self.label_imgA.setPixmap(QtGui.QPixmap('C:\감자그림\감자2.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        elif mileage >= 400 and mileage < 500 :
            self.labelC.setText('등급 : 골드')
            self.label_imgA.setPixmap(QtGui.QPixmap('C:\감자그림\감자3.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        elif mileage >= 500 and mileage < 600 :
            self.labelC.setText('등급 : 플레티넘')
            self.label_imgA.setPixmap(QtGui.QPixmap('C:\감자그림\감자4.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        elif mileage >= 600 :
            self.labelC.setText('등급 : 다이아몬드')
            self.label_imgA.setPixmap(QtGui.QPixmap('C:\감자그림\감자5.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
'''          
        
    
        
app = QApplication(sys.argv)
myWin = loginWindow()
myWin.show()
app.exec_()


