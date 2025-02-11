import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic student data
first_names = ["Aarav", "Vivaan", "Aditya", "Karthik", "Rohan", "Krishna", "Aryan", "Dev", "Rajat", "Shivam",
               "Meera", "Aditi", "Pooja", "Ananya", "Sneha", "Riya", "Kavya", "Ishita", "Tanvi", "Neha"]
last_names = ["Sharma", "Verma", "Iyer", "Reddy", "Patel", "Das", "Gupta", "Chopra", "Singh", "Mehta"]
branches = ["BTech CS", "BTech Mechanical", "BTech Civil", "BTech CS (AI/ML)", "BTech DS", "BTech IT", 
            "BTech Electrical", "BTech Electronics"]

# Create a dataset with 90 students
data = []
for i in range(1, 91):
    name = random.choice(first_names) + " " + random.choice(last_names)
    branch = random.choice(branches)
    attendance_2023 = random.randint(50, 100)  # Attendance % for Jan 2023-24
    attendance_2024 = random.randint(50, 100)  # Attendance % for Jan 2024-25
    data.append([i, name, branch, attendance_2023, attendance_2024])

# Create DataFrame
df_students = pd.DataFrame(data, columns=["Student ID", "Name", "Branch", "Attendance 2023-24 Jan", "Attendance 2024-25 Jan"])

# Save the student dataset to Excel
student_file_path = "student_data.xlsx"
df_students.to_excel(student_file_path, index=False)
print(f"Student data saved to: {student_file_path}")

# Group data by branch and calculate average attendance
attendance_comparison = df_students.groupby("Branch")[["Attendance 2023-24 Jan", "Attendance 2024-25 Jan"]].mean()

# Calculate percentage change in attendance
attendance_comparison["Percentage Change"] = ((attendance_comparison["Attendance 2024-25 Jan"] -  
                                               attendance_comparison["Attendance 2023-24 Jan"]) /  
                                               attendance_comparison["Attendance 2023-24 Jan"]) * 100

# Save the attendance comparison data to Excel
comparison_file_path = "attendance_comparison.xlsx"
attendance_comparison.to_excel(comparison_file_path, index=True)
print(f"Attendance comparison data saved to: {comparison_file_path}")

# Function to create a bar chart
def plot_bar_chart(data, title, ylabel, color):
    plt.figure(figsize=(10, 5))
    plt.bar(data.index, data, color=color, edgecolor="black")
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel("BTech Branch", fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

# Plot bar graphs
plot_bar_chart(attendance_comparison["Attendance 2023-24 Jan"], 
               "Average Attendance (Jan 2023-24)", "Average Attendance %", "blue")

plot_bar_chart(attendance_comparison["Attendance 2024-25 Jan"], 
               "Average Attendance (Jan 2024-25)", "Average Attendance %", "orange")

# Plot percentage change with a reference line at 0%
plt.figure(figsize=(10, 5))
plt.bar(attendance_comparison.index, attendance_comparison["Percentage Change"], color="green", edgecolor="black")
plt.axhline(y=0, color='red', linestyle='--')  # Add reference line at 0% change
plt.title("Attendance Percentage Change (Jan 2023-24 to Jan 2024-25)", fontsize=14, fontweight="bold")
plt.xlabel("BTech Branch", fontsize=12)
plt.ylabel("Percentage Change (%)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
