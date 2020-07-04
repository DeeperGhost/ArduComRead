import serial
import datetime

def addData(h,t):
    dt = datetime.datetime.now()

    f = open("data/" + dt.strftime("%Y-%m-%d") + '.csv', 'a')
    f.write(str(h)+";"+str(t)+";"+str(dt)+"\n")
    f.close()

    # f = open("C:/Users/007/PycharmProjects/FlaskServTest/data/indicators.i",'w')
    # f.write(str(h) + ";" + str(t) + ";" + str(dt) + "\n")
    # f.close()

def ON():
    # comport = 'COM3' # for win
    comport = '/dev/ttyACM0'
    try:
        port = serial.Serial(comport,9600)
        while 1:
            buf = str(port.readline())
            addData(h=int(buf[3:5]), t=int(buf[7:9]))
            print(buf[2:9])
        port.close()

    except serial.SerialException:
        print('Соединение не удалось')
        exit(1)

def main():
    ON()


if __name__ == "__main__":
    main()
