# -*- coding:utf-8 -*-

from odbAccess import *
from abaqusConstants import *
import os
import numpy as np

filename = 'sdw2D.txt'

odbname = 'sdw_2d.odb'
instancename = 'WMZ-1'

elem_ls=[i for i in range(0,53)]

odb = openOdb(odbname)
frames = odb.steps['Step-1'].frames[-1]

instance = odb.rootAssembly.instances[instancename]

stress_feild = frames.fieldOutputs['S'].getSubset(region=instance)

target_stress = [stress_feild.values[elem_index].mises for elem_index in elem_ls]

target_stress_np = np.array(target_stress)

np.savetxt(os.path.join(os.getcwd(), filename), target_stress_np, delimiter=',', fmt='%.3f')

odb.close()