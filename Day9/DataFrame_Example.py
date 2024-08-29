import pandas as pd
data={
    "Name": ["Alma","Blerta","Dhurata"],
    "Age":[25,35,22],
    "City":["New York","San Francisco","San Francisco"],
}

df_people=pd.DataFrame(data)
print(df_people)