import pandas as pd
import csv
import plotly.express as ps

df = pd.read_csv("data_4_vis.csv")

mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

fig = ps.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")

fig.show()