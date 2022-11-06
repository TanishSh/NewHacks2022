import pandas

window_size = 10
data = pandas.read_csv("bpm.csv")
filtered_data = data.rolling(window_size).median().dropna()
print(filtered_data)
filtered_data.to_csv('filtered_bpm.csv')
