# DS605 Lab Assignment 8: Decision Trees and Support Vector Machines

## Overview

This project implements and evaluates Decision Tree and Support Vector Machine (SVM) classification algorithms using the **UCI Banknote Authentication dataset**.

The assignment focuses on understanding the underlying algorithms by implementing both a decision tree and a linear SVM from scratch, then comparing their performance with Scikit-learn implementations.

## Objectives

- Implement a Decision Tree classifier from scratch.
- Implement a linear SVM classifier from scratch without using Scikit-learn estimators.
- Explore Gini impurity and entropy for decision tree splitting.
- Visualize decision boundaries using two input features.
- Evaluate final model performance using all four dataset features.
- Compare custom implementations with Scikit-learn models.
- Evaluate model performance using classification metrics and confusion matrices.

## Dataset

**Dataset:** Banknote Authentication

**Source:** UCI Machine Learning Repository  
https://archive.ics.uci.edu/dataset/267/banknote+authentication

The dataset contains four numerical features extracted from images of banknotes.

| Feature | Description |
|---|---|
| Variance | Variance of the Wavelet Transformed image |
| Skewness | Skewness of the Wavelet Transformed image |
| Curtosis | Curtosis of the Wavelet Transformed image |
| Entropy | Entropy of the image |

**Target:** Class label indicating authentic or forged banknotes.

- Total samples: 1,372
- Number of input features: 4
- Number of target classes: 2

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

Scikit-learn is used for benchmark models, data splitting, and evaluation utilities where appropriate. The two required custom algorithms are implemented independently of Scikit-learn estimators.

## Data Preparation

The dataset is divided into training and testing sets using a stratified 75:25 split.

| Dataset partition | Samples | Features |
|---|---:|---:|
| Training set | 1,029 | 4 |
| Testing set | 343 | 4 |

Stratification preserves the class distribution across the training and testing sets.

### Feature usage

Two different feature configurations are used to meet the assignment requirements:

1. **2D decision-boundary visualization:** Uses two selected features for training and plotting the decision boundaries.
2. **Final performance evaluation:** Uses all four features for model training and testing.

The two-feature configuration is used only for visualization experiments. Final performance comparisons use the complete four-feature input.

## Algorithms Implemented From Scratch

### 1. Decision Tree

The custom Decision Tree implementation includes:

- Gini impurity calculation.
- Entropy calculation.
- Information gain and split selection.
- Recursive tree construction.
- Stopping criteria for tree growth.
- Prediction using the constructed tree.
- Tree visualization and complexity analysis.

The custom implementation is compared with Scikit-learn's `DecisionTreeClassifier`.

### 2. Linear Support Vector Machine (SVM)

The custom linear SVM is implemented using NumPy rather than Scikit-learn's SVM estimators.

The implementation includes:

- Feature standardization.
- Weight and bias initialization.
- Hinge-loss-based optimization.
- Gradient or subgradient updates.
- Prediction using the learned decision function.
- Margin and classification-boundary analysis.

The custom implementation is compared with Scikit-learn's `SVC` configured with a linear kernel.

## Decision-Boundary Visualization

Two-dimensional decision-boundary plots are generated using two selected input features.

These visualizations illustrate:

- Classification regions.
- Decision boundaries.
- Training samples from different classes.
- Differences between the custom and Scikit-learn implementations.

Because the visualizations use only two features, their results are separate from the final four-feature performance evaluation.

## Additional SVM Experiments

Nonlinear classification experiments using synthetic datasets, such as `make_moons`, demonstrate how different SVM kernels behave.

Kernels may include:

- Linear
- Polynomial
- Radial Basis Function (RBF)

These experiments illustrate the difference between linear and nonlinear decision boundaries.

## Model Evaluation

Final model comparisons use all four input features and the same held-out test set.

Evaluation may include:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrices
- Training time
- Decision tree depth, number of leaves, and total nodes

The notebook compares custom implementations with corresponding Scikit-learn benchmark models. Actual performance values are reported in the notebook output.

## Project Structure

```text
DS605-Lab-Assignment-8/
├── README.md
├── requirements.txt
└── DS605_Lab_Assignment_8.ipynb
```

*Adjust the notebook filename above to match the actual filename in your repository.*

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Alternatively, install the dependencies directly:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

## How to Run

1. Clone or download this repository.
2. Install the required dependencies.
3. Open the Jupyter Notebook.
4. Run the notebook cells in order, starting with data loading and preprocessing.
5. Review the algorithm implementations, visualizations, and evaluation results.

Start Jupyter with:

```bash
jupyter notebook
```

## Key Assignment Requirements

- [x] Decision Tree implemented from scratch.
- [x] Linear SVM implemented from scratch without Scikit-learn estimators.
- [x] Two features used for 2D decision-boundary data preparation.
- [x] All four features retained for final performance evaluation.
- [x] Scikit-learn comparison models included.
- [x] Model evaluation and visualization included.

**Note:** The checklist reflects the intended notebook implementation. Confirm that the plotting cells actually train on the two-feature arrays and that the final evaluation cells use the four-feature arrays before submission.

## Conclusion

This project demonstrates the implementation and evaluation of Decision Tree and linear SVM classifiers, emphasizing the algorithms' underlying mechanics. Comparing the custom implementations with Scikit-learn benchmarks provides a basis for examining predictive performance, model complexity, and computational cost.

## References

1. Dua, D. and Graff, C. (2019). *UCI Machine Learning Repository*. University of California, Irvine, School of Information and Computer Sciences.
2. UCI Machine Learning Repository — Banknote Authentication: https://archive.ics.uci.edu/dataset/267/banknote+authentication
3. Scikit-learn documentation: https://scikit-learn.org/stable/
4. NumPy documentation: https://numpy.org/doc/
5. Matplotlib documentation: https://matplotlib.org/stable/

---

**Course:** DS605  
**Assignment:** Lab Assignment 8 — Decision Trees and SVMs
