#!/usr/bin/env

'''
import optparse

parser = optparse.OptionParser()
parser.add_option('-i', '--input_directory', action="store", type="string", help = 'input directory', dest = 'i')
parser.add_option('-o', '--output_directory', action="store", type="string", help = 'output directory', dest = 'o')
(options, args) = parser.parse_args()
'''

with open('outputtmhmm.gff', 'w') as f:
    f.write("##gff-version 3" + "\n")
f.close()
    

tmhmmout = open("output.txt")
tmhmm=[]
for line in tmhmmout:
    row = line.strip().split()
    tmhmm.append(row)
    

source="TMHMM2.0"
typ="TMhelix"
score="."
phase ="."
attributes = "."
strand = "."


for i in range(len(tmhmm)):
    if tmhmm[i][0].startswith("#"):
        continue
    if tmhmm[i][2] == "TMhelix":
        seqid = tmhmm[i][0]
        start= int(tmhmm[i][3])
        end = start + int(tmhmm[int(i)][4])


        with open("outputtmhmm.gff", 'a') as f:
            f.write(seqid + "\t" + source + "\t" + typ + "\t" + str(start) + "\t" + str(end) + "\t" + score + "\t" + strand + "\t" + phase + "\t" + attributes + "\n")
f.close()
