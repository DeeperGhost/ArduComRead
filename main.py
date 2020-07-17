import serial
import datetime
import os
import platform


class ArduComRead:
    # Путь для сохранения истории
    # __pathSaveData = ""
    # Файл с последним значением данных
    # __indicatorNow = ""
    # комп порт текущей ОС
    # __comport = ""
    # словарь ком портов различных ОС
    __os_switch_com = {"Linux": "/dev/ttyACM0",
                       "Windows": "COM3",
                       "Darwin": "/dev/tty.tty0"} #надо проверять работоспособность неизвестна

    def __init__(self,pathSaveData="/data", indicatorFileNow=""):
        self.__comport = self.__os_switch_com[platform.system()]
        self.__pathSaveData = pathSaveData

        # если нет выделенного пути то сохранять рядом с общей базой
        if indicatorFileNow == "":
            self.__indicatorNow = os.path.abspath(os.curdir) + pathSaveData + "/indicators.i"
        else:
            self.__indicatorNow = indicatorFileNow


    def __save_data(self,h,t):
    #Сохраняет прочитаные данные в файлы
        dt = datetime.datetime.now()

        f = open(self.__pathSaveData + dt.strftime("%Y-%m-%d") + '.csv', 'a')
        f.write(str(h)+";"+str(t)+";"+str(dt)+"\n")
        f.close()

        f = open(self.__indicatorNow,'w')
        f.write(str(h) + ";" + str(t) + ";" + str(dt) + "\n")
        f.close()


    def on(self):
        # читает данные из ком порта и записывает в файлы
        try:
            port = serial.Serial(self.__comport,9600)
            while 1:
                buf = str(port.readline())
                self.__save_data(h=int(buf[3:5]), t=int(buf[7:9]))
                print(buf[2:9])
            port.close()

        except serial.SerialException:
            print('Соединение не удалось')
            exit(1)



if __name__ == "__main__":
    t = ArduComRead(indicatorFileNow="C:/Users/007/PycharmProjects/FlaskServTest/data/indicators.i")
    t.on()



