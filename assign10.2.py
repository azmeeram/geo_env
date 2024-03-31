import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# File paths and labels
file_paths = [
    r"C:\Users\AZMEERAM\Documents\GitHub\CWatM-main\CWatM-main\Tutorials\11_SensitivityAnalysis_Climate\output8\runoff_areaavg_daily.tss",
    r"C:\Users\AZMEERAM\Documents\GitHub\CWatM-main\CWatM-main\Tutorials\11_SensitivityAnalysis_Climate\output2\runoff_areaavg_daily.tss",
    r"C:\Users\AZMEERAM\Documents\GitHub\CWatM-main\CWatM-main\Tutorials\11_SensitivityAnalysis_Climate\output7\runoff_areaavg_daily.tss"
]

labels = [
    "TempSnow 0.97",
    "TempSnow 1.03"
]

# Load baseline data
baseline_data = np.loadtxt(file_paths[1], skiprows=7)

# Initialize lists to store sensitivity analysis data
sensitivity_data = []

# Perform sensitivity analysis
for i, file_path in enumerate(file_paths):
    # Skip baseline file
    if i == 1:
        continue
    # Load data skipping the first few rows
    data = np.loadtxt(file_path, skiprows=7)
    # Subtract baseline from current data
    sensitivity = data[:, 1] - baseline_data[:, 1]
    sensitivity_data.append(sensitivity)

# Define start and end dates
start_date = datetime(1990, 1, 1)
end_date = datetime(1996, 12, 31)

# Generate dates for x-axis ticks
dates = [start_date + timedelta(days=int(data_point[0])-1) for data_point in baseline_data]

# Plot the sensitivity analysis
plt.figure(figsize=(12, 6))

for i, sensitivity in enumerate(sensitivity_data):
    if i == 0:
        plt.plot(dates, sensitivity, label=labels[i], color='tab:red', linewidth=1.5)
    else:
        plt.plot(dates, sensitivity, label=labels[i], color='tab:green', linewidth=1.5)

plt.title('Model Sensitivity to TempSnow and its Impact on Runoff', fontsize=16)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Sensitivity (Difference from Baseline) [degrees C]', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('tempSnow_Sensitivity.png', dpi=300)
plt.show()


