# BFClust-python
 Boundary Forest Clustering - python implementation

## Installation 
Current version is 0.2.3:     
https://test.pypi.org/project/BFClust/0.2.3/

If you do not have conda installed, run the following lines
```
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest-Linux-x86_64.sh
export PATH=~/miniconda2/bin:$PATH
```

Please download and use the [bfclust24_env.yml](https://github.com/dsurujon/BFClust-python/blob/master/bfclust24_env.yml) file to set up the conda environment specific for BFClust, and then install BFClust via pip

```
conda env create -f bfclust24_env.yml    
conda activate bfclust_env

pip install -i https://test.pypi.org/simple/ BFClust==0.2.3
```

## Usage

```
BFC.py -i [input gbk directory] -o [output directory] -n [number of trees in the forest] -t [threshold] -m [maxChild] -l [minsequencelength] -s [whether or not to ignore internal stop codons]
```

The input files need to be in the same directory as genbank files. The CDS annotation from these genbank files will be used for orthologue clustering.    
An output directory will be created, with the following structure:     
```
outputdir
├── Forest
│   ├──fasta
│   │   fasta files containing representatives on each Boundary-Tree
│   ├──pickle
│   │   each Boundary-Tree stored as a pickle file
│   ├──diamond
│   │   output of diamond on each Boundary-Tree
│   └──MCL
│       output of MCL on each Boundary-Tree
└── Consensus
    ├──consensus.p
    ├──cluster_consensus_scores.csv
    └──cluster_assignments.csv
```

```cluster_assignments.csv``` contains the cluster assignments and item consensus scores for each input sequence, and ```cluster_consensus_scores.csv``` contains the consensus scores for each cluster. 

## Cluster augmentation
```
./BFCaugment.py -i [input gbk directory] -o [output directory] -b [whether or not to perform initial representative selection] -l [minseqlength] -s [whether or not to ignore internal stop codons]
```
The input sequences will be added to the clustering results for an existing output directory. The existing output directory will include an additional sub-directory named ```Augmentation```

```
outputdir
├── Forest
├─- Consensus
└── Augmentation
    ├──cluster_consensus_scores.csv
    └──cluster_assignments.csv
```
