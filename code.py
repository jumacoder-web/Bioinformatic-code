import pandas as pd
data={
    "samples":["s1","s2","s3","s4"],
    "species":["E coli","Aspagullus","Mycetes","E coli"],
    "treatment":["drug_1","drud_2","cure","control"],
    "gene_A":[23,78,56,67],
    "gene_B":[43.2,78.1,90.5,62.1]
}
df=pd.DataFrame(data)
print(df)
df.head()
print(df.describe())
print(df.info())
print(df.dtypes)
print(df["gene_A"].mean())
for gene in "gene_A":
    print(gene)
gene_D = 45
if gene_D>45:
    print("danger")
elif gene_D<90:
    print("better")
else:
    print("problem")
# functions
def gene_k(dna):
    gc_content=dna.count("G") + dna.count("C")
    return gc_content/len(dna)*100
print(gene_k("AATCGTACCCTACCCTGA"))
# visualization
import matplotlib.pyplot as plt
plt.hist("gene_content")
plt.xlabel("gene_A")
plt.ylabel("gene_B")
plt.title("computational biology")
plt.show()
print(df.groupby("gene_A")["gene_B"].mean())
print(df.dtypes)
print(df[["gene_B","gene_A"]].sum())
print(df.duplicated)
print(df.dropna())
count = 3
while count < 4:
    print("count")
         



