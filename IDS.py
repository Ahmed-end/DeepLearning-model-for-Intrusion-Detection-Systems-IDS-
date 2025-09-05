import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import joblib


df = pd.read_csv("train.csv")


target_col = "class"
y = df[target_col]
X = df.drop(columns=[target_col])


le = LabelEncoder()
y_encoded = le.fit_transform(y)


class_counts = pd.Series(y_encoded).value_counts()
rare_classes = class_counts[class_counts < 2].index

mask = ~pd.Series(y_encoded).isin(rare_classes)
X = X[mask]
y_encoded = y_encoded[mask]

print(f"Removed {len(rare_classes)} rare classes. Remaining classes: {np.unique(y_encoded)}")


X_train, X_val, y_train, y_val = train_test_split(
    X, y_encoded, test_size=0.2, stratify=y_encoded, random_state=42
)


num_cols = [c for c in X.columns if np.issubdtype(X[c].dtype, np.number)]
cat_cols = [c for c in X.columns if c not in num_cols]

num_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))  # FIXED
])

pre = ColumnTransformer([
    ("num", num_pipe, num_cols),
    ("cat", cat_pipe, cat_cols)
])

# Fit-transform
X_train_proc = pre.fit_transform(X_train)
X_val_proc = pre.transform(X_val)

input_dim = X_train_proc.shape[1]
num_classes = len(np.unique(y_encoded))


model = keras.Sequential([
    layers.Input(shape=(input_dim,)),
    layers.Dense(256, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(64, activation="relu"),
])

if num_classes == 2:
    # Binary classification
    model.add(layers.Dense(1, activation="sigmoid"))
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
else:
    # Multi-class classification
    model.add(layers.Dense(num_classes, activation="softmax"))
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])


es = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True, monitor="val_loss")

history = model.fit(
    X_train_proc, y_train,
    validation_data=(X_val_proc, y_val),
    epochs=100,
    batch_size=64,
    callbacks=[es],
    verbose=1
)


loss, acc = model.evaluate(X_val_proc, y_val, verbose=0)
print(f"Validation Accuracy: {acc:.4f}")

model.save("dl_model.keras")

joblib.dump(pre, "preprocessor.joblib")
joblib.dump(le, "label_encoder.joblib")
