# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyRailBaronNaIZhB.ui'
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
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(949, 820)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(680, 300))
        MainWindow.setMaximumSize(QSize(16384, 16384))
        MainWindow.setStyleSheet(u"\n"
"background-color: #c3ceda;\n"
"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setMinimumSize(QSize(700, 0))
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
        self.gridLayout_2 = QGridLayout(self.tab_payout)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chk_rbUS = QCheckBox(self.tab_payout)
        self.chk_rbUS.setObjectName(u"chk_rbUS")
        self.chk_rbUS.setStyleSheet(u"color: rgb(0, 75, 112);")
        self.chk_rbUS.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.chk_rbUS)

        self.chk_bcUS = QCheckBox(self.tab_payout)
        self.chk_bcUS.setObjectName(u"chk_bcUS")
        self.chk_bcUS.setStyleSheet(u"color: rgb(0, 75, 112);")
        self.chk_bcUS.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.chk_bcUS)

        self.chk_bcUK = QCheckBox(self.tab_payout)
        self.chk_bcUK.setObjectName(u"chk_bcUK")
        self.chk_bcUK.setStyleSheet(u"color: rgb(0, 75, 112);")
        self.chk_bcUK.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.chk_bcUK)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.tab_payout)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setStyleSheet(u"color: rgb(0, 75, 112);")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.doubleSpinBox = QDoubleSpinBox(self.tab_payout)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(75, 30))
        font = QFont()
        font.setPointSize(9)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setStyleSheet(u"background-color: rgb(12, 65, 96);\n"
"color: rgb(195, 206, 218);")
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(1.000000000000000)
        self.doubleSpinBox.setMaximum(3.000000000000000)
        self.doubleSpinBox.setSingleStep(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.label = QLabel(self.tab_payout)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(0, 75, 112);")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.tab_payout)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 75, 112);")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_payout_symbol = QLabel(self.tab_payout)
        self.lbl_payout_symbol.setObjectName(u"lbl_payout_symbol")
        self.lbl_payout_symbol.setMaximumSize(QSize(35, 16777215))
        font1 = QFont()
        font1.setPointSize(36)
        self.lbl_payout_symbol.setFont(font1)
        self.lbl_payout_symbol.setStyleSheet(u"background-color: rgb(12, 65, 96);\n"
"color: rgb(195, 206, 218);")

        self.horizontalLayout_2.addWidget(self.lbl_payout_symbol)

        self.lbl_payout = QLabel(self.tab_payout)
        self.lbl_payout.setObjectName(u"lbl_payout")
        self.lbl_payout.setMaximumSize(QSize(300, 16777215))
        self.lbl_payout.setFont(font1)
        self.lbl_payout.setStyleSheet(u"background-color: rgb(12, 65, 96);\n"
"color: rgb(195, 206, 218);")
        self.lbl_payout.setTextFormat(Qt.TextFormat.AutoText)
        self.lbl_payout.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lbl_payout)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 4, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lv_source = QListWidget(self.tab_payout)
        self.lv_source.setObjectName(u"lv_source")
        self.lv_source.setMinimumSize(QSize(50, 50))
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

        self.horizontalLayout_5.addWidget(self.lv_source)

        self.lv_destination = QListWidget(self.tab_payout)
        self.lv_destination.setObjectName(u"lv_destination")
        self.lv_destination.setMinimumSize(QSize(50, 50))
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

        self.horizontalLayout_5.addWidget(self.lv_destination)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 3, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 4, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.tab_payout)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.textEdit = QTextEdit(self.tab_payout)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
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

        self.verticalLayout_4.addWidget(self.textEdit)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 3, 2, 1, 2)

        self.tab_widget.addTab(self.tab_payout, "")
        self.tab_destination = QWidget()
        self.tab_destination.setObjectName(u"tab_destination")
        self.gridLayout = QGridLayout(self.tab_destination)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.tab_destination)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(0, 75, 112);")

        self.verticalLayout_3.addWidget(self.label_4)

        self.tbl_region = QTableWidget(self.tab_destination)
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

        self.verticalLayout_3.addWidget(self.tbl_region)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.tab_destination)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(0, 75, 112);")

        self.verticalLayout_2.addWidget(self.label_5)

        self.tbl_destination = QTableWidget(self.tab_destination)
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

        self.verticalLayout_2.addWidget(self.tbl_destination)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.tab_widget.addTab(self.tab_destination, "")

        self.horizontalLayout.addWidget(self.tab_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RailBaron", None))
        self.chk_rbUS.setText(QCoreApplication.translate("MainWindow", u"Rail Baron US", None))
        self.chk_bcUS.setText(QCoreApplication.translate("MainWindow", u"Box Cars US", None))
        self.chk_bcUK.setText(QCoreApplication.translate("MainWindow", u"Box Cars UK", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Payout Multiplier", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destination", None))
        self.lbl_payout_symbol.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.lbl_payout.setText(QCoreApplication.translate("MainWindow", u"999999", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Game Notes:", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_payout), QCoreApplication.translate("MainWindow", u"Payouts", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Select Region:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destinations Table:", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_destination), QCoreApplication.translate("MainWindow", u"Destination Selection", None))
    # retranslateUi

