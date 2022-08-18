import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QLineEdit
from PyQt5 import QtGui
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))    
    return os.path.join(base_path, relative_path)

form1 = resource_path('join.ui')
UI_class1 = uic.loadUiType(form1)[0]

form2 = resource_path('login.ui')
UI_class2 = uic.loadUiType(form2)[0]

form3 = resource_path('Main_window.ui')
UI_class3 = uic.loadUiType(form3)[0]

'''UI_class1 = uic.loadUiType('D:\python\knu\Team\join.ui')[0]
UI_class2 = uic.loadUiType('D:\python\knu\Team\login.ui')[0]
UI_class3 = uic.loadUiType('D:\python\knu\Team\Main_window.ui')[0]'''
# 회원가입창
class joinWindow(QWidget,UI_class1) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        QtGui.QPixmap('D:\python\knu\Team\로그인, 회원가입 그림\회원가입.png').scaled(self.width()-300, self.height()-300)
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
    global W_mileage
    W_mileage = 0
    global G_mileage
    G_mileage = 0
    global E_mileage
    E_mileage = 0
    global C_mileage
    C_mileage = 0
    global R_mileage
    R_mileage = 0
    
    


    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        
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
        
        self.buttonShop.clicked.connect(self.shop)
    
    # 버튼 1
    def button1_clicked(self) :
        global mileage
        global W_mileage
        self.labelA.setText(f'{self.button1.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20
        W_mileage += 20
        self.labelB.setText(f'마일리지 : {mileage}')
        self.label_4.setText(f'물절약 마일리지 : {W_mileage}')
        return W_mileage
        
    # 버튼 2
    def button2_clicked(self) :
        global mileage
        global G_mileage
        self.labelA.setText(f'{self.button2.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20 
        G_mileage += 20
        self.labelB.setText(f'마일리지 : {mileage}')
        self.label_5.setText(f'가스절약 마일리지 : {G_mileage}')
        return G_mileage
    
    # 버튼 3
    def button3_clicked(self) :
        global mileage
        global E_mileage
        self.labelA.setText(f'{self.button3.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20
        E_mileage += 20 
        self.labelB.setText(f'마일리지 : {mileage}')
        self.label_6.setText(f'전기절약 마일리지 : {E_mileage}')
        return E_mileage
    
    # 버튼 4
    def button4_clicked(self) :
        global mileage
        global C_mileage
        self.labelA.setText(f'{self.button4.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20
        C_mileage += 20
        self.label_7.setText(f'CO2감소 마일리지 : {C_mileage}') 
        self.labelB.setText(f'마일리지 : {mileage}')
        return C_mileage
    
    # 버튼 5
    def button5_clicked(self) :
        global mileage
        global R_mileage
        self.labelA.setText(f'{self.button5.text()}를 성공하여 20마일리지가 적립되었습니다.') # 마일리지 조정하기 
        mileage += 20
        R_mileage += 20 
        self.label_8.setText(f'재활용 마일리지 : {R_mileage}')
        self.labelB.setText(f'마일리지 : {mileage}')
        return R_mileage
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
