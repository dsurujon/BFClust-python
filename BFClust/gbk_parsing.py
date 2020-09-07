#!/usr/bin/env python3

import os
from Bio import SeqIO
from Bio import SeqRecord 

def feature2record(thisfeature, thiscontig, strainname):
    thisrecord = thisfeature.extract(thiscontig.seq).translate()
    thisrecord = SeqRecord.SeqRecord(thisrecord)
    thisrecord.id = thisfeature.qualifiers['locus_tag'][0]
    thisrecord.strain = strainname
    thisrecord.description = thisfeature.qualifiers['locus_tag'][0]
    return(thisrecord)

def get_records_from_contigGBKs(thisdir):
    #n=1
    gbks = os.listdir(thisdir)
    
    allfeatures = []
    for gbkfile in gbks:
        fullfilename = os.path.join(thisdir,gbkfile)
        # the assembled chromosome is not available, so we need to
        # parse into a list of contigs
        mystrain = list(SeqIO.parse(fullfilename,"genbank"))

        strainname = os.path.splitext(gbkfile)[0]

        strainfeatures = []
        for contig in mystrain: 
            newfeatures = [feature2record(i,contig,strainname) for i in contig.features if i.type=="CDS"]
            strainfeatures = strainfeatures+newfeatures

        allfeatures = allfeatures+strainfeatures

    return(allfeatures)
        