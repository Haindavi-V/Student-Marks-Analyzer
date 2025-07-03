import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('marks.csv')
print("\n📊 Average Marks:")
print(df[['Maths', 'Science', 'English']].mean())
df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)
topper = df.loc[df['Total'].idxmax()]
print(f"\n👑 Topper: {topper['Name']} with {topper['Total']} marks")
df.set_index('Name')[['Maths', 'Science', 'English']].plot(kind='bar', figsize=(10, 6))
plt.title("Student Marks Comparison")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals.png")
plt.show()