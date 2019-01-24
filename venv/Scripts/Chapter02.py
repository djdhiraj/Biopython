import Bio
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
print(Bio._Version_)
my_sequence=Seq('ATCGATCGTAGCTGACGT',generic_dna)
print(my_sequence)
print(my_sequence.reverse())
print(my_sequence.complement())
print(my_sequence.reverse_complement())
