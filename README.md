## TEAM 1 FUNCTIONAL ANNOTATION

##### MEMBERS:
Aekansh Goel, Gargi Damle, Harini Adepu, Jintian Lyu, Marcus Valancius, Yifan Lang
  ___
##### INTRODUCTION

Functional annotation is defined as the process of collecting information about and describing a genome feature’s biological identity, including its various aliases, molecular function, biological role(s), subcellular location, and its expression domains within the organism. This process can be done based on either previously known sequences (Homology based tools) or intrinsic characteristics that a subset of genes/proteins all contain (Ab-initio tools). The following chart will show the comparison between Homology based method and Ab-initio method.

In our study, we are concerned with implications of subset of genes and features which have greater relevance to outbreaks (anti-microbial genes, CRISPR regions etc). We will perform a full functional annotation on the genes and proteins determined by Group Gene Prediction in Team 1.
  ___
##### PREREQUISITES:
This pipeline assumes all tools listed below and their dependencies have already been installed.
-	git
-	conda
-	make
-	Perl & CPAN
- Python 2.7 and 3.0
- [USEARCH](https://www.drive5.com/usearch/download.html)
- [DeepARG](https://bench.cs.vt.edu/deeparg)
- [EggNOG-Mapper](https://github.com/eggnogdb/eggnog-mapper)
- [MicrobesOnline](http://www.microbesonline.org/)
- [SignalP 5.0](https://services.healthtech.dtu.dk/service.php?SignalP-5.0)
- [TMHMM 2.0](https://services.healthtech.dtu.dk/service.php?TMHMM-2.0)
- [PilerCR](https://www.drive5.com/pilercr/)
  ___
##### TOOLS INSTALLED/INVOKED:  
- Clustering: USEARCH
- Homology Based: DeepARG, EggNOG-Mapper, MicrobesOnline
- Ab-initio Based: SignalP 5.0, PILER-CR, TMHMM 2.0
  ___
##### 1. CLUSTERING: USEARCH

Because shared homology molecular level provides functional insight (by evolution at the molecular level being a largely conserved process) and significant sequence similarity implies shared function, we will cluster sequences to reduce repeat queries and improve speed and aid in understanding the functions of the sequences. As protein function is decided by amino acid sequence, we've decided to cluster amino acid sequences and use them through our pipeline.

USEARCH is a widely used program for sequence clustering, among other functions.
- Uses a greedy-incremental heuristic algorithm that sorts by order
- Centroid representatives for clusters
- Identity is calculated using kmers and global alignment

Command used:
> usearch_path -cluster_fast input_fasta -id identity_threshold -centroids centroids_output -uc uclust_output
  ___
##### 2. HOMOLOGY BASED TOOLS

Homology is a similarity due to shared ancestry between a pair of structures of genes in different texa. The homology-based tool uses this phenomenon in characterizing the function/structure of unknown sequences. The gene databases used here are collections of annotated genes. By searching a gene against the database, we will look for homology between our gene sequences and those in the database to transfer annotation.

##### Antimicrobial Resistance Genes: DeepARG
Annotates antibiotic resistance genes in metagenomes
- Will get a list of antibiotic categories, protein family membership, molecular function, cellular component ​
- Uses a machine learning solution

- Input file format:  .fasta/blast
- Output file format: probabilities of each read/gene belonging to a specific resistance category, .gff

Command Used:
> deeparg predict --model SS -i <input_file> -o <output_path> -d <database_location> --type proct --min-prob 0.8

##### Protein Regions: EggNOG-Mapper
Find orthology assignments using precomputed clustering

- Input file format:  .fasta
- Output file format: sequence description including molecular function, .gff

Command Used:
> python emapper.py -i <input_centroid_file> --output <output_file_name> -m diamond -d bact -o <output_directory> --cpu <cpu>

##### Operons & Gene Clusters: MicrobesOnline
Predicts whether pairs of adjacent genes that are on the same strand are in the same operon, based on the intergenic distance between them, whether orthologs of the genes are near each other in other genomes, and their predicted functions.

- Create a database using Blast:
> makeblastdb -in <fasta_ref_file> -dbtype prot -out <database_name>

- Query the clustered sequences with the reference protein database:
> blastp -query <fasta_file> -db <operon_db> -evalue 0.01 -max_target_seqs 1 -max_hsps 1 -out <output_directory> -num_threads 5
  ___
##### 3. AB-INITIO APPROACH

Ab-Initio Tools predict and annotate different regions of the prokaryotic genome using
- sequence composition
- likelihoods within the gene models
- gene content
- Signal Detection

The Ab-Initio Approach can be used for finding new genes, and no external data or evidence is needed for the prediction. However, it is limited by the presence of False Positives in the predicted data as well as over-prediction of small genes.

##### Signal Peptides: SignalP 5.0

The SignalP 5.0 tool predicts the presence of signal peptides and the location of their cleavage sites in proteins from Archaea, Gram-positive Bacteria, Gram-negative Bacteria, and Eukarya. For Bacteria and Archaea, SignalP 5.0 is known to discriminate between three types of signal peptides Sec/SPI (standard signal peptide), Sec/SPII (lipoprotein signal peptide) and Tat/SPI (tat signal peptide). SignalP 5.0 is based on a deep convolutional and recurrent neural network architecture including a conditional random field.

- Input file format:  .fasta
- Output file format: .gff

Command used:
> signalp -fasta input_file_path -org gram- -format short -prefix output_file_path -gff3

##### CRISPR Regions: PILER-CR

Predict CRISPR regions based on identified repeats. It's default options are that 3 repeats minimum in an array, 16 minimum repeat length, 64 maximum repeat length, 8 minimum spacer length, 64 maximum spacer length, 0.9 minimum repeat ratio, 0.75 minimum spacer ratio.

- Input file format:  .fasta
- Output file format: .gff

Command used:
> pilercr -in input_file_path -out output_file_path -noinfo

##### Transmembrane Domains: TMHMM

TMHMM is a membrane protein topology prediction tool that focuses on the prediction of transmembrane helices in proteins with high accuracy. Its accuracy can be comprised in the presence of signal peptides.

- Input file format:  .fasta
- Output format: short/long, .gff

Command used:
> ./tmhmm -output_format input_file_path > output_file_path
  ___
##### CITATIONS
- Edgar,RC (2010) Search and clustering orders of magnitude faster than BLAST, Bioinformatics 26(19), 2460-2461. doi: 10.1093/bioinformatics/btq461
- Armenteros, J. J. A., Tsirigos, K. D., Sønderby, C. K., Petersen, T. N., Winther, O., Brunak, S., ... & Nielsen, H. (2019). SignalP 5.0 improves signal peptide predictions using deep neural networks. Nature biotechnology, 37(4), 420-423.
- Krogh, A., Larsson, B., Von Heijne, G., & Sonnhammer, E. L. (2001). Predicting transmembrane protein topology with a hidden Markov model: application to complete genomes. Journal of molecular biology, 305(3), 567-580.
- Edgar, R.C. (2007) PILER-CR: fast and accurate identification of CRISPR repeats, BMC Bioinformatics, Jan 20;8:18.
- Jones, Philip, et al. "InterProScan 5: genome-scale protein function classification." Bioinformatics 30.9 (2014): 1236-1240.
- Arango-Argoty, Gustavo, et al. "DeepARG: a deep learning approach for predicting antibiotic resistance genes from metagenomic data." Microbiome 6.1 (2018): 1-15.
- Fast genome-wide functional annotation through orthology assignment by eggNOG-mapper. Jaime Huerta-Cepas, Kristoffer Forslund, Luis Pedro Coelho, Damian Szklarczyk, Lars Juhl Jensen, Christian von Mering and Peer Bork.Mol Biol Evol (2017). doi: 10.1093/molbev/msx148
- Fast genome-wide functional annotation through orthology assignment by eggNOG-mapper. Jaime Huerta-Cepas, Damian Szklarczyk, Lars Juhl Jensen, Christian von Mering and Peer Bork. Submitted (2016).
