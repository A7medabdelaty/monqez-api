# import libraries
import numpy as np
from keras.utils import load_img, img_to_array
from keras.models import model_from_json
import pickle
import base64
from io import BytesIO
from PIL import Image
import numpy as np


class mymodel():
    def __init__(self, s):

        # Load Model
        with open('D:/fastApi/Model/ResultsMap.pkl', 'rb') as f:
            self.ResultMap = pickle.load(f)

        json_file = open('D:/fastApi/Model/classifier.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("D:/fastApi/Model/model.h5")

        # convert from Base64 To image
        image_code = base64.b64decode(s)
        im_file = BytesIO(image_code)
        # preprocessing on image
        ImagePath = im_file
        test_image = load_img(ImagePath, target_size=(64, 64))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        self.result = loaded_model.predict(test_image, verbose=0)

    # the Prediction
    def prediction(self):
        return self.ResultMap[np.argmax(self.result)]
