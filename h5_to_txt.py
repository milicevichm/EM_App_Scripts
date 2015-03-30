# Script disaggregates REDD building data based on input arguments
# Author: Michael Milicevich
# Date: 16/02/2015

# command linen test variables to use:
# python disag_script.py 1 "fridge" "2011-05-01" "2011-05-02"

# import modules/dependencies
from __future__ import print_function, division
import sys
from dateutil import parser
import pandas as pd
from key_map import *
from nilmtk import HDFDataStore, DataSet, TimeFrame, MeterGroup
from nilmtk.disaggregate import CombinatorialOptimisation
import warnings

redd_fp = 'C:/NILM/Data/REDD/redd_data.h5'
output_fp = 'C:/NILM/Data/REDD/redd_output.h5'


redd_data = DataSet(redd_fp)

elec = redd_data.buildings[1].elec

#co = CombinatorialOptimisation()

#co.train(elec)

mains = elec.mains()

#output = HDFDataStore(output_fp,'w')

#co.disaggregate(mains,output)

#print(len(output.store.get('/building1/elec/meter1')))
#print(len(mains.dataset.store.get('/building1/elec/meter1')))

test_mains = mains.power_series_all_data()

redd_data.store.close()
#output.close()

f1 = open('C:/NILM/Data/txt_output/b1_mains.txt','w')
f1.write(test_mains)

print ("finished.")