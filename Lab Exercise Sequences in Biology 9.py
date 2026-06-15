def mymain():
    # Sets: Finding unique mutations: You have sequenced the genomes of two different viral strains. you need to identify which mutations are unique to the new strain and which are shared between both.
    # Data:  strain_a = {"C241T", "C3037T", "A23403G"}
    #        strain_b = {"C241T", "G25563T", "C3037T", "T28144C"}
    #
    # a. Find the mutations present in both strains (Intersection).
    # b. Find the mutations that exist only in strain_b (Difference).
    # c. Combine all unique mutations found across both strains into one master list (Union).
    strain_a = {"C241T", "C3037T", "A23403G"}
    strain_b = {"C241T", "G25563T", "C3037T", "T28144C"}
    both_strains = strain_a & strain_b
    only_in_strain_b = strain_a - strain_b
    all_unique_mutations = strain_a | strain_b
    master_list = list(all_unique_mutations)
    print("1. Shared mutations (Intersection):", both_strains)
    print("2. Mutations only in strain_b (Difference):", only_in_strain_b)
    print("3. Master list of all unique mutations (Union):", master_list)

    # Given a DNA sequence, find its reverse complement. First, find the complement (A↔T, C↔G), then reverse the entire string.
    pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}
    sequence = "ATGC"
    # put an empty string
    reverse_complement = " "
    for base in sequence:
        complement = pairs[base]
        reverse_complement = complement + reverse_complement
    print(reverse_complement)

    dna_sequence = "AAATTTGAATTCACCCTTTA"
    target_site = "GAATTC"
    fragments = dna_sites_clean(dna_sequence, target_site)
    print(fragments)


    sequence1 = "ATCGTA"
    sequence2 = "AGCGAA"
    hamming_sequence_append(sequence1, sequence2)




# Simulating Restriction Enzyme Digestion: Restriction enzymes cut DNA at specific "recognition sites" (e.g., EcoRI cuts at GAATTC). Given a long DNA string and a recognition sequence, write a function that "digests" the DNA and returns a list of fragments.
def dna_sites_clean(dna, target):
    return dna.split(target)

# Calculating Hamming Distance: The Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different. It’s used to measure evolutionary distance. Compare two sequences and return the total number of point mutations (mismatches).
# Doubt
def hamming_sequence_append(seq1, seq2):
    mismatch = []
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mismatch.append(i)

if __name__=="__main__":
    mymain()
