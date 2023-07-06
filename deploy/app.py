from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.metrics import euclidean_distances

app = Flask(__name__)

# Memuat model
with open('model2.pkl', 'rb') as f:
    model = pickle.load(f)

label_encoder = LabelEncoder()
scaler = MinMaxScaler()

categorical_features = ['smoking', 'stroke', 'diabetic', 'diff_walking', 'physical_activity', 'kidney_disease', 'skin_cancer', 'sex']
numerical_features = ['physical_health']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    smoking = request.form.get('smoking')
    stroke = request.form.get('stroke')
    diabetic = request.form.get('diabetic')
    diff_walking = request.form.get('diff_walking')
    physical_activity = request.form.get('physical_activity')
    kidney_disease = request.form.get('kidney_disease')
    skin_cancer = request.form.get('skin_cancer')
    sex = request.form.get('sex')
    physical_health = float(request.form.get('physical_health'))

    transformed_features = []
    for feature in categorical_features:
        label_encoder.fit([request.form.get(feature)])  
        transformed_feature = label_encoder.transform([request.form.get(feature)])
        transformed_features.append(transformed_feature[0])

    input_features = [transformed_features + [physical_health]]

    input_features_scaled = scaler.fit_transform(input_features)

    prediction = model.predict(input_features_scaled)

    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)