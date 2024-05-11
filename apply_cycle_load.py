from abaqus import *
from abaqusConstants import *
import regionToolset

#needs to be changed:thisModel, time_list, amplitude_list, timePeriod, Load

thisModel = mdb.models['Model-1']

time_list = range(31)
amplitude_list = [0] + [1, 0] * 15
datatzip = tuple(zip(time_list, amplitude_list))
thisModel.TabularAmplitude(name='Amp-1', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=datatzip)

# 执行这一步会删除Step-1的荷载
# thisModel.StaticStep(name='Step-1', previous='Initial', timePeriod=30, maxNumInc=1000000, 
#                      initialInc=0.01, minInc=1e-5, maxInc=0.1)