import pandas as pd
import numpy as np
df = pd.read_csv('datasets_672162_1182853_dataset.csv')
print(df['Disease'].value_counts())
# Malaria and Pneumonia
df_malaria = df[df['Disease'] == 'Malaria']
df_penumonia = df[df['Disease'] == 'Pneumonia']
df_diabetes = df[df['Disease'] == 'Diabetes']
df_2_diseases = pd.concat([df_malaria, df_penumonia, df_diabetes])
#print(df_2_diseases.iloc[140,:])
unique_values = []
column_list = df_2_diseases.columns.values.tolist()
del column_list[0]
for column_name in column_list:
    unique_values.extend(df_2_diseases[column_name].unique())
unique_values = list(np.unique(unique_values))
unique_values = list(filter(lambda a: a != 'nan', unique_values))
# Features are the unique values
unique_values.append('Disease')
df = pd.DataFrame(columns = unique_values)
for a in range(0,len(df_2_diseases)):
  new_sample = []
  for b in unique_values:
    samples = list(df_2_diseases.iloc[a,:].values)
    if b in samples:
      new_sample.append(1)
    else:
      new_sample.append(0)
  new_sample[len(new_sample)-1] = samples[0]
  df_length = len(df)
  df.loc[df_length] = new_sample
df.to_csv('fe_data.csv', index=False)
