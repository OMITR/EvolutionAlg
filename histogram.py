import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_csv('output/harry_potter.csv', usecols = [0]))
plt.style.use('ggplot')

fig, axs = plt.subplots(2,1)
plt.suptitle('Correlation')
plt.subplot(211)
plt.xlabel('Gens')
plt.ylabel('Count')
plt.hist(df, bins = 10)

plt.subplot(212)
plt.xlabel('Sentence')
plt.ylabel('Evos')
plt.plot(df)

fig.savefig('analys_data_test.png')
fig.show()
