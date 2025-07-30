import tensorflow as tf
from tensorflow.keras import layer, models
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

model = models.Sequential([
    layers.Flatten(input_shape='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.complete(optimizer='adam',
               loss='spare_categoricl_crossentropy',
               matrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

prediction = model.predict(x_test)

plt.imshow(x_test[0], cmap.cm.binary)
plt.title(f"Predicted: {prediction[0].argmax()}")
plt.show()

