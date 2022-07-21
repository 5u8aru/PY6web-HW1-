from abc import ABC, abstractmethod
import json


class SerializationInterface(ABC):
    @abstractmethod
    def writing(self, file, data):
        ...

    @abstractmethod
    def reading(self, file):
        ...


class SerializeJson(SerializationInterface):
    def writing(self, file, data):
        with open(file, 'w') as file:
            json.dump(data, file)

    def reading(self, file):
        with open(file, 'r') as file:
            return json.load(file)


class SerializeBin(SerializationInterface):
    def writing(self, file, data):
        with open(file, 'w') as file:
            file.write(data)

    def reading(self, file_name):
        with open(file_name, 'r') as file:
            return file.read()


if __name__ == '__main__':
    ...