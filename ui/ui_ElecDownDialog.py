# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_ElecDownDialog.ui'
#
# Created: Tue May 09 17:49:39 2017
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

class Ui_AGTElecDownDialog(object):
    def setupUi(self, AGTElecDownDialog):
        AGTElecDownDialog.setObjectName(_fromUtf8("AGTElecDownDialog"))
        AGTElecDownDialog.resize(444, 494)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AGTElecDownDialog.sizePolicy().hasHeightForWidth())
        AGTElecDownDialog.setSizePolicy(sizePolicy)
        AGTElecDownDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout = QtGui.QGridLayout(AGTElecDownDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.box = QtGui.QGroupBox(AGTElecDownDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box.sizePolicy().hasHeightForWidth())
        self.box.setSizePolicy(sizePolicy)
        self.box.setTitle(_fromUtf8(""))
        self.box.setObjectName(_fromUtf8("box"))
        self.gridLayout_2 = QtGui.QGridLayout(self.box)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineStepSpin = QtGui.QDoubleSpinBox(self.box)
        self.lineStepSpin.setSingleStep(0.1)
        self.lineStepSpin.setProperty("value", 0.5)
        self.lineStepSpin.setObjectName(_fromUtf8("lineStepSpin"))
        self.gridLayout_2.addWidget(self.lineStepSpin, 11, 2, 1, 1)
        self.gridSizeSpinX = QtGui.QSpinBox(self.box)
        self.gridSizeSpinX.setProperty("value", 30)
        self.gridSizeSpinX.setObjectName(_fromUtf8("gridSizeSpinX"))
        self.gridLayout_2.addWidget(self.gridSizeSpinX, 5, 2, 1, 1)
        self.outputLabel = QtGui.QLabel(self.box)
        self.outputLabel.setObjectName(_fromUtf8("outputLabel"))
        self.gridLayout_2.addWidget(self.outputLabel, 0, 0, 1, 1)
        self.probeConfigCombo = QtGui.QComboBox(self.box)
        self.probeConfigCombo.setObjectName(_fromUtf8("probeConfigCombo"))
        self.gridLayout_2.addWidget(self.probeConfigCombo, 12, 3, 1, 2)
        self.radioButton15 = QtGui.QRadioButton(self.box)
        self.radioButton15.setObjectName(_fromUtf8("radioButton15"))
        self.gridLayout_2.addWidget(self.radioButton15, 2, 0, 1, 1)
        self.radioButton85 = QtGui.QRadioButton(self.box)
        self.radioButton85.setChecked(True)
        self.radioButton85.setObjectName(_fromUtf8("radioButton85"))
        self.gridLayout_2.addWidget(self.radioButton85, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.box)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 1, 1, 1)
        self.outputLabel_2 = QtGui.QLabel(self.box)
        self.outputLabel_2.setObjectName(_fromUtf8("outputLabel_2"))
        self.gridLayout_2.addWidget(self.outputLabel_2, 5, 1, 1, 1)
        self.outputFilename = QtGui.QLineEdit(self.box)
        self.outputFilename.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.outputFilename.setObjectName(_fromUtf8("outputFilename"))
        self.gridLayout_2.addWidget(self.outputFilename, 0, 1, 1, 2)
        self.ButtonBrowse = QtGui.QPushButton(self.box)
        self.ButtonBrowse.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ButtonBrowse.setObjectName(_fromUtf8("ButtonBrowse"))
        self.gridLayout_2.addWidget(self.ButtonBrowse, 0, 4, 1, 1)
        self.nbGridSpin = QtGui.QSpinBox(self.box)
        self.nbGridSpin.setMinimum(1)
        self.nbGridSpin.setObjectName(_fromUtf8("nbGridSpin"))
        self.gridLayout_2.addWidget(self.nbGridSpin, 3, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.box)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 9, 1, 1, 2)
        self.nbChannelSpin = QtGui.QSpinBox(self.box)
        self.nbChannelSpin.setMinimum(1)
        self.nbChannelSpin.setProperty("value", 3)
        self.nbChannelSpin.setObjectName(_fromUtf8("nbChannelSpin"))
        self.gridLayout_2.addWidget(self.nbChannelSpin, 7, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.box)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 12, 1, 1, 2)
        self.label_5 = QtGui.QLabel(self.box)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 11, 1, 1, 1)
        self.nbProbeSpin = QtGui.QSpinBox(self.box)
        self.nbProbeSpin.setMinimum(1)
        self.nbProbeSpin.setProperty("value", 4)
        self.nbProbeSpin.setObjectName(_fromUtf8("nbProbeSpin"))
        self.gridLayout_2.addWidget(self.nbProbeSpin, 9, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.box)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 6, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.box)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 7, 1, 1, 2)
        self.probeSpaceSpin = QtGui.QDoubleSpinBox(self.box)
        self.probeSpaceSpin.setSingleStep(0.1)
        self.probeSpaceSpin.setProperty("value", 0.5)
        self.probeSpaceSpin.setObjectName(_fromUtf8("probeSpaceSpin"))
        self.gridLayout_2.addWidget(self.probeSpaceSpin, 6, 2, 1, 1)
        self.gridSizeSpinY = QtGui.QSpinBox(self.box)
        self.gridSizeSpinY.setProperty("value", 30)
        self.gridSizeSpinY.setObjectName(_fromUtf8("gridSizeSpinY"))
        self.gridLayout_2.addWidget(self.gridSizeSpinY, 5, 4, 1, 1)
        self.outputLabel_3 = QtGui.QLabel(self.box)
        self.outputLabel_3.setObjectName(_fromUtf8("outputLabel_3"))
        self.gridLayout_2.addWidget(self.outputLabel_3, 5, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.box)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 13, 1, 1, 2)
        self.currentIntSpin = QtGui.QDoubleSpinBox(self.box)
        self.currentIntSpin.setMaximum(200.0)
        self.currentIntSpin.setSingleStep(0.1)
        self.currentIntSpin.setProperty("value", 10.0)
        self.currentIntSpin.setObjectName(_fromUtf8("currentIntSpin"))
        self.gridLayout_2.addWidget(self.currentIntSpin, 13, 3, 1, 1)
        self.collectedPtNbSpin = QtGui.QSpinBox(self.box)
        self.collectedPtNbSpin.setMinimum(6)
        self.collectedPtNbSpin.setObjectName(_fromUtf8("collectedPtNbSpin"))
        self.gridLayout_2.addWidget(self.collectedPtNbSpin, 10, 3, 1, 1)
        self.label_10 = QtGui.QLabel(self.box)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 10, 1, 1, 1)
        self.gridLayout.addWidget(self.box, 0, 0, 1, 1)
        self.gBox_filter = QtGui.QGroupBox(AGTElecDownDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gBox_filter.sizePolicy().hasHeightForWidth())
        self.gBox_filter.setSizePolicy(sizePolicy)
        self.gBox_filter.setTitle(_fromUtf8(""))
        self.gBox_filter.setObjectName(_fromUtf8("gBox_filter"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gBox_filter)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_8 = QtGui.QLabel(self.gBox_filter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)
        self.comCombo = QtGui.QComboBox(self.gBox_filter)
        self.comCombo.setObjectName(_fromUtf8("comCombo"))
        self.gridLayout_3.addWidget(self.comCombo, 4, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.gBox_filter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)
        self.baudCombo = QtGui.QComboBox(self.gBox_filter)
        self.baudCombo.setObjectName(_fromUtf8("baudCombo"))
        self.gridLayout_3.addWidget(self.baudCombo, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.gBox_filter, 1, 0, 1, 1)
        self.widget = QtGui.QWidget(AGTElecDownDialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.runButton = QtGui.QPushButton(self.widget)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.horizontalLayout_3.addWidget(self.runButton)
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)

        self.retranslateUi(AGTElecDownDialog)
        QtCore.QMetaObject.connectSlotsByName(AGTElecDownDialog)

    def retranslateUi(self, AGTElecDownDialog):
        AGTElecDownDialog.setWindowTitle(_translate("AGTElecDownDialog", "RM15/RM85 download", None))
        self.outputLabel.setText(_translate("AGTElecDownDialog", "Output file", None))
        self.radioButton15.setText(_translate("AGTElecDownDialog", "RM15", None))
        self.radioButton85.setText(_translate("AGTElecDownDialog", "RM85", None))
        self.label.setText(_translate("AGTElecDownDialog", "Number of grids", None))
        self.outputLabel_2.setText(_translate("AGTElecDownDialog", "Grid size (m)", None))
        self.ButtonBrowse.setText(_translate("AGTElecDownDialog", "browse", None))
        self.label_4.setText(_translate("AGTElecDownDialog", "Number of probes", None))
        self.label_6.setText(_translate("AGTElecDownDialog", "Probe configuration", None))
        self.label_5.setText(_translate("AGTElecDownDialog", "Line step (m)", None))
        self.label_2.setText(_translate("AGTElecDownDialog", "Probe spacing (m)", None))
        self.label_3.setText(_translate("AGTElecDownDialog", "Number of channels", None))
        self.outputLabel_3.setText(_translate("AGTElecDownDialog", " X", None))
        self.label_7.setText(_translate("AGTElecDownDialog", "Current intensity (mA)", None))
        self.label_10.setText(_translate("AGTElecDownDialog", "Number of collected points/step", None))
        self.label_8.setText(_translate("AGTElecDownDialog", "COM port", None))
        self.label_9.setText(_translate("AGTElecDownDialog", "Baud rate", None))
        self.runButton.setText(_translate("AGTElecDownDialog", "run", None))
