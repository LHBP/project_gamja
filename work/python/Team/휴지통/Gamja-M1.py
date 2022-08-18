# Gamja-4-로그인.py >>> 로그인창, 로그인 클릭시 메인창으로 이동
# Gamja-5-회원가입.py >>> 회원가입창, 회원가입시 아이디, 비밀번호 member 딕셔너리에 저장, 잘못된 아이디와 비밀번호로 로그인시 로그인 불가

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QLineEdit
from PyQt5 import QtGui
from PyQt5 import uic 

UI_class3 = uic.loadUiType("D:\python\knu\GMZA\Main_window.ui")
"""
# 회원가입창
class joinWindow(QWidget) :
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
        
        
        # 회원가입 버튼
        self.button_join = QPushButton('회원가입', self)
        self.button_join.move(100,120)
        self.button_join.clicked.connect(self.button_join_clicked)
        
        global member
        member = {} # 회원가입 정보 딕셔너리
        
    def button_join_clicked(self) :
        member[self.edit0.text()] = self.edit1.text() # 회원가입 정보 입력
        self.hide() # 로그인창 숨김
        self.myWin = loginWindow() # myWin을 loginWindow로 변경
        self.myWin.show() # 메인창 띄움
        
        
# 로그인창
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
        
        # 상태창
        self.label3 = QLabel(self)
        self.label3.setText('아이디와 비밀번호를 입력하세요.')
        self.label3.move(100, 10)
        self.label3.resize(500, 50)
        
        
        # 로그인 버튼
        self.button_login = QPushButton('로그인', self)
        self.button_login.move(100,120)
        self.button_login.clicked.connect(self.button_login_clicked)
        
        
    def button_login_clicked(self) :
        while True :
            if member.get(self.edit0.text()) == self.edit1.text() :
                self.label3.setText('로그인 성공!!')
                self.hide() # 로그인창 숨김
                self.myWin = MainWindow() # myWin을 MainWindow로 변경
                self.myWin.show() # 메인창 띄움
                break
            
            if member.get(self.edit0.text()) != self.edit1.text() :
                self.label3.setText('아이디 또는 비밀번호를 확인해 주세요')
                break
                continue
        
"""

class MainWindow(QWidget, UI_class3) :
    def __init__(self) :
        
        super().__init__()
        self.setWindowTitle('')
        self.setGeometry(0, 0, 400, 400)
            
        # 안내창
        self.labelA = QLabel(self)
        self.labelA.setText('') # 텍스트 변경가능
        self.labelA.move(80, 40)
        self.labelA.resize(500, 50)
        
        
        # 총 마일리지
        global mileage
        mileage = 0
        self.labelB = QLabel(self)
        self.labelB.setText(f"" '{mileage}')
        self.labelB.move(120, 0)
        self.labelB.resize(500, 50)
        #self.label_W.setText(f'')
        
        # 등급
        self.labelC = QLabel(self)
        self.labelC.setText('')
        self.labelC.move(0, 0)
        self.labelC.resize(500, 50)
        
        #등급별 그림
        self.label_imgA = QLabel(self)
        #self.label_imgA.setPixmap(QtGui.QPixmap('D:\python\knu\GMZA\level1.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        self.label_imgA.move(150,150)
        self.label_imgA.resize(100,100)
        
        
        # 버튼 복붙으로 여러개 만들기 가능
        self.button1 = QPushButton(self)
        self.button1.setText('') # 텍스트 변경 가능
        self.button1.setCheckable(True)
        self.button1.move(100, 100) # 버튼 위치 변경
        self.button1.clicked.connect(self.button1_clicked)
        self.button1.clicked.connect(self.level)
        
        self.button2 = QPushButton(self)
        self.button2.setText('') # 텍스트 변경 가능
        self.button2.setCheckable(True)
        self.button2.move(100, 200) # 버튼 위치 변경
        self.button2.clicked.connect(self.button2_clicked)
        self.button2.clicked.connect(self.level)
        
        self.button3 = QPushButton(self)
        self.button3.setText('') # 텍스트 변경 가능
        self.button3.setCheckable(True)
        self.button3.move(100, 300) # 버튼 위치 변경
        self.button3.clicked.connect(self.button3_clicked)
        self.button3.clicked.connect(self.level)
        
        self.button4 = QPushButton(self)
        self.button4.setText('') # 텍스트 변경 가능
        self.button4.setCheckable(True)
        self.button4.move(100, 400) # 버튼 위치 변경
        self.button4.clicked.connect(self.button4_clicked)
        self.button4.clicked.connect(self.level)
        
        self.button5 = QPushButton(self)
        self.button5.setText('') # 텍스트 변경 가능
        self.button5.setCheckable(True)
        self.button5.move(100, 500) # 버튼 위치 변경
        self.button5.clicked.connect(self.button5_clicked)
        self.button5.clicked.connect(self.level)

    
      
    # 버튼 클릭시 마일리지 상승 복붙가능
    # 버튼 1
    def button1_clicked(self) :
        global mileage
        self.labelA.setText(f'{self.button1.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 # 마일리지 조정하기 
        #self.label_W.setText(f'물절약 마일리지 : {mileage}')
        return mileage
    
    def button2_clicked(self) :
        global mileage
        self.labelA.setText(f'{self.button2.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 # 마일리지 조정하기 
        self.labelB.setText(f'가스절약 마일리지 : {mileage}')
        return mileage
    
    def button3_clicked(self) :
        global mileage
        self.labelA.setText(f'{self.button3.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 # 마일리지 조정하기 
        self.labelB.setText(f'전기절약 마일리지 : {mileage}')
        return mileage
    
    def button4_clicked(self) :
        global mileage
        self.labelA.setText(f'{self.button4.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 # 마일리지 조정하기 
        self.labelB.setText(f'CO2절약 마일리지 : {mileage}')
        return mileage
    
    def button5_clicked(self) :
        global mileage
        self.labelA.setText(f'{self.button1.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 # 마일리지 조정하기 
        self.labelB.setText(f'재활용 마일리지 : {mileage}')
        return mileage
    
    # 등급
    def level(self) :
        if mileage <= 300 :
            self.labelC.setText('등급 : 알감자')                         
            self.label_imgA.setPixmap(QtGui.QPixmap('D:\python\knu\GMZA\level1.png').scaled(self.width()-300, self.height()-300))
        elif mileage >= 300 and mileage < 400 :
            self.labelC.setText('등급 : 깬자')                         
            self.label_imgA.setPixmap(QtGui.QPixmap('D:\python\knu\GMZA\level2.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        elif mileage >= 400 and mileage < 500 :
            self.labelC.setText('등급 : 깜자')
            self.label_imgA.setPixmap(QtGui.QPixmap('D:\python\knu\GMZA\level3.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        elif mileage >= 500 and mileage < 600 :
            self.labelC.setText('등급 : 완자')
            self.label_imgA.setPixmap(QtGui.QPixmap('D:\python\knu\GMZA\level4.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        elif mileage >= 600 :
            self.labelC.setText('등급 : 대홍단감자')
            self.label_imgA.setPixmap(QtGui.QPixmap('D:\python\knu\GMZA\level4.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        
        
    
        
app = QApplication(sys.argv)
myWin = MainWindow()
myWin.show()
app.exec_()
