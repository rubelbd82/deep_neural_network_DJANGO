import tensorflow as tf, keras
from keras import backend as K
from keras.models import load_model
import tensorflow_hub as hub
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"




class KerasModel(object):
    gModelObjs = dict()

    @staticmethod
    def load_model_from_path(path):
        graph = tf.get_default_graph()
        model = load_model(path)
        model._make_predict_function()

        # model = tf.keras.models.load_model(path)

        # model = tf.saved_model.load(str(path), None)
        # model = tf.compat.v2.saved_model.load(str(path), None)
        #### model.summary()
        return graph, model

    @staticmethod
    def load_all_models():
        KerasModel.gModelObjs = {
            'model_1': KerasModel.load_model_from_path('/home/asus-pc/workspace/jyu/deeplearning/notebooks/deep_neural_network/models/fer2013_set_adam_50_model.h5'),
        }


KerasModel.load_all_models()


# @staticmethod
# def load_all_models():
#     KerasModel.gModelObjs = {
#         'model_1': KerasModel.load_model_from_path(
#             '/home/asus-pc/workspace/jyu/deeplearning/notebooks/deep_neural_network/models/retrained_model_new.h5'),
#     }
