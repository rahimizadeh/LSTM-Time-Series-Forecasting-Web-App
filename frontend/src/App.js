import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [plot, setPlot] = useState('');
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);
    
    try {
      const response = await axios.post('http://localhost:5000/predict', formData);
      setPlot(`data:image/png;base64,${response.data.plot}`);
      setPredictions(response.data.predictions);
    } catch (error) {
      alert('Error: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Time Series Predictor</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="file" 
          accept=".csv" 
          onChange={(e) => setFile(e.target.files[0])} 
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Processing...' : 'Predict'}
        </button>
      </form>
      
      {plot && <img src={plot} alt="Prediction" style={{maxWidth: '100%'}} />}
      
      {predictions.length > 0 && (
        <div>
          <h2>Results</h2>
          <pre>{JSON.stringify(predictions, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;