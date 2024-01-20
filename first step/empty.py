import time
print('Hi')

# for i in range(99):
#     print(i ** 3)

name = 'AhunovTIMUR'

for i in name:
    print(i, end='')
    print('', end='\r')
    time.sleep(.5)
