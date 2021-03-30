# get unknown function
from os import *
import codecs
from re import *
    # change directory
chdir("C:\\Users\\surface\\Documents\\GitHub\\IBI1_2020-21\\Practical8")
    # read fasta file
with codecs.open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",
                 "r", "utf-8") as infile:
    lines = infile.readlines()
    # extract data from file
result_list = []
for i in range(len(lines)):
    if lines[i].startswith(">"):
        result_list.append(findall(r'(>.+?)_', lines[i])[0])
        bases = ""
        for j in range(len(lines[i:-1])):
            if not lines[i+j+1].startswith(">"):
                bases += lines[i+j+1][:-1]
            else:
                break
        bases += "\n"
        result_list.append(bases)
    # add lengths of bases
for i in range(len(result_list)):
    if result_list[i].startswith(">"):
        result_list[i] += "  "
        result_list[i] += str(len(result_list[i+1]))
        result_list[i] += "\n"
    # write result into outfile
fout = codecs.open('unknown_function.fa', "w", "utf-8")
for line in result_list:
    fout.write(line)
fout.close()
