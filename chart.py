import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducible results
np.random.seed(42)

# Generate synthetic customer support response time data
def generate_support_data():
    channels = ['Email', 'Phone', 'Chat', 'Social Media']
    data = []
    
    # Generate realistic response times for each channel
    for channel in channels:
        if channel == 'Email':
            # Email typically has longer response times
            times = np.random.lognormal(mean=2.5, sigma=0.8, size=200)
        elif channel == 'Phone':
            # Phone has immediate response but variable resolution time
            times = np.random.gamma(shape=2, scale=15, size=180)
        elif channel == 'Chat':
            # Chat has quick response times
            times = np.random.exponential(scale=8, size=220)
        else:  # Social Media
            # Social media has varied response times
            times = np.concatenate([
                np.random.exponential(scale=5, size=80),  # Quick responses
                np.random.lognormal(mean=3, sigma=0.5, size=70)  # Slower responses
            ])
        
        # Add channel data to list
        for time in times:
            data.append({'Channel': channel, 'Response_Time_Hours': max(0.1, time)})
    
    return pd.DataFrame(data)

# Generate the dataset
df = generate_support_data()

# Set up the plot style for professional presentation
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.1)

# Create figure with specified size for 512x512 output
plt.figure(figsize=(8, 8))

# Create violin plot
ax = sns.violinplot(
    data=df, 
    x='Channel', 
    y='Response_Time_Hours',
    palette='viridis',
    inner='quart'
)

# Customize the plot
plt.title('Customer Support Response Time Distribution\nby Support Channel', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Support Channel', fontsize=14, fontweight='semibold')
plt.ylabel('Response Time (Hours)', fontsize=14, fontweight='semibold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the chart with exact specifications
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

# Display the plot
plt.show()

# Print summary statistics
print("Summary Statistics by Channel:")
print(df.groupby('Channel')['Response_Time_Hours'].describe().round(2))
