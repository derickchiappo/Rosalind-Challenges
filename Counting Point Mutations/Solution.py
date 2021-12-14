file = open("rosalind_hamm.txt","r")

data = file.read()

splits = rex.split("[A,C,G,T]\n",data)

seq1 = list(splits[0])

seq2 = list(splits[1])


if len(seq1) == len(seq2):
    count = 0
    for n in range(0,(len(seq1)-1)):
        if(seq1[n] != seq2[n]):
            count += 1
        
print(count)
