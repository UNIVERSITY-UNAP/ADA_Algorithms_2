from json import dump, load
from random import shuffle, random

arr = list(range(1,101))
shuffle(arr,random)
with open('100.json', 'w') as file:
	dump(arr,file)
arr.clear()

arr = list(range(1,1001))
shuffle(arr,random)
with open('1000.json', 'w') as file:
	dump(arr,file)
arr.clear()

arr = list(range(1,10001))
shuffle(arr,random)
with open('10000.json', 'w') as file:
	dump(arr,file)