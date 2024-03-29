{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SharmilaNakka/Data-analysis/blob/main/BrainTumor.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mP0zLYc85F2b"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e1OIH6XPinqc",
        "outputId": "61d9cbf1-3531-4c2b-9fbd-1ccb1c409863"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "lElQXIzykuDL"
      },
      "outputs": [],
      "source": [
        "import tensorflow as tf\n",
        "from tensorflow import keras\n",
        "from tensorflow.keras import layers\n",
        "from tensorflow.keras.preprocessing.image import ImageDataGenerator\n",
        "# Define image size and batch size\n",
        "IMG_SIZE = 224\n",
        "BATCH_SIZE = 32"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c0ZmXu49lDGN",
        "outputId": "b76b2e95-327e-4e78-c675-b01f3ce9f7dd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 2400 images belonging to 2 classes.\n",
            "Found 600 images belonging to 2 classes.\n",
            "Found 60 images belonging to 1 classes.\n"
          ]
        }
      ],
      "source": [
        "train_datagen = ImageDataGenerator(\n",
        "    rescale=1./255,\n",
        "    validation_split=0.2\n",
        ")\n",
        "\n",
        "train_generator = train_datagen.flow_from_directory(\n",
        "    '/content/drive/MyDrive/BrainTumor/train',\n",
        "    target_size=(IMG_SIZE, IMG_SIZE),\n",
        "    batch_size=BATCH_SIZE,\n",
        "    class_mode='binary',\n",
        "    subset='training'\n",
        ")\n",
        "\n",
        "val_generator = train_datagen.flow_from_directory(\n",
        "    '/content/drive/MyDrive/BrainTumor/train',\n",
        "    target_size=(IMG_SIZE, IMG_SIZE),\n",
        "    batch_size=BATCH_SIZE,\n",
        "    class_mode='binary',\n",
        "    subset='validation'\n",
        ")\n",
        "test_datagen = ImageDataGenerator(rescale=1./255)\n",
        "\n",
        "test_generator = test_datagen.flow_from_directory(\n",
        "    '/content/drive/MyDrive/BrainTumor/test',\n",
        "    target_size=(IMG_SIZE, IMG_SIZE),\n",
        "    batch_size=BATCH_SIZE,\n",
        "    class_mode='binary'\n",
        ")\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ZiDfYP2EluA6"
      },
      "outputs": [],
      "source": [
        "model = keras.Sequential([\n",
        "    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),\n",
        "    layers.MaxPooling2D((2, 2)),\n",
        "    layers.Conv2D(64, (3, 3), activation='relu'),\n",
        "    layers.MaxPooling2D((2, 2)),\n",
        "    layers.Conv2D(128, (3, 3), activation='relu'),\n",
        "    layers.MaxPooling2D((2, 2)),\n",
        "    layers.Flatten(),\n",
        "    layers.Dense(128, activation='relu'),\n",
        "    layers.Dense(1, activation='sigmoid')\n",
        "])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ueQ76XaGl3ar"
      },
      "outputs": [],
      "source": [
        "model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "99SmT6szmANK",
        "outputId": "44f7816a-5789-48ea-f078-99dc5acf47f1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/5\n",
            "75/75 [==============================] - 841s 11s/step - loss: 0.6590 - accuracy: 0.7050 - val_loss: 0.5197 - val_accuracy: 0.7300\n",
            "Epoch 2/5\n",
            "75/75 [==============================] - 317s 4s/step - loss: 0.3449 - accuracy: 0.8575 - val_loss: 0.2849 - val_accuracy: 0.8683\n",
            "Epoch 3/5\n",
            "75/75 [==============================] - 333s 4s/step - loss: 0.2086 - accuracy: 0.9162 - val_loss: 0.1635 - val_accuracy: 0.9400\n",
            "Epoch 4/5\n",
            "75/75 [==============================] - 321s 4s/step - loss: 0.1215 - accuracy: 0.9588 - val_loss: 0.0899 - val_accuracy: 0.9717\n",
            "Epoch 5/5\n",
            "75/75 [==============================] - 335s 4s/step - loss: 0.0675 - accuracy: 0.9812 - val_loss: 0.0587 - val_accuracy: 0.9833\n"
          ]
        }
      ],
      "source": [
        "history = model.fit(train_generator,validation_data=val_generator,epochs=5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fSaI2fQlm1P5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0167bc7c-4bbb-4e44-b1a3-5fde58e3e1ea"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3103: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.\n",
            "  saving_api.save_model(\n",
            "WARNING:tensorflow:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n"
          ]
        }
      ],
      "source": [
        "model.save(\"Model.h5\",\"label.txt\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "P2NLwpoI4qlW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TGXtOJa6nUAT",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0febdc45-edb6-48c8-e0d5-0e4bd40a4498"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:tensorflow:No training configuration found in the save file, so the model was *not* compiled. Compile it manually.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1/1 [==============================] - 0s 255ms/step\n",
            "prediction :no tumor(probability: 0.50070363 )\n"
          ]
        }
      ],
      "source": [
        "# @title Default title text\n",
        "from keras.models import load_model\n",
        "from tensorflow.keras.preprocessing import image  # TensorFlow is required for Keras to work\n",
        "from PIL import Image, ImageOps  # Install pillow instead of PIL\n",
        "import numpy as np\n",
        "\n",
        "#load the model\n",
        "model = load_model('/content/Model.h5')\n",
        "test_image_path='/content/drive/MyDrive/BrainTumor/train/no/No15.jpg'\n",
        "img=image.load_img(test_image_path,target_size=(224,224))\n",
        "img_array=image.img_to_array(img)\n",
        "img_array=np.expand_dims(img_array,axis=0)\n",
        "img_array/=225.\n",
        "prediction=model.predict(img_array)\n",
        "if prediction<0:\n",
        "  print(\"prediction :no tumor(probability:\",prediction[0][0],\")\")\n",
        "else:\n",
        "    print(\"prediction :no tumor(probability:\",prediction[0][0],\")\")\n",
        "class_names = ['You have Brain Tumor','You do not have Brain Tumor']\n",
        "data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n"
      ],
      "metadata": {
        "id": "qWRqC6SFeT6h"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Cxa_OoqTnZda"
      },
      "outputs": [],
      "source": [
        "\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
