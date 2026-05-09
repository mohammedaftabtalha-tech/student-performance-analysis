import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file = pd.read_csv("data.csv")

# Calculate average marks
file["Average"] = (
    file["Math"] +
    file["Science"] +
    file["English"]
) / 3

# Top performer
highest = file.loc[file["Average"].idxmax()]

print("===== STUDENT PERFORMANCE ANALYSIS =====")
print()

print("Average Marks of Students:")
print(file[["Name", "Average"]])
print()

print("Top Performer:")
print(highest["Name"])
print("Average Marks:", round(highest["Average"], 2))
print()

# Overall class average
class_average = file["Average"].mean()
print("Class Average:", round(class_average, 2))

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(file["Name"], file["Average"])
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
# Save chart
plt.savefig("output_chart.png")

plt.show()

print()
print("Chart saved as output_chart.png")