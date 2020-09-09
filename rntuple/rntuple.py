# a python code for producing histograms of 'compressed size' or 'decompression time'

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def plot(filename, column_name, fig_title):
    data = pd.read_csv(filename + '.csv')
    # name of csv file produced by rootbench
    
    height = data[column_name]
    label = ['LZ4', 'LZ4BS', 'ZSTD', 'ZLIB', 'LZMA']
    left = np.array([1, 5, 9, 13, 17])
    
    plt.bar(left, height, tick_label = label, align = 'center', color = ['blue', 'orange', 'g', 'red', 'yellow', 'black'], width = 3.0)
    plt.title(fig_title)

    # assume `column_name` is 'size' or 'real_time'
    if column_name == 'size':
        plt.ylabel('Size (byte)')
        plt.savefig('rntuple_' + filename + '_size.png')
    elif column_name == 'real_time':
        plt.ylabel('Time (us)')
        plt.savefig('rntuple_' + filename + '_time.png')

plot('atlas', 'size', 'Filesize of ATLAS in RNTuple')
# plot('atlas', 'real_time', 'Decompression Time of ATLAS in RNTuple')