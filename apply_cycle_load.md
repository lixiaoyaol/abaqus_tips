# 施加三角波

```python
from abaqus import *
from abaqusConstants import *
import regionToolset

#needs to be changed:thisModel, time_list, amplitude_list, timePeriod, Load
#needs to change step time in model

thisModel = mdb.models['Model-1']

time_list = range(31)
amplitude_list = [0] + [1, 0] * 15
datatzip = tuple(zip(time_list, amplitude_list))
thisModel.TabularAmplitude(name='Amp-1', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=datatzip)

# 执行这一步会删除Step-1的荷载
# thisModel.StaticStep(name='Step-1', previous='Initial', timePeriod=30, maxNumInc=1000000, 
#                      initialInc=0.01, minInc=1e-5, maxInc=0.1)
```
# 施加 $\sin$ 或 $\cos$ 波
<img width="960" alt="abaqus_period_load" src="https://github.com/lixiaoyaol/abaqus_tips/assets/111038388/d80cee22-70a5-4ab7-8ae2-4b9628d1d19f">


