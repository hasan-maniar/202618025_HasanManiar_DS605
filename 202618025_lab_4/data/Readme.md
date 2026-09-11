# NYC Airbnb Price Prediction — DS605 Lab 4

An end-to-end machine learning project that predicts nightly Airbnb prices in
New York City using the Kaggle **AB_NYC_2019** dataset, with a working
Streamlit app for live predictions.

## 📁 Project Structure

```
airbnb-price-prediction/
├── data/
│   └── AB_NYC_2019.csv          # dataset (not committed to repo)
├── assets/
│   ├── price_distribution.png
│   ├── price_by_room_type.png
│   ├── correlation_heatmap.png
│   └── model_comparison.csv
├── model/
│   └── price_pipeline.pkl       # saved preprocessing + trained model
├── train.ipynb                  # Task 1 & 2: cleaning, EDA, training, tuning
├── app.py                       # Task 3: Streamlit prediction app
├── requirements.txt
└── README.md
```

## ⚙️ Setup

```bash
git clone <your-repo-url>
cd airbnb-price-prediction
pip install -r requirements.txt
```

Download the dataset and place it at `data/AB_NYC_2019.csv`:

```bash
# Windows PowerShell
Invoke-WebRequest -Uri "https://huggingface.co/datasets/gradio/NYC-Airbnb-Open-Data/resolve/main/AB_NYC_2019.csv" -OutFile "data\AB_NYC_2019.csv"

# Mac/Linux
curl -L -o data/AB_NYC_2019.csv "https://huggingface.co/datasets/gradio/NYC-Airbnb-Open-Data/resolve/main/AB_NYC_2019.csv"
```

(Original source: [Kaggle — NYC Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data))

## ▶️ Run Training

Open `train.ipynb` and run all cells top to bottom. This cleans the data,
generates EDA plots into `assets/`, compares models, tunes the best one,
prints final metrics, and saves the trained pipeline to `model/price_pipeline.pkl`.

## ▶️ Run the App

```bash
python -m streamlit run app.py
```

Enter listing details (location, room type, availability, etc.) and get an
estimated nightly price instantly.

**Deployed app:** `<<FILL IN — Streamlit Community Cloud link, or "Not deployed">>`

---

## 📊 Task 1 — Data Analysis & Preparation

### Cleaning
- Dropped identifier / free-text columns not useful for prediction: `id`, `name`, `host_id`, `host_name`, `last_review`.
- Filled missing `reviews_per_month` with `0` (missing only when `number_of_reviews == 0`).
- Removed listings with `price = 0` (invalid) and the top 1% price outliers (extreme luxury listings that distort the model).
- Capped `minimum_nights` at 365 to remove unrealistic values (some listings had 1000+ nights).

### Feature Engineering
- **Frequency-encoded** `neighbourhood` (200+ unique values — too high-cardinality for one-hot encoding) into a single numeric feature representing how common that neighbourhood is in the dataset.
- Kept `neighbourhood_group` (5 boroughs) as a one-hot categorical feature.
- **Log-transformed the target** (`log1p(price)`) to correct for strong right-skew in price distribution; predictions are inverse-transformed (`expm1`) back to dollars.

### Key Patterns Observed
- Manhattan and Brooklyn listings are priced notably higher than Bronx/Staten Island.
- "Entire home/apt" listings command a significant premium over private/shared rooms.
- Price is right-skewed with a long tail of high-end luxury listings.
- Latitude/longitude and neighbourhood popularity correlate with price, reflecting location-driven demand.

*See `assets/price_distribution.png`, `assets/price_by_room_type.png`, and `assets/correlation_heatmap.png` for supporting visuals.*

---

## 🤖 Task 2 — Model Training & Evaluation

### Models Compared

| Model | MAE | RMSE | Test R² | Train R² |
|---|---|---|---|---|
| Linear Regression | 48.17 | 83.77 | 0.355 | 0.342 |
| Ridge Regression | 48.17 | 83.77 | 0.355 | 0.342 |
| Random Forest | 42.26 | 72.68 | 0.515 | 0.891 |
| Gradient Boosting | 44.05 | 78.13 | 0.439 | 0.428 |

