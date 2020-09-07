#!/usr/bin/env python3


from BFClust.cluster_de_novo import *
from BFClust.consensus import *
from BFClust.gbk_parsing import *
from BFClust.augmentation import * 

#from BFClust import *

import os
from optparse import OptionParser
import time

options = OptionParser(usage='%prog -i inputdir -o outputdir -b False ',
		description = "Specify the input directory, output directory, and whether or not to do an initial representative selection step")
		
options.add_option("-i", "--input", dest="inputdir", help="input directory with GBK files")
options.add_option("-o", "--outputdir", dest="outputdir", help="output directory (same as the output directory of the existing clustering solution)")
options.add_option("-b", "--bt", dest="bt", help="whether or not to construct an initial Boundary-Tree as representative selection", default = False)


def main():
	#read input args
	opts, args = options.parse_args()
	inputdir = opts.inputdir
	outdir = opts.outputdir
	bt = opts.bt

	tic = time.perf_counter()
	
	incoming_seqs = get_records_from_contigGBKs(inputdir)
	print('All files successfully parsed')
	
	augment_and_output(incoming_seqs, outdir, bt)
	toc = time.perf_counter()
	print("Time elapsed (s):",toc-tic)

if __name__ == '__main__':
	main()