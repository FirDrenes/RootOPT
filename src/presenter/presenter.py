from abc import ABC, abstractmethod


class Presenter(ABC):
    @staticmethod
    @abstractmethod
    def convert_obj_to_repr(obj):
        pass

    @staticmethod
    @abstractmethod
    def convert_repr_to_obj(present):
        pass
