# Protein Alignment

# import acquired modules
from Bio.SubsMat import MatrixInfo

# Input Files
    # design a function to read fasta file


def read_fasta(filename):
    """
    Input: A string of fasta filename (absolute path)
    Returns:
        A list containing the name of the sequence and the sequence
    """
    infile = open(filename, "r")
    lines = infile.readlines()
    name = lines[0][:-1]
    seq = lines[1][:-1]
    return [name, seq]

    # read the three fasta file into lists using read_fasta
sod2_human = read_fasta("C:\\Users\\surface\\Documents\\GitHub"
                        "\\IBI1_2020-21\\Practical11\\SOD2_human.fa")

sod2_mouse = read_fasta("C:\\Users\\surface\\Documents\\GitHub"
                        "\\IBI1_2020-21\\Practical11\\SOD2_human.fa")

random_seq = read_fasta("C:\\Users\\surface\\Documents\\GitHub"
                        "\\IBI1_2020-21\\Practical11\\RandomSeq.fa")

    # create the BLOSUM62 matrix using BioPython module
blosum62 = MatrixInfo.blosum62

# Compare Sequences

    # create function to generate final score
def my_blosum_62(seq1, seq2):
    """
    Input: Two protein sequences (string) (seq1, seq2)
    Returns:
         The alignment score of the two proteins using BLOSUM62 matrix
         If proteins are of different lengths, the maximum score will be returned
    """
    # create function for alignment with sequences of the same length
    def one_alignment(s1, s2):
        """
        Input: Two protein sequences with same length (string) (s1, s2)
        Returns:
            The alignment score of the two proteins using BLOSUM62 matrix
        """
        score = 0
        for i in range(len(s1)):
            amino_pair = (s1[i], s2[i])
            if amino_pair not in blosum62:
                revered_pair = (s2[i], s1[i])
                score += blosum62[revered_pair]
            else:
                score += blosum62[amino_pair]
        return score

    # if sequences are of the same length, one alignment will be sufficient
    if len(seq1) == len(seq2):
        return one_alignment(seq1, seq2)

    # if sequences are not of the same length, multiple alignments are needed
    # using the sliding window algorithm, best score will be returned

    else:
        diff = abs(len(seq1)-len(seq2))
        score_list = []
        if len(seq1) < len(seq2):
            for i in range(diff+1):
                score = one_alignment(seq1, seq2[i:i+len(seq1)])
                score_list.append(score)

        else:
            for i in range(diff+1):
                score = one_alignment(seq2, seq1[i:i+len(seq2)])
                score_list.append(score)

        return max(score_list)


# human-mouse alignment
human_mouse_score = my_blosum_62(sod2_human[1], sod2_mouse[1])

# human-random alignment
human_random_score = my_blosum_62(sod2_human[1], random_seq[1])

# mouse-random alignment
mouse_random_score = my_blosum_62(sod2_mouse[1], random_seq[1])

# Print Output
def gen_output(fasta1, fasta2):
    for item in fasta1:
        print(item)
    for item in fasta2:
        print(item)
    print(my_blosum_62(fasta1[1], fasta2[1]))
