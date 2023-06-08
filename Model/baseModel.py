class mymodel():
    def __init__(self, s):
        from tensorflow.keras.models import model_from_json
        from tensorflow.keras.preprocessing import image
        import numpy as np
        import pickle
        import base64
        from io import BytesIO
        from PIL import Image
        from keras.utils import load_img, img_to_array

        # Load Model
        json_file = open('D:/fastApi/Model/model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("D:/fastApi/Model/model.h5")

        with open('D:/fastApi/Model/classes.pkl', 'rb') as f:
            self.classes = pickle.load(f)

        # convert from Base64 To image

        image_code = base64.b64decode(s)
        image_path = BytesIO(image_code)

        img = image.load_img(image_path, target_size=(224, 224, 3))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        self.pred = loaded_model.predict(images, batch_size=32)

    def prediction(self):
        import numpy as np
        return int(self.classes[np.argmax(self.pred)])