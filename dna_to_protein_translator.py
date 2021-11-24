"""
Implement a python program to read the DNA sequence of a gene, 
and translate it into the corresponding protein sequence 
by using the provided translation table.
Part 1:
Create a python dictionary data structure by reading the codon 
table file codon_table.dat file into a python dictionary data 
structure, using the triplet codon sequences (first column in 
the file) as the key and the amino acid characters (second column
in the file) as the value.
Part 2:
Using the python string concatenation operator (+) read all the 
sequences in the DNA sequence file (Nep3-PA.fa) and join then 
into one long continuous string. For translation into a protein 
sequence, the length of the DNA sequence of the gene has to be 
a multiple of three, and DNA sequences are a combination of the 
letters A, T, G, and C. A sample DNA sequence for the gene 
Nep3-PA.fa is provided
Part 3:
Starting from the beginning of the python string containing the 
DNA sequence, select the next three letters (called triplets or codons) 
and use them as a key to lookup or return the corresponding amino 
acid letter value, they represent. Then write the translated amino acid 
value into an output file. Continue by repeatedly selecting the next 
three DNA letters, and translate again, until we get to the end of the 
DNA sequence file
"""
dnadict = {}
lines = open("codon_table-1.dat", "r")
for line in lines:
    entry = line.split()
    key = entry[0]
    value = entry[1]
    dnadict.update({key : value})
#print(len(dnadict))
lines.close()
"""for x in dnadict:
    print(x)
    print(dnadict[x])"""

dna_string = ""
bldg_blocks = "ACGT"
read_file = open("Nep3-PA.fa", "r")
read_file.readline()
for line in read_file:
    for char in line:
        if char in bldg_blocks:
            dna_string += char
#print(dna_string)    
read_file.close()

output_file = open("translated_dna.txt", "w")
length = len(dna_string)
counter = 0
#print(length)
for i in range(0, length, 3):   
    codon = dna_string[i:i+3]
    #print(codon)                  
    amino_acid_letter = dnadict[codon] 
    #print(amino_acid_letter)
    counter += 1
    if counter % 79 == 0:
        output_file.write("\n") 
    output_file.write(amino_acid_letter)   
output_file.close()
#checking that my output has at most 80 amino acid sequences per line (i.e. 80 chars max per line)
count = 1
output_file = open("translated_dna.txt", "r")
for line in output_file:
    for char in line:
        count += 1
    print(count)
#quick check of my result vs emboss's result
"""string1 = "MTRYKQTEFTEDDSSSIGGIQLNEATGHTGMQIRYHTARATWNWRSRNKTEKWLLITTFVMAITIFTLLIVLFTDGGS"
string2 = "MTRYKQTEFTEDDSSSIGGIQLNEATGHTGMQIRYHTARATWNWRSRNKTEKWLLITTFVMAITIFTLLIVLFTDGGS"
if string1 is string2:
    print("They match!")"""