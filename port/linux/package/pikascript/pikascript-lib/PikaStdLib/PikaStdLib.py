from PikaObj import *


class MemChecker(TinyObj):
    def max():
        pass

    def now():
        pass

    def getMax()->float:
        pass

    def getNow()->float:
        pass

    def resetMax():
        pass


class SysObj(BaseObj):
    def type(arg: any):
        pass

    def remove(argPath: str):
        pass

    def int(arg: any) -> int:
        pass

    def float(arg: any) -> float:
        pass


class List(TinyObj):
    def init():
        pass

    def append(arg: any):
        pass

    def get(i: int) -> any:
        pass

    def set(i: int, arg: any):
        pass

    def len() -> int:
        pass