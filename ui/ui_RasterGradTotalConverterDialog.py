# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_RasterGradTotalConverterDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AGTRasterGradTotalConverterDialog(object):
    def setupUi(self, AGTRasterGradTotalConverterDialog):
        AGTRasterGradTotalConverterDialog.setObjectName("AGTRasterGradTotalConverterDialog")
        AGTRasterGradTotalConverterDialog.resize(451, 578)
        self.gridLayout = QtWidgets.QGridLayout(AGTRasterGradTotalConverterDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.outputLabel = QtWidgets.QLabel(AGTRasterGradTotalConverterDialog)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout.addWidget(self.outputLabel, 1, 0, 1, 1)
        self.outputFilename = QtWidgets.QLineEdit(AGTRasterGradTotalConverterDialog)
        self.outputFilename.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.outputFilename.setObjectName("outputFilename")
        self.gridLayout.addWidget(self.outputFilename, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(AGTRasterGradTotalConverterDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ButtonBrowseRaster = QtWidgets.QPushButton(AGTRasterGradTotalConverterDialog)
        self.ButtonBrowseRaster.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ButtonBrowseRaster.setObjectName("ButtonBrowseRaster")
        self.gridLayout.addWidget(self.ButtonBrowseRaster, 1, 2, 1, 1)
        self.runButton = QtWidgets.QPushButton(AGTRasterGradTotalConverterDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.runButton.setObjectName("runButton")
        self.gridLayout.addWidget(self.runButton, 9, 2, 1, 1)
        self.rastercomboBox = QtWidgets.QComboBox(AGTRasterGradTotalConverterDialog)
        self.rastercomboBox.setObjectName("rastercomboBox")
        self.gridLayout.addWidget(self.rastercomboBox, 0, 1, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(AGTRasterGradTotalConverterDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_acquisition_totalfield = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_acquisition_totalfield.setGeometry(QtCore.QRect(20, 30, 95, 20))
        self.radioButton_acquisition_totalfield.setObjectName("radioButton_acquisition_totalfield")
        self.radioButton_acquisition_difference = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_acquisition_difference.setGeometry(QtCore.QRect(280, 30, 95, 20))
        self.radioButton_acquisition_difference.setChecked(True)
        self.radioButton_acquisition_difference.setObjectName("radioButton_acquisition_difference")
        self.radioButton_acquisition_difftotalfield = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_acquisition_difftotalfield.setGeometry(QtCore.QRect(140, 30, 111, 20))
        self.radioButton_acquisition_difftotalfield.setObjectName("radioButton_acquisition_difftotalfield")
        self.gridLayout.addWidget(self.groupBox_2, 4, 0, 1, 3)
        self.groupBox_4 = QtWidgets.QGroupBox(AGTRasterGradTotalConverterDialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.doubleSpinBox_acquisition_topsensor = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_acquisition_topsensor.setGeometry(QtCore.QRect(230, 50, 93, 22))
        self.doubleSpinBox_acquisition_topsensor.setProperty("value", 0.95)
        self.doubleSpinBox_acquisition_topsensor.setObjectName("doubleSpinBox_acquisition_topsensor")
        self.doubleSpinBox_acquisition_botsensor = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_acquisition_botsensor.setGeometry(QtCore.QRect(230, 20, 93, 22))
        self.doubleSpinBox_acquisition_botsensor.setProperty("value", 0.3)
        self.doubleSpinBox_acquisition_botsensor.setObjectName("doubleSpinBox_acquisition_botsensor")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 105, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 105, 31))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.groupBox_4, 5, 0, 1, 3)
        self.groupBox_5 = QtWidgets.QGroupBox(AGTRasterGradTotalConverterDialog)
        self.groupBox_5.setObjectName("groupBox_5")
        self.doubleSpinBox_inclinaison = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_inclinaison.setGeometry(QtCore.QRect(230, 20, 62, 22))
        self.doubleSpinBox_inclinaison.setMaximum(90.0)
        self.doubleSpinBox_inclinaison.setProperty("value", 65.0)
        self.doubleSpinBox_inclinaison.setObjectName("doubleSpinBox_inclinaison")
        self.doubleSpinBox_alpha = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_alpha.setGeometry(QtCore.QRect(230, 50, 62, 22))
        self.doubleSpinBox_alpha.setObjectName("doubleSpinBox_alpha")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.groupBox_5, 3, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(AGTRasterGradTotalConverterDialog)
        self.groupBox.setObjectName("groupBox")
        self.radioButton_sim_totalfield = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_sim_totalfield.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.radioButton_sim_totalfield.setObjectName("radioButton_sim_totalfield")
        self.radioButton_sim_difference = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_sim_difference.setGeometry(QtCore.QRect(270, 30, 95, 20))
        self.radioButton_sim_difference.setChecked(True)
        self.radioButton_sim_difference.setObjectName("radioButton_sim_difference")
        self.radioButton_sim_difftotalfield = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_sim_difftotalfield.setGeometry(QtCore.QRect(140, 30, 111, 20))
        self.radioButton_sim_difftotalfield.setObjectName("radioButton_sim_difftotalfield")
        self.radioButton_sim_totalfield.raise_()
        self.radioButton_sim_difference.raise_()
        self.groupBox_4.raise_()
        self.radioButton_sim_difftotalfield.raise_()
        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 3)
        self.groupBox_3 = QtWidgets.QGroupBox(AGTRasterGradTotalConverterDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.doubleSpinBox_sim_topsensor = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_sim_topsensor.setGeometry(QtCore.QRect(230, 50, 93, 22))
        self.doubleSpinBox_sim_topsensor.setProperty("value", 0.95)
        self.doubleSpinBox_sim_topsensor.setObjectName("doubleSpinBox_sim_topsensor")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 105, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 105, 21))
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox_sim_botsensor = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_sim_botsensor.setGeometry(QtCore.QRect(230, 20, 93, 22))
        self.doubleSpinBox_sim_botsensor.setProperty("value", 0.3)
        self.doubleSpinBox_sim_botsensor.setObjectName("doubleSpinBox_sim_botsensor")
        self.gridLayout.addWidget(self.groupBox_3, 7, 0, 1, 3)

        self.retranslateUi(AGTRasterGradTotalConverterDialog)
        QtCore.QMetaObject.connectSlotsByName(AGTRasterGradTotalConverterDialog)

    def retranslateUi(self, AGTRasterGradTotalConverterDialog):
        _translate = QtCore.QCoreApplication.translate
        AGTRasterGradTotalConverterDialog.setWindowTitle(_translate("AGTRasterGradTotalConverterDialog", "Difference to Total Field Convertor"))
        self.outputLabel.setText(_translate("AGTRasterGradTotalConverterDialog", "Raster output"))
        self.label.setText(_translate("AGTRasterGradTotalConverterDialog", "Select raster layer"))
        self.ButtonBrowseRaster.setText(_translate("AGTRasterGradTotalConverterDialog", "Browse"))
        self.runButton.setText(_translate("AGTRasterGradTotalConverterDialog", "Run"))
        self.groupBox_2.setTitle(_translate("AGTRasterGradTotalConverterDialog", "Acquisition technic"))
        self.radioButton_acquisition_totalfield.setText(_translate("AGTRasterGradTotalConverterDialog", "Total Field "))
        self.radioButton_acquisition_difference.setText(_translate("AGTRasterGradTotalConverterDialog", "Difference"))
        self.radioButton_acquisition_difftotalfield.setText(_translate("AGTRasterGradTotalConverterDialog", "Dif Total Field"))
        self.groupBox_4.setTitle(_translate("AGTRasterGradTotalConverterDialog", "Acquisition parameters"))
        self.label_3.setText(_translate("AGTRasterGradTotalConverterDialog", "Bottom sensor"))
        self.label_2.setText(_translate("AGTRasterGradTotalConverterDialog", "Top sensor"))
        self.groupBox_5.setTitle(_translate("AGTRasterGradTotalConverterDialog", "Field characteristics"))
        self.label_6.setText(_translate("AGTRasterGradTotalConverterDialog", "Inclinaison"))
        self.label_7.setText(_translate("AGTRasterGradTotalConverterDialog", "Angle alpha"))
        self.groupBox.setTitle(_translate("AGTRasterGradTotalConverterDialog", "Simulated technic"))
        self.radioButton_sim_totalfield.setText(_translate("AGTRasterGradTotalConverterDialog", "Total Field"))
        self.radioButton_sim_difference.setText(_translate("AGTRasterGradTotalConverterDialog", "Difference"))
        self.radioButton_sim_difftotalfield.setText(_translate("AGTRasterGradTotalConverterDialog", "Dif Total Field"))
        self.groupBox_3.setTitle(_translate("AGTRasterGradTotalConverterDialog", "Simulated parameters"))
        self.label_4.setText(_translate("AGTRasterGradTotalConverterDialog", "Top sensor"))
        self.label_5.setText(_translate("AGTRasterGradTotalConverterDialog", "Bottom sensor"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AGTRasterGradTotalConverterDialog = QtWidgets.QDialog()
    ui = Ui_AGTRasterGradTotalConverterDialog()
    ui.setupUi(AGTRasterGradTotalConverterDialog)
    AGTRasterGradTotalConverterDialog.show()
    sys.exit(app.exec_())
