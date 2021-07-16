---
title: 'BFClust: a python package for pangenome clustering with confidence scores'
tags:
- python
- pangenome
- ortholog clustering
authors:
- name: Defne Surujon
  orcid: 0000-0001-7964-3057
  affiliation: 1

affiliations:
- name: Independent Researcher
  index: 1

date: 15 July 2021
bibliography: paper.bib
---

# Summary

Bacterial species often vary considerably in terms of genetic content across different strains. Some genes are common to all strains in a species, and form the core genome, and others can be present or absent in a given strain, forming the accessory genome. Together, the core and accessory genomes comprise the pangenome, the entirety of gene content within a species. It is not trivial to identify genes with the same evolutionary ancestor and/or function (orthologous genes) from different strains because of high variability across strains of the same species. Boundary Forest Clustering (BFClust) is a tool for clustering annotated coding sequences in a bacterial pangenome. BFClust is unique in its ability to report confidence scores, both for each cluster of orthologous genes, and for each gene's membership to the cluster it was assigned to. It is also possible to perform initial unsupervised clustering on a large dataset using BFClust, and later assign clusters for a smaller, previously unseen dataset in. asupervised fashion (cluster augmentation). 

# Statement of Need

Ortholog clustering is a necessary step in pan-genomic analyses, comparative genetics, and recovering the evolutionary history of a bacterial species. There are multiple software tools that were developed for ortholog clustering in bacterial pangenomes [@panX]  [@Roary]. [@SynerClust]  [@panaroo]  [@PIRATE]. However, none of these clustering solutions provide a way to assess the confidence that their output is a meaningful and robust set of clusters with biological relevance. Moreover, the majority of these tools do not readily allow cluster augmentation. BFClust is the only pangenome clustering tool that can produce confidence scores for each cluster and each sequence both during de novo clustering, and also during cluster augmentation.  

# Algorithm

The BFClust workflow consists of 4 main steps: 1. representative selection, 2. clustering of representatives, 3. conseensus clustering, 4. computing confidence scores. Representative selection is done by building a set of Boundary Trees [@mathy2015boundary], which store sequences sufficiently different from each other in a tree structure, and skips those that are sufficiently close to an existing representative already on the tree. The Boundary Tree construction is a greedy process, and is influenced by the order in which sequences are read. BFClust generates multiple Boundary Trees and clusters representatives on each tree independently using Markov clustering (MCL) based on pairwise BLAST distances. For each set of representatives, the cluster assignments are then expanded to sequences that were not selecteed as representatives. Once all sequences have a cluster assignment, it is possible to compare the clustering solutions across diffeerent trees. A final consensus clustering step is applied to the vectors of cluster assignmeents across different trees. The confidence scores that BFClust computes represent the agreement across different clustering solutions prior to consensus clustering. 

# Acknowledgements

DS would like to thank Jose Bento for his help, mentorship and feedback during the development of BFClust; Sam Dyckman, Matt Crum and Federico Rosconi for their helpful feedback and support. In addition, DS would like to acknowledge Juance Ortiz-Marques, Suyen Espinoza, and Bharathi Sundaresh for their social and scientific support. Finally DS would like to acknowledge Tim van Opijnen for his professional conduct and computational expertise. 

# Authorship

Defne Surujon 

# References
