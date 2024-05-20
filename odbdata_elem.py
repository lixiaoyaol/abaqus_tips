# -*- coding:utf-8 -*-

from odbAccess import *
from abaqusConstants import *
import os

filename = 'sdw2D.csv'

odbname = 'sdw_2d.odb'
instancename = 'WMZ-1'

elem_ls=[i for i in range(0,53)]

odb = openOdb(odbname)
frames = odb.steps['Step-1'].frames[-1]

instance = odb.rootAssembly.instances[instancename]

stress_feild = frames.fieldOutputs['S'].getSubset(region=instance)

target_stress = [stress_feild.values[elem_index].mises for elem_index in elem_ls]

simu_res_dir = os.path.join(os.getcwd(), filename)
with open(simu_res_dir, 'w') as f:
    f.write('Stress\n')
    for i in range(len(elem_ls)):
        f.write('{}\n'.format(target_stress[i]))

odb.close()
