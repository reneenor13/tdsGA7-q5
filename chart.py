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
        # Email typically has longer, more variable response times
        times = np.random.lognormal(mean=2.0, sigma=0.7, size=150)
    elif channel == 'Phone':
        # Phone has immediate pickup but variable call resolution
        times = np.random.gamma(shape=3, scale=5, size=200)
    elif channel == 'Chat':
        # Chat has quick response times, mostly under 2 hours
        times = np.random.exponential(scale=1.5, size=180)
    else:  # Social Media
        # Social media has bimodal distribution - quick or very slow
        quick_responses = np.random.exponential(scale=0.5, size=80)
        slow_responses = np.random.lognormal(mean=2.5, sigma=0.5, size=70)
        times = np.concatenate([quick_responses, slow_responses])
    
    # Add channel data to list
    for time in times:
        data.append({'Support_Channel': channel, 'Response_Time_Hours': max(0.1, time)})

# Create DataFrame
df = pd.DataFrame(data)

# Set professional styling for executive presentation
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.2)

# Create figure with exact specifications
plt.figure(figsize=(8, 8))

# Create violin plot with professional styling
sns.violinplot(
    data=df,
    x='Support_Channel',
    y='Response_Time_Hours',
    palette='Set2',
    inner='quartile'
)

# Professional styling and labels
plt.title('Customer Support Response Time Distribution\nby Support Channel', 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Support Channel', fontsize=12, fontweight='semibold')
plt.ylabel('Response Time (Hours)', fontsize=12, fontweight='semibold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=0)

# Add subtle grid
plt.grid(True, alpha=0.3, axis='y')

# Ensure tight layout
plt.tight_layout()

# Save chart with exact specifications for 512x512 pixels
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

# Display summary statistics
print("Response Time Analysis Summary:")
print(df.groupby('Support_Channel')['Response_Time_Hours'].describe().round(2))

plt.show()
