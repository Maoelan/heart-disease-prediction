## Heart Disease Prediction

Dataset : https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease

### Oversampling

Classifier Comparison

![image](https://github.com/Maoelan/heart-disease-prediction/assets/58927608/5f9591a9-cbef-463e-8b9d-8300784f7f23)

Roc Curve

![image](https://github.com/Maoelan/heart-disease-prediction/assets/58927608/212c9c83-087f-4dfb-aa40-961425fbbbc4)

### Undersampling

![image](https://github.com/Maoelan/heart-disease-prediction/assets/58927608/380dd871-3c1f-403b-9d61-8eccd7f188d9)

Roc Curve

![image](https://github.com/Maoelan/heart-disease-prediction/assets/58927608/33b3ed28-dfd3-4bc3-b66b-4a2af039258f)

### Deploy -> Website

The algorithm that I use for classification on websites is knn which I save in model2.pkl

how to run website :

- venv/Scripts/activate
- cd deploy
- set FLASK_APP=app.py
- flask run

and run http://127.0.0.1:5000 :

![ezgif com-video-to-gif](https://github.com/Maoelan/heart-disease-prediction/assets/58927608/cc10a0c4-b41a-43e1-9cf2-c12e304190ac)






