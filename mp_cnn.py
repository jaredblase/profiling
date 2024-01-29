from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Dense,Flatten,Dropout
from memory_profiler import profile

@profile(precision=10)
def mp_cnn_1(image_shape):
	model = Sequential()
	model.add(Conv2D(32, kernel_size=3, activation='relu', input_shape=image_shape, name='Conv2D-1'))
	model.add(MaxPooling2D(pool_size=2, name='MaxPool'))
	model.add(Dropout(0.2, name='Dropout'))
	model.add(Flatten(name='flatten'))
	model.add(Dense(32, activation='relu', name='Dense'))
	model.add(Dense(10, activation='softmax', name='Output'))

@profile(precision=10)
def mp_cnn_2(image_shape):
	model = Sequential()
	model.add(Conv2D(32, kernel_size=3, activation='relu', input_shape=image_shape, name='Conv2D-1'))
	model.add(MaxPooling2D(pool_size=2, name='MaxPool'))
	model.add(Dropout(0.2, name='Dropout-1'))
	model.add(Conv2D(64, kernel_size=3, activation='relu', name='Conv2D-2'))
	model.add(Dropout(0.25, name='Dropout-2'))
	model.add(Flatten(name='flatten'))
	model.add(Dense(64, activation='relu', name='Dense'))
	model.add(Dense(10, activation='softmax', name='Output'))

@profile(precision=10)
def mp_cnn_3(image_shape):
	model = Sequential()
	model.add(Conv2D(32, kernel_size=3, activation='relu', input_shape=image_shape, kernel_initializer='he_normal', name='Conv2D-1'))
	model.add(MaxPooling2D(pool_size=2, name='MaxPool'))
	model.add(Dropout(0.25, name='Dropout-1'))
	model.add(Conv2D(64, kernel_size=3, activation='relu', name='Conv2D-2'))
	model.add(Dropout(0.25, name='Dropout-2'))
	model.add(Conv2D(128, kernel_size=3, activation='relu', name='Conv2D-3'))
	model.add(Dropout(0.4, name='Dropout-3'))
	model.add(Flatten(name='flatten'))
	model.add(Dense(128, activation='relu', name='Dense'))
	model.add(Dropout(0.4, name='Dropout'))
	model.add(Dense(10, activation='softmax', name='Output'))
