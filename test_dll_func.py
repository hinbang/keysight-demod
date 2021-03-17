import sys
import clr

## 需要 pip install pythonnet

sys.path.append("C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces")
clr.AddReference('C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.Interfaces.dll')
clr.AddReference('C:\Program Files\Agilent\89600 Software 2019\89600 VSA Software\Examples\DotNET\Interfaces\Agilent.SA.Vsa.DigitalDemod.Interfaces.dll')
from Agilent.SA.Vsa import *

app = ApplicationFactory.Create()


# Delete object
del app

