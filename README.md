# Time Series Prediction Web App

![Docker](https://img.shields.io/badge/Docker-2.5GB→300MB-success)
![React](https://img.shields.io/badge/React-18-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-green)

A Dockerized web application for time series forecasting using LSTM, featuring:
- CSV file uploads
- Interactive prediction plots
- Optimized Docker images (~300MB backend)

## 📦 Project Structure

```
timeseries-app/
├── backend/               # Flask + LSTM
│   ├── app.py             # Prediction API
│   ├── requirements.txt   # Python dependencies
│   └── model/             # Trained models
├── frontend/              # React.js
│   ├── src/               # React components
│   └── public/            # Static assets
├── docker-compose.yml     # Full stack definition
└── README.md
```

## 🚀 Deployment Options

### Option 1: Using Pre-built Images (Fastest)
```bash
docker pull rahimizadeh/timeseries-backend:latest
docker pull rahimizadeh/timeseries-frontend:latest
docker-compose up -d
```

### Option 2: Build from Source
```bash
# 1. Clone repository
git clone https://github.com/yourrepo/timeseries-app.git
cd timeseries-app

# 2. Build optimized images
docker-compose build --no-cache

# 3. Start services
docker-compose up -d
```

## 🔍 Access the Application

| Service       | URL                   | Port  |
|---------------|-----------------------|-------|
| Frontend      | http://localhost:3000 | 3000  |
| Backend API   | http://localhost:5000 | 5000  |

## 🧪 Testing the Application

1. **Prepare a CSV file** (`sample.csv`):
   ```csv
   value
   0.1
   0.5
   0.9
   1.2
   1.6
   ```

2. **Test via Web UI**:
   - Open http://localhost:3000
   - Upload `sample.csv`
   - View predictions and plot

3. **Test API directly**:
   ```bash
   curl -X POST -F "file=@sample.csv" http://localhost:5000/predict
   ```

## 🛠 Maintenance Commands

| Command                          | Purpose                          |
|----------------------------------|----------------------------------|
| `docker-compose logs -f backend` | View backend logs                |
| `docker exec -it backend bash`   | Enter backend container          |
| `docker system prune`            | Clean unused Docker objects      |

## 🐛 Troubleshooting

**Problem**: CSV upload fails
- Solution: Verify file format matches the expected structure

**Problem**: "Model not found" error
- Solution: Rebuild with `docker-compose build --no-cache backend`

**Problem**: High CPU/RAM usage
- Solution: Limit resources in `docker-compose.yml`:
  ```yaml
  services:
    backend:
      deploy:
        resources:
          limits:
            cpus: '1'
            memory: 1G
  ```

## 📊 Performance Metrics

| Component       | Original Size | Optimized Size |
|-----------------|---------------|----------------|
| Backend         | 2.5GB         | 300MB          |
| Frontend        | 42MB          | 42MB           |

---

## 🔄 CI/CD Pipeline Example

```yaml
# .github/workflows/deploy.yml
name: Deploy
on: push

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: docker-compose -f docker-compose.prod.yml build
      - run: docker push rahimizadeh/timeseries-backend
      - run: docker push rahimizadeh/timeseries-frontend
```

---

## 📜 License

MIT © 2023

---

This README provides:
✅ Clear deployment instructions  
✅ Maintenance commands  
✅ Troubleshooting guide  
✅ Performance benchmarks  
✅ CI/CD integration example  

To update the project:
1. Modify the backend/frontend code
2. Update the version tags
3. Rebuild and push images:
   ```bash
   docker-compose build
   docker push rahimizadeh/timeseries-backend:v2
   docker push rahimizadeh/timeseries-frontend:v2
   ```