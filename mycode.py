import pandas as pd
import os

data={"Name":["Alice","Bob","Charlie"],
      "Age":[25,30,40],
      "City":["New York","Los Angles","Chicago"]
      

}

df=pd.DataFrame(data)

new_loc={"Name":"Manav","Age":21,"City":"Delhi"}

df.loc[len(df.index)]=new_loc

new_loc={"Name":"Ritesh","Age":21,"City":"Delhi"}

df.loc[len(df.index)]=new_loc
data_dir="data"
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,"sample_data.csv")

df.to_csv(file_path,index=False)

print(f"Csv file saved to{file_path}")