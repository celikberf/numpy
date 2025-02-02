import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
result = numbers[-1]
result = numbers[:3] #0dan 2. indexe kadar yazdırır
result = numbers[3:] #3.indextetn sona kadar yazdırır
result = numbers[::] #tüm listeyi yazdırır
result = numbers[::-1]  # listeyi ters yazdırır  birer birer
result = numbers[::-2]  # listeyi ters yazdırır ikişer ikişer

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numbers2[0]
result = numbers2[2]
result = numbers2[0,2] #1.satırın 2.indexindeki eleman
result = numbers2[2,1] #3.satırın 1. indexindeki eleman
result = numbers2[:,2] #birden fazla satırdan belirli elemanları getirir. # [10-25-85]
result = numbers2[:,0:2] #seçmiş olduğumuz her satır içerisinden 0  ile 1. indexleri  al
result = numbers2[-1,:] #son satırdaki tüm sütunları alır
result = numbers2[:2,:2] # 2 satırdan 2 sütun

# print(result)

arr1 = np.arange(0,10)
#arr2 = arr1 # referance copy
arr2 = arr1.copy()

arr2[0] = 20

print(arr1)
print(arr2)
