import matplotlib.pyplot as plt
import numpy as np

employees = np.array(["Tommy", "Jacob", "Yoppies", "Samia", "Valerie"])

salary = np.array([12000, 30000, 90000, 20000, 60000])

plt.plot(employees, salary, marker = "o", ms = 5, mec = "blue", color = "green")
plt.title("Employee's Salary at Oceara")
plt.xlabel("Employee Names")
plt.ylabel("Salaries")
plt.show()
