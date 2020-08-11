# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_RasterEquivalentLayerDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AGTRasterEquivalentLayerDialog(object):
    def setupUi(self, AGTRasterEquivalentLayerDialog):
        AGTRasterEquivalentLayerDialog.setObjectName("AGTRasterEquivalentLayerDialog")
        AGTRasterEquivalentLayerDialog.resize(422, 493)
        self.gridLayout = QtWidgets.QGridLayout(AGTRasterEquivalentLayerDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(AGTRasterEquivalentLayerDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_acquisition_totalfield = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_acquisition_totalfield.setGeometry(QtCore.QRect(20, 30, 95, 20))
        self.radioButton_acquisition_totalfield.setObjectName("radioButton_acquisition_totalfield")
        self.radioButton_acquisition_difference = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_acquisition_difference.setGeometry(QtCore.QRect(280, 30, 95, 20))
        self.radioButton_acquisition_difference.setChecked(True)
        self.radioButton_acquisition_difference.setObjectName("radioButton_acquisition_difference")
        self.gridLayout.addWidget(self.groupBox_2, 4, 0, 1, 3)
        self.groupBox_4 = QtWidgets.QGroupBox(AGTRasterEquivalentLayerDialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.doubleSpinBox_acquisition_topsensor = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_acquisition_topsensor.setGeometry(QtCore.QRect(280, 50, 93, 22))
        self.doubleSpinBox_acquisition_topsensor.setProperty("value", 0.95)
        self.doubleSpinBox_acquisition_topsensor.setObjectName("doubleSpinBox_acquisition_topsensor")
        self.doubleSpinBox_acquisition_botsensor = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_acquisition_botsensor.setGeometry(QtCore.QRect(280, 20, 93, 22))
        self.doubleSpinBox_acquisition_botsensor.setProperty("value", 0.3)
        self.doubleSpinBox_acquisition_botsensor.setObjectName("doubleSpinBox_acquisition_botsensor")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 105, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 105, 31))
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox_acquisition_topsensor.raise_()
        self.doubleSpinBox_acquisition_botsensor.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.gridLayout.addWidget(self.groupBox_4, 5, 0, 1, 3)
        self.groupBox_5 = QtWidgets.QGroupBox(AGTRasterEquivalentLayerDialog)
        self.groupBox_5.setObjectName("groupBox_5")
        self.doubleSpinBox_inclinaison = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_inclinaison.setGeometry(QtCore.QRect(290, 20, 91, 22))
        self.doubleSpinBox_inclinaison.setMaximum(90.0)
        self.doubleSpinBox_inclinaison.setProperty("value", 65.0)
        self.doubleSpinBox_inclinaison.setObjectName("doubleSpinBox_inclinaison")
        self.doubleSpinBox_alpha = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_alpha.setGeometry(QtCore.QRect(290, 50, 91, 22))
        self.doubleSpinBox_alpha.setObjectName("doubleSpinBox_alpha")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.groupBox_5, 3, 0, 1, 3)
        self.outputLabel = QtWidgets.QLabel(AGTRasterEquivalentLayerDialog)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout.addWidget(self.outputLabel, 1, 0, 1, 1)
        self.outputFilename = QtWidgets.QLineEdit(AGTRasterEquivalentLayerDialog)
        self.outputFilename.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.outputFilename.setObjectName("outputFilename")
        self.gridLayout.addWidget(self.outputFilename, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(AGTRasterEquivalentLayerDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ButtonBrowseRaster = QtWidgets.QPushButton(AGTRasterEquivalentLayerDialog)
        self.ButtonBrowseRaster.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ButtonBrowseRaster.setObjectName("ButtonBrowseRaster")
        self.gridLayout.addWidget(self.ButtonBrowseRaster, 1, 2, 1, 1)
        self.runButton = QtWidgets.QPushButton(AGTRasterEquivalentLayerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.runButton.setObjectName("runButton")
        self.gridLayout.addWidget(self.runButton, 8, 2, 1, 1)
        self.rastercomboBox = QtWidgets.QComboBox(AGTRasterEquivalentLayerDialog)
        self.rastercomboBox.setObjectName("rastercomboBox")
        self.gridLayout.addWidget(self.rastercomboBox, 0, 1, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(AGTRasterEquivalentLayerDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.doubleSpinBox_thicknesslayer = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_thicknesslayer.setGeometry(QtCore.QRect(280, 50, 93, 22))
        self.doubleSpinBox_thicknesslayer.setProperty("value", 1.0)
        self.doubleSpinBox_thicknesslayer.setObjectName("doubleSpinBox_thicknesslayer")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 151, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 161, 21))
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox_depthlayer = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_depthlayer.setGeometry(QtCore.QRect(280, 20, 93, 22))
        self.doubleSpinBox_depthlayer.setProperty("value", 0.0)
        self.doubleSpinBox_depthlayer.setObjectName("doubleSpinBox_depthlayer")
        self.gridLayout.addWidget(self.groupBox_3, 6, 0, 1, 3)

        self.retranslateUi(AGTRasterEquivalentLayerDialog)
        QtCore.QMetaObject.connectSlotsByName(AGTRasterEquivalentLayerDialog)

    def retranslateUi(self, AGTRasterEquivalentLayerDialog):
        _translate = QtCore.QCoreApplication.translate
        AGTRasterEquivalentLayerDialog.setWindowTitle(_translate("AGTRasterEquivalentLayerDialog", "Couche équivalente"))
        self.groupBox_2.setTitle(_translate("AGTRasterEquivalentLayerDialog", "Acquisition technic"))
        self.radioButton_acquisition_totalfield.setText(_translate("AGTRasterEquivalentLayerDialog", "Total Field "))
        self.radioButton_acquisition_difference.setText(_translate("AGTRasterEquivalentLayerDialog", "Difference"))
        self.groupBox_4.setTitle(_translate("AGTRasterEquivalentLayerDialog", "Acquisition parameters"))
        self.label_3.setText(_translate("AGTRasterEquivalentLayerDialog", "Bottom sensor"))
        self.label_2.setText(_translate("AGTRasterEquivalentLayerDialog", "Top sensor"))
        self.groupBox_5.setTitle(_translate("AGTRasterEquivalentLayerDialog", "Field characteristics"))
        self.label_6.setText(_translate("AGTRasterEquivalentLayerDialog", "Inclinaison"))
        self.label_7.setText(_translate("AGTRasterEquivalentLayerDialog", "Angle alpha"))
        self.outputLabel.setText(_translate("AGTRasterEquivalentLayerDialog", "Raster output"))
        self.label.setText(_translate("AGTRasterEquivalentLayerDialog", "Select raster layer"))
        self.ButtonBrowseRaster.setText(_translate("AGTRasterEquivalentLayerDialog", "Browse"))
        self.runButton.setText(_translate("AGTRasterEquivalentLayerDialog", "Run"))
        self.groupBox_3.setTitle(_translate("AGTRasterEquivalentLayerDialog", "Propriétés de la couche"))
        self.label_4.setText(_translate("AGTRasterEquivalentLayerDialog", "Epaisseur"))
        self.label_5.setText(_translate("AGTRasterEquivalentLayerDialog", "Profondeur"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AGTRasterEquivalentLayerDialog = QtWidgets.QDialog()
    ui = Ui_AGTRasterEquivalentLayerDialog()
    ui.setupUi(AGTRasterEquivalentLayerDialog)
    AGTRasterEquivalentLayerDialog.show()
    sys.exit(app.exec_())