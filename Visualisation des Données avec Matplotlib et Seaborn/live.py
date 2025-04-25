import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")

# sns.histplot(df['total_bill'])
# plt.title("Histogramme avec seaborn sur le total_bill")
# plt.show()

# sns.boxplot(x="sex", y="tip", data=df)
# plt.title("Boxplot des pourboir (tip) par sexe")
# plt.show()

correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Heatmap des correlations entre variables numeriques")
plt.show()