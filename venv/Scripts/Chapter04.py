import os
nucleicaid = input("Enter D to convert to DNA or R to convert to RNA")
if nucleicaid.lower() == "r":
  dna =[]
  data = input("Press Enter to add a DNA nucleobase. Enter Exit to exit.")
  While data == "":
    nucleobase = input("Enter A for adenine, C for cytosine, G for Guanine, or T for Thymine.")
    dna.append(nucleobase.upper())
    data = input("Press Enter to add another DNA nucleobase. Enter Exit if you are finished.")
  rna = dna[:]
  while "T" in rna:
    rna[rna.index("T")] = "U"
if nucleicaid.lower() == "d":
   rna = []
   data = input("Press Enter to add an RNA nucleobase. Enter Exit to exit.")
   while data = "":
      nucleobase = input("Enter A for Adenine, C for cytosine, G for Guanine, or U for Uracil.")
      rna.append(nucleobase.upper())
      data = input("Enter to add anther RNA nucleobase. Enter Exit if you are finished.")
   dna = rna[:]
   while "U"in dna:
      dna[dna.index("U")] = "T"
 
 os.system("cls")
 print("Here is your bioinformatical report:")
 print()
 print("Your DNA sequence")
 print(dna)
 print()
 print("Your RNA sequence")
 print(rna)
 
