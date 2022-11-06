import matplotlib.pyplot as plt
import csv

time = []
bpm = []

with open('filtered_bpm.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		time.append(float(row[1]))
		bpm.append(float(row[2]))

plt.scatter(time, bpm, color = 'g', marker=".")
plt.xticks(rotation = 25)
plt.xlabel('Time (mms)')
plt.ylabel('Heart Rate (bpm)')
plt.title('Analyzing Health conditions, Mood, and Sleeping Patterns from Heart Beats', fontsize = 17)
plt.show()
