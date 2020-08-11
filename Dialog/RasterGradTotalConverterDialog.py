# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AGT - Archaeological Geophysics Toolbox
                                 A QGIS plugin
 This plugin does basic processes on geophysical data for Archaeology
                              -------------------
        begin                : 2016-04-14
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Nariman HATAMI / INRAP
        email                : nariman.hatami@inrap.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

#using Unicode for all strings
from __future__ import unicode_literals

import os

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QSettings, QTextCodec, QCoreApplication, Qt

from qgis.core import QgsProject,QgsMapLayer
 
import processing
from ..core.AGTEngine import EngineRaster
from processing.core.Processing import Processing
from processing.tools import *
from osgeo import gdal
from osgeo import ogr,osr, gdal

from ..ui.ui_RasterGradTotalConverterDialog import Ui_AGTRasterGradTotalConverterDialog
from ..toolbox.AGTUtilities import Utilities, AGTEnconding
from ..toolbox.AGTExceptions import *


class RasterGradTotalConverterDialog(QtWidgets.QDialog, Ui_AGTRasterGradTotalConverterDialog):
    def __init__(self, iface, parent=None):
        """Constructor."""
        super(RasterGradTotalConverterDialog, self).__init__(parent)  
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)        
        self.iface = iface
        self.populateProc()
        self.ButtonBrowseRaster.clicked.connect(self.outFileBrowse)            
        self.runButton.clicked.connect(self.rasterGradTotalConverter)
    
    def populateProc(self):
        
        self.rastercomboBox.clear()  
        #layers = self.iface.legendInterface().layers()
        layers = [tree_layer.layer() for tree_layer in QgsProject.instance().layerTreeRoot().findLayers()]
        layer_list = []
        for layer in layers:
            if layer.type() == QgsMapLayer.RasterLayer:
                layer_list.append(layer.name())
        self.rastercomboBox.addItems(layer_list)
        
    def outFileBrowse(self):
        """Opens an open file dialog"""
            
        outFilename = Utilities.saveFileDialog(self, '.tif') 
        if not outFilename:
            return
        self.outputFilename.setText(outFilename)

    def tr(self, message):
        """Get the translation for a string using Qt translation API.        
        """
        return QCoreApplication.translate(u"RasterDlg", message)
    
    def rasterGradTotalConverter(self):


        layers = [tree_layer.layer() for tree_layer in QgsProject.instance().layerTreeRoot().findLayers()]
        layer_list = []
        for layer in layers :
            if layer.type() == QgsMapLayer.RasterLayer:
                layer_list.append(layer)
        selectedLayerIndex = self.rastercomboBox.currentIndex() 
        rasterfile = layer_list[selectedLayerIndex]    
        
        if self.radioButton_acquisition_totalfield.isChecked() and self.radioButton_sim_difference.isChecked():
            case = 1
            sense = 0
        if self.radioButton_acquisition_totalfield.isChecked() and self.radioButton_sim_difftotalfield.isChecked():
            case = 2
            sense = 0
        if self.radioButton_acquisition_difference.isChecked() and self.radioButton_sim_totalfield.isChecked():
            case = 1
            sense = 1
        if self.radioButton_acquisition_difference.isChecked() and self.radioButton_sim_difftotalfield.isChecked():
            case = 3
            sense = 0
        if self.radioButton_acquisition_difftotalfield.isChecked() and self.radioButton_sim_totalfield.isChecked():
            case = 2
            sense = 1
        if self.radioButton_acquisition_difftotalfield.isChecked() and self.radioButton_sim_difference.isChecked():
            case = 3
            sense = 1


        self.engine = EngineRaster(rawDataFilename = rasterfile.source(), outputRasterfile = self.outputFilename.text(), case = case, sense = sense,
                                   botSensorused = self.doubleSpinBox_acquisition_botsensor.value(), topSensorused = self.doubleSpinBox_acquisition_topsensor.value(), 
                                   botSensorsim = self.doubleSpinBox_sim_botsensor.value(), topSensorsim = self.doubleSpinBox_sim_topsensor.value(), 
                                   inclineAngle = self.doubleSpinBox_inclinaison.value(), alphaAngle = self.doubleSpinBox_alpha.value())
        
        self.engine.openRaster()
        self.engine.gradMagTotalfieldconversion()
        self.engine.saveRaster()
        self.addRasterToCanvas()
        self.hideDialog()
    
    def addRasterToCanvas(self):
    
        message = QCoreApplication.translate(u"MagDlg",'Created output Rasterfile:')
        message = '\n'.join([message, unicode(self.outputFilename.text())])
        message = '\n'.join([message, QCoreApplication.translate(u"MagDlg","Would you like to add the new layer to your project?")])            
        addToTOC = QtWidgets.QMessageBox.question(self, "AGT", message,
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.NoButton)
        if addToTOC == QtWidgets.QMessageBox.Yes:
            Utilities.addShapeToCanvas(unicode(self.outputFilename.text()))
        
    def hideDialog(self):
        self.hide()
        
        
        
        
        