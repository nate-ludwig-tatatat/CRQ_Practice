#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import random
import math
import datetime
import time
import os
import platform
import importlib
import pip
import codecs
modules_needed = ["PyQt5"]
def randomize_list(iList):
    c = iList;
    return_value = []
    for i in range(0,len(c)):
        b = random.choice(c)
        return_value.append(b)
        c.remove(b)
    return return_value;
def wait(interval): #used to wait an interval of time. 
    s_time= time.time()
    while True:
        if time.time() > s_time + float(interval): #checks if the current time is greater than the starting time + the interval to wait
            break
exiting = False
if len(modules_needed) > 0:
   for module in range(0,len(modules_needed)):
      module_loader = importlib.find_loader(modules_needed[module])
      module_found = module_loader is not None
      if not module_found: #doesn't have module
         exiting = True
         print(modules_needed[module] + " was not found!")
         print("Attempting to install " + modules_needed[module])
         try:
           os.system("pip install " + modules_needed[module])
         except:
           print("Failed to install " + modules_needed[module])
   if exiting:
      print ("Exiting the program. Please reopen.")
      wait(1)
      exit()
del exiting
del modules_needed



from PyQt5.QtWidgets import *; #(QWidget, QSlider, QHBoxLayout, QLabel, QGridLayout, QVBoxLayout, QVBoxLayout, QMainWindow, QTextEdit, QLineEdit, QInputDialog, QFileDialog, QAction, qApp, QToolTip, QPushButton, QApplication, QMessageBox) # QLCDNumber
from PyQt5.QtGui import *; #(QIcon, QFont)
from PyQt5.QtCore import *; #(QCoreApplication, Qt)
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.file = ""
        self.isLoaded = False;
        self.questions = [];
        self.answers = [];
        self.chinese = [];
        self.initUI()
        
        
    def initUI(self):
        
        #title = QLabel('Title')
        #author = QLabel('Author')
        #review = QLabel('Review')
        #self.QuestionGrid()
        #self.decryptButton.setGeometry(50,50,50,50)
        self.grid = QGridLayout()
        self.grid.setSpacing(15)
        self.setLayout(self.grid)
        #w=QGridLayout()
        
        self.setGeometry(300, 300, 350, 300)
        #self.setWindowTitle('')    
        self.show()
    def newLoad(self):
        try:
            for i in reversed(range(self.grid.count())): 
              #self.grid.itemAt(i).widget().setParent(None)
              self.grid.itemAt(i).widget().deleteLater()
        except:
            pass
        self.questions = []
        self.answers = []
        self.file = ex.file;
        text = ""
        with codecs.open(self.file,'r',encoding='utf8') as f:
            text = f.read()
        #print(str(text))#str(text,'utf8'))
        
        text_split = text.split(";"); text_splitted = text;
        self.chinese = [];
        counter = 0;
        cur_text = [];
        for i in range(0,len(text)):
            if text[i] not in (",",u",",u";",";","/n",u"，",u"；"):
                continue;
            elif text[i] in (u",",",",u"，"):
                cur_text.append(text[counter: i])
                counter = i + 1;
                continue;
            elif text[i] in (u";",";",u"；"):
                cur_text.append(text[counter: i])
                counter = i + 1;
                self.chinese.append(cur_text);
                cur_text = [];
                continue;
            else:
                continue;
        self.chinese = randomize_list(self.chinese);
        #print(len(self.chinese))
                
            
