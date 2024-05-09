from abaqus import *
from abaqusConstants import *
import regionToolset

time_list = [i for i in range(101)]
amplitude_list = [0] + [1, 0] * 100
datatzip = tuple(zip(time_list, amplitude_list))
mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=datatzip)