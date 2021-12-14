file = open('rosalind_revc.txt',"r")

sequence = file.read()

seq_list = list(sequence)

for n in range(0,len(sequence)):
    if seq_list[n] == "A":
        seq_list[n] = "T"
    elif seq_list[n] == "T":
        seq_list[n] = "A" 
    elif seq_list[n] == "G": 
        seq_list[n] = "C"
    elif seq_list[n] == "C":
        seq_list[n] = "G"
    
print(''.join(reversed(seq_list)))
