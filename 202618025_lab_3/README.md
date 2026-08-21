# DS605: Fundamentals of Machine Learning — Lab Assignment 3

**Title:** Scikit-learn: Data Preprocessing and Model Performance Evaluation
**Name:** mohammedhasan maniar
**Student ID:**  202618025
**Course:** DS605 – Fundamentals of Machine Learning

## Dataset

**Name:** Hotel Booking Demand
**Source:** [Kaggle - Hotel Booking Demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)
**Rows / Columns (original):** 119,390 rows × 32 columns
**Target variable:** `is_canceled` (1 = booking cancelled, 0 = not cancelled)

## Project Structure


## Preprocessing Choices

- **Dropped `company`** — missing in approximately [XX]% of rows, too sparse to be usable as a feature.
- **Dropped `reservation_status` and `reservation_status_date`** — these directly reveal the booking outcome and would cause data leakage if kept.
- **Kept `agent`, `country`, `children`** despite missing values — imputed instead of dropped since missingness was low/moderate and the columns carry useful signal.
- **Outlier handling:** Checked `lead_time`, `adr`, `stays_in_week_nights`, and `stays_in_weekend_nights` using boxplots. Only extreme/erroneous values in `adr` (e.g. a booking with adr ≈ 5400, and negative values) were removed using an IQR-based upper bound (Q3 + 3×IQR, widened from the standard 1.5× since `adr` naturally has a long right tail). **[X] rows removed** as a result.
- **Train/test split:** 80/20 stratified split on `is_canceled`, `random_state=42`, used consistently across all four experiments.
- **Numerical features:** `KNNImputer(n_neighbors=5)` for missing values, followed by either `StandardScaler` (Pipeline A) or `MinMaxScaler` (Pipeline B).
- **Categorical features:** `SimpleImputer(strategy="most_frequent")` followed by `OneHotEncoder(handle_unknown="ignore")`.
- All preprocessing was wrapped in `ColumnTransformer` + `Pipeline` and fitted only on the training data to avoid leakage into the test set.

## Models Trained

| # | Model | Pipeline |
|---|-------|----------|
| 1 | Logistic Regression (`max_iter=1000`) | Pipeline A (StandardScaler) |
| 2 | Logistic Regression (`max_iter=1000`) | Pipeline B (MinMaxScaler) |
| 3 | Decision Tree (`random_state=42`) | Pipeline A (StandardScaler) |
| 4 | Decision Tree (`random_state=42`) | Pipeline B (MinMaxScaler) |

## Results

| Model | Train Accuracy | Test Accuracy | Precision | Recall | F1-score | Train-Test Gap |
|---|---|---|---|---|---|---|
| LogReg + Pipeline A (Standard) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| LogReg + Pipeline B (MinMax) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Tree + Pipeline A (Standard) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Tree + Pipeline B (MinMax) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

*(Full table also available in `model_comparison_results.csv`)*

Confusion matrices for the best Logistic Regression and best Decision Tree result are in `figures/confusion_matrices.png`.

## Final Observations

1. **Best overall combination:** [Fill in — e.g. "Tree + Pipeline A gave the strongest overall result, with the highest F1-score of X and test accuracy of Y."]
2. **Effect of scaler on Logistic Regression:** [Fill in — e.g. "StandardScaler and MinMaxScaler produced nearly identical results for Logistic Regression, with less than X% difference in test accuracy."]
3. **Effect of scaling on Decision Tree:** [Fill in — e.g. "Scaling had no meaningful effect on the Decision Tree's performance, as expected, since trees split on raw feature thresholds rather than distances."]
4. **Overfitting:** [Fill in — e.g. "The Decision Tree showed a noticeably larger train-test accuracy gap (X) compared to Logistic Regression (Y), indicating it overfit the training data more."]
5. **General takeaway:** [Fill in — e.g. "Logistic Regression generalized more consistently across both pipelines, while the Decision Tree achieved higher raw performance but at the cost of overfitting."]

## How to Run

1. Clone this repository.
2. Install dependencies: