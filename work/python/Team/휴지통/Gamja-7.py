# Gamja-4-로그인.py >>> 로그인창, 로그인 클릭시 메인창으로 이동
# Gamja-5-회원가입.py >>> 회원가입창, 회원가입시 아이디, 비밀번호 member 딕셔너리에 저장, 잘못된 아이디와 비밀번호로 로그인시 로그인 불가

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QLineEdit
from PyQt5 import QtGui
from PyQt5 import uic

UI_class1 = uic.loadUiType('D:\python\knu\Team\join.ui')[0]
UI_class2 = uic.loadUiType('D:\python\knu\Team\login.ui')[0]
UI_class3 = uic.loadUiType('D:\python\knu\Team\Main_window.ui')[0]
# 회원가입창
class joinWindow(QWidget,UI_class1) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.button_join.clicked.connect(self.button_join_clicked)
        
        global member
        member = {} # 회원가입 정보 딕셔너리
        
    def button_join_clicked(self) :
        member[self.edit0.text()] = self.edit1.text() # 회원가입 정보 입력
        self.hide() # 로그인창 숨김
        self.myWin = loginWindow() # myWin을 loginWindow로 변경
        self.myWin.show() # 메인창 띄움
        
        
# 로그인창
class loginWindow(QWidget,UI_class2) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
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
        


class MainWindow(QWidget,UI_class3) :
    global mileage
    mileage = 0
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # 총 마일리지
        global mileage
        mileage = 0
        
        #등급별 그림
        self.label_imgA.setPixmap(QtGui.QPixmap('D:\python\knu\Team\감자그림\감자1.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
    
        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)
        self.button4.clicked.connect(self.button4_clicked)
        self.button5.clicked.connect(self.button5_clicked)
        
        self.button1.clicked.connect(self.level)
        self.button2.clicked.connect(self.level)
        self.button3.clicked.connect(self.level)
        self.button4.clicked.connect(self.level)
        self.button5.clicked.connect(self.level)
    
    # 버튼 1
    def button1_clicked(self) :
        global mileage
        self.labelA.setText(f'{self.button1.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 # 마일리지 조정하기 
        self.labelB.setText(f'마일리지 : {mileage}')
        return mileage
        
    # 버튼 2
    def button2_clicked(self) :
        global mileage
        self.labelA.setText(f'{self.button2.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 # 마일리지 조정하기 
        self.labelB.setText(f'마일리지 : {mileage}')
        return mileage
    
    # 버튼 3
    def button3_clicked(self) :
        global mileage
        self.labelA.setText(f'{self.button3.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 # 마일리지 조정하기 
        self.labelB.setText(f'마일리지 : {mileage}')
        return mileage
    
    # 버튼 4
    def button4_clicked(self) :
        global mileage
        self.labelA.setText(f'{self.button4.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 # 마일리지 조정하기 
        self.labelB.setText(f'마일리지 : {mileage}')
        return mileage
    
    # 버튼 5
    def button5_clicked(self) :
        global mileage
        self.labelA.setText(f'{self.button5.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 # 마일리지 조정하기 
        self.labelB.setText(f'마일리지 : {mileage}')
        return mileage
    

    def level(self) :
        if mileage >= 300 and mileage < 400 :
            self.labelC.setText('등급 : 실버')                         
            self.label_imgA.setPixmap(QtGui.QPixmap('D:\python\knu\Team\감자그림\감자2.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        elif mileage >= 400 and mileage < 500 :
            self.labelC.setText('등급 : 골드')
            self.label_imgA.setPixmap(QtGui.QPixmap('D:\python\knu\Team\감자그림\감자3.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        elif mileage >= 500 and mileage < 600 :
            self.labelC.setText('등급 : 플레티넘')
            self.label_imgA.setPixmap(QtGui.QPixmap('D:\python\knu\Team\감자그림\감자4.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
        elif mileage >= 600 :
            self.labelC.setText('등급 : 다이아몬드')
            self.label_imgA.setPixmap(QtGui.QPixmap('D:\python\knu\Team\감자그림\감자5.png').scaled(self.width()-300, self.height()-300)) #사진링크 바꾸기
     
        
    
        
app = QApplication(sys.argv)
myWin = joinWindow()
myWin.show()
app.exec_()
