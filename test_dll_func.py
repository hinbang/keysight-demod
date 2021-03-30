#! --utf-8--
#! 需要 pip install pythonnet
# import sys
import clr
import time

# 将动态连接库的函数导出
clr.AddReference('C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.Interfaces.dll')
clr.AddReference('C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.DigitalDemod.Interfaces.dll')
from Agilent.SA.Vsa import *
from Agilent.SA.Vsa.DigitalDemod import *

# 实例化一个 application
app = ApplicationFactory.Create()
if app == None:
    app = ApplicationFactory.Create(True, '', '', -1)
# 设置 application 的基本属性
app.IsVisible = True
app.Title = 'Demod Measurement Test'

# 创建一次测量，选取当前的硬件通道作为输入
appMeas = app.Measurements.SelectedItem

# 校准当前的硬件
appCAL = appMeas.SelectedAnalyzer.Calibration
appCAL.Calibrate()

# 创建解调器
genericHandle = appMeas.SetMeasurementExtension(MeasurementExtension.ExtensionType())
measHandle = MeasurementExtension.CastToExtensionType(genericHandle)
del measHandle
genericHandle = appMeas.MeasurementExtension
measHandle = MeasurementExtension.CastToExtensionType(genericHandle)
# 设置解调的参数
measHandle.Format = Format.Qam32
measHandle.PointsPerSymbol = 5
measHandle.SymbolRate = 12e7
measHandle.ResultLength = 4000
measHandle.FilterAlphaBT = 0.2
filterType = getattr(MeasurementFilter,'None')
measHandle.MeasurementFilter = filterType
# measHandle.RecallStateDefinitionsFile('C:\Users\Administrator\Desktop\VSABitErrorRate\QAM32.csd')
# 设置中心频率和显示频谱宽度
appFreq = appMeas.Frequency
appFreq.Center = 8e7
appFreq.Span = 1.5e8

# 选取输入端，数据来自仿真或者是硬件
appMeas.Input.DataFrom = DataSource.Hardware

# 设置连续测量
appMeas.IsContinuous = True
appMeas.Restart()

# 设置均衡
measHandle.IsEqualized = True
measHandle.EqualizerFilterLength = 9
measHandle.EqualizerConvergence = 2e-10

# measHandle.EqualizerReset()

measHandle.EqualizerMode = EqualizerMode.Run  # EqualizerMode.Run or EqualizerMode.Hold

# wait for measdone, but don't bother it too often
# Set timeout to 2 seconds
bMeasDone = 0
t0=time.time()
appMeasStatus = appMeas.Status


while(bMeasDone==0 and (time.time()-t0)<=2):
   time.sleep(1)
   bMeasDone = StatusBits.MeasurementDone

# 删除对象
del app
del appMeas
del appCAL

