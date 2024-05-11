from abaqus import *
from abaqusConstants import *
import regionToolset

#needs to be changed:thisModel, time_list, amplitude_list, timePeriod

thisModel = mdb.models['Model-1']

time_list = range(5)
amplitude_list = [0] + [1, -1] * 4
datatzip = tuple(zip(time_list, amplitude_list))
thisModel.TabularAmplitude(name='Amp-1', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=datatzip)

thisModel.StaticStep(name='Step-1', previous='Initial', timePeriod=4.0, maxNumInc=1000000, 
                     initialInc=0.01, minInc=1e-5, maxInc=0.1)