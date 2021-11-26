""" my python code created from scratch; commented out lines were used to troubleshoot and check my results """
dnadict = {}
lines = open("codon_table-1.dat", "r")
for line in lines:
    entry = line.split()
    key = entry[0]
    value = entry[1]
    dnadict.update({key : value})
#print(len(dnadict))
lines.close()
#for x in dnadict:
    #print(x)
    #print(dnadict[x])

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
#count = 1
#output_file = open("translated_dna.txt", "r")
#for line in output_file:
    #for char in line:
        #count += 1
    #print(count)
