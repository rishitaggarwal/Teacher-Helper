import pandas as pd
import csv
import plotly.graph_objects as px

df = pd.read_csv("data.csv")

studentdf = df.loc[df["student_id"]=="TRL_rst"]
print(studentdf.groupby("level")["attempt"].mean())

fig = px.Figure(px.Bar(x = studentdf.groupby("level")["attempt"].mean(),
y = ["Level 1","Level 2","Level 3", "Level 4"],
orientation = "h"))


fig.show()