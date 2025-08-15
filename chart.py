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

# Create figure (512x512 px ~ 8x8 inches at dpi=64)
plt.figure(figsize=(8, 8))
sns.violinplot(x='Channel', y='ResponseTime', data=df, palette='Set2')

plt.title('Customer Support Response Time Distribution by Channel')
plt.xlabel('Support Channel')
plt.ylabel('Response Time (minutes)')

# Save as chart.png with exact size
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.close()
