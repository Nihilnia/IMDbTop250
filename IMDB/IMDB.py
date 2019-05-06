from PyQt5.QtWidgets import QPushButton, QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QFileDialog, QWidget, QApplication, QCheckBox
from PyQt5 import QtGui
import sys, os

from bs4 import BeautifulSoup
import requests

class IMdb(QWidget):

    def __init__(self):

        super().__init__()
        self.userInterface()

    def userInterface(self):

        self.logo = QLabel()
        self.logo.setPixmap(QtGui.QPixmap("logo.jpg"))

        self.textEdit01 = QTextEdit()

        self.checkBox50 = QCheckBox("Top 50")
        self.checkBox100 = QCheckBox("Top 100")
        self.checkBox150 = QCheckBox("Top 150")
        self.checkBox200 = QCheckBox("Top 200")
        self.checkBox250 = QCheckBox("Top 250")


        self.buttonGet = QPushButton("Get list!")
        self.buttonClear = QPushButton("Clear")
        self.buttonSave = QPushButton("Save")

        hBoxForLogo = QHBoxLayout()
        hBoxForLogo.addWidget(self.logo)

        vBoxForText = QVBoxLayout()
        vBoxForText.addWidget(self.textEdit01)

        hBoxForBox = QHBoxLayout()
        hBoxForBox.addWidget(self.checkBox50)
        hBoxForBox.addWidget(self.checkBox100)
        hBoxForBox.addWidget(self.checkBox150)
        hBoxForBox.addWidget(self.checkBox200)
        hBoxForBox.addWidget(self.checkBox250)

        hBoxForButtons = QHBoxLayout()
        hBoxForButtons.addWidget(self.buttonGet)
        hBoxForButtons.addWidget(self.buttonClear)
        hBoxForButtons.addWidget(self.buttonSave)

        vBoxForLeft = QVBoxLayout()
        vBoxForLeft.addLayout(vBoxForText)
        vBoxForLeft.addLayout(hBoxForBox)
        vBoxForLeft.addLayout(hBoxForButtons)

        hBoxForEverything = QHBoxLayout()
        hBoxForEverything.addLayout(hBoxForLogo)
        hBoxForEverything.addLayout(vBoxForLeft)

        self.buttonGet.clicked.connect(lambda : self.whenClicked(self.checkBox50.isChecked(), self.checkBox100.isChecked(), self.checkBox150.isChecked(), self.checkBox200.isChecked(), self.checkBox250.isChecked()))
        self.buttonClear.clicked.connect(self.clearSave)
        self.buttonSave.clicked.connect(self.clearSave)


        self.setLayout(hBoxForEverything)
        self.show()

    def getInfos(self, url):

        response = requests.get(url)

        content = response.content

        bringIt = BeautifulSoup(content, "html.parser")

        # movieNames = list()
        # movieDates = list()
        # movieNumbers = list()

        # theList = """"""

        for movies in bringIt.find_all("h3", {"class": "lister-item-header"}):
            # theList += movies.text
            # for namez in movies.find_all("a"):
            #     movieNames.append(namez.text)

            # for numberz in movies.find_all("span", {"class": "lister-item-index unbold text-primary"}):
            #     movieNumbers.append(numberz.text)

            # for datez in movies.find_all("span", {"class": "lister-item-year text-muted unbold"}):
            #     movieDates.append(datez.text)

        # for f, y, z in zip(movieNumbers, movieNames, movieDates):
        #     # theList += f + " "
        #     # theList += y + " "
        #     # theList += z + "\n"
                
            self.textEdit01.append(movies.text)
        

    def whenClicked(self, checkBox50, checkBox100, checkBox150, checkBox200, checkBox250):

        if checkBox50:
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt")
            
        elif checkBox100:
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")

        elif checkBox150:
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt")

        elif checkBox200:
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt")

        elif checkBox250:
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=1&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt")
            self.getInfos(url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt")

    def clearSave(self):

        sender = self.sender()

        if sender.text() == "Clear":
            self.textEdit01.clear()
        elif sender.text() == "Save":
            fileWay = QFileDialog.getSaveFileName(self, "Save...", os.getenv("HOME"))
            userFile = open(fileWay[0], "w", encoding = "utf-8")
            userFile.write(self.textEdit01.toPlainText())
            userFile.close()
            



myApp = QApplication(sys.argv)

createIt = IMdb()

sys.exit(myApp.exec_())