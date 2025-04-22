import pandas as pd
import os

#create a sample dataframe with column names
data = {'Name':['Alice','Bob','Charlie'],
        'Age': [25, 28, 30],
        'City': ['New york', 'Los Angeles','Chicago']}

df = pd.DataFrame(data)

#Ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

#Save the Dataframe to CSV file, including column names
df.to_csv(file_path, index=False)
print(f"CSV file saved to {file_path}")