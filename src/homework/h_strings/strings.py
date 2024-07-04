#
def get_hamming_distance(dna1, dna2):
    hamming_distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming_distance += 1
    return hamming_distance
    
def get_dna_complement(dna):

    complements_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    dna_reversed  = []

    for dna_base in range(len(dna) -1, -1, -1):
        dna_reversed.append(dna[dna_base])

    dna_complement = []

    for dna_base in dna_reversed:
        dna_complement.append(complements_dict[dna_base])
    
    result = ''

    for bases in dna_complement:
        result += bases
    
    return result