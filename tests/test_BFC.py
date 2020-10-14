import os
from BFClust.cluster_de_novo import *
from BFClust.consensus import *
from BFClust.gbk_parsing import *
from BFClust.augmentation import * 

def test_BFCdenovo():
    testinputdir = os.path.join(os.path.dirname(__file__), 'minigenomes')
    testoutputdir = os.path.join(os.path.dirname(__file__), 'output')

    records = get_records_from_contigGBKs(testinputdir, 0, False)
    print(len(records))
    run_BFC(records, testoutputdir, 10, 0.1, 10)	

def test_BFCaugment():
    testinputdir = os.path.join(os.path.dirname(__file__), 'minigenomes')
    testoutputdir = os.path.join(os.path.dirname(__file__), 'output')

    incoming_seqs = get_records_from_contigGBKs(testinputdir, 0, False)
    augment_and_output(incoming_seqs, testoutputdir , False)

if __name__ == "__main__":
    test_BFCdenovo()
    test_BFCaugment()
    print("Everything passed")