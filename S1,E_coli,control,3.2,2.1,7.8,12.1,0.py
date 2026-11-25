import os
import pandas as pd
bioinformatic_path=r"C:\Users\JUMA\OneDrive\Desktop\Bioinformatic"
file_location=os.path.join(bioinformatic_path,("bio_data.csv"))
df=pd.read_csv(file_location,header=None)
print(df)
print(df.dtypes)
print(df.describe())
print(df.info)
print(df.mean)
print(df.columns)
print(df.shape)
df.mean
print(df.duplicated)
print(df.isna)
df.drop_duplicates
import pandas as pd
import os
print(os.listdir())
import pandas as pd
df=pd.read_csv("bioinformatics_gene_expression_practice.csv")
print(df)
print(df.columns.tolist())
print(df.describe())
print(df.info())
print(df.isna())
print(df.duplicated())
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("bioinformatics_gene_expression_practice.csv")
plt.xlabel("sample")
plt.ylabel("gene A expression")
plt.title("EVANS JUMA LUTOMIA")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bioinformatics_gene_expression_practice.csv")

df = df[df["sample"] != "import pandas as pd"]

plt.hist(df["gene_A"], bins=5, alpha=0.5, label="Gene A")
plt.hist(df["gene_B"], bins=5, alpha=0.5, label="Gene B")
plt.hist(df["gene_C"], bins=5, alpha=0.5, label="Gene C")
plt.hist(df["gene_D"], bins=5, alpha=0.5, label="Gene D")

plt.xlabel("Gene expression")
plt.ylabel("Number of samples")
plt.title("Distribution of Gene Expression")

plt.legend()

plt.show()
