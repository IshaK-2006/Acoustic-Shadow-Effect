import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv(r"C:\Users\Isha Kulshrestha\Desktop\IshaAcoustics\Acoustic Shadow Effect\Data\SPL_level.csv")

# Extract Direct SPL value
direct_spl = data.loc[data["Material"] == "Direct", " SPL_dB"].values[0]

# Compute attenuation relative to Direct
data["Attenuation_dB"] = data[" SPL_dB"] - direct_spl

# Remove Direct from plot (attenuation of Direct is zero by definition)
plot_data = data[data["Material"] != "Direct"]

# Plot bar chart
plt.figure()
plt.bar(plot_data["Material"], plot_data["Attenuation_dB"])
plt.xlabel("Material")
plt.ylabel("Attenuation relative to Direct (dB)")
plt.title("Acoustic Shadow Attenuation by Material")

plt.show()
