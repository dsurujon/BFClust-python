#!/usr/bin/env python3


from scripts.cluster_de_novo import *
from scripts.consensus import *
from scripts.gbk_parsing import *

import os
from optparse import OptionParser

options = OptionParser(usage='%prog -i inputdir -o outputdir -n 10 -t 0.1 -m 10',
		description = "Specify the input directory, output directory, number of trees in the forest, sequence similarity threshold and maxChild.")
		
options.add_option("-i", "--input", dest="inputdir", help="input directory with GBK files")
options.add_option("-o", "--outputdir", dest="outputdir", help="output directory")
options.add_option("-n", "--ntrees", dest="ntrees", help="number of trees in the forest", default = 10)
options.add_option("-t", "--threshold", dest="threshold", help="sequence distance threhold (Jukes Cantor distance) to be used when picking representatives", default=0.1)
options.add_option("-m", "--maxChild", dest="maxChild", help="max number of children a node is allowed to have in the Boundary-Tree", default=10)


def main():
	#read input args
	opts, args = options.parse_args()
	inputdir = opts.inputdir
	outdir = opts.outputdir
	ntrees = opts.ntrees
	t = opts.threshold
	maxChild = opts.maxChild

	tic = time.perf_counter()
	
	records = get_records_from_contigGBKs(inputdir)
	print('All files successfully parsed')
	
	run_BFC(records, outdir, ntrees, t, maxChild)
	toc = time.perf_counter()
	print("Time elapsed (s):",toc-tic)

if __name__ == '__main__':
	main()