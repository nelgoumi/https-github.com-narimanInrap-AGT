# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_magDialog.ui'
#
# Created: Mon Apr 24 17:40:53 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AGTMagDialog(object):
    def setupUi(self, AGTMagDialog):
        AGTMagDialog.setObjectName(_fromUtf8("AGTMagDialog"))
        AGTMagDialog.resize(359, 534)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AGTMagDialog.sizePolicy().hasHeightForWidth())
        AGTMagDialog.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QtGui.QGridLayout(AGTMagDialog)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.widget_2 = QtGui.QWidget(AGTMagDialog)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.inFileLine = QtGui.QLineEdit(self.widget_2)
        self.inFileLine.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.inFileLine.setObjectName(_fromUtf8("inFileLine"))
        self.horizontalLayout.addWidget(self.inFileLine)
        self.ButtonBrowse = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonBrowse.sizePolicy().hasHeightForWidth())
        self.ButtonBrowse.setSizePolicy(sizePolicy)
        self.ButtonBrowse.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ButtonBrowse.setObjectName(_fromUtf8("ButtonBrowse"))
        self.horizontalLayout.addWidget(self.ButtonBrowse)
        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 1, 1)
        self.gBox_Output = QtGui.QGroupBox(AGTMagDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gBox_Output.sizePolicy().hasHeightForWidth())
        self.gBox_Output.setSizePolicy(sizePolicy)
        self.gBox_Output.setObjectName(_fromUtf8("gBox_Output"))
        self.gridLayout = QtGui.QGridLayout(self.gBox_Output)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboEncoding = QtGui.QComboBox(self.gBox_Output)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboEncoding.sizePolicy().hasHeightForWidth())
        self.comboEncoding.setSizePolicy(sizePolicy)
        self.comboEncoding.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comboEncoding.setObjectName(_fromUtf8("comboEncoding"))
        self.gridLayout.addWidget(self.comboEncoding, 1, 3, 1, 3)
        self.label_georefscr = QtGui.QLabel(self.gBox_Output)
        self.label_georefscr.setObjectName(_fromUtf8("label_georefscr"))
        self.gridLayout.addWidget(self.label_georefscr, 2, 0, 1, 2)
        self.datFilechkbox = QtGui.QCheckBox(self.gBox_Output)
        self.datFilechkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.datFilechkbox.setObjectName(_fromUtf8("datFilechkbox"))
        self.gridLayout.addWidget(self.datFilechkbox, 3, 0, 1, 4)
        self.coordFieldschk = QtGui.QCheckBox(self.gBox_Output)
        self.coordFieldschk.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.coordFieldschk.setObjectName(_fromUtf8("coordFieldschk"))
        self.gridLayout.addWidget(self.coordFieldschk, 3, 4, 1, 2)
        self.ButtonBrowseShape = QtGui.QPushButton(self.gBox_Output)
        self.ButtonBrowseShape.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ButtonBrowseShape.setObjectName(_fromUtf8("ButtonBrowseShape"))
        self.gridLayout.addWidget(self.ButtonBrowseShape, 0, 5, 1, 1)
        self.outputFilename = QtGui.QLineEdit(self.gBox_Output)
        self.outputFilename.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.outputFilename.setObjectName(_fromUtf8("outputFilename"))
        self.gridLayout.addWidget(self.outputFilename, 0, 1, 1, 4)
        self.outputLabel = QtGui.QLabel(self.gBox_Output)
        self.outputLabel.setObjectName(_fromUtf8("outputLabel"))
        self.gridLayout.addWidget(self.outputLabel, 0, 0, 1, 1)
        self.label_enconding = QtGui.QLabel(self.gBox_Output)
        self.label_enconding.setObjectName(_fromUtf8("label_enconding"))
        self.gridLayout.addWidget(self.label_enconding, 1, 0, 1, 2)
        self.comboCRS = QtGui.QComboBox(self.gBox_Output)
        self.comboCRS.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboCRS.sizePolicy().hasHeightForWidth())
        self.comboCRS.setSizePolicy(sizePolicy)
        self.comboCRS.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboCRS.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comboCRS.setObjectName(_fromUtf8("comboCRS"))
        self.gridLayout.addWidget(self.comboCRS, 2, 3, 1, 3)
        self.gridLayout_5.addWidget(self.gBox_Output, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(AGTMagDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.decimChk = QtGui.QCheckBox(self.groupBox_4)
        self.decimChk.setChecked(True)
        self.decimChk.setObjectName(_fromUtf8("decimChk"))
        self.horizontalLayout_2.addWidget(self.decimChk)
        self.decimSpin = QtGui.QSpinBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decimSpin.sizePolicy().hasHeightForWidth())
        self.decimSpin.setSizePolicy(sizePolicy)
        self.decimSpin.setSuffix(_fromUtf8(""))
        self.decimSpin.setPrefix(_fromUtf8("1/"))
        self.decimSpin.setMinimum(1)
        self.decimSpin.setMaximum(100)
        self.decimSpin.setProperty("value", 10)
        self.decimSpin.setObjectName(_fromUtf8("decimSpin"))
        self.horizontalLayout_2.addWidget(self.decimSpin)
        self.gridLayout_5.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(AGTMagDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        self.medchk = QtGui.QCheckBox(self.groupBox_2)
        self.medchk.setChecked(True)
        self.medchk.setObjectName(_fromUtf8("medchk"))
        self.gridLayout_3.addWidget(self.medchk, 0, 0, 1, 1)
        self.percentilechk = QtGui.QCheckBox(self.groupBox_2)
        self.percentilechk.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentilechk.sizePolicy().hasHeightForWidth())
        self.percentilechk.setSizePolicy(sizePolicy)
        self.percentilechk.setObjectName(_fromUtf8("percentilechk"))
        self.gridLayout_3.addWidget(self.percentilechk, 3, 1, 1, 1)
        self.percentSpin = QtGui.QSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentSpin.sizePolicy().hasHeightForWidth())
        self.percentSpin.setSizePolicy(sizePolicy)
        self.percentSpin.setSuffix(_fromUtf8(""))
        self.percentSpin.setPrefix(_fromUtf8(""))
        self.percentSpin.setMinimum(0)
        self.percentSpin.setMaximum(100)
        self.percentSpin.setProperty("value", 25)
        self.percentSpin.setObjectName(_fromUtf8("percentSpin"))
        self.gridLayout_3.addWidget(self.percentSpin, 3, 2, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(AGTMagDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.polyOrdSpin = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.polyOrdSpin.sizePolicy().hasHeightForWidth())
        self.polyOrdSpin.setSizePolicy(sizePolicy)
        self.polyOrdSpin.setSuffix(_fromUtf8(""))
        self.polyOrdSpin.setPrefix(_fromUtf8(""))
        self.polyOrdSpin.setMinimum(1)
        self.polyOrdSpin.setMaximum(3)
        self.polyOrdSpin.setProperty("value", 3)
        self.polyOrdSpin.setObjectName(_fromUtf8("polyOrdSpin"))
        self.gridLayout_2.addWidget(self.polyOrdSpin, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.trendchk = QtGui.QCheckBox(self.groupBox_3)
        self.trendchk.setObjectName(_fromUtf8("trendchk"))
        self.gridLayout_2.addWidget(self.trendchk, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(AGTMagDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 1, 1, 1, 1)
        self.thresSpin = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresSpin.sizePolicy().hasHeightForWidth())
        self.thresSpin.setSizePolicy(sizePolicy)
        self.thresSpin.setDecimals(1)
        self.thresSpin.setSingleStep(0.1)
        self.thresSpin.setProperty("value", 1.2)
        self.thresSpin.setObjectName(_fromUtf8("thresSpin"))
        self.gridLayout_4.addWidget(self.thresSpin, 1, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 2, 1, 1, 1)
        self.gpsSpin = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpsSpin.sizePolicy().hasHeightForWidth())
        self.gpsSpin.setSizePolicy(sizePolicy)
        self.gpsSpin.setSuffix(_fromUtf8(""))
        self.gpsSpin.setPrefix(_fromUtf8(""))
        self.gpsSpin.setMinimum(1)
        self.gpsSpin.setMaximum(16)
        self.gpsSpin.setProperty("value", 3)
        self.gpsSpin.setObjectName(_fromUtf8("gpsSpin"))
        self.gridLayout_4.addWidget(self.gpsSpin, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 0, 1, 1)
        self.stationRmvchk = QtGui.QCheckBox(self.groupBox)
        self.stationRmvchk.setObjectName(_fromUtf8("stationRmvchk"))
        self.gridLayout_4.addWidget(self.stationRmvchk, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 5, 0, 1, 1)
        self.widget = QtGui.QWidget(AGTMagDialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.progressBar = QtGui.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.allProcess_button = QtGui.QPushButton(self.widget)
        self.allProcess_button.setObjectName(_fromUtf8("allProcess_button"))
        self.horizontalLayout_3.addWidget(self.allProcess_button)
        self.gridLayout_5.addWidget(self.widget, 6, 0, 1, 1)

        self.retranslateUi(AGTMagDialog)
        QtCore.QMetaObject.connectSlotsByName(AGTMagDialog)

    def retranslateUi(self, AGTMagDialog):
        AGTMagDialog.setWindowTitle(_translate("AGTMagDialog", "MXPDA processing", None))
        self.label.setText(_translate("AGTMagDialog", "Raw data (.asc)", None))
        self.ButtonBrowse.setText(_translate("AGTMagDialog", "browse", None))
        self.gBox_Output.setTitle(_translate("AGTMagDialog", "Output files", None))
        self.label_georefscr.setText(_translate("AGTMagDialog", "CRS projection", None))
        self.datFilechkbox.setText(_translate("AGTMagDialog", "Export also as .DAT", None))
        self.coordFieldschk.setText(_translate("AGTMagDialog", "Add coordinates fields", None))
        self.ButtonBrowseShape.setText(_translate("AGTMagDialog", "browse", None))
        self.outputLabel.setText(_translate("AGTMagDialog", "Shapefile", None))
        self.label_enconding.setText(_translate("AGTMagDialog", "Character encoding", None))
        self.decimChk.setText(_translate("AGTMagDialog", "Decimation", None))
        self.medchk.setText(_translate("AGTMagDialog", "Median removal", None))
        self.percentilechk.setText(_translate("AGTMagDialog", "Percentile threshold", None))
        self.label_2.setText(_translate("AGTMagDialog", "Polynomial order", None))
        self.trendchk.setText(_translate("AGTMagDialog", "Trend removal", None))
        self.label_3.setText(_translate("AGTMagDialog", "Threshold", None))
        self.label_8.setText(_translate("AGTMagDialog", "GPS located on probe", None))
        self.stationRmvchk.setText(_translate("AGTMagDialog", "Stationary point removal", None))
        self.allProcess_button.setText(_translate("AGTMagDialog", "run", None))
