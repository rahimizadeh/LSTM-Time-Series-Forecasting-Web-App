from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and file.filename.endswith('.csv'):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        
        # Process data
        df = pd.read_csv(filename)
        data = scaler.transform(df.values)
        
        # Predict
        predictions = model.predict(data)
        predictions = scaler.inverse_transform(predictions)
        
        # Generate plot
        plt.figure(figsize=(10, 6))
        plt.plot(df.values, label='Actual')
        plt.plot(predictions, label='Predicted')
        plt.legend()
        
        # Convert plot to base64
        img_bytes = io.BytesIO()
        plt.savefig(img_bytes, format='png')
        img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
        
        return jsonify({
            'predictions': predictions.flatten().tolist(),
            'plot': img_base64
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host='0.0.0.0', port=5000)