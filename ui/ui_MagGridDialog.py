# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_MagGridDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AGTMagGridDialog(object):
    def setupUi(self, AGTMagGridDialog):
        AGTMagGridDialog.setObjectName("AGTMagGridDialog")
        AGTMagGridDialog.resize(375, 465)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AGTMagGridDialog.sizePolicy().hasHeightForWidth())
        AGTMagGridDialog.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QtWidgets.QGridLayout(AGTMagGridDialog)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_4 = QtWidgets.QGroupBox(AGTMagGridDialog)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.inFileLine = QtWidgets.QLineEdit(self.groupBox_4)
        self.inFileLine.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.inFileLine.setObjectName("inFileLine")
        self.gridLayout_4.addWidget(self.inFileLine, 0, 1, 1, 1)
        self.ButtonBrowse = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonBrowse.sizePolicy().hasHeightForWidth())
        self.ButtonBrowse.setSizePolicy(sizePolicy)
        self.ButtonBrowse.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ButtonBrowse.setObjectName("ButtonBrowse")
        self.gridLayout_4.addWidget(self.ButtonBrowse, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.gBox_Output = QtWidgets.QGroupBox(AGTMagGridDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gBox_Output.sizePolicy().hasHeightForWidth())
        self.gBox_Output.setSizePolicy(sizePolicy)
        self.gBox_Output.setObjectName("gBox_Output")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gBox_Output)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.coordFieldschk = QtWidgets.QCheckBox(self.gBox_Output)
        self.coordFieldschk.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.coordFieldschk.setObjectName("coordFieldschk")
        self.gridLayout_3.addWidget(self.coordFieldschk, 1, 2, 1, 2)
        self.outputFilename = QtWidgets.QLineEdit(self.gBox_Output)
        self.outputFilename.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.outputFilename.setObjectName("outputFilename")
        self.gridLayout_3.addWidget(self.outputFilename, 0, 1, 1, 2)
        self.ButtonBrowseShape = QtWidgets.QPushButton(self.gBox_Output)
        self.ButtonBrowseShape.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ButtonBrowseShape.setObjectName("ButtonBrowseShape")
        self.gridLayout_3.addWidget(self.ButtonBrowseShape, 0, 3, 1, 1)
        self.datFilechkbox = QtWidgets.QCheckBox(self.gBox_Output)
        self.datFilechkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.datFilechkbox.setObjectName("datFilechkbox")
        self.gridLayout_3.addWidget(self.datFilechkbox, 1, 0, 1, 2)
        self.outputLabel = QtWidgets.QLabel(self.gBox_Output)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout_3.addWidget(self.outputLabel, 0, 0, 1, 1)
        self.outputLabel.raise_()
        self.outputFilename.raise_()
        self.coordFieldschk.raise_()
        self.ButtonBrowseShape.raise_()
        self.datFilechkbox.raise_()
        self.gridLayout_7.addWidget(self.gBox_Output, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(AGTMagGridDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 0, 1, 1)
        self.medchk = QtWidgets.QCheckBox(self.groupBox_2)
        self.medchk.setChecked(True)
        self.medchk.setObjectName("medchk")
        self.gridLayout_5.addWidget(self.medchk, 0, 0, 1, 1)
        self.percentSpin = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentSpin.sizePolicy().hasHeightForWidth())
        self.percentSpin.setSizePolicy(sizePolicy)
        self.percentSpin.setSuffix("")
        self.percentSpin.setPrefix("")
        self.percentSpin.setMinimum(0)
        self.percentSpin.setMaximum(100)
        self.percentSpin.setProperty("value", 25)
        self.percentSpin.setObjectName("percentSpin")
        self.gridLayout_5.addWidget(self.percentSpin, 1, 2, 1, 1)
        self.percentilechk = QtWidgets.QCheckBox(self.groupBox_2)
        self.percentilechk.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentilechk.sizePolicy().hasHeightForWidth())
        self.percentilechk.setSizePolicy(sizePolicy)
        self.percentilechk.setObjectName("percentilechk")
        self.gridLayout_5.addWidget(self.percentilechk, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(AGTMagGridDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 0, 1, 1)
        self.trendchk = QtWidgets.QCheckBox(self.groupBox_3)
        self.trendchk.setObjectName("trendchk")
        self.gridLayout_6.addWidget(self.trendchk, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 1, 1, 1, 1)
        self.trendPercentileChk = QtWidgets.QCheckBox(self.groupBox_3)
        self.trendPercentileChk.setObjectName("trendPercentileChk")
        self.gridLayout_6.addWidget(self.trendPercentileChk, 2, 1, 1, 1)
        self.polyOrdSpin = QtWidgets.QSpinBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.polyOrdSpin.sizePolicy().hasHeightForWidth())
        self.polyOrdSpin.setSizePolicy(sizePolicy)
        self.polyOrdSpin.setSuffix("")
        self.polyOrdSpin.setPrefix("")
        self.polyOrdSpin.setMinimum(1)
        self.polyOrdSpin.setMaximum(3)
        self.polyOrdSpin.setProperty("value", 3)
        self.polyOrdSpin.setObjectName("polyOrdSpin")
        self.gridLayout_6.addWidget(self.polyOrdSpin, 1, 2, 1, 1)
        self.trendPercentileSpinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.trendPercentileSpinBox.setMaximum(100)
        self.trendPercentileSpinBox.setProperty("value", 25)
        self.trendPercentileSpinBox.setObjectName("trendPercentileSpinBox")
        self.gridLayout_6.addWidget(self.trendPercentileSpinBox, 2, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_3, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(AGTMagGridDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_geo = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_geo.setEnabled(True)
        self.checkBox_geo.setObjectName("checkBox_geo")
        self.gridLayout_2.addWidget(self.checkBox_geo, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 4, 0, 1, 1)
        self.widget = QtWidgets.QWidget(AGTMagGridDialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)
        self.allProcess_button = QtWidgets.QPushButton(self.widget)
        self.allProcess_button.setObjectName("allProcess_button")
        self.gridLayout.addWidget(self.allProcess_button, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.widget, 5, 0, 1, 1)

        self.retranslateUi(AGTMagGridDialog)
        QtCore.QMetaObject.connectSlotsByName(AGTMagGridDialog)

    def retranslateUi(self, AGTMagGridDialog):
        _translate = QtCore.QCoreApplication.translate
        AGTMagGridDialog.setWindowTitle(_translate("AGTMagGridDialog", "MXPDA/GRAD601 processing - Grid survey"))
        self.label.setText(_translate("AGTMagGridDialog", "Raw data (.dat)"))
        self.ButtonBrowse.setText(_translate("AGTMagGridDialog", "browse"))
        self.gBox_Output.setTitle(_translate("AGTMagGridDialog", "Output files"))
        self.coordFieldschk.setText(_translate("AGTMagGridDialog", "Add coordinates fields"))
        self.ButtonBrowseShape.setText(_translate("AGTMagGridDialog", "browse"))
        self.datFilechkbox.setText(_translate("AGTMagGridDialog", "Export also as .DAT"))
        self.outputLabel.setText(_translate("AGTMagGridDialog", "Shapefile"))
        self.medchk.setText(_translate("AGTMagGridDialog", "Median removal"))
        self.percentilechk.setText(_translate("AGTMagGridDialog", "Percentile threshold"))
        self.trendchk.setText(_translate("AGTMagGridDialog", "Trend removal"))
        self.label_2.setText(_translate("AGTMagGridDialog", "Polynomial order"))
        self.trendPercentileChk.setText(_translate("AGTMagGridDialog", "Percentile threshold"))
        self.checkBox_geo.setText(_translate("AGTMagGridDialog", "Georeferencing"))
        self.allProcess_button.setText(_translate("AGTMagGridDialog", "run"))

