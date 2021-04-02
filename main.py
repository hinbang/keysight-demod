import sys
import time,clr
import pandas as pd
import threading
import numpy as np
from PyQt5 import QtWidgets
from mainwindow import *
import math

try:
    clr.AddReference('C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.Interfaces.dll')
    clr.AddReference('C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.DigitalDemod.Interfaces.dll')
    from Agilent.SA.Vsa import *
    from Agilent.SA.Vsa.DigitalDemod import *
except Exception as e:
    pass

import pandas as pd
import threading
import numpy as np
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox,QApplication
from mainwindow import *


""" class Thread(QThread):
    def __init__(self):
        super(Thread, self).__init__()
    def run(self):
        pass """
    
class DisplayWindow(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(DisplayWindow,self).__init__(parent)
        self.setUi()
    
    def setUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.InstrumentSetup()

        self.demodem_1 = self.ui.comboBox.currentText()
        self.symbol_rate_1 = self.ui.lineEdit.text()
        self.center_freq_1 = self.ui.lineEdit_2.text()
        self.filter_val_1 = self.ui.lineEdit_3.text()

        self.times = 0
        self.ber_count = 0
        self.error_count_total = 0
        self.ber = 0 

        # plot timer
        # self.IQ_data = []
        # threading.Timer(1,self.PlotMap).start()

        self.ui.graphicsView.setRange(xRange=(-1,1), yRange=(-1,1),disableAutoRange=True)
        self.ui.graphicsView.setMouseEnabled(x=False, y=False)
        self.ui.graphicsView_2.setRange(xRange=(-1,1), yRange=(-1,1),disableAutoRange=True)
        self.ui.graphicsView_2.setMouseEnabled(x=False, y=False)

        # channel 1
        self.ui.pushButton.clicked.connect(lambda:self.startDemod(self.ui.comboBox_3.currentText(),self.ui.comboBox.currentText(),self.ui.lineEdit.text(),self.ui.lineEdit_2.text(),self.ui.lineEdit_3.text(),self.appMeasItem_1,1,self.ui.graphicsView,self.ui.label_16))
        self.ui.pushButton_2.clicked.connect(lambda:self.stopDemod(self.timer1,self.ui.label_16,self.ui.graphicsView))
        
        # channel 2
        self.ui.pushButton_3.clicked.connect(lambda:self.startDemod(self.ui.comboBox_4.currentText(),self.ui.comboBox_2.currentText(),self.ui.lineEdit_4.text(),self.ui.lineEdit_5.text(),self.ui.lineEdit_6.text(),self.appMeasItem_2,2,self.ui.graphicsView_2,self.ui.label_17))
        self.ui.pushButton_4.clicked.connect(lambda:self.stopDemod(self.timer1,self.ui.label_16,self.ui.graphicsView))

        #self.ui.pushButton_5.clicked.connect(lambda: self.showDialog(self.ui.label_18))
        #self.ui.pushButton_6.clicked.connect(lambda: self.showDialog(self.ui.label_19))
    
    def showDialog(self,label):
        fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\Users\Administrator\Desktop\VSABitErrorRate')
        originfile_path = fname[0]
        filelist = originfile_path.split('/')
        filename = filelist[-1]
        #if len(filename)>15:
            #filename = filename[0:14]+'...'
        label.setText(filename)

    def stopDemod(self,timer,label,graphViewer):
        timer.stop()
        graphViewer.clear()
        label.setText('关闭')
    
    def InstrumentSetup(self):
        # 实例化一个 application
        self.app = ApplicationFactory.Create()
        if self.app == None:
            self.app = ApplicationFactory.Create(True, '', '', -1)
        # 设置 application 的基本属性
        self.appDisp = self.app.Display
        self.app.IsVisible = True
        self.app.Title = 'Demod Measurement Test'
        # Create four measurement
        self.appMeasItem_1 = self.app.Measurements.SelectedItem
        #self.appMeasItem_2 = self.app.Measurements.SelectedItem
        # self.appMeasItem_2 = self.app.Measurements.SelectedItem # Need to be overWrite 

    # def demod_thread(self):
        # threading.Thread(target=lambda:self.StartDemod(self.ui.comboBox.currentText(),self.ui.lineEdit.text(),self.ui.lineEdit_2.text(),self.ui.lineEdit_3.text(),self.appMeasItem_1,channel_num=0)).start()
                
    def startDemod(self,filename,demodem,symbol_rate,center_freq,filter_val,appMeas,channel_num,graphViewer,filepath):
        print([demodem,symbol_rate,center_freq,filter_val])
        for item in [demodem,symbol_rate,center_freq,filter_val]: 
            if item == '':
                QMessageBox.question(self,"Error","缺少参数！")
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
        measHandle.SymbolRate = int(symbol_rate)*1000000
        measHandle.ResultLength = 4000
        measHandle.FilterAlphaBT = filter_val
        filterType = getattr(MeasurementFilter,'None')
        measHandle.MeasurementFilter = filterType
        measHandle.RecallStateDefinitionsFile(r'C:\Users\Administrator\Desktop\VSABitErrorRate\QAM32.csd')
 

        # 设置中心频率和显示频谱宽度
        appFreq = appMeas.Frequency
        appFreq.Center = int(center_freq)*1000000
        appFreq.Span = 1.5e8

        appMeas.Input.DataFrom = DataSource.Hardware
        appMeas.IsContinuous = True
        appMeas.Restart()

        bMeasDone = 0
        times = 10
        t0=time.time()
        appMeasStatus = appMeas.Status

        while(bMeasDone==0 and (time.time()-t0)<=2):
            time.sleep(1)
            bMeasDone = StatusBits.MeasurementDone
        
        # select IQ trace
        self.appDisp.Traces.SelectedIndex = (channel_num-1)*4
        appTrace_IQ = self.appDisp.Traces.SelectedItem
        # select symbol trace
        self.appDisp.Traces.SelectedIndex = (channel_num-1)*4+3
        appTrace_symbol = self.appDisp.Traces.SelectedItem

        file_dict = {
            '32QAM_120M.csv': r'C:\Users\Administrator\Desktop\VSABitErrorRate\zeros_len4020_32QAM_origin_sym.csv',
            '64QAM_120M.csv': r'C:\Users\Administrator\Desktop\VSABitErrorRate\zeros_len4020_32QAM_origin_sym.csv',
            '64QAM_150M.csv': r'C:\Users\Administrator\Desktop\VSABitErrorRate\zeros_len4020_32QAM_origin_sym.csv',
        }
        Data_origin = pd.read_csv(file_dict[filename])
        self.initChannelTimer(appTrace_IQ,appTrace_symbol,Data_origin,graphViewer,channel_num,demodem)                            


    def initChannelTimer(self,appTrace_IQ,appTrace_symbol,Data_origin,graphViewer,channel_num,demodem):
        exec('self.plot_timer{} = QtCore.QTimer()'.format(channel_num))
        timer = eval('self.plot_timer{}'.format(channel_num))
        timer.timeout.connect(lambda: self.DisplayAll(appTrace_IQ,appTrace_symbol,Data_origin,demodem,channel_num,graphViewer))
        timer.start(100)
        # self.plot_timer = QtCore.QTimer()
        # self.plot_timer.timeout.connect(lambda: self.DisplayAll(self,appTrace_IQ,appTrace_symbol,Data_origin,demodem,channel_num,graphViewer))
        # self.plot_timer.start(100)

    def DisplayAll(self,appTrace_IQ,appTrace_symbol,Data_origin,demodem,channel_num,graphViewer):
        self.PlotMap(appTrace_IQ,graphViewer,channel_num)
        self.BerCal(Data_origin,appTrace_symbol,channel_num,demodem)
     
    def PlotMap(self,appTrace_IQ,graphViewer,channel_num):
        file_path = r'C:\Users\Administrator\Desktop\VSABitErrorRate\demod_Qam_IQ_Data_channel'+str(channel_num)+r'.csv'
        appTrace_IQ.SaveFile(file_path,'CSV', False)
        Data_output = pd.read_csv(file_path)  
        I = Q = []

        tmp_data = Data_output.T.values.tolist()
        print(np.array(tmp_data).shape)
        I = tmp_data[0]
        Q = tmp_data[1]

        graphViewer.clear()
        graphViewer.plot(I,Q,pen=None,symbol='+',symbolSize=1,symbolpen=None,symbolBrush=(100,100,255,50))


    def BerCal(self,Data_origin,appTrace_symbol,channel_num,demodem):
        demod_N = demodem[3:] # value is 16 32 64 or 128
        Demod_N=int(demod_N)
        M=int(math.log(Demod_N,2))   
        self.ber_count += 1
        if self.ber_count==200:
            self.times = 0
            self.ber_count = 0
            self.error_count_total = 0
            self.ber = 0 

        file_path = r'C:\Users\Administrator\Desktop\VSABitErrorRate\demod_Qam_Symbol_Data_channel'+str(channel_num)+r'.csv'
        appTrace_symbol.SaveFile(file_path,'CSV', False)
        Data_output = pd.read_csv(file_path)  
        symbol_list = Data_output.T.values.tolist()  # demod symbol 
        origin_list = Data_origin.T.values.tolist()

        bit_Data_origin = []
        bit_symbol_list = []

        for i in origin_list[0]:
            origin_bin = bin(i)
            origin_bin_list = list(origin_bin[2:])
            zeros_seq = [0 for index in range(M-len(origin_bin_list))] # 生成长度为M-len(b)的零列表
            origin_bit = np.hstack((np.array(zeros_seq),np.array(origin_bin_list)))
            bit_Data_origin.append(list(origin_bit))
        
        #print('111111111111111111111111')
        for j in symbol_list[0]:
            symbol_bin = bin(j)
            symbol_bin_list = list(symbol_bin[2:])
            zeros_seq = [0 for index in range(M-len(symbol_bin_list))] # 生成长度为M-len(b)的零列表
            symbol_bit = np.hstack((np.array(zeros_seq),np.array(symbol_bin_list)))
            bit_symbol_list.append(list(symbol_bit))

        #print('222222222222222222222222')
        frameHeader = bit_Data_origin[0:80]
        frameHeader_array = np.array(frameHeader,dtype='int')
        count_array = np.array(bit_symbol_list[0:80],dtype='int')-frameHeader_array
        count = 80 - np.sum(count_array==0)   
        match_rate = count/80 

        if match_rate>=0.5:
            self.times += 1
            data_array = np.array(bit_symbol_list[80:],dtype='int')
            origin_data_array = np.array(bit_Data_origin[80:],dtype='int')
            error = data_array-origin_data_array
            error_count = len(bit_symbol_list[80:]) - np.sum(error==0)
            self.error_count_total = self.error_count_total+error_count
            self.ber =  self.error_count_total/(self.times*len(bit_symbol_list[80:]))

        print('ber is',self.ber)
        self.ui.label_21.setText(self.ber)
    
    def DataRateCal(self): 
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplayWindow()
    window.show()
    sys.exit(app.exec_())