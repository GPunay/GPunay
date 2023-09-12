#Trabajando con ciclo for

for variable in range(10):
    print("La variable es: ", variable)

for j in range(2, 8):
    print("j = ", j)

'''
192.168.255.0
hasta
192.168.255.255
'''

for i in range(256):
    print("192.168.255.", i)

'''
192.168.0.0
hasta 192.168.255.255
'''

print("-------------------------------------------------")
for tercerOcteto in range(255):
    for cuartoOcteto in range (255):
        print("192.168", tercerOcteto, cuartoOcteto, sep=".")    
