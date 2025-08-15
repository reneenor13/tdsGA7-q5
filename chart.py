import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducible data
np.random.seed(42)

# Generate synthetic customer support response time data
n_samples = 300

# Create realistic response time distributions for different channels (in minutes)
email_times = np.random.lognormal(mean=2.5, sigma=0.8, size=n_samples//3)
phone_times = np.random.lognormal(mean=1.8, sigma=0.6, size=n_samples//3)
chat_times = np.random.lognormal(mean=1.2, sigma=0.5, size=n_samples//3)

# Create DataFrame
data = pd.DataFrame({
    'Channel': ['Email'] * (n_samples//3) + ['Phone'] * (n_samples//3) + ['Chat'] * (n_samples//3),
    'Response_Time_Minutes': np.concatenate([email_times, phone_times, chat_times])
})

# Set up the plot style and context
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.1)

# Create figure with fixed size for exact 512x512 pixels
fig = plt.figure(figsize=(8, 8), dpi=64)

# Create violinplot
sns.violinplot(data=data, x='Channel', y='Response_Time_Minutes',
               palette=['#2E86AB', '#A23B72', '#F18F01'],
               inner='box')

# Customize the plot
plt.title('Customer Support Response Time Distribution\nby Support Channel',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Support Channel', fontsize=14, fontweight='semibold')
plt.ylabel('Response Time (Minutes)', fontsize=14, fontweight='semibold')

# Improve tick labels
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Save without bbox_inches to avoid size changes
plt.savefig('chart.png', dpi=64)

# Display the plot
plt.show()
