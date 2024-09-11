import matplotlib.pyplot as plt

countries = ['United States','India','China','Russian Federation','Japan']
populations = [334914895,1428627663,1410710000,143826130,124516650]

plt.figure(figsize=(10,5))
plt.bar(countries, populations, color='skyblue')
plt.xlabel('Countries')
plt.ylabel('Population')
plt.title('Population Distribution Of Countries (2023)')

plt.show()
