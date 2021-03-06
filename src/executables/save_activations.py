from src.pre_processing.read_data import Data
from src.processing.model_architecture import ModelArchitecture
from src.processing.tools import Tools
from keras.models import Model

# img = image_preprocess_tri("/home/gsasikiran/Desktop/Semester_3/SDP/Monitoring-Neuron-Activations/triangles/drawing(1).png")

TRAIN_PATH = "../../MNIST_data/train.csv"
TEST_PATH = "../../MNIST_data/test.csv"
MNIST_data = Data(TRAIN_PATH, TEST_PATH)

X_train, y_train = MNIST_data.get_data()
X_train_images = MNIST_data.df_to_images(X_train)

model_architecture = ModelArchitecture()
model_cnn = model_architecture.CNN()

tools = Tools()
conv_layer_list = tools.get_conv_layers(model_cnn)

outputs = [model_cnn.layers[i].output for i in conv_layer_list]
model = Model(inputs=model_cnn.inputs, outputs=outputs)
