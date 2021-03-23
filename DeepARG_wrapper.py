#!/usr/bin/env python3

import os
import subprocess
import optparse
#import argparse


##----------------------OPTIONS-------------------------------
def opts():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--input_file_path', help='Provide the input file path', dest='i')
    parser.add_option('-m', '--model', help='SS for short sequence reads and LS for genes', dest='m')
    parser.add_option('-o', '--output_file_path', help='Provide the output file path', dest='o')
    parser.add_option('-d', '--database_directory', help='Provide the database directory path', dest='d')
    parser.add_option('-t', '--sequence_type', help='Prot for protein and nucl for nucleotides', dest='t')
    parser.add_option('-p', '--min_probability',help= 'Minimal probability to define the ARG category to which the input belongs to.', dest='p')
    return (parser.parse_args())


##---------------DEEPARG----------------------------------
##need to be in eggnog env - which is python version python2.7
##tool needs to be added to the PATH so you can access it from anywhere

def perform_deepARG(input_file_path, model, output_directory, database_directory, sequence_type, min_probability):
    command_to_run = ['deeparg', 'predict', '-i', input_file_path, '--model', model, '-o', output_directory, '-d', database_directory, '--type', sequence_type, '--min-prob', min_probability]
    print(command_to_run)
    subprocess.call(command_to_run)


##---------------------------MAIN--------------------------------

def main():
    args, options = opts()
    #print(options, args)
    #print(type(options), type(args))
    input_file_path = args.i
    model = args.m
    output_directory = args.o
    database_directory = args.d
    sequence_type = args.t
    min_probability = args.p

    ##create temp directories
    #if not os.path.exists(output_directory):
    #    os.makedirs(output_directory)
    #if not os.path.exists(output_directory + '/deeparg'):
     #   os.makedirs(output_directory + '/deeparg')

    # run the pipeline
    perform_deepARG(input_file_path, model, output_directory, database_directory, sequence_type, min_probability)


if __name__ == '__main__':
    main()