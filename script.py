import serial


with open("bpm.csv", 'w') as b:
    with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
        try:
            while True:
                line = ser.readline()   # read a '\n' terminated line
                if line:
                    print(line)
                    data = line.decode("utf-8")
                    if len(data.split(",")) == 2:
                        b.write(data)
                        
        except KeyboardInterrupt:
            pass



        

                    