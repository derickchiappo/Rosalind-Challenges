#This solution is dependent on functions in the re package using RegEX expression
import re as rex

file = open("rosalind_gc.txt","r")

data = file.read()

sequence_names = rex.findall(">Rosalind_\\d+",data)
                
      
for n in sequence_names:
    
    GC_content = []
    
    Seqs = []
    
    if rex.match(n,data) != "None":
        for k in range(0,len(sequence_names)):
            if k + 1 < len(sequence_names):
                GC_content += [ ( (data[data.index(sequence_names[k]) + 14:data.index(sequence_names[k + 1])].count("G") +
                      data[data.index(sequence_names[k]) + 14:data.index(sequence_names[k + 1])].count("C")) / (
                      len(data[data.index(sequence_names[k]) + 14:data.index(sequence_names[k+1])]) -
                               data[data.index(sequence_names[k]) + 14:data.index(sequence_names[k+1])].count("\n") )
                                ) *100
                              ]
                     
                
                Seqs += [sequence_names[k]]
                
            if k  == (len(sequence_names) - 1):
                
                GC_content += [ ( (data[data.index(sequence_names[k]) + 14:len(data)].count("G") +
                      data[data.index(sequence_names[k]) + 14:len(data) + 1].count("C") ) / (
                    
                      len(data[data.index(sequence_names[k]) + 14:len(data)]) -
                               data[data.index(sequence_names[k]) + 14:len(data)].count("\n") ) ) * 100
                              ]
                
                Seqs += [sequence_names[k]]
                

print(Seqs[GC_content.index(max(GC_content))])
print(round(max(GC_content),6))
