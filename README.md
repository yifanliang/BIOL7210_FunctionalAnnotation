# Team 1 Functional Annotation

Team members: Aekansh Goel, Gargi Damle, Harini Adepu, Jintian Lyu, Marcus Valancius, Yifan Lang

Introduction

Background

Functional annotation is defined as the process of collecting information about and describing a genome feature’s biological identity, including its various aliases, molecular function, biological role(s), subcellular location, and its expression domains within the organism. This process can be done based on either previously known sequences (Homology based tools) or intrinsic characteristics that a subset of genes/proteins all contain (Ab-initio tools). The following chart will show the comparison between Homology based method and Ab-initio method.

In our study, we are concerned with implications of subset of genes and features which have greater relevance to outbreaks (anti-microbial genes, CRISPR regions etc). We will perform a full functional annotation on the genes and proteins determined by Group Gene Prediction in Team 1.

Pros and Cons of Homology Based Tools

Pros	Cons	
Accurate and reliable in comparison to Ab-initio tools	Dependent on existing databases and annotation
Target specific purposes: virulence factors or antibiotic resistance genes​	Knowledge derived from prior experiments​
Useful for mining large numbers of gene or operon variants from homologous gene clusters​	


Pros and Cons of Ab-initio Tools

Pros	Cons	
No external data or evidence is needed for the prediction	Presence of False Positives in the predicted data
Applicable in finding new genes​	Over-predict small genes


Data

The genomes from the gene prediction group were identified during assembly as Escherichia coli. E Coli is a Gram-Negative bacteria found in the environment, foods, and intestines of people and animals. With a 4.6 million bases in its genome and 4242 protein, E Coli is the most highly studied microorganism. There is a remarkable amount of diversity in the E Coli genome, only about 20% of each genome represents sequences present in every one of the isolates, while around 80% of each genome can vary among isolates

Pipeline

(need to have a figure)

Clustering

Because shared homology molecular level provides functional insight (by evolution at the molecular level being a largely conserved process) and significant sequence similarity implies shared function, we will use cluster sequences to reduce repeat queries and improve speed and aid in understanding the functions of the sequences. Sequences within the same group are deemed similar. Isolated groups are considered dissimilar from each other. The clustering tools we are using are USEARCH and CD-HIT.

USEARCH

Algorithm	Notes	
Greedy-Incremental	Uses more RAM
Processes sequence by order​	Less documentation
Centroid representative​	


CD-HIT

Algorithm	Notes	
Greedy-Incremental	Tends to produce more clusters
Processes sequence by length​	Takes roughly the same time as USEARCH
If too dissimilar, added as new representative sequence	


Homology-based Tools

Homology is a similarity due to shared ancestry between a pair of structures of genes in different texa. The homology-based tool uses this phenomenon in characterizing the function/structure of unknown sequences. The gene databases used here are collections of annotated genes. By searching a gene against the database, we will look for homology between our gene sequences and those in the database to transfer annotation. This method is more accurate and reliable compared to Ab-initio tools. However, it is highly dependent on existing databases and annotation.

Antimicrobial Resistance Genes

Resfinder

Detects presence of whole resistance genes where a predictive phenotype can be inferred.​

Detects genes that were present in multiple copies​
Finds genes with 30% identity and 20% coverage ​
Avoids unspecific hits in for the identification of antimicrobial resistance genes​
Input file format:

.fasta/fastq
Output file format:

Best matched antimicrobial resistance genes
DeepARG

Annotates antibiotic resistance genes in metagenomes

Short run time ​
Will get a list of antibiotic categories, protein family membership, molecular function, cellular component ​
Uses a machine learning solution
Input file format:

.fasta/BLAST file
Output file format:

probabilities of each read/gene belonging to a specific resistance category
Protein Regions

InterProScan

Genome scale protein classification. Gives overview of families that a protein belongs to and the domain sites. ​

Heavily curated database ​
Powerful and sensitive ​
Protein signatures
Input file format:

