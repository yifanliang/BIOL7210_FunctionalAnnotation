# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:37:33 2021

@author: gargi
"""

#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

import os
import subprocess
import optparse

#OPTIONS----------------------------------------------------------------------------
parser = optparse.OptionParser()
parser.add_option('-i', '--input_directory', action="store", type="string", help = 'input directory', dest = 'i')
parser.add_option('-o', '--output_directory', action="store", type="string", help = 'output directory', dest = 'o')
parser.add_option('-g', '--organism', action="store", type="string", help = 'option for type of bacteria: gram+ or gram-', dest = 'org')
(options, args) = parser.parse_args()


#SIGNALP FUNCTION------------------------------------------------------------------
def run_signalp(inputdir, outputdir, org):
    if org == "gram-":
        for i in os.listdir(inputdir): 
            command = ['signalp', '-fasta', inputdir+'/'+i, '-org','gram-', '-format','short', '-prefix', outputdir + '/' + i[:-6]+'signalp_out','-gff3']    
            subprocess.call(command)
    if org == "gram+": 
         for i in os.listdir(inputdir): 
            command = ['signalp', '-fasta', inputdir+'/'+i, '-org','gram+', '-format','short', '-prefix', outputdir + '/' + i[:-6]+'signalp_out','-gff3']    
            subprocess.call(command)


#MAIN FUNCTION-------------------------------------------------------------------   
def main():
    run_signalp(options.i, options.o, options.org)
    
if __name__ == "__main__":
    main()
    
    
    
    

