import serial  # pip install pyserial

ser = serial.Serial()
ser.port = '/dev/ttyUSB0'  # Replace with the required port connected
ser.baudrate = 115200  # Baudrate of connected UART input
ser.setDTR(False)
ser.setRTS(False)

ser.open()

while True:
    data = ser.readline()
    print(data)
