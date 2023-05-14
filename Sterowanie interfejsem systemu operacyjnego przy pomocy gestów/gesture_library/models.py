from keras.models import load_model


class ModelFactory:

    def __init__(self, absolute_path):
        self.rgbpath = absolute_path + '/trained_models/rgblstm.h5'

    def getModel(self):
        return load_model(self.rgbpath)