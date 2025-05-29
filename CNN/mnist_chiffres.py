import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Chargement des données
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. Prétraitement
X_train = X_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
X_test = X_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

# 3. Création du modèle CNN
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),  # Pour éviter l'overfitting
    tf.keras.layers.Dense(10, activation='softmax')  # 10 classes de 0 à 9
])

# 4. Compilation du modèle
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 5. Entraînement
history = model.fit(X_train, y_train, epochs=5, batch_size=128, validation_split=0.1)

# 6. Évaluation
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"\nTest accuracy: {test_acc*100:.2f}%")

# 7. Prédictions
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# 8. Rapport de classification
print("\nClassification Report :")
print(classification_report(y_test, y_pred_classes))

# 9. Matrice de confusion
conf_mat = confusion_matrix(y_test, y_pred_classes)
plt.figure(figsize=(8,6))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
plt.title("Matrice de Confusion - MNIST CNN")
plt.xlabel("Prédiction")
plt.ylabel("Vérité")
plt.show()

# 10. Courbe de perte
plt.plot(history.history['loss'], label='Train loss')
plt.plot(history.history['val_loss'], label='Val loss')
plt.xlabel('Épochs')
plt.ylabel('Loss')
plt.legend()
plt.title('Courbe de perte')
plt.show()
