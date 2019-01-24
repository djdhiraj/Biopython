import Bio
from Bio.Seq import Seq
print(Bio._Version_)
my_sequence=Seq('AGTATACTATGTGCATAGTCAGTCAGTCGA')
print(my_sequence)
print(my_sequence.alphabet())
my_sequence_complement=my_sequence.complement()
print(my_sequence_complement)
