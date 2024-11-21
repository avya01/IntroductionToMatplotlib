import matplotlib.pyplot as plt
import numpy as np

employees = np.array(["Tommy", "Jacob", "Yoppies", "Samia", "Valerie"])

salary = np.array([12000, 30000, 90000, 20000, 60000])

plt.bar(employees, salary, color = "blue")
plt.title("Employee's Salary at Oceara")
plt.xlabel("Employee Names")
plt.ylabel("Salaries")
plt.show()
