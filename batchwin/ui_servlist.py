# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'servlist.ui'
#
# Created: Fri Oct 26 13:10:09 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_serversdlg(object):
    def setupUi(self, serversdlg):
        serversdlg.setObjectName(_fromUtf8("serversdlg"))
        serversdlg.resize(832, 465)
        self.buttonBox = QtGui.QDialogButtonBox(serversdlg)
        self.buttonBox.setGeometry(QtCore.QRect(560, 400, 191, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.Newserv = QtGui.QPushButton(serversdlg)
        self.Newserv.setGeometry(QtCore.QRect(20, 410, 93, 31))
        self.Newserv.setObjectName(_fromUtf8("Newserv"))
        self.Delserv = QtGui.QPushButton(serversdlg)
        self.Delserv.setGeometry(QtCore.QRect(140, 410, 93, 31))
        self.Delserv.setObjectName(_fromUtf8("Delserv"))
        self.label = QtGui.QLabel(serversdlg)
        self.label.setGeometry(QtCore.QRect(30, 60, 181, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lahost = QtGui.QLineEdit(serversdlg)
        self.lahost.setGeometry(QtCore.QRect(210, 60, 271, 27))
        self.lahost.setObjectName(_fromUtf8("lahost"))
        self.servlist = QtGui.QTableWidget(serversdlg)
        self.servlist.setGeometry(QtCore.QRect(20, 110, 801, 231))
        self.servlist.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.servlist.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.servlist.setShowGrid(False)
        self.servlist.setObjectName(_fromUtf8("servlist"))
        self.servlist.setColumnCount(7)
        self.servlist.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.servlist.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.servlist.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.servlist.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.servlist.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.servlist.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.servlist.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.servlist.setHorizontalHeaderItem(6, item)
        self.servlist.verticalHeader().setVisible(False)
        self.dispUperms = QtGui.QPushButton(serversdlg)
        self.dispUperms.setGeometry(QtCore.QRect(540, 370, 211, 27))
        self.dispUperms.setObjectName(_fromUtf8("dispUperms"))
        self.label_2 = QtGui.QLabel(serversdlg)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 141, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.wusername = QtGui.QLineEdit(serversdlg)
        self.wusername.setGeometry(QtCore.QRect(210, 10, 271, 27))
        self.wusername.setObjectName(_fromUtf8("wusername"))
        self.connectserv = QtGui.QPushButton(serversdlg)
        self.connectserv.setGeometry(QtCore.QRect(20, 370, 141, 27))
        self.connectserv.setObjectName(_fromUtf8("connectserv"))
        self.disconnserv = QtGui.QPushButton(serversdlg)
        self.disconnserv.setGeometry(QtCore.QRect(200, 370, 141, 27))
        self.disconnserv.setObjectName(_fromUtf8("disconnserv"))
        self.label_3 = QtGui.QLabel(serversdlg)
        self.label_3.setGeometry(QtCore.QRect(520, 60, 41, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.laport = QtGui.QComboBox(serversdlg)
        self.laport.setGeometry(QtCore.QRect(590, 60, 78, 27))
        self.laport.setEditable(True)
        self.laport.setObjectName(_fromUtf8("laport"))
        self.laport.addItem(_fromUtf8(""))
        self.laport.addItem(_fromUtf8(""))
        self.laport.addItem(_fromUtf8(""))
        self.laport.addItem(_fromUtf8(""))
        self.laport.addItem(_fromUtf8(""))
        self.laport.addItem(_fromUtf8(""))
        self.laport.addItem(_fromUtf8(""))
        self.getlafrom = QtGui.QPushButton(serversdlg)
        self.getlafrom.setGeometry(QtCore.QRect(390, 370, 98, 27))
        self.getlafrom.setObjectName(_fromUtf8("getlafrom"))
        self.setla = QtGui.QPushButton(serversdlg)
        self.setla.setGeometry(QtCore.QRect(710, 60, 61, 27))
        self.setla.setObjectName(_fromUtf8("setla"))

        self.retranslateUi(serversdlg)
        self.laport.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), serversdlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), serversdlg.reject)
        QtCore.QMetaObject.connectSlotsByName(serversdlg)
        serversdlg.setTabOrder(self.wusername, self.lahost)
        serversdlg.setTabOrder(self.lahost, self.laport)
        serversdlg.setTabOrder(self.laport, self.setla)
        serversdlg.setTabOrder(self.setla, self.servlist)
        serversdlg.setTabOrder(self.servlist, self.connectserv)
        serversdlg.setTabOrder(self.connectserv, self.disconnserv)
        serversdlg.setTabOrder(self.disconnserv, self.Newserv)
        serversdlg.setTabOrder(self.Newserv, self.Delserv)
        serversdlg.setTabOrder(self.Delserv, self.getlafrom)
        serversdlg.setTabOrder(self.getlafrom, self.dispUperms)
        serversdlg.setTabOrder(self.dispUperms, self.buttonBox)

    def retranslateUi(self, serversdlg):
        serversdlg.setWindowTitle(QtGui.QApplication.translate("serversdlg", "Servers List", None, QtGui.QApplication.UnicodeUTF8))
        self.Newserv.setToolTip(QtGui.QApplication.translate("serversdlg", "Add a new server to the list", None, QtGui.QApplication.UnicodeUTF8))
        self.Newserv.setText(QtGui.QApplication.translate("serversdlg", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.Delserv.setToolTip(QtGui.QApplication.translate("serversdlg", "Delete the currently-selected server", None, QtGui.QApplication.UnicodeUTF8))
        self.Delserv.setText(QtGui.QApplication.translate("serversdlg", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("serversdlg", "Obtain local address from", None, QtGui.QApplication.UnicodeUTF8))
        self.lahost.setToolTip(QtGui.QApplication.translate("serversdlg", "<html><head/><body><p>Use this host to discover what &quot;my&quot; IP address is. This can be a web address or another machine in the same network. Make sure you get the port number right - it should be 80 for web hosts.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.servlist.setToolTip(QtGui.QApplication.translate("serversdlg", "List of servers we speak to - double-click to edit", None, QtGui.QApplication.UnicodeUTF8))
        self.servlist.setSortingEnabled(True)
        item = self.servlist.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("serversdlg", "Server", None, QtGui.QApplication.UnicodeUTF8))
        item = self.servlist.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("serversdlg", "Alias", None, QtGui.QApplication.UnicodeUTF8))
        item = self.servlist.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("serversdlg", "IP", None, QtGui.QApplication.UnicodeUTF8))
        item = self.servlist.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("serversdlg", "User", None, QtGui.QApplication.UnicodeUTF8))
        item = self.servlist.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("serversdlg", "A/C", None, QtGui.QApplication.UnicodeUTF8))
        item = self.servlist.horizontalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("serversdlg", "Conn", None, QtGui.QApplication.UnicodeUTF8))
        item = self.servlist.horizontalHeaderItem(6)
        item.setText(QtGui.QApplication.translate("serversdlg", "Sync", None, QtGui.QApplication.UnicodeUTF8))
        self.dispUperms.setToolTip(QtGui.QApplication.translate("serversdlg", "Display user permissions on server", None, QtGui.QApplication.UnicodeUTF8))
        self.dispUperms.setText(QtGui.QApplication.translate("serversdlg", "User Permissions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("serversdlg", "Windows user name", None, QtGui.QApplication.UnicodeUTF8))
        self.wusername.setToolTip(QtGui.QApplication.translate("serversdlg", "This is the windows user name", None, QtGui.QApplication.UnicodeUTF8))
        self.connectserv.setToolTip(QtGui.QApplication.translate("serversdlg", "Click here to connect to server", None, QtGui.QApplication.UnicodeUTF8))
        self.connectserv.setText(QtGui.QApplication.translate("serversdlg", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.disconnserv.setToolTip(QtGui.QApplication.translate("serversdlg", "Click here to disconnect from server", None, QtGui.QApplication.UnicodeUTF8))
        self.disconnserv.setText(QtGui.QApplication.translate("serversdlg", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("serversdlg", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.laport.setToolTip(QtGui.QApplication.translate("serversdlg", "<html><head/><body><p>Specify the port number to use with the host given to get the local address. Use port 80 if it\'s a web server to get the HTTP port.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.laport.setItemText(0, QtGui.QApplication.translate("serversdlg", "80", None, QtGui.QApplication.UnicodeUTF8))
        self.laport.setItemText(1, QtGui.QApplication.translate("serversdlg", "22", None, QtGui.QApplication.UnicodeUTF8))
        self.laport.setItemText(2, QtGui.QApplication.translate("serversdlg", "23", None, QtGui.QApplication.UnicodeUTF8))
        self.laport.setItemText(3, QtGui.QApplication.translate("serversdlg", "25", None, QtGui.QApplication.UnicodeUTF8))
        self.laport.setItemText(4, QtGui.QApplication.translate("serversdlg", "515", None, QtGui.QApplication.UnicodeUTF8))
        self.laport.setItemText(5, QtGui.QApplication.translate("serversdlg", "2000", None, QtGui.QApplication.UnicodeUTF8))
        self.laport.setItemText(6, QtGui.QApplication.translate("serversdlg", "2200", None, QtGui.QApplication.UnicodeUTF8))
        self.getlafrom.setToolTip(QtGui.QApplication.translate("serversdlg", "<html><head/><body><p>Click to say that you want to get the local IP address from the selected server.</p><p>It will try some likely ports, starting with what you put in the port number at the top.</p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.getlafrom.setText(QtGui.QApplication.translate("serversdlg", "LA from", None, QtGui.QApplication.UnicodeUTF8))
        self.setla.setToolTip(QtGui.QApplication.translate("serversdlg", "<html><head/><body><p>Press this to obtain local address from the host and port given and if OK do this each time.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.setla.setText(QtGui.QApplication.translate("serversdlg", "Set", None, QtGui.QApplication.UnicodeUTF8))

