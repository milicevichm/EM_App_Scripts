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

redd_fp = '/home/group20/data/redd_data.h5'
output_fp = '/home/group20/data/redd_output.h5'


redd_data = DataSet(redd_fp)

elec = redd_data.buildings[1].elec

co = CombinatorialOptimisation()

co.train(elec)

mains = elec.mains()

output = HDFDataStore(output_fp, 'w')
redd = HDFDataStore(redd_fp)

co.disaggregate(mains,output)

print ("finished.")