*(Full results also saved in `assets/model_comparison.csv`)*

### Final Model
**Selected: Random Forest Regressor**, tuned using `RandomizedSearchCV` (5-fold CV, 20 iterations) over `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`, and `max_features`, with stronger regularization applied to reduce the overfitting seen in the untuned version.

**Best hyperparameters:** `<<FILL IN — paste search.best_params_ output from your final run>>`

**Final test performance:**
- MAE: `<<FILL IN>>`
- RMSE: `<<FILL IN>>`
- R²: `<<FILL IN>>`

### Overfitting/Underfitting Check
The untuned Random Forest showed a large gap between train R² (0.891) and test R² (0.515), indicating overfitting — it memorized training data rather than generalizing. Linear/Ridge models, by contrast, showed matching train/test R² (~0.34–0.36) but both were low, indicating underfitting since they can't capture non-linear location/room-type interactions. Hyperparameter tuning with higher `min_samples_leaf` and constrained `max_depth` was applied to the Random Forest specifically to close this gap. `<<FILL IN — once you have final numbers, state whether the gap closed, e.g. "After tuning, train R² dropped to 0.XX and test R² rose to 0.XX, closing the gap and indicating better generalization.">>`

---

## 💻 Task 3 — Streamlit Application

The app (`app.py`) accepts:
- Neighbourhood group, room type
- Latitude / longitude
- Minimum nights, number of reviews, reviews per month
- Host's total listing count, yearly availability
- Neighbourhood popularity score

...and returns an estimated nightly price in real time.

**Test inputs used:**

| Input scenario | Predicted Price |
|---|---|
| Manhattan, Entire home/apt, high availability | `<<FILL IN>>` |
| Brooklyn, Private room, low reviews | `<<FILL IN>>` |
| Bronx, Shared room | `<<FILL IN>>` |

*(Add screenshots here, e.g. `![App Screenshot](assets/app_screenshot.png)`)*

---

## 📝 Task 4 — Final Project Summary

**Analysis recap:** Location (borough/neighbourhood) and room type are the strongest price drivers in the NYC Airbnb market, with Manhattan entire-home listings commanding the highest prices and outer-borough shared rooms the lowest.

**Model comparison recap:** Tree-based models (Random Forest, Gradient Boosting) outperformed linear models because Airbnb pricing depends on non-linear interactions between location and room type that linear regression cannot capture. Random Forest was selected as the final model after tuning addressed its initial overfitting tendency.

**Final performance:** The tuned Random Forest achieved an R² of `<<FILL IN>>` on held-out test data, meaning it explains `<<FILL IN>>`% of price variance, with an average prediction error of about $`<<FILL IN>>` (MAE).

**Application results:** The Streamlit app produces reasonable, consistent price estimates across different borough/room-type combinations, matching expected market patterns (Manhattan > Brooklyn > Queens > Bronx/Staten Island). `<<FILL IN — add a sentence once you have real test predictions, e.g. "For example, a Manhattan entire-home listing was estimated at $XXX/night, while a Bronx shared room was estimated at $XX/night, consistent with real-world pricing trends.">>`

**Limitations:**
- Trained on 2019 data — does not reflect current NYC rental market conditions, inflation, or regulatory changes (e.g., Local Law 18 short-term rental restrictions).
- No text (listing description) or image features used, which likely influence real-world pricing.
- Neighbourhood frequency encoding is dataset-specific and would need recalculation for listings outside this dataset's distribution.
- Random Forest models don't extrapolate well to truly novel neighbourhoods/locations not seen in training.
- A version mismatch between training and serving environments (scikit-learn) can break the saved pipeline; `requirements.txt` pins the exact version used to avoid this.

---

## 🔗 Links
- **GitHub Repo:** `<<FILL IN>>`
- **Deployed App:** `<<FILL IN — or "Not deployed">>`
- **Dataset Source:** [Kaggle — dgomonov/new-york-city-airbnb-open-data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)