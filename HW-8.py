#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


# 1.Загрузите датасет с помощью функции np.genfromtxt()


# In[5]:


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')


# In[56]:


iris[:5]


# In[7]:


iris.shape


# In[8]:


# 2.Вычислите простейшие статистики: min, max, median, mean, 0,25-percentile, 0,75-percentile
#- для каждого из числовых атрибутов в датасете(через цикл)


# In[19]:


data = np.genfromtxt(url, delimiter=',', dtype='float')
atr_1 = data[:,[0]]
atr_2 = data[:,[1]]
atr_3 = data[:,[2]]
atr_4 = data[:,[3]]
atr_5 = np.genfromtxt(url, delimiter=',', dtype='str', usecols=[4])


# In[36]:


massiv = [atr_1, atr_2, atr_3, atr_4]
a = np.array(massiv)


# In[ ]:


#Что-то похожее на данный пример
#for i in range(4):
   # print(f'Гистограмма для атрибута {i}')
#Через f можно передать параметр


# In[55]:


for val in a:
    print('\nПростейшие статистики для атрибутов')
    print('Максимум =',np.max(val))
    print('Минимум =',np.min(val))
    print('Медиана для =', np.median(val))
    print('Персентиль 0,25=',np.percentile(val, 25))
    print('Персентиль 0,75 =',np.percentile(val, 75))  


# In[ ]:


# 3. Постройте гистограмму для каждого из числовых атрибутов в датасете


# In[25]:


import matplotlib.pyplot as plt


# In[ ]:


for val in a:


# In[46]:


for val in a:
    plt.hist(val)
    plt.title('')
    plt.show()


# In[ ]:


# 4. Сгруппируйте датасет по категории (последний столбец датасета) и повторите
#шаги 2 и 3 для групп.


# In[57]:


atr_5


# In[59]:


np.unique(atr_5)


# In[61]:


new_1 = []
for group_val in np.unique(atr_5):
       new_1.append(atr_1[atr_5==group_val].mean())
new_1


# In[64]:


new_2 = []
for group_val in np.unique(atr_5):
       new_2.append(atr_2[atr_5==group_val].mean())
new_2


# In[69]:


new_3 = []
for group_val in np.unique(atr_5):
       new_3.append(atr_3[atr_5==group_val].mean())
new_3


# In[70]:


new_4 = []
for group_val in np.unique(atr_5):
       new_4.append(atr_4[atr_5==group_val].mean())
new_4


# In[78]:


massiv = [new_1, new_2, new_3, new_4]
b = np.arrey=(massiv)


# In[80]:


for val in b:
    plt.hist(val)
    plt.title('')
    plt.show()
    print('\nПростейшие статистики для атрибутов')
    print('Максимум =',np.max(val))
    print('Минимум =',np.min(val))
    print('Медиана для =', np.median(val))
    print('Персентиль 0,25=',np.percentile(val, 25))
    print('Персентиль 0,75 =',np.percentile(val, 75)) 


# In[ ]:




