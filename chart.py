import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic customer support response time data
np.random.seed(42)
channels = ['Email', 'Chat', 'Phone']
data = []

for ch in channels:
    times = np.random.gamma(shape=2, scale=10, size=100)  # realistic response times
    for t in times:
        data.append({'Channel': ch, 'ResponseTime': t})

df = pd.DataFrame(data)

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create figure (size in inches doesn't matter now)
fig, ax = plt.subplots()

# Create violinplot
sns.violinplot(x='Channel', y='ResponseTime', data=df, palette='Set2', ax=ax)

# Titles and labels
ax.set_title('Customer Support Response Time Distribution by Channel')
ax.set_xlabel('Support Channel')
ax.set_ylabel('Response Time (minutes)')

# Save chart as exactly 512x512 px
fig.set_size_inches(5.12, 5.12)  # size in inches
plt.savefig('chart.png', dpi=100, bbox_inches='tight')  # 5.12*100 = 512 px
plt.close()
