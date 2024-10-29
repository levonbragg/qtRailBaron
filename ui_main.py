# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyRailBaronxPXZnh.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDoubleSpinBox,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 719)
        MainWindow.setMinimumSize(QSize(800, 719))
        MainWindow.setMaximumSize(QSize(800, 719))
        MainWindow.setStyleSheet(u"\n"
"background-color: #c3ceda;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setMinimumSize(QSize(0, 0))
        self.tab_widget.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid #c3ceda;\n"
"/*  top:-1px; */ \n"
"  background-color: rgb(115, 143, 167);\n"
"  \n"
"	color: rgb(0, 75, 112);\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"  background-color: rgb(115, 143, 167);\n"
"  border: 1px solid #c3ceda; \n"
"  padding: 15px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  \n"
"	color: rgb(195, 206, 218);\n"
"  background-color: #0c4160;\n"
"/*  margin-bottom: -1px;  */\n"
"}")
        self.tab_payout = QWidget()
        self.tab_payout.setObjectName(u"tab_payout")
        self.tab_payout.setStyleSheet(u"QTabWidget{\n"
"	background-color: rgb(115, 143, 167);\n"
"}")
        self.label = QLabel(self.tab_payout)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 140, 67, 21))
        self.label.setStyleSheet(u"color: rgb(0, 75, 112);")
        self.label_2 = QLabel(self.tab_payout)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 140, 111, 21))
        self.label_2.setStyleSheet(u"color: rgb(0, 75, 112);")
        self.lv_source = QListWidget(self.tab_payout)
        self.lv_source.setObjectName(u"lv_source")
        self.lv_source.setGeometry(QRect(30, 170, 256, 440))
        self.lv_source.setMinimumSize(QSize(256, 440))
        self.lv_source.setStyleSheet(u"QListWidget{\n"
"        color: rgb(0, 75, 112);\n"
"    }\n"
"    QScrollBar:vertical {\n"
"            border: 0px solid #999999;\n"
"            background:#c3ceda;\n"
"            width:10px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"          	border: 0px solid red;\n"
"			border-radius: 4px;\n"
"			background-color: #0c4160;\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.lv_source.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.lv_destination = QListWidget(self.tab_payout)
        self.lv_destination.setObjectName(u"lv_destination")
        self.lv_destination.setGeometry(QRect(300, 170, 256, 440))
        self.lv_destination.setMinimumSize(QSize(256, 440))
        self.lv_destination.setStyleSheet(u"QListWidget{\n"
"        color: rgb(0, 75, 112);\n"
"    }\n"
"    QScrollBar:vertical {\n"
"            border: 0px solid #999999;\n"
"            background:#c3ceda;\n"
"            width:10px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"          	border: 0px solid red;\n"
"			border-radius: 4px;\n"
"			background-color: #0c4160;\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.layoutWidget = QWidget(self.tab_payout)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 20, 141, 85))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.chk_rbUS = QCheckBox(self.layoutWidget)
        self.chk_rbUS.setObjectName(u"chk_rbUS")
        self.chk_rbUS.setStyleSheet(u"color: rgb(0, 75, 112);")
        self.chk_rbUS.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.chk_rbUS)

        self.chk_bcUS = QCheckBox(self.layoutWidget)
        self.chk_bcUS.setObjectName(u"chk_bcUS")
        self.chk_bcUS.setStyleSheet(u"color: rgb(0, 75, 112);")
        self.chk_bcUS.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.chk_bcUS)

        self.chk_bcUK = QCheckBox(self.layoutWidget)
        self.chk_bcUK.setObjectName(u"chk_bcUK")
        self.chk_bcUK.setStyleSheet(u"color: rgb(0, 75, 112);")
        self.chk_bcUK.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.chk_bcUK)

        self.layoutWidget1 = QWidget(self.tab_payout)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(570, 170, 221, 68))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_payout_symbol = QLabel(self.layoutWidget1)
        self.lbl_payout_symbol.setObjectName(u"lbl_payout_symbol")
        self.lbl_payout_symbol.setMaximumSize(QSize(35, 16777215))
        font = QFont()
        font.setPointSize(36)
        self.lbl_payout_symbol.setFont(font)
        self.lbl_payout_symbol.setStyleSheet(u"background-color: rgb(12, 65, 96);\n"
"color: rgb(195, 206, 218);")

        self.horizontalLayout_2.addWidget(self.lbl_payout_symbol)

        self.lbl_payout = QLabel(self.layoutWidget1)
        self.lbl_payout.setObjectName(u"lbl_payout")
        self.lbl_payout.setFont(font)
        self.lbl_payout.setStyleSheet(u"background-color: rgb(12, 65, 96);\n"
"color: rgb(195, 206, 218);")
        self.lbl_payout.setTextFormat(Qt.TextFormat.AutoText)
        self.lbl_payout.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lbl_payout)

        self.layoutWidget2 = QWidget(self.tab_payout)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(200, 20, 178, 32))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(0, 75, 112);")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.doubleSpinBox = QDoubleSpinBox(self.layoutWidget2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(9)
        self.doubleSpinBox.setFont(font1)
        self.doubleSpinBox.setStyleSheet(u"background-color: rgb(12, 65, 96);\n"
"color: rgb(195, 206, 218);")
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(1.000000000000000)
        self.doubleSpinBox.setMaximum(3.000000000000000)
        self.doubleSpinBox.setSingleStep(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox)

        self.tab_widget.addTab(self.tab_payout, "")
        self.tab_destination = QWidget()
        self.tab_destination.setObjectName(u"tab_destination")
        self.layoutWidget3 = QWidget(self.tab_destination)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 70, 801, 402))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 0, 6, 0)
        self.tbl_region = QTableWidget(self.layoutWidget3)
        if (self.tbl_region.columnCount() < 3):
            self.tbl_region.setColumnCount(3)
        if (self.tbl_region.rowCount() < 11):
            self.tbl_region.setRowCount(11)
        self.tbl_region.setObjectName(u"tbl_region")
        self.tbl_region.setMinimumSize(QSize(350, 400))
        font2 = QFont()
        font2.setPointSize(12)
        self.tbl_region.setFont(font2)
        self.tbl_region.setStyleSheet(u"QTableWidget{\n"
"        border: 0px;\n"
"        padding: 5px;\n"
"        selection-background-color: rgb(11, 65, 95);\n"
"        selection-color: #c3ceda;\n"
"        color: rgb(0, 75, 112);\n"
"        alternate-background-color: #adb6c1;\n"
"    }")
        self.tbl_region.setLineWidth(0)
        self.tbl_region.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tbl_region.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tbl_region.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_region.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tbl_region.setRowCount(11)
        self.tbl_region.setColumnCount(3)
        self.tbl_region.horizontalHeader().setVisible(False)
        self.tbl_region.verticalHeader().setVisible(False)

        self.horizontalLayout_4.addWidget(self.tbl_region)

        self.tbl_destination = QTableWidget(self.layoutWidget3)
        if (self.tbl_destination.columnCount() < 3):
            self.tbl_destination.setColumnCount(3)
        if (self.tbl_destination.rowCount() < 11):
            self.tbl_destination.setRowCount(11)
        self.tbl_destination.setObjectName(u"tbl_destination")
        self.tbl_destination.setMinimumSize(QSize(350, 400))
        self.tbl_destination.setFont(font2)
        self.tbl_destination.setStyleSheet(u"QTableWidget{\n"
"        border: 0px;\n"
"        padding: 5px;\n"
"        selection-background-color: rgb(11, 65, 95);\n"
"        selection-color: #c3ceda;\n"
"        color: rgb(0, 75, 112);\n"
"        alternate-background-color: #adb6c1;\n"
"    }\n"
"")
        self.tbl_destination.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tbl_destination.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tbl_destination.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tbl_destination.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_destination.setRowCount(11)
        self.tbl_destination.setColumnCount(3)
        self.tbl_destination.horizontalHeader().setVisible(False)
        self.tbl_destination.verticalHeader().setVisible(False)

        self.horizontalLayout_4.addWidget(self.tbl_destination)

        self.label_4 = QLabel(self.tab_destination)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 141, 21))
        self.label_4.setStyleSheet(u"color: rgb(0, 75, 112);")
        self.label_5 = QLabel(self.tab_destination)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 40, 151, 21))
        self.label_5.setStyleSheet(u"color: rgb(0, 75, 112);")
        self.tab_widget.addTab(self.tab_destination, "")

        self.horizontalLayout.addWidget(self.tab_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RailBaron", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destination", None))
        self.chk_rbUS.setText(QCoreApplication.translate("MainWindow", u"Rail Baron US", None))
        self.chk_bcUS.setText(QCoreApplication.translate("MainWindow", u"Box Cars US", None))
        self.chk_bcUK.setText(QCoreApplication.translate("MainWindow", u"Box Cars UK", None))
        self.lbl_payout_symbol.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.lbl_payout.setText(QCoreApplication.translate("MainWindow", u"999999", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Payout Multiplier", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_payout), QCoreApplication.translate("MainWindow", u"Payouts", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Select Region:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destinations Table:", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_destination), QCoreApplication.translate("MainWindow", u"Destination Selection", None))
    # retranslateUi

