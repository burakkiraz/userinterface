import sys
import sqlite3
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.create_connection()
        self.init_ui()
    def create_connection(self):
        connection = sqlite3.connect("database.db")
        self.cursor = connection.cursor()
        self.cursor.execute("Create Table If not exists users (username TEXT,parola TEXT)")
        connection.commit()
    def init_ui(self):
        self.username = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")
        self.register = QtWidgets.QPushButton("Sign Up")
        self.text_area = QtWidgets.QLabel()


        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.username)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.text_area)
        v_box.addStretch()
        v_box.addWidget(self.login)
        v_box.addWidget(self.register)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("User Interface")

        self.login.clicked.connect(self.loginn)
        self.register.clicked.connect(self.registerr)

        self.show()
    def loginn(self):
        nam = self.username.text()
        par = self.parola.text()

        self.cursor.execute("Select * From users where username = ? and parola = ?",(nam,par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.text_area.setText("User Not Found !\nPlease Try Again ...")
        else:
            self.text_area.setText("Welcome '{}' =)".format(nam))
    def registerr(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Sign Up")
        self.text_area = QtWidgets.QLabel(self.window)
        self.text_area1 = QtWidgets.QLabel(self.window)
        self.text_area2 = QtWidgets.QLabel(self.window)
        self.text_area3 = QtWidgets.QLabel(self.window)
        self.new_username = QtWidgets.QLineEdit(self.window)
        self.new_passcode = QtWidgets.QLineEdit(self.window)
        self.new_passcode.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_passcode2 = QtWidgets.QLineEdit(self.window)
        self.new_passcode2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.registration = QtWidgets.QPushButton(self.window)
        self.cancel = QtWidgets.QPushButton(self.window)
        self.text_area.setText("Username :")
        self.text_area1.setText("Parola :")
        self.text_area2.setText("Verify Parola :")
        self.text_area3.setText("************************************************************************************")
        self.registration.setText("Sign Up")
        self.cancel.setText("Cancel")
        self.text_area.move(25, 50)
        self.text_area1.move(25, 100)
        self.text_area2.move(25, 150)
        self.text_area3.move(25, 220)
        self.new_username.move(105, 48)
        self.new_passcode.move(105, 98)
        self.new_passcode2.move(105, 148)
        self.registration.move(75, 198)
        self.cancel.move(175, 198)
        self.window.setGeometry(500, 500, 275, 275)
        self.registration.clicked.connect(self.sign)
        self.cancel.clicked.connect(self.closee)
        self.window.show()
    def sign(self):
        name = self.new_username.text()
        passcode = self.new_passcode.text()
        passcode2 = self.new_passcode2.text()
        self.cursor.execute("Select * from users where username = ? ",(name,))
        data = self.cursor.fetchall()
        if (len(name) != 0) or (len(passcode)) != 0 or (len(passcode2)) != 0 :
            if len(data) == 0:
                if passcode == passcode2:
                    self.cursor.execute("Insert into users values(?,?)", (name,passcode))
                    self.connection.commit()
                    self.text_area3.setText("Your registration has been succesfully completed...")
                    #self.closee()
                else:
                    self.text_area3.setText("Passwords doesn't match...\nPlease try again..")
                    self.new_username.clear()
                    self.new_passcode.clear()
                    self.new_passcode2.clear()
            else:
                self.text_area3.setText("You cannot use this username since your username has been taken already! Please try it with some other username")
                self.new_username.clear()
        else:
            self.text_area3.setText("You must fill to all blank spaces...")
    def closee(self):
        self.window.close()

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())