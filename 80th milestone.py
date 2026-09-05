
from abc import ABC, abstractmethod
class absclass(ABC):
    def print(self, x):
        print('Passed value: ', x)
    

    @abstractmethod
    def task(self):
        print('We are inside abs class task')
    
class krvkfkvnfknfvonviotngnigijiivfivifnv(absclass):
    def task(self):
        print('We are inside test class krvkfkvnfknfvonviotngnigijiivfivifnv')
    
obj = krvkfkvnfknfvonviotngnigijiivfivifnv()
obj.task()
obj.print(98478347384564637834728198721899287389049849384739874483478493487475647384749586595876473847273562837483945840348493948738984748394865495689506789859876784934764328365438374497890487805648834652346573467848565723484257349263483567637827466734485754837467894273862353875748965387658767285694367365)