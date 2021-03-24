import sys
import time,csv,clr
import numpy as np
from PyQt5 import QtWidgets
from mainwindow import *


try:
    clr.AddReference('C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.Interfaces.dll')
    clr.AddReference('C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.DigitalDemod.Interfaces.dll')
    from Agilent.SA.Vsa import *
    from Agilent.SA.Vsa.DigitalDemod import *
except Exception as e:
    pass


class DisplayWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(DisplayWindow,self).__init__(parent)
        self.setUi()
    
    def setUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.InstrumentSetup()

        self.demodem_1 = self.ui.comboBox.currentText()
        self.symbol_rate_1 = self.ui.lineEdit.text()
        self.center_freq_1 = self.ui.lineEdit_2.text()
        self.filter_val_1 = self.ui.lineEdit_3.text()
        self.appMeasItem_1 = ''

        self.ui.graphicsView.setRange(xRange=(-3,3), yRange=(-3,3),disableAutoRange=True)
        self.ui.graphicsView.setMouseEnabled(x=False, y=False)
        self.ui.graphicsView_2.setRange(xRange=(-3,3), yRange=(-3,3),disableAutoRange=True)
        self.ui.graphicsView_2.setMouseEnabled(x=False, y=False)
        self.ui.pushButton.clicked.connect(lambda:self.StartDemod(self.demodem_1,self.symbol_rate_1,self.center_freq_1,self.filter_val_1,self.appMeasItem_1),channel_num=0)
        #self.ui.pushButton_3.clicked.connect(lambda:self.StartDemod())

    def InstrumentSetup(self):
        # 实例化一个 application
        self.app = ApplicationFactory.Create()
        if self.app == None:
            self.app = ApplicationFactory.Create(True, '', '', -1)
        # 设置 application 的基本属性
        self.appDisp = app.Display
        self.app.IsVisible = True
        self.app.Title = 'Demod Measurement Test'
        # Create a measurement
        self.appMeasItem_1 = self.app.Measurements.SelectedItem
        self.appMeasItem_2 = self.app.Measurements.SelectedItem # Need to be overWrite 


    def StartDemod(self,demodem,symbol_rate,center_freq,filter_val,appMeas,channel_num):
        print([demodem,symbol_rate,center_freq,filter_val,appMeas])
        for item in [demodem,symbol_rate,center_freq,filter_val]: 
            if item == '':
                QtWidgets.QMessageBox.question(self,"Error","缺少参数！")
                return None
        # Calibrate the hardware
        appCAL = appMeas.SelectedAnalyzer.Calibration
        appCAL.Calibrate()

        # Config channel
        genericHandle = appMeas.SetMeasurementExtension(MeasurementExtension.ExtensionType())
        measHandle = MeasurementExtension.CastToExtensionType(genericHandle)
        del measHandle
        genericHandle = appMeas.MeasurementExtension
        measHandle = MeasurementExtension.CastToExtensionType(genericHandle)

        # Demod config
        measHandle.Format = getattr(Format,demodem)
        measHandle.PointsPerSymbol = 5
        measHandle.SymbolRate = symbol_rate
        measHandle.ResultLength = 4000
        measHandle.FilterAlphaBT = filter_val
        filterType = getattr(MeasurementFilter,'None')
        measHandle.MeasurementFilter = filterType 

        # 设置中心频率和显示频谱宽度
        appFreq = appMeas.Frequency
        appFreq.Center = center_freq
        appFreq.Span = 1.5e8

        appMeas.Input.DataFrom = DataSource.Hardware
        appMeas.Restart

        bMeasDone = 0
        times = 100
        t0=time.time()
        appMeasStatus = appMeas.Status

        while(bMeasDone==0 and (time.time()-t0)<=2):
            time.sleep(1)
            bMeasDone = StatusBits.MeasurementDone
        
        appTrace = self.appDisp.Traces.Item(3+channel_num*4)

        # plot timer
        self.initPlotTimer()

        Data_origin = csv.reader(r"C:\Users\Administrator\Desktop\VSABitErrorRate\len4020_32QAM_origin_sym.csv")

        for i in range (0,times):
            appTrace.SaveFile(r'C:\Users\Administrator\Desktop\VSABitErrorRate\demod_Qam_Data.csv','CSV', false)
            self.Data_output = csv.reader(r'C:\Users\Administrator\Desktop\VSABitErrorRate\demod_Qam_Data.csv')    
            IQ = []
            self.IQ_data = []
            constellation_32 = np.array([-1-1j, -1-3j, -1+1j, -1+3j, -3-1j, -3-3j, -3+1j, -3+3j, 
                                    1-1j, 1-3j, 1+1j, 1+3j, 3-1j, 3-3j, 3+1j, 3+3j, 
                                    -5-3j, -1-5j, -5+3j, -1+5j, -5-1j, -3-5j, -5+1j, -3+5j, 
                                    5-3j, 1-5j, 5+3j, 1+5j, 5-1j, 3-5j, 5+1j, 3+5j]) / pow(34,0.5)
            constellation_64 = np.array([-7+7j, -7+5j, -7+1j, -7+3j, -7-7j, -7-5j, -7-1j, -7-3j, 
                                    -5+7j, -5+5j, -5+1j, -5+3j, -5-7j, -5-5j, -5-1j, -5-3j, 
                                    -1+7j, -1+5j, -1+1j, -1+3j, -1-7j, -1-5j, -1-1j, -1-3j, 
                                    -3+7j, -3+5j, -3+1j, -3+3j, -3-7j, -3-5j, -3-1j, -3-3j, 
                                    7+7j, 7+5j, 7+1j, 7+3j, 7-7j, 7-5j, 7-1j, 7-3j, 
                                    5+7j, 5+5j, 5+1j, 5+3j, 5-7j, 5-5j, 5-1j, 5-3j, 
                                    1+7j, 1+5j, 1+1j, 1+3j, 1-7j, 1-5j, 1-1j, 1-3j, 
                                    3+7j, 3+5j, 3+1j, 3+3j, 3-7j, 3-5j, 3-1j, 3-3j]) / pow(98,0.5) 
            for i in self.Data_output:
                IQ.append(constellation_32[i])
            self.IQ_data = IQ
                           


    def PlotMap(self):
        self.ui.graphicsView.clear()
        self.ui.graphicsView.plot(self.IQ_data.real, self.IQ_data.imag)
        
    def BerCal(self):
        return None
    
    def DataRateCal(self): 
        return None

    def initPlotTimer(self):
        self.serial_plot_timer = QtCore.QTimer()
        self.serial_plot_timer.timeout.connect(self.PlotMap)
        self.serial_plot_timer.start(1000)

# 删除对象
del app
del appMeas
del appCAL   


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = DisplayWindow()
    window.show()
    sys.exit(app.exec_())