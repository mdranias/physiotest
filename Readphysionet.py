# This code is to read data from physionet into python environment.
# code is modified from jupyter code https://github.com/MIT-LCP/wfdb-python/blob/master/demo.ipynb 
# capital letter comments are my own.

from IPython.display import display
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
import os
import shutil
import wfdb

# Demo 1 - Read a wfdb record using the 'rdrecord' function into a wfdb.Record object.
# Plot the signals, and show the data.

#rd = SHORT FOR READ RECORD; PATH TO SAMPLE DATA NEEDS TO BE UPDATED
path = '~/PPG/
record = wfdb.rdrecord('DATA/sample-data/a103l') 
wfdb.plot_wfdb(record=record, title='Record a103l from Physionet Challenge 2015') 
display(record.__dict__)


# Can also read the same files hosted on Physiobank https://physionet.org/physiobank/database/
# in the challenge/2015/training/ database subdirectory. 
Full url = 'https://physionet.org/physiobank/database/challenge/2015/training/'
record2 = wfdb.rdrecord('a103l', pb_dir=Full url)
