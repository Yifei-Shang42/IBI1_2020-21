# convert unknown DNA to protein
from os import *
import codecs
from re import *
    # create translation function
def translate_dna_to_protein(seq):
    translation_dict = {"TTT": "F",
                        "TTC": "F",
                        "TTA": "L",
                        "TTG": "L",
                        "CTT": "L",
                        "CTC": "L",
                        "CTA": "L",
                        "CTG": "L",
                        "ATT": "I",
                        "ATC": "I",
                        "ATA": "I",
                        "ATG": "M",
                        "GTT": "V",
                        "GTC": "V",
                        "GTA": "V",
                        "GTG": "V",
                        "TCT": "S",
                        "TCC": "S",
                        "TCA": "S",
                        "TCG": "S",
                        "CCT": "P",
                        "CCC": "P",
                        "CCA": "P",
                        "CCG": "P",
                        "ACT": "T",
                        "ACC": "T",
                        "ACA": "T",
                        "ACG": "T",
                        "GCT": "A",
                        "GCC": "A",
                        "GCA": "A",
                        "GCG": "A",
                        "TAT": "Y",
                        "TAC": "Y",
                        "TAA": "O",
                        "TAG": "U",
                        "CAT": "H",
                        "CAC": "H",
                        "CAA": "Q",
                        "CAG": "Q",
                        "AAT": "N",
                        "AAC": "N",
                        "AAA": "K",
                        "AAG": "K",
                        "GAT": "D",
                        "GAC": "D",
                        "GAA": "E",
                        "GAG": "E",
                        "TGT": "C",
                        "TGC": "C",
                        "TGA": "X",
                        "TGG": "W",
                        "CGT": "R",
                        "CGC": "R",
                        "CGA": "R",
                        "CGG": "R",
                        "AGT": "S",
                        "AGC": "S",
                        "AGA": "R",
                        "AGG": "R",
                        "GGT": "G",
                        "GGC": "G",
                        "GGA": "G",
                        "GGG": "G"}
    # create string to store translated amino acids
    protein = ""
    # translate amino acids one by one
    for i in range(0, len(seq), 3):
        protein += translation_dict[seq[i:i + 3]]
        if seq[i:i + 3] in ["TAA", "TAG", "TGA"]:
            break
    return protein

# change directory
chdir("C:\\Users\\surface\\Documents\\GitHub\\IBI1_2020-21\\Practical8")
    # input filename
name = input()
    # read input data
with codecs.open(name, "r", "utf-8") as infile:
    lines = infile.readlines()
    # create list to store result
result = []
    # translate dna to protein
for line in lines:
    if line.startswith(">"):
        result.append(line)
    else:
        result.append(translate_dna_to_protein(line))
    # replace dna length with protein length
for i in range(len(result)):
    if result[i].startswith(">"):
        result[i] = findall(r'>.+? ', result[i])[0]
        result[i] += str(len(result[i+1]))
        result[i] += "\n"
    else:
        result[i] += "\n"
    # write result into outfile
fout = codecs.open("protein.fa", "w", "utf-8")
for line in result:
    fout.write(line)
fout.close()
