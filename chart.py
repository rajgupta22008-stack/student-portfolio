import matplotlib.pyplot as plt

subjects = ["Python", "HTML", "Git", "ML"]
marks = [85, 90, 80, 88]

plt.bar(subjects, marks)

plt.title("Student Skills")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.savefig("chart.png")
plt.show()
