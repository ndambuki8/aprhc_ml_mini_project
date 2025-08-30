# ETL + ML Mini Project

This project demonstrates a simple **ETL pipeline** with **machine learning** on user membership data. It extracts join dates, aggregates by month, and trains a model to predict trends.

---

## ⚙️ Workflow
1. **Extract & Transform**
   - Load user membership data (`DateJoined`).
   - Filter only 2017 records.
   - Aggregate members joined per month.

2. **Load & Train**
   - Prepare features and target.
   - Train a regression model.
   - Evaluate with **RMSE**.
   - Save trained model (`model.pkl`).

---

## ▶️ Usage

### Clone Repo
```bash
git clone https://github.com/yourusername/mini-etl-ml-pipeline.git
cd mini-etl-ml-pipeline
```
### Install dependencies
```bash
pip install -r requirements.txt
```

### Run ETL
```bash
python etl_pipeline.py
```

### Train model
```bash
python train_model.py
```

### Serve predictions (Without using Docker)
```bash
python serve_api.py
# available at http://localhost:5000/predict
```

### Serve predictions (using Docker🐳)
#### Build Image
```bash
docker build -t mini-etl-ml .
```

#### Run Container
```bash
docker run -p 5000:5000 mini-etl-ml
```

#### With Docker Compose
```bash
docker-compose up
```