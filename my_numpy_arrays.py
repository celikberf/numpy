import numpy as np

#result = np.array([1,3,5,7,9])
#result = np.arange(1,10) # 1 den 10 a oto verdi
#result = np.arange(10,100,3) # 10la 100 arası 3 adım atarak 
#result = np.zeros(10) # 10 tane 0 verir
#result = np.ones(10) # 10 tane 1  verir
#result = np.linspace(0,100,5) #0 dan 100 e 5 eşit parçaya bölsün
#result = np.linspace(0,5,5) # 0dan 5 e kadar gir 5 eşit parçaya böl
#result = np.random.randint(0,10) # 0-9 arası random sayı üretir
#result = np.random.randint(20) # 0 dan 20 ye
#result = np.random.randint(1,10,3) # 1 le 10 arasıında 3 sayı üret
#result = np.random.rand(5) #0 la 1 arasında 5 sayı üret
#result = np.random.randn(5) #0la 1 arasında eksilerrde dahil 5 sayı üret
"""
np_array = np.arange(50)
np_multi = np_array.reshape(5,10) #5 e 10luk  bir matris oluşturur
print(np_multi.sum(axis=1))#matristeki satırların toplamı
print(np_multi.sum(axis=0)) #matristeki sütunların ttoplamı

"""

rnd_numbers = np.random.randint(1,100,10)
result = rnd_numbers.max() # üretilen sayıların içinde en büyüğü
result = rnd_numbers.min() # üretilen sayıların içinde en küçüğü
result = rnd_numbers.mean() # üretilen sayıların ortalaması
result = rnd_numbers.argmax() # üretilen sayıların en büyüğünün indexi
result = rnd_numbers.argmin() # üretilen sayıların en küçüğünün indexi


print(rnd_numbers)
print(result)