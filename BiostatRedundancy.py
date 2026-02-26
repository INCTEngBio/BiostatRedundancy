import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2_contingency

# 1. Data extracted from research results
biomes = ['Amazon', 'Atlantic\nForest', 'Caatinga', 'Cerrado', 'Pantanal', 'Pampa']
copies = np.array([98, 292, 259, 251, 251, 1313])
exemplars = np.array([91, 273, 235, 225, 230, 1112])
retained_80 = np.array([91, 82, 57, 69, 59, 148])

# 2. STATISTICAL ANALYSIS (Chi-square test on retention rate)
# Comparing Retained vs Discarded (Exemplars - Retained)
discarded = exemplars - retained_80
contingency_table = np.array([retained_80, discarded]).T
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Print results to the terminal
print("="*60)
print("STATISTICAL ANALYSIS RESULTS (Redundancy by Biome)")
print("="*60)
print(f"Chi-square statistic: {chi2:.2f}")
print(f"p-value: {p_value:.2e}")
if p_value < 0.05:
    print("Conclusion: The retention rate is SIGNIFICANTLY dependent on the biome (p < 0.05).")
else:
    print("Conclusion: No significant difference in retention rate between biomes.")
print("="*60)

# 3. Plot configuration
x = np.arange(len(biomes))  # Label locations
width = 0.25                # Width of the bars

fig, ax = plt.subplots(figsize=(14, 8))

# Create grouped bars
bar1 = ax.bar(x - width, copies, width, label='Initial Copies', color='#d9d9d9', edgecolor='black')
bar2 = ax.bar(x, exemplars, width, label='Exemplars', color='#a6a6a6', edgecolor='black')
bar3 = ax.bar(x + width, retained_80, width, label='Retained (80% Threshold)', color='#d62728', edgecolor='black')

# Add text annotations on top of each bar
def autolabel(rects):
    """Attach a text label above each bar displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', 
                    fontsize=13)

autolabel(bar1)
autolabel(bar2)
autolabel(bar3)

# 4. Axis formatting and labels
ax.set_ylabel('Number of Sequences', fontsize=16, fontweight='bold')

# Increasing Y-axis tick label size
ax.tick_params(axis='y', labelsize=14) 

# Formatting the p-value for the title
if p_value < 0.0001:
    p_text = "p < 0.0001"
else:
    p_text = f"p = {p_value:.4f}"

# Adding statistics to the chart title
ax.set_title(f'Impact of the 80% Redundancy Threshold by Biome\n($\chi^2$ = {chi2:.2f}; {p_text})', 
             fontsize=16, fontweight='bold', pad=20)

ax.set_xticks(x)
ax.set_xticklabels(biomes, fontsize=14)

# Configure legend
ax.legend(fontsize=14, loc='upper left')

# Hide top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 5. Save and display the plot
plt.tight_layout()
plt.savefig('redundancy_threshold_with_stats.png', dpi=300, bbox_inches='tight')
print("\nChart generated and saved as 'redundancy_threshold_with_stats.png'!")
plt.show()