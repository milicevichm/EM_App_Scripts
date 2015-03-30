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

redd = DataSet(redd_fp)

mains1 = redd.store.__getitem__('/building1/elec/meter1')
mains2 = redd.store.__getitem__('/building1/elec/meter2')

mains1 = mains1.fillna(value=0)
mains1 = mains1.resample("1min")

mains2 = mains2.fillna(value=0)
mains2 = mains2.resample("1min")

mains_sum = mains1 + mains2

print("writing to csv")

#output_file = open('C:/NILM/Data/REDD/redd_b1_mains.csv','w')
#output_file.write(mains_sum.to_csv())


plot(mains_sum)


redd.store.close()
print ("script finished.")