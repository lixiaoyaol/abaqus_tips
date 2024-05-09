# -*- coding: utf-8 -*-
'''
@Author  :   libofeng 
@Mail    :   bf_li@qq.com
@Time    :   2024/05/09 20:17:13
@License :   All rights reserved
@Desc    :   None
'''

#-*-coding:utf-8-*-

from abaqus import *
from abaqusConstants import *
import regionToolset

#Create the model
mdb.Model(name='Model-1', absoluteZero=-273, modelType=STANDARD_EXPLICIT)
thisModel = mdb.models['Model-1']

#Create the part
import sketch
import part

#part_1

#part_n

#Create material
import material
huanyMaterial = thisModel.Material(name='Material-1')
huanyMaterial.Elastic(table=((10000.0, 0.33), ))
huanyMaterial.Expansion(table=((2.3e-05,), ))

#Create section and assign
import section
huanySection = qfnModel.HomogeneousSolidSection(name='Section-huany', material='huanyang', thickness=None)

huany_region = (huanypart.cells,)
huanypart.SectionAssignment(region=huany_region, sectionName='Section-huany')

#Create the assembly
import assembly

thisAssembly = thisModel.rootAssembly
xinpInstance = thisAssembly.Instance(name='Part-xinpian-1', part=xinppart, dependent=ON)

#Create step
import step

thisModel.StaticStep(name='Step-shengwen', previous='Initial', timePeriod=utimeperiod, maxNumInc=1000000, 
                     initialInc=0.05, minInc=0.0001, maxInc=0.05)

#Create the field output request
thisModel.fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'E'), timeInterval=0.5, region=MODEL, exteriorOnly=OFF, 
sectionPoints=DEFAULT, rebar=EXCLUDE)
#Create the history output request
thisModel.historyOutputRequests['H-Output-1'].setValues(variables=('ALLAE', ), timeInterval=0.5, region=MODEL, sectionPoints=DEFAULT, 
rebar=EXCLUDE)

#Apply load
#constrain

fixFaces = pcbInstance.faces.findAt(((0,0,-2.6),))
region = regionToolset.Region(faces=(fixFaces))
thisModel.EncastreBC(name='BC-1', createStepName='Initial', region=region, localCsys=None)


time_list = [i for i in range(101)]
amplitude_list = [0] + [1, 0] * 100
datatzip = tuple(zip(time_list, amplitude_list))
mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=datatzip)

#Create mesh
import mesh

#Job and inp