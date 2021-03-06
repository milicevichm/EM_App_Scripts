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
output_fp = 'C:/NILM/Data/REDD/r_output.h5'
csv_fp = ''

#redd_data = DataSet(redd_fp)

#elec = redd_data.buildings[1].elec

#co = CombinatorialOptimisation()

#co.train(elec)

#mains = elec.mains()

#output = HDFDataStore(output_fp, 'w')
#redd = HDFDataStore(redd_fp)

#co.disaggregate(mains,output)

#output = DataSet(output_fp)

#output_file = open('C:/NILM/Data/REDD/fridge_output.csv','w')

#output_file.write(output.store.__getitem__('/building1/elec/meter5').to_csv())

#output.store.close()

redd = DataSet(redd_fp)

redd_downsampled = redd.store.__getitem__('/building1/elec/meter1').resample('1min')
redd_downsampled = redd_downsampled.fillna(value=0)


output_file = open('C:/NILM/Data/REDD/redd_downs2.csv','w')
output_file.write(redd_downsampled.to_csv())

redd.store.close()
print ("finished.")