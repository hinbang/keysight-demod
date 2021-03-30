import sys
from PyQt5 import QtWidgets
from mainwindow import *
from ctypes import *
#from Agilent.SA.Vsa import *    #Overwriting by dll method

class DisplayWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(DisplayWindow,self).__init__(parent)
        self.setUi()
    
    def setUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.interface_dll = CDLL("C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.Interfaces.dll")
        self.demod_dll = CDLL("C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.DigitalDemod.Interfaces.dll")
        self.InstrumentSetup()

        self.demodem_1 = self.ui.comboBox.currentText()
        self.symbol_rate_1 = self.ui.lineEdit.text()
        self.center_freq_1 = self.ui.lineEdit_2.text()
        self.filter_val_1 = self.ui.lineEdit_3.text()

        self.ui.graphicsView.setRange(xRange=(-3,3), yRange=(-3,3),disableAutoRange=True)
        self.ui.graphicsView.setMouseEnabled(x=False, y=False)
        self.ui.graphicsView_2.setRange(xRange=(-3,3), yRange=(-3,3),disableAutoRange=True)
        self.ui.graphicsView_2.setMouseEnabled(x=False, y=False)
        self.ui.pushButton.clicked.connect(lambda:self.StartDemod(self.demodem_1,self.symbol_rate_1,self.center_freq_1,self.filter_val_1,self.appMeasItem_1))
        self.ui.pushButton_3.clicked.connect(lambda:self.StartDemod())

    def InstrumentSetup(self):
        self.app = self.dll.ApplicationFactory.Create()
        if self.app is None:
            self.app = self.dll.ApplicationFactory.Create(True, '', '', -1)
        self.app.IsVisible = True
        # Create a measurement
        self.appMeasItem_1 = self.app.Measurements.SelectedItem
        self.appMeasItem_2 = self.app.Measurements.SelectedItem # OverWrite ！！！


    def StartDemod(self,demodem,symbol_rate,center_freq,filter_val,appMeasItem):
        print([demodem,symbol_rate,center_freq,filter_val])
        for item in [demodem,symbol_rate,center_freq,filter_val]: 
            if item == '':
                QtWidgets.QMessageBox.question(self,"Error","缺少参数！")
                return None
        # Calibrate the hardware
        self.appCAL = self.appMeasItem.SelectedAnalyzer.Calibration
        self.appCAL.Calibrate

        # Config channel
        self.measExtensionType = Agilent.SA.Vsa.DigitalDemod.MeasurementExtension.ExtensionType
        self.genericHandle = self.appMeasItem.SetMeasurementExtension(self.measExtensionType)
        self.measHandle = Agilent.SA.Vsa.DigitalDemod.MeasurementExtension.CastToExtensionType(self.genericHandle)
        self.measHandle.delete
        self.genericHandle = self.appMeasItem.MeasurementExtension
        self.measHandle = Agilent.SA.Vsa.DigitalDemod.MeasurementExtension.CastToExtensionType(self.genericHandle)

        # Demod config
        self.measHandle.Format = Agilent.SA.Vsa.DigitalDemod.Format.Qam32
        self.measHandle.PointsPerSymbol = 5
        self.measHandle.SymbolRate = 8e7
        self.measHandle.ResultLength = 4000
        self.measHandle.FilterAlphaBT = 0.2
        self.measHandle.MeasurementFilter = Agilent.SA.Vsa.DigitalDemod.MeasurementFilter
        self.measHandle.RecallStateDefinitionsFile('C:\Users\Administrator\Desktop\VSABitErrorRate\QAM32.csd')



    def PlotMap(self):
        return None
        
    def BerCal(self):
        
        return None
    
    def DataRateCal(self): 
        return None
    


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = DisplayWindow()
    window.show()
    sys.exit(app.exec_())