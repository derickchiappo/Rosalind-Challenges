#Codon-to-protein lookup table
file = open("RNAProteinCode.txt","r")

RNAproteintable = file.read().strip()

proteins = rex.findall("(?<=\w\w\w\s)\w{1,4}",RNAproteintable)

#amino acid seqeunce provided by Rosalind for challenge
file2 = open("rosalind_mrna.txt","r")

mRNA = file2.read().strip()

#dictionary to count the number unique codons that encode each amino acid
counts_AA = {}
    
for n in proteins:
    counts_AA[n] = proteins.count(n)

#Calculation of the number of possible mRNA sequences from the amino acid sequence provided
sum = 1

for n in mRNA:
        sum = counts_AA[n]*sum   
sum = sum * 3

print(sum % 1000000)
