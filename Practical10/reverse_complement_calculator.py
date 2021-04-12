# Reverse Complement Calculator


def reverse_complement_calculator(seq):
    """
    Input:
        seq, A DNA sequence (string)
    Returns:
        The reverse complement strand of the DNA in UPPER CASE (string)
    """
        # capitalize all bases
    seq.capitalize()

        # generate complement strand
    complement = []
    for base in seq:
        if base == "A":
            complement.append("T")
        elif base == "T":
            complement.append("A")
        elif base == "C":
            complement.append("G")
        else:
            complement.append("C")

        # generate reverse strand
    reverse = reversed(complement)
    result = "".join(reverse)

    return result

# example
reverse_complement_calculator("ATCGATCGATCG")