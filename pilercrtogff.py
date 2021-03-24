# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:16:11 2021

@author: gargi
"""
import os 
import optparse


parser = optparse.OptionParser()
parser.add_option('-i', '--input_directory', action="store", type="string", help = 'input directory', dest = 'i')
parser.add_option('-o', '--output_directory', action="store", type="string", help = 'output directory', dest = 'o')
(options, args) = parser.parse_args()


with open(options.o, 'w') as f:
    f.write("##gff-version 3" + "\n")
f.close()
    
for filename in os.listdir(options.i):
    pilercrout = open(options.i + "/" + filename)
    pilercr=[]
    for line in pilercrout:
        row = line.strip().split()
        pilercr.append(row)
        

    source="PILERCR"
    typ="CRISPR"
    score="."
    phase ="."
    attributes = "."
  
    summary = (pilercr.index(['SUMMARY', 'BY', 'SIMILARITY']) + 6)

    for i in range(summary, len(pilercr)):
        if not pilercr[i]: 
            continue
        if pilercr[i][0].startswith("*"):
            continue
        if pilercr[i][0].startswith("SUMMARY"):
            break
        else:
            seqid = filename.split("_")[0] + pilercr[i][1]
            start= int(pilercr[i][2])
            end = start + int(pilercr[int(i)][3])
            strand = pilercr[i][7]

        with open(options.o, 'a') as f:
            f.write(seqid + "\t" + source + "\t" + typ + "\t" + str(start) + "\t" + str(end) + "\t" + score + "\t" + strand + "\t" + phase + "\t" + attributes + "\n")
f.close()
