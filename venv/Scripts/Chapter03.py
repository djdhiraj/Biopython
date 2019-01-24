import Bio
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
print("Bio._Version_")
my_sequence=Seq('AGTCTGAGTGCTGATGCTGA',generic_dna)
print(my_sequence)
my_rna=my_sequence.transcribe()
print(my_rna)
print(my_rna_rna.back_transcribe())
print(my_rna.back_transcribe())
print(my_rna.back_transcribe().complement())
print(my_rna.back_transcribe().reverse_complement())

