from keras.models import Sequential
from keras.layers import Dense,Dropout,BatchNormalization
from memory_profiler import profile

@profile(precision=10)
def mp_ann_1(image_shape):
	model = Sequential()
	model.add(Dense(128, activation='relu', input_shape=(image_shape,)))
	model.add(Dropout(0.3))
	model.add(BatchNormalization())
	model.add(Dense(24, activation='relu'))
	model.add(Dropout(0.3))
	model.add(BatchNormalization())
	model.add(Dense(24, activation='relu'))
	model.add(Dropout(0.3))
	model.add(BatchNormalization())
	model.add(Dense(10,activation='softmax'))
