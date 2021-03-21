## TEAM 1 FUNCTIONAL ANNOTATION

##### MEMBERS:
Aekansh Goel, Gargi Damle, Harini Adepu, Jintian Lyu, Marcus Valancius, Yifan Lang
  ___
##### INTRODUCTION

Functional annotation is defined as the process of collecting information about and describing a genome feature’s biological identity, including its various aliases, molecular function, biological role(s), subcellular location, and its expression domains within the organism. This process can be done based on either previously known sequences (Homology based tools) or intrinsic characteristics that a subset of genes/proteins all contain (Ab-initio tools). The following chart will show the comparison between Homology based method and Ab-initio method.

In our study, we are concerned with implications of subset of genes and features which have greater relevance to outbreaks (anti-microbial genes, CRISPR regions etc). We will perform a full functional annotation on the genes and proteins determined by Group Gene Prediction in Team 1.
  ___
##### PREREQUISITES:
-	git
-	conda
-	make
-	Perl & CPAN
- R
  ___
##### TOOLS INSTALLED/INVOKED:  
- Clustering: USEARCH AND CD-HIT
- Homology Based: DeepARG, InterProScan, EggNOG-Mapper
- Ab-initio Based: SignalP 5.0, PILER-CR, TMHMM 2.0
  ___
##### 1. CLUSTERING: USEARCH

Because shared homology molecular level provides functional insight (by evolution at the molecular level being a largely conserved process) and significant sequence similarity implies shared function, we will use cluster sequences to reduce repeat queries and improve speed and aid in understanding the functions of the sequences. Sequences within the same group are deemed similar. Isolated groups are considered dissimilar from each other.

COMMAND USED:

  ___

##### 2. HOMOLOGY BASED TOOLS

Homology is a similarity due to shared ancestry between a pair of structures of genes in different texa. The homology-based tool uses this phenomenon in characterizing the function/structure of unknown sequences. The gene databases used here are collections of annotated genes. By searching a gene against the database, we will look for homology between our gene sequences and those in the database to transfer annotation.

COMMAND USED:

  ___
##### 3. AB-INITIO APPROACH

Ab-Initio Tools predict and annotate different regions of the prokaryotic genome using 1) sequence composition, 2) likelihoods within the gene models, 3) gene content and 4) Signal Detection. The Ab-Initio Approach can be used for finding new genes, and no external data or evidence is needed for the prediction. However, it is limited by the presence of False Positives in the predicted data as well as over-prediction of small genes.

##### SignalP 5.0

The SignalP 5.0 tool predicts the presence of signal peptides and the location of their cleavage sites in proteins from Archaea, Gram-positive Bacteria, Gram-negative Bacteria, and Eukarya. For Bacteria and Archaea, SignalP 5.0 is known to discriminate between three types of signal peptides Sec/SPI (standard signal peptide), Sec/SPII (lipoprotein signal peptide) and Tat/SPI (tat signal peptide). SignalP 5.0 is based on a deep convolutional and recurrent neural network architecture including a conditional random field.

- Input file format:  .fasta
- Output file format: .gff
- Command used:       
  ___
##### CRISPR Regions: PILER-CR

Predict CRISPR regions based on identified repeats. It's default options are that 3 repeats minimum in an array, 16 minimum repeat length, 64 maximum repeat length, 8 minimum spacer length, 64 maximum spacer length, 0.9 minimum repeat ratio, 0.75 minimum spacer ratio.

- Input file format:  .fasta
- Output file format: .gff
- Command used:
___
##### Transmembrane Domains: TMHMM

TMHMM is a membrane protein topology prediction tool that focuses on the prediction of transmembrane helices in proteins with high accuracy. Its accuracy can be comprised in the presence of signal peptides.

- Input file format:  .fasta
- Output file format: .gff
- Command used: ./tmhmm <input file path> > <output file path>
