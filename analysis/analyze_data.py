import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv(r"C:\Users\Isha Kulshrestha\Desktop\IshaAcoustics\Acoustic Shadow Effect\Data\SPL_level.csv")

# Create bar chart
plt.figure()
plt.bar(data["Material"], data[" SPL_dB"])
plt.xlabel("Material")
plt.ylabel("SPL (dB)")
plt.title("Acoustic Shadow Effect for Different Materials")

plt.show()