# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(601, 177)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.max_matches_line = QtWidgets.QLineEdit(self.frame)
        self.max_matches_line.setGeometry(QtCore.QRect(10, 10, 561, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.max_matches_line.setFont(font)
        self.max_matches_line.setInputMethodHints(QtCore.Qt.ImhNone)
        self.max_matches_line.setInputMask("")
        self.max_matches_line.setText("")
        self.max_matches_line.setMaxLength(2)
        self.max_matches_line.setFrame(True)
        self.max_matches_line.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.max_matches_line.setCursorPosition(0)
        self.max_matches_line.setDragEnabled(False)
        self.max_matches_line.setReadOnly(False)
        self.max_matches_line.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.max_matches_line.setClearButtonEnabled(False)
        self.max_matches_line.setObjectName("max_matches_line")
        self.AI_or_player_line = QtWidgets.QLineEdit(self.frame)
        self.AI_or_player_line.setGeometry(QtCore.QRect(10, 55, 561, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.AI_or_player_line.setFont(font)
        self.AI_or_player_line.setMaxLength(1)
        self.AI_or_player_line.setObjectName("AI_or_player_line")
        self.decorLine = QtWidgets.QFrame(self.frame)
        self.decorLine.setWindowModality(QtCore.Qt.NonModal)
        self.decorLine.setEnabled(True)
        self.decorLine.setGeometry(QtCore.QRect(10, 104, 561, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 161, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.decorLine.setPalette(palette)
        self.decorLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.decorLine.setAcceptDrops(False)
        self.decorLine.setFrameShadow(QtWidgets.QFrame.Raised)
        self.decorLine.setLineWidth(2)
        self.decorLine.setMidLineWidth(0)
        self.decorLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.decorLine.setObjectName("decorLine")
        self.continue_btn = QtWidgets.QPushButton(self.frame)
        self.continue_btn.setEnabled(True)
        self.continue_btn.setGeometry(QtCore.QRect(10, 126, 561, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.continue_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.continue_btn.setFont(font)
        self.continue_btn.setTabletTracking(False)
        self.continue_btn.setCheckable(False)
        self.continue_btn.setChecked(False)
        self.continue_btn.setAutoRepeat(False)
        self.continue_btn.setAutoDefault(False)
        self.continue_btn.setDefault(False)
        self.continue_btn.setFlat(False)
        self.continue_btn.setObjectName("continue_btn")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.max_matches_line.setPlaceholderText(_translate("MainWindow", "Максимальное количество спичек в игре (от 6 до 20)"))
        self.AI_or_player_line.setPlaceholderText(_translate("MainWindow", "Против кого играть (0 - ИИ, 1 - игрок)"))
        self.continue_btn.setText(_translate("MainWindow", "Продолжить"))
        self.continue_btn.setShortcut(_translate("MainWindow", "F"))