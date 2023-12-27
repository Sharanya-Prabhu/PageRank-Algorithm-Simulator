import ast
import pandas as pd


# Read the text file
with open("output.txt", "r") as f:
    data_out = f.read()

# Convert the string to a list
out_list = ast.literal_eval(data_out)

df = pd.DataFrame(out_list, columns=['node', 'rank'])
df['node'] = df['node'].astype(int)
print(df.head())


df_in = pd.read_csv("web_Google.adj", sep=" ", header=None, names=['node', 'ini_rank','outlinks'])
print(df_in.head())

print(df_in.dtypes)
print(df.dtypes)

df_combine = pd.merge(df, df_in, on='node')
print(df_combine.head())

#save the file as output_merged.txt with columns node, rank and outlinks
df_combine.to_csv('output_reformatted.txt', sep=' ', index=False, header=False, columns=['node', 'rank', 'outlinks'])


