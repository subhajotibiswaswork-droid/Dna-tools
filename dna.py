#Function to transcribe DNA to RNA
def transcribe(dna_sequence):
    return dna_sequence.replace('T', 'U')
#parameters
valid_bases = {'A', 'T', 'G', 'C'}

#Input
while True:
    dna = input("Enter a DNA sequence: ").upper()
    valid_sequence = True

#validate the DNA sequence
    for base in dna:
        if base not in valid_bases:
            valid_sequence = False
            print("Invalid DNA sequence. Please enter a sequence containing only A, T, G, C.")
            break
    if not valid_sequence:
        continue

#output
    rna = transcribe(dna_sequence=dna)
    print("RNA sequence:", rna)
    break