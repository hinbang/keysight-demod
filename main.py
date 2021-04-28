import sys
import time,clr
import pandas as pd
import numpy as np
from PyQt5 import QtCore
from mainwindow import *
import math,sympy

try:
    clr.AddReference('C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.Interfaces.dll')
    clr.AddReference('C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.DigitalDemod.Interfaces.dll')
    from Agilent.SA.Vsa import *
    from Agilent.SA.Vsa.DigitalDemod import *
except Exception as e:
    pass

from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox,QApplication


class PlotThread(QtCore.QThread):
    update_data = QtCore.pyqtSignal(dict)
    def __init__(self, appTrace_IQ,channel_num,demodem,appTrace_symbol,data_origin,max_rate):
        super().__init__()
        self.appTrace_IQ = appTrace_IQ
        self.channel_num = channel_num
        self.demodem = demodem
        self.appTrace_symbol = appTrace_symbol
        self.data_origin = data_origin
        self.max_rate = max_rate
    def run(self):
        self.fuc = DataProcess(self.appTrace_IQ,self.channel_num,self.demodem,self.appTrace_symbol,self.data_origin,self.max_rate)
        while True: 
            IQ_data = self.fuc.plot()
            self.update_data.emit(IQ_data)
            time.sleep(10)

class BerThread(QtCore.QThread):
    update_data = QtCore.pyqtSignal(dict)
    def __init__(self, appTrace_IQ,channel_num,demodem,appTrace_symbol,data_origin,max_rate):
        super().__init__()
        self.appTrace_IQ = appTrace_IQ
        self.channel_num = channel_num
        self.demodem = demodem
        self.appTrace_symbol = appTrace_symbol
        self.data_origin = data_origin
        self.max_rate = max_rate
    def run(self):
        self.fuc = DataProcess(self.appTrace_IQ,self.channel_num,self.demodem,self.appTrace_symbol,self.data_origin,self.max_rate)
        while True:    
            ber = self.fuc.ber()
            self.update_data.emit(ber)

