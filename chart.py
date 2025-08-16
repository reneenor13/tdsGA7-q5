import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducible results
np.random.seed(42)

# Generate synthetic customer support response time data
channels = ['Email', 'Phone', 'Chat', 'Social Media']
data = []

# Generate realistic response times for each channel
for channel in channels:
    if channel == 'Email':
        times = np.random.lognormal(mean=2.0, sigma=0.7, size=150)
    elif channel == 'Phone':
        times = np.random.gamma(shape=3, scale=5, size=200)
    elif channel == 'Chat':
        times = np.random.exponential(scale=1.5, size=180)
    else:  # Social Media
        quick_responses = np.random.exponential(scale=0.5, size=80)
        slow_responses = np.random.lognormal(mean=2.5, sigma=0.5, size=70)
        times = np.concatenate([quick_responses, slow_responses])
    
    for time in times:
        data.append({'Support_Channel': channel, 'Response_Time_Hours': max(0.1, time)})

# Create DataFrame
df = pd.DataFrame(data)

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.0)

# Create figure with EXACT 512x512 pixel specifications
plt.figure(figsize=(5.12, 5.12), dpi=100)

# Create violin plot
sns.violinplot(
    data=df,
    x='Support_Channel',
    y='Response_Time_Hours',
    palette='Set2',
    inner='quartile'
)

# Styling
plt.title('Customer Support Response Time Distribution\nby Support Channel', 
          fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Support Channel', fontsize=10, fontweight='semibold')
plt.ylabel('Response Time (Hours)', fontsize=10, fontweight='semibold')

# Add grid
plt.grid(True, alpha=0.3, axis='y')

# Save with EXACT 512x512 dimensions - NO bbox_inches='tight'!
plt.savefig('chart.png', dpi=100)

print("Chart saved as exactly 512x512 pixels")
plt.show()
