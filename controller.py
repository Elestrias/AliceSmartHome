import serial
qte = input().split()
if len(qte) > 4:
    qte = qte[:4]
elif len(qte) < 4:
    while len(qte) < 4:
        qte.append('0')
    qte[-1] = '13'
qte[0] = '0'
ser = serial.Serial('COM3', 9600)
s = ser.read(100)


for i in range(len(qte)):
    ser.write(int(qte[i]))


