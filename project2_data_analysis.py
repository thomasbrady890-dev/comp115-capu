import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('/home/thomasbrady890/COMP115/__pycache__/Project 2/BC Census 2016 data.csv')

# TASK 1: High Rent Burden Areas
# Finding areas where over 50% of renters spend 30%+ of income on shelter
high_burden = df[df['shelt_rent_30plus_rate'] > 50]

print("TASK 1 RESULTS")
print(f"Found {len(high_burden)} areas with high rent burden.")
print(high_burden[['chsa', 'shelt_rent_30plus_rate']])
print("\n")

# TASK 2: Regional Subsidization Comparison
regional_averages = df.groupby('pha')['shelt_rent_subsidized_rate'].mean()

print("TASK 2 RESULTS")
print("Average Subsidization Rates by Health Authority:")
print(regional_averages)

# Bar Chart
plt.figure(figsize=(10, 6))
regional_averages.sort_values().plot(kind='barh', color='teal')
plt.title('Average Shelter Subsidization Rate by BC Region (2016)')
plt.xlabel('Average Subsidization Rate (%)')
plt.ylabel('Health Authority (PHA)')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the bar chart
plt.savefig('regional_subsidies.png')
print("\nChart saved as 'regional_subsidies.png'")

# Show the bar chart on screen
plt.show()