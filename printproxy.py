import time 
from abc import *
from asyncio.windows_events import NULL

class Printable(metaclass = ABCMeta):
    def __init__(self):
        self.name = ""
    @abstractmethod
    def setPrintName(self):
        pass
    @abstractmethod
    def getPrintName(self):
        pass
    @abstractmethod
    def printText(self):
        pass
    
class Printer(Printable):
    def __init__(self,name):
        self.name = name
        self.heavyJob("printer의 인스턴스: "+self.name+" 생성 중")
    def setPrintName(self, name):
        self.name = name
    def getPrintName(self):
        return self.name
    def printText(self, msg):
        print("===" + self.name + "===", end= ": ")
        print(msg)
    def heavyJob(self,msg):
        print(msg)
        time.sleep(5)
        print("완료")    
        
class PrinterProxy(Printable):
    def __init__(self, name):
        self.name = name
        self.real = NULL
    def realize(self):
        if self.real == NULL:
            self.real = Printer(self.name)
    def setPrintName(self, name):
        if self.real != NULL:
            self.real.setPrintName(name)
        self.name = name
    def getPrintName(self):
        return self.name
    def printText(self, msg):
        self.realize()
        self.real.printText(msg)
        
p = PrinterProxy("보스토크")
print("현재이름은" + p.getPrintName() + "입니다.")
p.setPrintName("머큐리")
print("현재이름은" + p.getPrintName() + "입니다.")
p.printText("hello")
p.printText("hear me?")

p.setPrintName("아폴로")
print("현재이름은" + p.getPrintName() + "입니다.")
p.printText("arrived the moon")