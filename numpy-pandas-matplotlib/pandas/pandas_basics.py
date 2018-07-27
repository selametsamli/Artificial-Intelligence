import pandas as pd

dictionary = {"Name":['Ali','veli','fikret','selamet','hasan','hayri'],
              'Age':[1,2,3,4,5,6],
              'Maas':[100,200,300,400,500,600] }

dataFrame1 = pd.DataFrame(dictionary)


head = dataFrame1.head() #ilk 5 değerleri gösterir.
print(head)

print("--------------------")
tail = dataFrame1.tail()#son 5 değeri gösterir

print (tail)

