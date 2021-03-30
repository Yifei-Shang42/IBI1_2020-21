# DNA to protein convertor
seq = "ATGCGACTACGATCGAGGGCC"
def translate_dna_to_protein(seq):
        # construct the translation dict
    translation_dict = {"TTT":"F",
                        "TTC":"F",
                        "TTA":"L",
                        "TTG":"L",
                        "CTT":"L",
                        "CTC":"L",
                        "CTA":"L",
                        "CTG":"L",
                        "ATT":"I",
                        "ATC":"I",
                        "ATA":"I",
                        "ATG":"M",
                        "GTT":"V",
                        "GTC":"V",
                        "GTA":"V",
                        "GTG":"V",
                        "TCT":"S",
                        "TCC":"S",
                        "TCA":"S",
                        "TCG":"S",
                        "CCT":"P",
                        "CCC":"P",
                        "CCA":"P",
                        "CCG":"P",
                        "ACT":"T",
                        "ACC":"T",
                        "ACA":"T",
                        "ACG":"T",
                        "GCT":"A",
                        "GCC":"A",
                        "GCA":"A",
                        "GCG":"A",
                        "TAT":"Y",
                        "TAC":"Y",
                        "TAA":"STOP",
                        "TAG":"STOP",
                        "CAT":"H",
                        "CAC":"H",
                        "CAA":"Q",
                        "CAG":"Q",
                        "AAT":"N",
                        "AAC":"N",
                        "AAA":"K",
                        "AAG":"K",
                        "GAT":"D",
                        "GAC":"D",
                        "GAA":"E",
                        "GAG":"E",
                        "TGT":"C",
                        "TGC":"C",
                        "TGA":"STOP",
                        "TGG":"W",
                        "CGT":"R",
                        "CGC":"R",
                        "CGA":"R",
                        "CGG":"R",
                        "AGT":"S",
                        "AGC":"S",
                        "AGA":"R",
                        "AGG":"R",
                        "GGT":"G",
                        "GGC":"G",
                        "GGA":"G",
                        "GGG":"G"}
        # create string to store translated amino acids
    protein = ""
        # translate amino acids one by one
    for i in range(0,len(seq),3):
        if translation_dict[seq[i:i+3]] != "STOP":
            protein += translation_dict[seq[i:i+3]]
        else:
            break
    return protein
translate_dna_to_protein(seq)