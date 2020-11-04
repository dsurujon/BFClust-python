# BFClust-python
 Boundary Forest Clustering - python implementation

Boundary-Forest Clustering is a pan-genome clustering pipeline written in MATLAB. Boundary-Forest Clustering is done in 3 major steps:    
1. **Boundary-Forest.** This generates a number of Boundary-Trees based on sequence similarity (See [Mathy et al., 2015](https://arxiv.org/abs/1505.02867) for more detail on Boundary-Forest). A sequence is either added to the tree as a new representative, or if there is an existing representative on the tree that is sufficiently close to this sequence, the sequence is annotated with this representative, and omitted from the tree. Boundary-Trees thus contain a small subset of input sequences as representative sequences, that are arranged in a tree-structure based on sequence similarity.
2. **Cluster.** Clustering is performed on each Boundary-Tree using Markovian clustering (MCL). Once the representative sequences are clustered, the clustering assignments are extended to the full dataset. 
3. **Consensus Clustering.** The clustering on the different Boundary-Tree representatives may not always yield identical results. Taking a consensus of the clustering assignments across the forest reduces errors for all downstream clustering methods. A consensus score for each element and each cluster will also be generated as a quality metric. The consensus score for a cluster or an item is a value between 0 and 1. A score of 1 indicates perfect agreement among individual clustering assignments.      

The major advantage of BFClust is that it outputs the level of certainty (a consensus score) associated with each item and/or each cluster. This gives a measure of cluster "quality" when we do not know what the "real" clusters are supposed to be. Another advantage of BFClust is that it stores the Boundary-Forest, making it possible to add new sequences to the clustering without having to alter the existing clustering assignments ("cluster augmentation"). This not only reduces the time necessary to obtain cluster assignments for an incoming set of sequences (e.g. a newly sequenced bacterial isolate), but also keeps the existing clustering assignments the same.    
    
There are three main scripts that can be used. ```BFC.py``` is for clustering a new dataset *de novo*, and ```BFCaugment.py``` is for adding new sequences to an existing clustering partition. 

## Installation 

Current version is 0.1.26.1:     
https://test.pypi.org/project/BFClust/0.1.26.1/


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


pip install BFClust==0.1.26.1
```

## Usage
In order to cluster annotated genomes, use the following command: 
```
BFC.py -i [input gbk directory] -o [output directory] -n [number of trees in the forest] -t [threshold] -m [maxChild] -l [minsequencelength] -s [whether or not to ignore internal stop codons]
```

The input files need to be anotated genbank files (one for each isolate), in the input genbank directory. The CDS annotation from these genbank files will be used for orthologue clustering.    
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

The ```Forest``` directory contains intermediate data generated during representative selection and clustering. The consensus clustering data and output are in the ```Consensus``` directory. 

```cluster_assignments.csv``` contains the cluster assignments and item consensus scores for each input sequence, and ```cluster_consensus_scores.csv``` contains the consensus scores for each cluster. 


## Cluster augmentation
This is used when a clustering partition already exists, and one wishes to assign clusters to a new sequence set. This is especially useful when a large number of sequences have already been clustered, and a relatively small sequence set is to be assigned clusters. The advantage here is three-fold:     
1. Existing cluster assignments are not changed
2. Adding new sequences is faster than clustering the old and new sequences together    
3. The confidence scores are computed again, giving a level of uncertainty for the newly added clustering      

```
BFCaugment.py -i [input gbk directory] -o [output directory] -l [minimum length] -s [ignore internal stop] -b [initial representative selection] 
```
The input sequences will be added to the clustering results for an **existing** output directory. The existing output directory will be amended with an additional sub-directory named ```Augmentation```, which will contain the updated scores, and cluster assignments for the new input sequences. 

```
outputdir
├── Forest
├─- Consensus
└── Augmentation
    ├──cluster_consensus_scores.csv
    └──cluster_assignments.csv
```

## Testing 
To test the installation and successful runs of ```BFC.py``` and ```BFCaugment.py```, please run ```python test_BFC.py```. If all tests are passed successfully, there should be no error messages.   
