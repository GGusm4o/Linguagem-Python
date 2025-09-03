# Exibe um contagem regressiva

from time import sleep
for count in range(10, -1, -1):
    print(count)
    sleep(1)
print("BUM!, BUM!, POOOW!")