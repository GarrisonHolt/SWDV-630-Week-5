from logging import exception


class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise exception("This is a singleton class.")
        else:
            Singleton.__instance = self

