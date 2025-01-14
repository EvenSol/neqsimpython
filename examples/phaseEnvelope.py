# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:08:09 2019

@author: esol
"""

import neqsim
from neqsim.thermo.thermoTools import *
import matplotlib.pyplot as plt

fluid1 = fluid('srk')
fluid1.addComponent("nitrogen", 1.0)
fluid1.addComponent("CO2", 2.5)
fluid1.addComponent("methane", 86.1)
fluid1.addComponent("ethane", 8.1)
fluid1.addComponent("propane", 3.1)
fluid1.addComponent("i-butane", 1.2)
fluid1.addComponent("n-butane", 3.1)

data = phaseenvelope(fluid1)


plt.plot(list(data.getOperation().get("dewT")),list(data.getOperation().get("dewP")), label="dew point")
#plt.plot(list(data.getOperation().get("dewT2")),list(data.getOperation().get("dewP2")), label="dew point2")
plt.plot(list(data.getOperation().get("bubT")),list(data.getOperation().get("bubP")), label="bubble point")
#plt.plot(list(data.getOperation().get("bubT2")),list(data.getOperation().get("bubP2")), label="bubble point2")
plt.title('PT envelope')
plt.xlabel('Temperature [\u00B0C]')
plt.ylabel('Pressure [bar]')
plt.legend()
plt.show()