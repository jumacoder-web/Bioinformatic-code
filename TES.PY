import pandas as pd
data={
    "sample":["s1","s2","s3","s4"],
    "treatments":["drug1","drug2","drug3","piriton"],
    "gene_A":[12.2,34.5,78.7,34.7],
    "gene_B":[23,56,89,199]
}
df = pd.DataFrame(data)
print(df)
print(df.describe())
df.info()
df.shape
print(df.dtypes)
import matplotlib.pyplot as plt
plt.hist("gene_A")
plt.xlabel("gene_B")
plt.ylabel("gene_A")
plt.title("CLEVIX TEST")
plt.show()
# conditions
juma_age = 18
if juma_age>23:
    print("adult")
elif juma_age>=15:
    print("youth")
else:
    print("young")
    