#%%
import pandas as pd

df = pd.read_csv("/Users/a2/Desktop/Penislänge von allen meinen Freunden.csv",delimiter=";")



# %%
df
# %%
i=df.iloc[:,1]# %%

# %%
import numpy as np
m=np.mean(df.iloc[:,1])# %%
# %%
m
# %%
n=np.std(i)
# %%
n
# %%
m*n
# %%
t=np.var(i)
# %%
t
# %%
