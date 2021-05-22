import pandas

df = pandas.read_csv("List_of_all_stars.csv")

df = df[df["Star_name"].notna()]
df = df[df["Distance"].notna()]
df = df[df["Mass"].notna()]
df = df[df["Radius"].notna()]

df = df.drop(["Unnamed: 0", "Unnamed: 5", "Star_name.1", "Distance.1", "Mass.1",
             "Radius.1"], axis=1)

df.to_csv("final_data.csv")
