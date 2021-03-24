#!/usr/bin/env

import os
import subprocess
import optparse

##----------------------OPTIONS-------------------------------
def opts():
    parser = optparse.OptionParser()
    ##parser.add_option('-t', '--tmhmm_path', help = 'tmhmm installation path', dest = 't')
    parser.add_option('-i', '--input_path', help='Provide the input file path', dest='i')
    parser.add_option('-o', '--output_path', help='Provide the output file path', dest='o')
    return (parser.parse_args())

##----------------------TMHMM----------------------------------
##tool needs to be added to the PATH so you can access it from anywhere
##usage perform_tmhmm(tmhmm_directory, input_directory, output_directory)

def perform_tmhmm(ipath, opath):
    
##command: ./tmhmm input_path > output_path/tmhmm/tmhmm.txt
    cd_tmhmm = ['cd', '/home/team1/functional_annotation/bin/tmhmm-2.0c']
    print(cd_tmhmm)

    command_to_run_tmhmm = ['./tmhmm', '-long', ipath, '>',opath + '/tmhmm/tmhmm_output.txt']
    print(command_to_run_tmhmm)
    subprocess.call(command_to_run_tmhmm)

##-----------------------MAIN----------------------------------

def main():
    args, options = opts()
    #print(options, args)
    #print(type(options), type(args))
    input_path = args.i
    output_path = args.o

    ##create temp directories
    #if not os.path.exists(output_path):
    #    os.makedirs(output_path)
    #if not os.path.exists(output_path + '/tmhmm'):
     #   os.makedirs(output_path + '/tmhmm')

    # run the pipeline
    perform_tmhmm(input_path, output_path)

if __name__ == '__main__':
    main()