# DS605: Fundamentals of Machine Learning — Lab Assignment 2
**Vectorized Programming with NumPy and Data Wrangling with Pandas**

**Name:** Hasan Maniar
**ID:** 202618025
**Dataset:** Kaggle Titanic Dataset (train.csv)

## Project Details
This lab covers:
- **Part A:** NumPy fundamentals — arrays, statistics, indexing, vectorized arithmetic, linear algebra, and normal distribution sampling.
- **Part B:** Pandas data wrangling on the Titanic dataset — loading/inspecting data, filtering, groupby aggregation, handling missing values, outlier detection, feature engineering, and visualizations.

## Repository Structure
- `DS605_Lab2.ipynb` — complete runnable notebook with all tasks
- `data/train.csv` — original Titanic dataset
- `data/train_cleaned.csv` — cleaned dataset with imputed values and engineered features (FamilySize, IsAlone)
- `figures/` — generated plots (histogram, missing values bar chart, correlation heatmap, survival by sex, age vs fare scatter)
- `observations.txt` — final written observations

## Key Observations
1. Females had a substantially higher survival rate than males.
2. Passenger class (Pclass) is negatively correlated with survival — 1st class passengers survived at much higher rates than 3rd class.
3. Fare is positively correlated with survival, closely tied to Pclass.
4. Age shows a weak negative correlation with survival; young children had relatively higher survival rates.
5. Passengers traveling alone had lower survival rates than those with small families.
6. Fare outliers exist mainly among 1st class passengers.
7. Embarked='S' had the most passengers but a lower average survival rate than Embarked='C'.

## How to Run
```bash
pip install pandas numpy matplotlib seaborn
jupyter notebook DS605_Lab2.ipynb
```