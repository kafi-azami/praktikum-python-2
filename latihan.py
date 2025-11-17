import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')
print(data.info())
print(data.head())
print(data.describe())

#print("Rata-rata:", data.gr['Nilai'].mean())
#print("Rata-rata:", data.gr['Nilai'].mean())
#print("Modus:", data['Nilai'].mode()[0])

Matematika = data[data['Matpel'] == 'Matematika']
print(Matematika)

data.groupby('Matpel')['Nilai'].agg(['max','min'])

rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()