# chart.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------
# 1. Generate synthetic data
# ----------------------------
np.random.seed(42)  # for reproducibility

# Example channels
channels = ['Email', 'Phone', 'Chat']

# Generate random response times (in minutes)
data = {
    'Channel': np.repeat(channels, 100),
    'ResponseTime': np.concatenate([
        np.random.normal(loc=30, scale=5, size=100),  # Email
        np.random.normal(loc=15, scale=3, size=100),  # Phone
        np.random.normal(loc=10, scale=2, size=100)   # Chat
    ])
}

df = pd.DataFrame(data)

# ----------------------------
# 2. Create the violinplot
# ----------------------------
sns.set_style('whitegrid')
plt.figure(figsize=(8, 8))  # ensures 512x512 when saved with dpi=64

palette = sns.color_palette("Set2")

ax = sns.violinplot(x='Channel', y='ResponseTime', data=df, palette=palette)
ax.set_title('Customer Support Response Times by Channel', fontsize=14)
ax.set_xlabel('Support Channel', fontsize=12)
ax.set_ylabel('Response Time (minutes)', fontsize=12)

# ----------------------------
# 3. Save the figure
# ----------------------------
plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.show()

