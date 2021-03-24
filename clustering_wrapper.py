#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

##---------------IMPORTING PACKAGES---------------
import os
import subprocess
import optparse

##---------------OPTIONS------------------
def opts():
	parser = optparse.OptionParser()
	parser.add_option('-I', '--input_directory', help = 'input protein sequence directory', dest = 'I')
	parser.add_option('-i', '--identity', default = 0.9, help = 'clustering identity', dest = 'i')
	parser.add_option('-u', '--usearch_loc', help = 'usearch absolute path', dest = 'u')
	parser.add_option('-O', '--output_directory', help = 'output directory', dest = 'O')
	return(parser.parse_args())


##--------------USEARCH-------------------

##usage: perform_usearch(input_path, input_files, clust_id, usearch_path, output_path)

def perform_usearch(inpath, filenames, identity, usearch_loc, outpath):

	##make clustering folder in outpath to put all outputs

	f_combined = open(outpath + '/clustering/combined_fasta.faa', 'w')
	for f in filenames:
		current_file = open(inpath + '/' + 'f', 'r')
		for line in current_file:
			if line[0] == '>':
				name = '>' + 'f' + line[1:]
				f_combined.write(name)
			else:
				f_combined.write(line)
		current_file.close()
	f_combined.close()
	
	##command: usearch_path -clusterfast outpath/clustering/comgined_fasta.faa -id str(identity) -centroids outpath/clustering/centroids.fa -uc outpath/clustering/seq_labels.uc
	command = [usearch_loc, 'cluster_fast', outpath + '/clustering/combined_fasta.faa', '-id', str(identity), '-centroids', outpath + '/clustering/centroids.fa', '-uc', outpath + '/clustering/seq_labels.uc']
	subprocess.call(command)

##---------------Sequence Matching-----------------
## returns dict with centroids as keys, list of all sequences in a cluster as values
#usage: centroid_matching(input_files, outpath+'/clustering/seq_labels.uc')
def centroid_matching(sequence_names, uc_file):
    centroid_matches = {}
    uc_clusters = open(uc_file, 'r')
    for line in uc_clusters:
        line = line.split('\t')
        centroid = line[9]
        sequence = line[8]
        if '*' in centroid:
            centroid = line[8]
        centroid = centroid.strip()
        sequence = sequence.strip()
        if centroid not in centroid_matches:
            centroid_matches[centroid].append(sequence)
        else:
            centroid_matches[centroid] = [centroid]
    return(centroid_matches)













##----------MAIN---------------
def main():
	options, args = opts()

	input_path = args.I
	input_files = os.listdir(input_path)
	clust_id = args.i
	usearch_path = args.u
	output_path = args.O

	##create temp directories
	if not os.path.exists(output_path):
		os.makedirs(output_path)
	if not os.path.exists(output_path + '/clustering'):
		os.makedirs(output_path + '/clustering')
	

	
	### run pipeline
    perform_usearch(input_path, input_files, clust_id, usearch_path, output_path)
    clust_dict = centroid_matching(input_files, output_path + '/clustering/seq_labels.uc')

if __name__ == '__main__':
	main()