class DataProcess(object): 
    def __init__(self,appTrace_IQ,channel_num,demodem,appTrace_symbol,data_origin,max_rate):
        self.appTrace_IQ = appTrace_IQ
        self.channel_num = channel_num
        self.demodem = demodem
        self.appTrace_symbol = appTrace_symbol
        self.data_origin = data_origin
        self.max_rate = max_rate

    def plot(self):
        file_path = r'C:\Users\Administrator\Desktop\VSABitErrorRate\demod_Qam_IQ_Data_channel'+str(self.channel_num)+r'.csv'
        self.appTrace_IQ.SaveFile(file_path,'CSV', False)
        Data_output = pd.read_csv(file_path)  
        IQ_data = Data_output.T.values.tolist()
        plot_dict = {'IQ_data':IQ_data,
                     'channel_num':self.channel_num
        }
        return plot_dict

    def ber(self):
        #demod_N = self.demodem[3:] # value is 16 32 64 or 128
        #Demod_N=int(demod_N)
        #M=int(math.log(Demod_N,2))
        ber = 1
        error_count_total = 0
        symbol_count_total = 0
        print('i am calculating------------')   

        start = time.time()
        for i in range(0,30):
            file_path = r'C:\Users\Administrator\Desktop\VSABitErrorRate\demod_Qam_EVM_channel'+str(self.channel_num)+r'.csv'
            self.appTrace_symbol.SaveFile(file_path,'CSV', False)
            Data_output = pd.read_csv(file_path)
            #print(len(Data_output))
            #print(len(self.data_origin))   
            symbol_list = Data_output.T.values.tolist()  # demod symbol
            origin_list = self.data_origin.T.values.tolist()

            bit_Data_origin = origin_list[0]
            #bit_Data_origin.insert(0,0)
            #print(bit_Data_origin)
            bit_symbol_list = symbol_list[0]
            #bit_symbol_list.insert(0,0)

            frameHeader = bit_Data_origin[0:10]
           # print(frameHeader)
            #print(bit_symbol_list)
            frameHeader_array = np.array(frameHeader,dtype='int')
            for n in range(0,len(bit_symbol_list)-9):
                count_array = np.array(bit_symbol_list[n:10+n],dtype='int')-frameHeader_array
                count = np.sum(count_array==0)   
                match_rate = count/10
                #print(match_rate) 
                if match_rate==1:
                    #print('bit_symbol_list',bit_symbol_list)
                    data_array = np.array(bit_symbol_list[10+n:],dtype='int')
                    print(n)
                    print(len(bit_symbol_list))
                    origin_data_array = np.array(bit_Data_origin[10:len(data_array)+10],dtype='int')
                    print(len(bit_Data_origin))
                    if len(data_array)<4009:   
                        error = data_array-origin_data_array
                        error_count = len(bit_symbol_list[10+n:]) - np.sum(error==0)
                        error_count_total = error_count_total+error_count
                        symbol_count_total = symbol_count_total+len(bit_symbol_list[10+n:])
                        ber =  error_count_total/symbol_count_total
                        print(ber,'--------------------------------')
                        break
            #print('误码率计算耗时',time.time()-start)    
        ber_dict = {'ber':ber,
                    'channel_num':self.channel_num,
                    'max_rate':self.max_rate
        }
        return ber_dict
    
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

        self.ui.graphicsView.setRange(xRange=(-1,1), yRange=(-1,1),disableAutoRange=True)
        self.ui.graphicsView.setMouseEnabled(x=False, y=False)
        self.curve1 = self.ui.graphicsView.plot([0],[0],pen=None,symbol='+',symbolSize=1,symbolpen=None,symbolBrush=(255,0,0,50))
        self.ui.graphicsView_2.setRange(xRange=(-1,1), yRange=(-1,1),disableAutoRange=True)
        self.ui.graphicsView_2.setMouseEnabled(x=False, y=False)
        self.curve2 = self.ui.graphicsView_2.plot([0],[0],pen=None,symbol='+',symbolSize=1,symbolpen=None,symbolBrush=(255,0,0,50))

        # channel 1
        self.ui.pushButton.clicked.connect(lambda:self.startDemod(self.ui.comboBox_3.currentText(),self.ui.comboBox.currentText(),self.ui.lineEdit.text(),self.ui.lineEdit_2.text(),self.ui.lineEdit_3.text(),self.appMeasItem_1,1))
        self.ui.pushButton_2.clicked.connect(lambda:self.stopDemod(self.timer1,self.ui.label_16,self.ui.graphicsView))
        
        # channel 2
        self.ui.pushButton_3.clicked.connect(lambda:self.startDemod(self.ui.comboBox_4.currentText(),self.ui.comboBox_2.currentText(),self.ui.lineEdit_6.text(),self.ui.lineEdit_5.text(),self.ui.lineEdit_4.text(),self.appMeasItem_2,2))
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
        setup_path = r'C:\Users\Administrator\Desktop\89600QamSetx\600M_and_600M.setx'
        self.app.RecallSetup(setup_path)
        self.app.Measurements.SelectedIndex = 1
        self.appMeasItem_1 = self.app.Measurements.SelectedItem
        self.app.Measurements.SelectedIndex = 2
        self.appMeasItem_2 = self.app.Measurements.SelectedItem
        # self.appMeasItem_2 = self.app.Measurements.SelectedItem
        # self.appMeasItem_2 = self.app.Measurements.SelectedItem # Need to be overWrite 
                
    def startDemod(self,filename,demodem,symbol_rate,center_freq,filter_val,appMeas,channel_num):
        print([demodem,symbol_rate,center_freq,filter_val])
        for item in [demodem,symbol_rate,center_freq,filter_val]: 
            if item == '':
                QMessageBox.question(self,"Error","缺少参数！")
                return None
        # Calibrate the hardware
        appCAL = appMeas.SelectedAnalyzer.Calibration
        appCAL.Calibrate()

        demod_N = demodem[3:] # value is 16 32 64 or 128
        Demod_N=int(demod_N)
        M=int(math.log(Demod_N,2))
        max_rate =  int(symbol_rate)*M  

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
        data_origin = pd.read_csv(file_dict[filename])
        #dp = DataProcess(appTrace_IQ,channel_num,demodem,appTrace_symbol,data_origin)
        exec('self.thread_plot{} = PlotThread(appTrace_IQ,channel_num,demodem,appTrace_symbol,data_origin,max_rate)'.format(channel_num))
        exec('self.thread_ber{} = BerThread(appTrace_IQ,channel_num,demodem,appTrace_symbol,data_origin,max_rate)'.format(channel_num))
        exec('self.thread_plot{}.update_data.connect(self.PlotMap)'.format(channel_num))
        exec('self.thread_ber{}.update_data.connect(self.BerDisp)'.format(channel_num))
        exec('self.thread_ber{}.update_data.connect(self.BerDisp)'.format(channel_num))
        exec('self.thread_plot{}.start()'.format(channel_num))
        exec('self.thread_ber{}.start()'.format(channel_num))   
         
        # self.thread_plot = PlotThread(appTrace_IQ,channel_num,demodem,appTrace_symbol,data_origin,max_rate)
        # self.thread_ber = BerThread(appTrace_IQ,channel_num,demodem,appTrace_symbol,data_origin,max_rate)
        # self.thread_plot.update_data.connect(self.PlotMap)
        # self.thread_ber.update_data.connect(self.BerDisp)
        # self.thread_plot.start()
        # self.thread_ber.start()
     
    def PlotMap(self,plot_dict):
        IQ_data = plot_dict['IQ_data']
        channel_num = plot_dict['channel_num']
        print('i am in',channel_num)
        I = IQ_data[0]
        Q = IQ_data[1]
        #print(len(I))
        start = time.time()
        #self.ui.graphicsView.clear()
        #self.ui.graphicsView.plot(I,Q,pen=None,symbol='+',symbolSize=1,symbolpen=None,symbolBrush=(255,0,0,50))
        exec('self.curve{}.setData(I,Q)'.format(channel_num))
        print('画图执行时间',time.time()-start)

    def BerDisp(self,ber_dict):
        max_rate = ber_dict['max_rate']
        ber = ber_dict['ber']
        channel_num = ber_dict['channel_num']
        label1 = 18+int(channel_num)*2
        label2 = 19+int(channel_num)*2
        bit_rate = max_rate*(1-ber)
        bitrate_str = str(bit_rate)+'Mbps'

        exec('self.ui.label_{}.setText(bitrate_str)'.format(label1))
        exec('self.ui.label_{}.setText(str(ber))'.format(label2))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplayWindow()
    window.show()
    sys.exit(app.exec_())