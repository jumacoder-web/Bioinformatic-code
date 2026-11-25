gene=("BRCAI")
dna=("ATGC")
gene_expression=22.1
people=2
people_2=True
print(people)
print(people_2)
print(gene)
print(dna)
print(gene_expression)
# lists
gene_A=["BRCA1","TP53","EGFR"]
print(gene_A)
# dictionary
data={
    "sample":["s1","s2"],
    "genes":["a","b"],
    "species":["lut","juj"]
}
print(data)
# conditions
gene_expression=12
if gene_expression >19:
    print("good")
elif gene_expression<15:
    print("moderate")
else:
    print("warning")
# loops
for gene in gene_A:
    print(gene)
for i in range(5):
    print(i)
# while loop
count=3
while count>4:
    print(count)
    count=count+1
# function
def dna_length(sequence):
    return len(sequence)
dna="ATGCGTAC"
print(dna_length(dna))
def gc_content(sequence):
    gc=sequence.count("G") + sequence.count("C")
    return gc/len(sequence)*100
print(gc_content("ATGCGTAC"))
def greet_biologist():
    print("welcome to computational biology")
greet_biologist()
def check_gene_expression(gene_expression):
    if gene_expression>10:
        print("High expression")
    else:
        print("Low expression")
check_gene_expression(7)
def calculate_gc_content(dna):
    gc_content=dna.count("G") + dna.count("C")
    print(gc_content/len(dna)*100)
def gc_content(dna):
    gc_content=dna.count("G") + dna.count("C")
    return gc_content/len(dna)*100
result=calculate_gc_content("ATGCGC")
print(result)
import pandas as pd
import matplotlib.pyplot as plt
data={
    "samples":["s1","s2","s3","s4"],
    "species":["E.coli","E.coli","E.coli","E.coli"],
    "treatment":["23.1","20.5","56.9","78.9"],
    "genes":["34","45","56","89"]
}
df=pd.DataFrame(data)
print(df)
plt.plot(df["treatment"], df["genes"])
plt.xlabel("treatment")
plt.ylabel("frequency")
plt.title("lutomia")
plt.show()
               
