# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jpermdlg.ui'
#
# Created: Sat Nov 17 08:49:37 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_jpermdlg(object):
    def setupUi(self, jpermdlg):
        jpermdlg.setObjectName(_fromUtf8("jpermdlg"))
        jpermdlg.resize(447, 458)
        self.buttonBox = QtGui.QDialogButtonBox(jpermdlg)
        self.buttonBox.setGeometry(QtCore.QRect(230, 400, 176, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(jpermdlg)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.edjob = QtGui.QLabel(jpermdlg)
        self.edjob.setGeometry(QtCore.QRect(110, 30, 331, 17))
        self.edjob.setText(_fromUtf8(""))
        self.edjob.setObjectName(_fromUtf8("edjob"))
        self.widget = QtGui.QWidget(jpermdlg)
        self.widget.setGeometry(QtCore.QRect(51, 72, 313, 304))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ugtake = QtGui.QCheckBox(self.widget)
        self.ugtake.setObjectName(_fromUtf8("ugtake"))
        self.gridLayout.addWidget(self.ugtake, 6, 1, 1, 1)
        self.ggtake = QtGui.QCheckBox(self.widget)
        self.ggtake.setObjectName(_fromUtf8("ggtake"))
        self.gridLayout.addWidget(self.ggtake, 6, 2, 1, 1)
        self.ogtake = QtGui.QCheckBox(self.widget)
        self.ogtake.setObjectName(_fromUtf8("ogtake"))
        self.gridLayout.addWidget(self.ogtake, 6, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.ugive = QtGui.QCheckBox(self.widget)
        self.ugive.setObjectName(_fromUtf8("ugive"))
        self.gridLayout.addWidget(self.ugive, 7, 1, 1, 1)
        self.gread = QtGui.QCheckBox(self.widget)
        self.gread.setObjectName(_fromUtf8("gread"))
        self.gridLayout.addWidget(self.gread, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.gggive = QtGui.QCheckBox(self.widget)
        self.gggive.setObjectName(_fromUtf8("gggive"))
        self.gridLayout.addWidget(self.gggive, 8, 2, 1, 1)
        self.oggive = QtGui.QCheckBox(self.widget)
        self.oggive.setObjectName(_fromUtf8("oggive"))
        self.gridLayout.addWidget(self.oggive, 8, 3, 1, 1)
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.udel = QtGui.QCheckBox(self.widget)
        self.udel.setObjectName(_fromUtf8("udel"))
        self.gridLayout.addWidget(self.udel, 9, 1, 1, 1)
        self.gwrmd = QtGui.QCheckBox(self.widget)
        self.gwrmd.setObjectName(_fromUtf8("gwrmd"))
        self.gridLayout.addWidget(self.gwrmd, 4, 2, 1, 1)
        self.owrmd = QtGui.QCheckBox(self.widget)
        self.owrmd.setObjectName(_fromUtf8("owrmd"))
        self.gridLayout.addWidget(self.owrmd, 4, 3, 1, 1)
        self.oshow = QtGui.QCheckBox(self.widget)
        self.oshow.setObjectName(_fromUtf8("oshow"))
        self.gridLayout.addWidget(self.oshow, 2, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.uwrmd = QtGui.QCheckBox(self.widget)
        self.uwrmd.setObjectName(_fromUtf8("uwrmd"))
        self.gridLayout.addWidget(self.uwrmd, 4, 1, 1, 1)
        self.owrite = QtGui.QCheckBox(self.widget)
        self.owrite.setObjectName(_fromUtf8("owrite"))
        self.gridLayout.addWidget(self.owrite, 1, 3, 1, 1)
        self.gdel = QtGui.QCheckBox(self.widget)
        self.gdel.setObjectName(_fromUtf8("gdel"))
        self.gridLayout.addWidget(self.gdel, 9, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 10, 0, 1, 1)
        self.ukill = QtGui.QCheckBox(self.widget)
        self.ukill.setObjectName(_fromUtf8("ukill"))
        self.gridLayout.addWidget(self.ukill, 10, 1, 1, 1)
        self.gkill = QtGui.QCheckBox(self.widget)
        self.gkill.setObjectName(_fromUtf8("gkill"))
        self.gridLayout.addWidget(self.gkill, 10, 2, 1, 1)
        self.okill = QtGui.QCheckBox(self.widget)
        self.okill.setObjectName(_fromUtf8("okill"))
        self.gridLayout.addWidget(self.okill, 10, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.odel = QtGui.QCheckBox(self.widget)
        self.odel.setObjectName(_fromUtf8("odel"))
        self.gridLayout.addWidget(self.odel, 9, 3, 1, 1)
        self.urdmd = QtGui.QCheckBox(self.widget)
        self.urdmd.setObjectName(_fromUtf8("urdmd"))
        self.gridLayout.addWidget(self.urdmd, 3, 1, 1, 1)
        self.ggive = QtGui.QCheckBox(self.widget)
        self.ggive.setObjectName(_fromUtf8("ggive"))
        self.gridLayout.addWidget(self.ggive, 7, 2, 1, 1)
        self.ogive = QtGui.QCheckBox(self.widget)
        self.ogive.setObjectName(_fromUtf8("ogive"))
        self.gridLayout.addWidget(self.ogive, 7, 3, 1, 1)
        self.grdmd = QtGui.QCheckBox(self.widget)
        self.grdmd.setObjectName(_fromUtf8("grdmd"))
        self.gridLayout.addWidget(self.grdmd, 3, 2, 1, 1)
        self.uread = QtGui.QCheckBox(self.widget)
        self.uread.setObjectName(_fromUtf8("uread"))
        self.gridLayout.addWidget(self.uread, 0, 1, 1, 1)
        self.oread = QtGui.QCheckBox(self.widget)
        self.oread.setObjectName(_fromUtf8("oread"))
        self.gridLayout.addWidget(self.oread, 0, 3, 1, 1)
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.uggive = QtGui.QCheckBox(self.widget)
        self.uggive.setObjectName(_fromUtf8("uggive"))
        self.gridLayout.addWidget(self.uggive, 8, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.utake = QtGui.QCheckBox(self.widget)
        self.utake.setObjectName(_fromUtf8("utake"))
        self.gridLayout.addWidget(self.utake, 5, 1, 1, 1)
        self.gtake = QtGui.QCheckBox(self.widget)
        self.gtake.setObjectName(_fromUtf8("gtake"))
        self.gridLayout.addWidget(self.gtake, 5, 2, 1, 1)
        self.otake = QtGui.QCheckBox(self.widget)
        self.otake.setObjectName(_fromUtf8("otake"))
        self.gridLayout.addWidget(self.otake, 5, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.ushow = QtGui.QCheckBox(self.widget)
        self.ushow.setObjectName(_fromUtf8("ushow"))
        self.gridLayout.addWidget(self.ushow, 2, 1, 1, 1)
        self.gshow = QtGui.QCheckBox(self.widget)
        self.gshow.setObjectName(_fromUtf8("gshow"))
        self.gridLayout.addWidget(self.gshow, 2, 2, 1, 1)
        self.uwrite = QtGui.QCheckBox(self.widget)
        self.uwrite.setObjectName(_fromUtf8("uwrite"))
        self.gridLayout.addWidget(self.uwrite, 1, 1, 1, 1)
        self.ordmd = QtGui.QCheckBox(self.widget)
        self.ordmd.setObjectName(_fromUtf8("ordmd"))
        self.gridLayout.addWidget(self.ordmd, 3, 3, 1, 1)
        self.gwrite = QtGui.QCheckBox(self.widget)
        self.gwrite.setObjectName(_fromUtf8("gwrite"))
        self.gridLayout.addWidget(self.gwrite, 1, 2, 1, 1)

        self.retranslateUi(jpermdlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), jpermdlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), jpermdlg.reject)
        QtCore.QMetaObject.connectSlotsByName(jpermdlg)
        jpermdlg.setTabOrder(self.uread, self.gread)
        jpermdlg.setTabOrder(self.gread, self.oread)
        jpermdlg.setTabOrder(self.oread, self.uwrite)
        jpermdlg.setTabOrder(self.uwrite, self.gwrite)
        jpermdlg.setTabOrder(self.gwrite, self.owrite)
        jpermdlg.setTabOrder(self.owrite, self.ushow)
        jpermdlg.setTabOrder(self.ushow, self.gshow)
        jpermdlg.setTabOrder(self.gshow, self.oshow)
        jpermdlg.setTabOrder(self.oshow, self.urdmd)
        jpermdlg.setTabOrder(self.urdmd, self.grdmd)
        jpermdlg.setTabOrder(self.grdmd, self.ordmd)
        jpermdlg.setTabOrder(self.ordmd, self.uwrmd)
        jpermdlg.setTabOrder(self.uwrmd, self.gwrmd)
        jpermdlg.setTabOrder(self.gwrmd, self.owrmd)
        jpermdlg.setTabOrder(self.owrmd, self.utake)
        jpermdlg.setTabOrder(self.utake, self.gtake)
        jpermdlg.setTabOrder(self.gtake, self.otake)
        jpermdlg.setTabOrder(self.otake, self.ugtake)
        jpermdlg.setTabOrder(self.ugtake, self.ggtake)
        jpermdlg.setTabOrder(self.ggtake, self.ogtake)
        jpermdlg.setTabOrder(self.ogtake, self.ugive)
        jpermdlg.setTabOrder(self.ugive, self.ggive)
        jpermdlg.setTabOrder(self.ggive, self.ogive)
        jpermdlg.setTabOrder(self.ogive, self.uggive)
        jpermdlg.setTabOrder(self.uggive, self.gggive)
        jpermdlg.setTabOrder(self.gggive, self.oggive)
        jpermdlg.setTabOrder(self.oggive, self.udel)
        jpermdlg.setTabOrder(self.udel, self.gdel)
        jpermdlg.setTabOrder(self.gdel, self.odel)
        jpermdlg.setTabOrder(self.odel, self.ukill)
        jpermdlg.setTabOrder(self.ukill, self.gkill)
        jpermdlg.setTabOrder(self.gkill, self.okill)
        jpermdlg.setTabOrder(self.okill, self.buttonBox)

    def retranslateUi(self, jpermdlg):
        jpermdlg.setWindowTitle(QtGui.QApplication.translate("jpermdlg", "Job Permissions", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("jpermdlg", "Perms on job:", None, QtGui.QApplication.UnicodeUTF8))
        self.ugtake.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that user can set the group to his/her own", None, QtGui.QApplication.UnicodeUTF8))
        self.ugtake.setText(QtGui.QApplication.translate("jpermdlg", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.ggtake.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that group can set the group", None, QtGui.QApplication.UnicodeUTF8))
        self.ggtake.setText(QtGui.QApplication.translate("jpermdlg", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.ogtake.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that others can set the group", None, QtGui.QApplication.UnicodeUTF8))
        self.ogtake.setText(QtGui.QApplication.translate("jpermdlg", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("jpermdlg", "Give away owner", None, QtGui.QApplication.UnicodeUTF8))
        self.ugive.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that user can give the job to a different owner", None, QtGui.QApplication.UnicodeUTF8))
        self.ugive.setText(QtGui.QApplication.translate("jpermdlg", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.gread.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that group has read permission", None, QtGui.QApplication.UnicodeUTF8))
        self.gread.setText(QtGui.QApplication.translate("jpermdlg", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("jpermdlg", "Write", None, QtGui.QApplication.UnicodeUTF8))
        self.gggive.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that group can give away group ownership", None, QtGui.QApplication.UnicodeUTF8))
        self.gggive.setText(QtGui.QApplication.translate("jpermdlg", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.oggive.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that others can give away group ownership", None, QtGui.QApplication.UnicodeUTF8))
        self.oggive.setText(QtGui.QApplication.translate("jpermdlg", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("jpermdlg", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.udel.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that user can delete the job", None, QtGui.QApplication.UnicodeUTF8))
        self.udel.setText(QtGui.QApplication.translate("jpermdlg", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.gwrmd.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that group can set permissions", None, QtGui.QApplication.UnicodeUTF8))
        self.gwrmd.setText(QtGui.QApplication.translate("jpermdlg", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.owrmd.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that others can set permissions", None, QtGui.QApplication.UnicodeUTF8))
        self.owrmd.setText(QtGui.QApplication.translate("jpermdlg", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.oshow.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that others have  reveal (is visible) permission", None, QtGui.QApplication.UnicodeUTF8))
        self.oshow.setText(QtGui.QApplication.translate("jpermdlg", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("jpermdlg", "Display mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("jpermdlg", "Read", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("jpermdlg", "Set mode", None, QtGui.QApplication.UnicodeUTF8))
        self.uwrmd.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that user can set permissions", None, QtGui.QApplication.UnicodeUTF8))
        self.uwrmd.setText(QtGui.QApplication.translate("jpermdlg", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.owrite.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that others have write permission", None, QtGui.QApplication.UnicodeUTF8))
        self.owrite.setText(QtGui.QApplication.translate("jpermdlg", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.gdel.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that group can delete the job", None, QtGui.QApplication.UnicodeUTF8))
        self.gdel.setText(QtGui.QApplication.translate("jpermdlg", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("jpermdlg", "Kill", None, QtGui.QApplication.UnicodeUTF8))
        self.ukill.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that user can kill the job", None, QtGui.QApplication.UnicodeUTF8))
        self.ukill.setText(QtGui.QApplication.translate("jpermdlg", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.gkill.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that group can kill the job", None, QtGui.QApplication.UnicodeUTF8))
        self.gkill.setText(QtGui.QApplication.translate("jpermdlg", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.okill.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that others can kill the job", None, QtGui.QApplication.UnicodeUTF8))
        self.okill.setText(QtGui.QApplication.translate("jpermdlg", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("jpermdlg", "Reveal", None, QtGui.QApplication.UnicodeUTF8))
        self.odel.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that others can delete the job", None, QtGui.QApplication.UnicodeUTF8))
        self.odel.setText(QtGui.QApplication.translate("jpermdlg", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.urdmd.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that the user can read the permissions", None, QtGui.QApplication.UnicodeUTF8))
        self.urdmd.setText(QtGui.QApplication.translate("jpermdlg", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.ggive.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that group can give away ownership", None, QtGui.QApplication.UnicodeUTF8))
        self.ggive.setText(QtGui.QApplication.translate("jpermdlg", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.ogive.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that others can give away ownership", None, QtGui.QApplication.UnicodeUTF8))
        self.ogive.setText(QtGui.QApplication.translate("jpermdlg", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.grdmd.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that the group can read the permissions", None, QtGui.QApplication.UnicodeUTF8))
        self.grdmd.setText(QtGui.QApplication.translate("jpermdlg", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.uread.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that user has read permission", None, QtGui.QApplication.UnicodeUTF8))
        self.uread.setText(QtGui.QApplication.translate("jpermdlg", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.oread.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that others have read permission", None, QtGui.QApplication.UnicodeUTF8))
        self.oread.setText(QtGui.QApplication.translate("jpermdlg", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("jpermdlg", "Give away group", None, QtGui.QApplication.UnicodeUTF8))
        self.uggive.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that user can give away the group ownership", None, QtGui.QApplication.UnicodeUTF8))
        self.uggive.setText(QtGui.QApplication.translate("jpermdlg", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("jpermdlg", "Assume ownership", None, QtGui.QApplication.UnicodeUTF8))
        self.utake.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that user can set the owner to him/herself", None, QtGui.QApplication.UnicodeUTF8))
        self.utake.setText(QtGui.QApplication.translate("jpermdlg", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.gtake.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that group can set the owner", None, QtGui.QApplication.UnicodeUTF8))
        self.gtake.setText(QtGui.QApplication.translate("jpermdlg", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.otake.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that others can set the owner", None, QtGui.QApplication.UnicodeUTF8))
        self.otake.setText(QtGui.QApplication.translate("jpermdlg", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("jpermdlg", "Assume group ownership", None, QtGui.QApplication.UnicodeUTF8))
        self.ushow.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that user has reveal (is visible) permission", None, QtGui.QApplication.UnicodeUTF8))
        self.ushow.setText(QtGui.QApplication.translate("jpermdlg", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.gshow.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that group  has reveal (is visible) permission", None, QtGui.QApplication.UnicodeUTF8))
        self.gshow.setText(QtGui.QApplication.translate("jpermdlg", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.uwrite.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that user has write permission", None, QtGui.QApplication.UnicodeUTF8))
        self.uwrite.setText(QtGui.QApplication.translate("jpermdlg", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.ordmd.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that others can read the permissions", None, QtGui.QApplication.UnicodeUTF8))
        self.ordmd.setText(QtGui.QApplication.translate("jpermdlg", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.gwrite.setToolTip(QtGui.QApplication.translate("jpermdlg", "Indicates that group has write permission", None, QtGui.QApplication.UnicodeUTF8))
        self.gwrite.setText(QtGui.QApplication.translate("jpermdlg", "G", None, QtGui.QApplication.UnicodeUTF8))

