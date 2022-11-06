import serial

count = 0

with open("bpm.csv", 'w') as b:
    with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
        try:
            while count < 100:
                line = ser.readline()   # read a '\n' terminated line
                if line:
                    print(line)
                    data = line.decode("utf-8")
                    if len(data.split(",")) == 2:
                        b.write(data)
                count += 1
        except KeyboardInterrupt:
            pass



        

                    