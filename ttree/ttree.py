# a python code for producing scatter diagrams of 'compressed size' and 'decompression time'

import pandas as pd 
import matplotlib.pyplot as plt 

def plot(filename, use_lzma, fig_title):
    data = pd.read_csv(filename + '.csv')
    # name of csv file produced by rootbench
    
    data_time = data['real_time']
    data_size = data['comp_size']
    data_name = data['name']

    color = ['r', 'r', 'r', 'b', 'b', 'b', 'g', 'g', 'g', 'k', 'k', 'k', 'y', 'y', 'y']
    # Red: ZLIB, Blue: LZMA, Green: LZ4, Black: ZSTD, Yellow: LZ4BS

    for (i, j, k, l) in zip(data_time, data_size, data_name, color):
        if use_lzma == False and 'LZMA' in k:
            # LZMA is optional because it has too slow decompression speed
            # compared with other algorithms
            continue
        plt.plot(i, j, 'o', color = l)
        plt.annotate(k, xy = (i, j), color = l)
        # the location of annotations may need heuristic optimization when plots are densely populated
    
    plt.title(fig_title)
    plt.xlabel('decompresion time (ms)')
    plt.ylabel('compressed size (byte)')
    if use_lzma:
        plt.savefig('ttree_' + filename + '_with_lzma.png')
    else:
        plt.savefig('ttree_' + filename + '.png')

plot('lhcb', False, 'LHCb file\n(lhcb_B2ppKK2011_md_noPIDstrip.root)')
# plot('nanoaod', False, 'NanoAOD file\n(Run2012B_DoubleMuParked.root)')
# plot('atlas', False, 'ATLAS file\n(gg_data-zstd.root)')
