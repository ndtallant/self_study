import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# For examples
import tensorflow_datasets as tfds

dataset, info = tfds.load(
    'imdb_reviews/subwords8k',
    with_info=True,
    as_supervised=True
)

train_dataset, test_dataset = dataset['train'], dataset['test']

encoder = info.features['text'].encoder

BUFFER_SIZE = 10000
BATCH_SIZE = 64

padded_shapes = ([None], ())

train_dataset = (train_dataset
                    .shuffle(BUFFER_SIZE)
                    .padded_batch(BATCH_SIZE, padded_shapes, padded_shapes))

test_dataset = (test_dataset
                    .shuffle(BUFFER_SIZE)
                    .padded_batch(BATCH_SIZE, padded_shapes, padded_shapes))

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(encoder.vocab_size, 64),
    tf.keras.layers.Biderectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    loss='binary_crossentropy',
    optimizer=tf.keras.optimizers.Adam(1e-4),
    metrics=['accuracy']
)

history = model.fit(train_dataset, epochs=5,
    validation_data=test_dataset, validation_steps=30)

def pad_to_size(vec, size):
    zeros = [0]*(size-len(vec))
    vec.extend(zeros)
    return vec

def sample_predict(sentence, model, pad=True):
    encoded_sample_pred_text = encoder.encode(sentence)
    if pad:
        encoded_sample_pred_text = pad_to_size(encoded_sample_pred_text(sentence, 64)
    encoded_sample_pred_text = tf.cast(encoded_sample_pred_text, tf.float32)
    predictions = model.predict(tf.expand_dims(encoded_sample_pred_text, 0))
    return predictions

sample_text = ('This movie was great. higly rec')
predictions = sample_predict(sample_text, pad=True) * 100

print(predictions)

model = tf.keras.Sequential([
    tf.keras.layers.Biderectional(tf.keras.layers.LSTM(64, return_wequences=True),
    tf.keras.layers.Biderectional(tf.keras.layers.LSTIM(32)),
    tf.keras.Dense(64, activation='relu'),
    # Helps overfitting
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='sigmoid')
)]

model.compile(
    loss='binary_crossentropy',
    optimizer=tf.keras.optimizers.Adam(1e-4),
    metrics=['accuracy']
)


history = model.fit(train_dataset, epochs=5,
    validation_data=test_dataset, validation_steps=30)