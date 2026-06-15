# write a program that takes a DNA string and outputs its RNA equivalent.
def transcribe_dna_to_rna(dna_string):
	rna_string=dna_string.replace('T','U')
	return rna_string

x="ATGCATGCATGCTTT"
a=transcribe_dna_to_rna(x)
print(a)

# calculate the percentage of 'G' and 'C' in a sequence
# doubt
def calculate_gc_content(sequence):
    """Calculates GC content percentage, handling case-sensitivity and empty strings."""
    # Prevent division by zero for empty inputs
    if not sequence:
        return 0.0

    # Standardize to uppercase to catch 'g' and 'c'
    sequence = sequence.upper()

    # Use built-in count for faster execution
    gc_count = sequence.count('G') + sequence.count('C')

    return (gc_count / len(sequence)) * 100

# Example Usage:
print(calculate_gc_content("ATGCATGC"))  # Output: 50.0
print(calculate_gc_content(""))  # Output: 0.0

# Pass the DNA string into the function call
dna_seq = "GCATGCATGCAT"
result = calculate_gc_content(dna_seq)

print("GC content percentage:", result)






# motif searching (Finding sequences): Find all starting positions of a specific sub-string within a long sequence
# doubt
def find_motif_positions(sequence, motif):
    """
    Finds all starting positions of a motif within a long sequence.
    Handles overlapping occurrences.
    """
    # Guard check for empty inputs or if motif is longer than the sequence
    if not sequence or not motif or len(motif) > len(sequence):
        return []

    positions = []
    # Loop through the sequence up to where the motif can still fit
    for i in range(len(sequence) - len(motif) + 1):
        # Slice the sequence to match the length of the motif
        if sequence[i: i + len(motif)] == motif:
            positions.append(i)

    return positions


# Example Usage:
genome_seq = "GATATATGCATATACTT"
target_motif = "ATAT"

# Run the function
result_indices = find_motif_positions(genome_seq, target_motif)

print(f"Sequence: {genome_seq}")
print(f"Motif:    {target_motif}")
print(f"Starting positions (0-indexed): {result_indices}")

# protein translation (codon mapping): Break a string into chunks of 3 and map them to their corresponding amino acid
# doubt
def translate_dna(sequence):
    codon_table = {
        "ATG": "M",  # Methionine
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",  # Alanine
        "TAA": "Stop", "TAG": "Stop", "TGA": "Stop"
    }

    protein = ""

    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]

        if len(codon) < 3:
            break

        amino_acid = codon_table.get(codon, "?")

        if amino_acid == "Stop":
            break

        protein += amino_acid

    return protein


dna = "ATGGCTTAA"
print(translate_dna(dna))


