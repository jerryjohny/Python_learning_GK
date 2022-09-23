from ast import Num


class ElectronicDevice(ABC):
    def __init__(imei: int):
        self.imei = imei