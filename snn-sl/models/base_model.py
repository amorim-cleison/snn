from tensorflow.python.keras.engine.training import Model


class BaseModel():
    def __init__(self, input_shape: tuple, num_classes: int):
        super().__init__()
        self.input_shape = input_shape
        self.num_classes = num_classes

    def build(self) -> Model:
        pass

    def name(self) -> str:
        return self.__class__.__name__

    def __str__(self):
        return self.name()

    def __repr__(self):
        return self.name()
