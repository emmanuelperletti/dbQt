# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt

from PyQt5.QtSql import QSqlTableModel, QSqlQuery, QSqlDatabase, QSqlDriver, QSqlQueryModel




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tv = tableView = QtWidgets.QTableView(self.centralwidget)
        self.tv.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tv)
        MainWindow.setCentralWidget(self.centralwidget)
        self.model = None
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("test.db")
        if db.open():
            print("open DB success.")
            query = QSqlQuery()
            query.prepare("insert into user ('nom','prenom' )values ('Bauer', 'Jack')")
            # query.exec_("create table person(id int primary key, name varchar(20), address varchar(30))")
            query.exec()

            # query.exec_("insert into user values('Jack', 'shanghai')")
            # query.exec_("insert into user values('Alex', 'chengdu')")
            # query.prepare("SELECT * FROM user")
            # query.exec()
            self.model = QSqlQueryModel()
            self.model.setQuery("SELECT * FROM user LIMIT 10,10")
            self.model.setHeaderData(0,QtCore.Qt.Horizontal,"Nom")
            self.model.setHeaderData(1,QtCore.Qt.Horizontal,"Prénom")
            self.model.setHeaderData(2,QtCore.Qt.Horizontal,"ID")

            # self.tv.setHorizontalHeaderLabels(QString("Nom;Prénom;ID").split(";"))
            # self.model.setHeaderData(1, Qt.Horizontal, "Prénom")
            self.tv.setModel(self.model)

            self.model.setQuery("SELECT * FROM user LIMIT 5")
            # self.tv.setModel(self.model)
            db.close()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
