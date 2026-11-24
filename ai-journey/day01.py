import pandas as pd

names = ["Amit", "Priya", "Rahul", "Sneha", "Vikram", "Anjali", "Rohit", "Kavya", "Arjun", "Neha"]
marks = [78, 92, 65, 88, 45, 95, 70, 81, 59, 90]

df = pd.DataFrame({"Name": names, "Marks": marks})

print(df)
print("Average:", df["Marks"].mean())
print("Topper:", df.loc[df["Marks"].idxmax(), "Name"])
print("Above average:")
print(df[df["Marks"] > df["Marks"].mean()])
