#!/usr/bin/env python2
# -*- encoding: utf-8 -*-


import os
import subprocess
import optparse

        
#OPTIONS------------------------------------------------------------------------------  
parser = optparse.OptionParser()
parser.add_option('-i', '--input_directory', action="store", type="string", help = 'input directory', dest = 'i')
parser.add_option('-o', '--output_directory', action="store", type="string", help = 'output directory', dest = 'o')
parser.add_option('-n', '--no_info', "-v", action="store_true", help= 'option for whether help statement should be printed in output, default=no info', dest="n")
(options, args) = parser.parse_args()


#PILERCR FUNCTION--------------------------------------------------------------------
def run_pilercr(inputdir, outputdir, info):
    for i in os.listdir(inputdir):
        print(i)
        if info == True:
            command = ['pilercr', '-in', inputdir+'/'+i,'-out', outputdir + '/' + i[:-6]+'_pilercr_out.txt']
            print(command)
            subprocess.call(command)
        else:
            command = ['pilercr', '-in', inputdir+'/'+i,'-out', outputdir + '/' + i[:-6]+'_pilercr_out.txt','-noinfo']
            print(command)
            subprocess.call(command)
  

#MAIN FUNCTION-----------------------------------------------------------------------
if __name__ == "__main__":
    run_pilercr(options.i, options.o, options.n)