.fasta
Output file format:

GFF3, HTML, TSV
Blast2GO

Considers function transfers for homologous proteins

Easy to install and setup​
Can access intermediary results ​
Can interrogate biological meaning of data
Input file format:

.fasta
Output file format:

sequence description including molecular function
EggNOG-Mapper

Find orthology assignments using precomputed clustering

~15x faster than BLAST and at least 2.5x faster than InterProScan​
"DIAMOND" command line for big dataset
Input file format:

.fasta
Output file format:

sequence description including molecular function
Operons & Gene Clusters

MicrobesOnline

Predicts whether pairs of adjacent genes that are on the same strand are in the same operon, based on the intergenic distance between them, whether orthologs of the genes are near each other in other genomes, and their predicted functions.

Download all the operon tables for Campylobacter jejuni
Use GID to retrieve the protein reference sequences
Create a database using Blast:
makeblastdb -in <fasta file> -dbtype prot -out <database>
Query the clustered sequences with the reference protein database:
blastp -query cdhit/faa_rep_seq.faa -db tmp/db_operon -evalue 0.01 -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out tmp/hits_0.01.txt -num_threads 5
AB-initio Approach

Ab-Initio Tools predict and annotate different regions of the prokaryotic genome using 1) sequence composition, 2) likelihoods within the gene models, 3) gene content and 4) Signal Detection. The Ab-Initio Approach can be used for finding new genes, and no external data or evidence is needed for the prediction. However, it is limited by the presence of False Positives in the predicted data as well as over-prediction of small genes.

Signal Peptides

A signal peptide is a short peptide (16-20 amino acids long) present at the N-terminus of newly synthesized proteins that are involved in the secretory pathway. In prokaryotes, the signal peptides are known to direct the synthesized protein to specific protein channels.

Ab-Initio tools take advantage of their common structure to predict the presence of signal peptides in the given protein sequences. The signal peptide structure is described as a positively charged n-region, followed by a hydrophobic h-region and a neutral but polar c-region.

SignalP 5.0

The SignalP 5.0 tool predicts the presence of signal peptides and the location of their cleavage sites in proteins from Archaea, Gram-positive Bacteria, Gram-negative Bacteria, and Eukarya.

For Bacteria and Archaea, SignalP 5.0 is known to discriminate between three types of signal peptides Sec/SPI (standard signal peptide), Sec/SPII (lipoprotein signal peptide) and Tat/SPI (tat signal peptide).

SignalP 5.0 is based on a deep convolutional and recurrent neural network architecture including a conditional random field.

Input file format:

.fasta
Output file format:

.___
Command used:

___
CRISPR Regions

CRT

Predict CRISPR regions based on K-mer based approaches
Fast and Memory Efficient, High Recall Rate and Quality
Faster for genomes containing larger number of repeats
PILER-CR

Predict CRISPR regions based on identified repeats. It's default options are that 3 repeats minimum in an array, 16 minimum repeat length, 64 maximum repeat length, 8 minimum spacer length, 64 maximum spacer length, 0.9 minimum repeat ratio, 0.75 minimum spacer ratio.
High Sensitivity and Fast - completes a 5 Mb genome in 5 seconds
More precision than the CRISPR Recognition Tool, so less false positives.
We went with PilerCR for the above reason, rather than CRT.
Command used:

___
Transmembrane Domains

Transmembrane protein is an integral membrane protein that spans the entirety of the cell membrane in an organism. Transmembrane proteins contain crucial components for cell-cell signaling, mediate the transport of ions and solutes across the membrane. Transmembrane helices are a basic type of transmembrane proteins.

TMHMM

TMHMM is a membrane protein topology prediction tool that focuses on the prediction of transmembrane helices in proteins with high accuracy. Its accuracy can be comprised in the presence of signal peptides.

Input file format:

.fasta
Output file format:

.gff
Command used:

./tmhmm <input file path> <output file path>
