#!/usr/bin/env python3

import os
import subprocess
import optparse


##----------------------OPTIONS-------------------------------
def opts():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--input_file',
                      help='input file is a protein .fa file. This needs to be in the directory you are working in',
                      dest='i')
    parser.add_option('-d', '--database_type', help='bact=bacteria/euk=eukaryotes/arch=archea', dest='d')
    parser.add_option('-D', '--data_dir', help='the path to where the database information is stored',
                      dest='D')
    parser.add_option('-o', '--output', help='base name for output file', dest='o')
    parser.add_option('-O', '--output_dir',
                      help='the directory where you want your output files to be located', dest='O')
    # SEE HOW TO ADD THIS AS OPTIONAL: parser.add_option('-cpu', '--cpu', help= 'Can run if you want to use CPU', dest='cpu',
    return (parser.parse_args())


##---------------EGGNOG-MAPPER----------------------------------
##need to be in eggnog env - which is python version python2.7
##tool needs to be added to the PATH so you can access it from anywhere

# ADD CPU?
def perform_eggnogmapper(input_file, data_directory, output_base, output_directory, database_type):
    # data_directory = is the path to where the database is
    # output_base is the output file name you want all your output files to have
    # output_directory = the path to where you want your outputs to go
    # database_type = is you are looking for bact, euk, arch
    command_to_run = ['emapper.py', '-i', input_file, '-d', database_type, '-m', 'diamond', '--data_dir', data_directory, '--output', output_base, '--output_dir', output_directory]
    print(command_to_run)
    subprocess.call(command_to_run)


##---------------------------MAIN--------------------------------

def main():
    args, options = opts()
    ##see if there is an input file directory
    input_file = args.i
    data_directory = args.D
    # to put output files base name
    output_base = args.o
    output_directory = args.O
    database_type = args.d

    ##create temp directories
    #if not os.path.exists(output_path):
     #   os.makedirs(output_path)
    #if not os.path.exists(output_path + '/eggnog'):
     #   os.makedirs(output_path + '/eggnog')

    # run the pipeline
    perform_eggnogmapper(input_file, data_directory, output_base, output_directory, database_type)


if __name__ == '__main__':
    main()