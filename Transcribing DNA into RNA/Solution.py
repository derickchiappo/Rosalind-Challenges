test = open('rosalind_rna.txt',"r")

data = test.read()

for n in data:
    if n == "T":
        new_file = str
        new_file = data.replace(n,"U")
        
print(new_file)
