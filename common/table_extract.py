import pandas as pd

table_MN = pd.read_html('https://sattamatka.co.com/record/kalyan-chart.php')

print(table_MN)

# table_MN[0].to_csv("kalyan_data_.csv", index=False)
