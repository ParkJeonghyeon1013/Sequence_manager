# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sequence_manager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import icons_rc

class Ui_MainWindow_Sequence_manager(object):
    def setupUi(self, MainWindow_Sequence_manager):
        if not MainWindow_Sequence_manager.objectName():
            MainWindow_Sequence_manager.setObjectName(u"MainWindow_Sequence_manager")
        MainWindow_Sequence_manager.resize(800, 600)
        self.centralwidget = QWidget(MainWindow_Sequence_manager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit__dirpath = QLineEdit(self.centralwidget)
        self.lineEdit__dirpath.setObjectName(u"lineEdit__dirpath")

        self.horizontalLayout.addWidget(self.lineEdit__dirpath)

        self.toolButton__dirpath = QToolButton(self.centralwidget)
        self.toolButton__dirpath.setObjectName(u"toolButton__dirpath")

        self.horizontalLayout.addWidget(self.toolButton__dirpath)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEdit__work_filepath = QLineEdit(self.centralwidget)
        self.lineEdit__work_filepath.setObjectName(u"lineEdit__work_filepath")

        self.horizontalLayout.addWidget(self.lineEdit__work_filepath)

        self.toolButton__work_filepath = QToolButton(self.centralwidget)
        self.toolButton__work_filepath.setObjectName(u"toolButton__work_filepath")

        self.horizontalLayout.addWidget(self.toolButton__work_filepath)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget__seq_info = QListWidget(self.centralwidget)
        self.listWidget__seq_info.setObjectName(u"listWidget__seq_info")

        self.verticalLayout.addWidget(self.listWidget__seq_info)

        self.label__seq_info = QLabel(self.centralwidget)
        self.label__seq_info.setObjectName(u"label__seq_info")

        self.verticalLayout.addWidget(self.label__seq_info)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.tabWidget__error_seq = QTabWidget(self.centralwidget)
        self.tabWidget__error_seq.setObjectName(u"tabWidget__error_seq")
        self.miss_frame_tab = QWidget()
        self.miss_frame_tab.setObjectName(u"miss_frame_tab")
        self.gridLayout_2 = QGridLayout(self.miss_frame_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidget__missing = QListWidget(self.miss_frame_tab)
        self.listWidget__missing.setObjectName(u"listWidget__missing")

        self.gridLayout_2.addWidget(self.listWidget__missing, 0, 0, 1, 1)

        icon = QIcon()
        icon.addFile(u":/icons/icons/baseline_drive_folder_upload_black_18dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget__error_seq.addTab(self.miss_frame_tab, icon, "")
        self.err_frame_tab = QWidget()
        self.err_frame_tab.setObjectName(u"err_frame_tab")
        self.gridLayout_3 = QGridLayout(self.err_frame_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.listWidget__error_frame = QListWidget(self.err_frame_tab)
        self.listWidget__error_frame.setObjectName(u"listWidget__error_frame")

        self.gridLayout_3.addWidget(self.listWidget__error_frame, 0, 0, 1, 1)

        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/baseline_memory_black_18dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget__error_seq.addTab(self.err_frame_tab, icon1, "")

        self.gridLayout.addWidget(self.tabWidget__error_seq, 1, 1, 1, 1)

        MainWindow_Sequence_manager.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow_Sequence_manager)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuType_Here = QMenu(self.menubar)
        self.menuType_Here.setObjectName(u"menuType_Here")
        MainWindow_Sequence_manager.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow_Sequence_manager)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow_Sequence_manager.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuType_Here.menuAction())

        self.retranslateUi(MainWindow_Sequence_manager)

        self.tabWidget__error_seq.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow_Sequence_manager)
    # setupUi

    def retranslateUi(self, MainWindow_Sequence_manager):
        MainWindow_Sequence_manager.setWindowTitle(QCoreApplication.translate("MainWindow_Sequence_manager", u"MainWindow", None))
        self.toolButton__dirpath.setText(QCoreApplication.translate("MainWindow_Sequence_manager", u"Open Dir", None))
        self.toolButton__work_filepath.setText(QCoreApplication.translate("MainWindow_Sequence_manager", u"Open File", None))
        self.label__seq_info.setText(QCoreApplication.translate("MainWindow_Sequence_manager", u"TextLabel", None))
        self.tabWidget__error_seq.setTabText(self.tabWidget__error_seq.indexOf(self.miss_frame_tab), QCoreApplication.translate("MainWindow_Sequence_manager", u"Missing Frame", None))
        self.tabWidget__error_seq.setTabText(self.tabWidget__error_seq.indexOf(self.err_frame_tab), QCoreApplication.translate("MainWindow_Sequence_manager", u"Error Frame", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow_Sequence_manager", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow_Sequence_manager", u"Help", None))
        self.menuType_Here.setTitle(QCoreApplication.translate("MainWindow_Sequence_manager", u"Type Here", None))
    # retranslateUi