##        for i in range(0,len(text_split) - 2):
##            cur_thingy = []
##            cur_thingy.append(text_splitted[0:text_splitted.index(u",")])
##            text_splitted = text_splitted[text_splitted.index(u",") + 1:len(text_splitted) - 1]
##            cur_thingy.append(text_splitted[0:text_splitted.index(u",")])
##            text_splitted = text_splitted[text_splitted.index(u",") + 1:len(text_splitted) - 1]
##            cur_thingy.append(text_splitted[0:text_splitted.index(u";")])
##            self.chinese.append(cur_thingy)
##            text_splitted = text_splitted[text_splitted.index(u";") + 1: len(text_splitted) - 1]
##        print(text_splitted[text_splitted.index(u",") + 1:])
##        """
##        cur_thingy = []
##        cur_thingy.append(text_splitted[0:text_splitted.index(u",")])
##        text_splitted = text_splitted[text_splitted.index(u",") + 1:len(text_splitted) - 1]
##        cur_thingy.append(text_splitted[0:text_splitted.index(u",")])
##        text_splitted = text_splitted[text_splitted.index(u",") + 1:len(text_splitted) - 1]
##        cur_thingy.append(text_splitted[0:len(text_splitted) - 2])
##        self.chinese.append(cur_thingy)
##        """
        #print(self.chinese[len(self.chinese) - 1][2])
        #self.chinese.append(text_splitted[0:text_splitted.index(u",")])
        #print(len(self.chinese))
        """
        text_split2 = []
        a = 0
        for i in range(0,len(text_split)):
            if (";" in text_split[i]):
                text_split2.append("".join(text_split[i - a:i]))
                a = 0
                continue
            else:
                a += 1
        """
        #print(len(text_split2))
        for i in range(0,len(text_split) - 1):
            #print(len(text_split2[i][0]))
            #b = text.split(";")[i];
            #b = b[0:b[i].index(',')];
            self.questions.append([
            QLabel(u"Chinese: " + self.chinese[i][0].lstrip()),
            QLabel('Pinyin'),
            QLineEdit(),
            QLabel('English'),
            QLineEdit(),
            (self.chinese[i]),
            ])
        questionlen = len(self.questions)
        if questionlen < 3:
            fontsize = 35;
        elif questionlen < 6:
            fontsize = 30;
        elif questionlen < 8:
            fontsize = 21;
        elif questionlen <= 14:
            fontsize = 17;
        elif questionlen > 14:
            fontsize = 13;
        for i in range(0,questionlen):
            self.questions[i][0].setFont(QFont('SimSun', 21));
        self.answers = []
        for i in range(0,len(self.chinese)):
            #print("A")
            #print(len(self.chinese))
            #print(len(self.chinese[i]))
            abc = (self.chinese[i][1:])
            for i in range(0,len(abc)):
                abc[i] = (abc[i].lstrip()).rstrip()
            self.answers.append(abc)
        #print(self.answers)
        #print(self.Questions[0][5])
        #print("A")
        for i in range(0,len(self.questions)):
            self.grid.addWidget(self.questions[i][0],i,0)
            self.grid.addWidget(self.questions[i][1],i,1)
            self.grid.addWidget(self.questions[i][2],i,2)
            self.grid.addWidget(self.questions[i][3],i,3)
            self.grid.addWidget(self.questions[i][4],i,4)
        #self.keyText.setText("")
        self.checkAnswersButton = QPushButton('Check Answers', self)
        self.checkAnswersButton.clicked.connect(self.checkAnswers)
        self.checkAnswersButton.setStatusTip('Checks answers')
        self.grid.addWidget(self.checkAnswersButton,len(self.questions) + 1,2)
        self.show()
    def checkAnswers(self):
        incorrectPinyin = []
        incorrectEnglish = []
        for i in range(0,len(self.questions)):
            pinyin = self.questions[i][2].text();
            english = self.questions[i][4].text();
            if (pinyin == "" or english == ""):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Error")
                msg.setText("Not all boxes were filled in.")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                self.show()
                return();
            if (pinyin.lower() != self.answers[i][0].lower()):
                incorrectPinyin.append(i)
            englishExpanded = []
            #print(self.answers)
            for a in range(1,len(self.answers[i])):
                self.answers[i][a] = self.answers[i][a].lower()
            if (english.lower() not in self.answers[i][1:]):
                incorrectEnglish.append(i)
        #print("iPinyin", incorrectPinyin)
        #print("iEnglish", incorrectEnglish)
        #for i in range(0,len(incorrectPinyin)):
        #    print(self.answers[incorrectPinyin[i]])
        #for i in range(0,len(incorrectEnglish)):
        #    print(self.answers[incorrectEnglish[i]])
        if (len(incorrectPinyin) > 0) or (len(incorrectEnglish) > 0):
            msg_text = []
            for i in incorrectPinyin:
                msg_text.append(u"Incorrect Pinyin for: " + self.chinese[i][0].lstrip() + ". Correct Pinyin: " + str(self.answers[i][0].lower()))
            for i in incorrectEnglish:
                msg_text.append(u"Incorrect English for: " + self.chinese[i][0].lstrip() + ". Correct English: " + str(self.answers[i][1].lower()))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Results")
            msg.setText("\n".join(msg_text))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.show()
            return();
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Results")
            msg.setText("You got them all right!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.show()
            return();
            
                
##
class Main(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.file = ""
        self.isDone = False
        self.initUI()        
    def initUI(self):
        #self.main_widget = QWidget(self)
        #self.main_layout = QVBoxLayout(self.main_widget)
        #self.main_layout.sizeConstraint = QLayout.SetDefaultConstraint
        #self.main_layout.addWidget(Example())
        #self.textEdit = QTextEdit()
        self.exam = Example()
        self.setCentralWidget(self.exam)
        #self.setPasses(5)
        openFile = QAction(QIcon('assets\web\open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showFileOpenDialog)
        exitAction = QAction(QIcon('assets\web\exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        QToolTip.setFont(QFont('SansSerif', 10))
##        
##        #self.setToolTip('This is a <b>QWidget</b> widget')
        #self.toolbar = self.addToolBar('Exit')
        #self.toolbar.addAction(exitAction)
        #btn = QPushButton('Quit', self)
        #btn.clicked.connect(QCoreApplication.instance().quit)
        #btn.resize(btn.sizeHint())
        #btn.move(50, 50)
        #self.btns = QPushButton('Dialog', self)
        #self.btns.move(20, 20)
        #self.btns.clicked.connect(self.showDialog)
        
        #self.le = QLineEdit(self)
        #self.le.move(130, 22)
        #passesLabel = QLabel('Passes:')
        #sssLabel = QLabel('Passes:')
        #passesSlider = QSlider(Qt.Horizontal, self)
        #passesSlider.valueChanged.connect(self.passesUpdate)
        #passesSlider.move(80,40)
        #hbox = QHBoxLayout()
        #hbox.addStretch(1)
        #hbox.addWidget(passesLabel)
        #hbox.addWidget(passesSlider)
        #vbox = QVBoxLayout()
        #self.setCentralWidget(QWidget(self))
        #vbox.addStretch(1)
        #vbox.addLayout(hbox)
        
        
        #mainGrid = QGridLayout()
        #mainGrid.setSpacing(10)
        #mainGrid.addWidget(passesLabel, 1, 0)
        #mainGrid.addWidget(passesSlider, 1, 1)
        #self.setSpacing(1)
        #self.addWidget(passesLabel, 1, 0)
        #self.addWidget(passesSlider, 1, 1)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(exitAction)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('CRQ Practice')
        #self.setWindowIcon(QIcon('assets\pointericon.png'))
        self.show()
    def closeEvent(self, event):
        event.accept()
    
    """def showDialog(self):
        
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        
        if ok:
            self.le.setText(str(text))
        
    """
    def showFileOpenDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File')
        if fname[0]:
            print(fname[0])
            self.saved = False;
            self.file = fname[0];
            self.exam.newLoad()
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())


        
        
##if __name__ == '__main__':
##    
##    app = QApplication(sys.argv)
##    ex = Example()
##    sys.exit(app.exec_())
