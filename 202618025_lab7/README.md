# DS605 – Fundamentals of Machine Learning
## Lab Assignment 7: Image Representation and Face Recognition Using PCA

### 1. Objective
The objective of this lab assignment is to study image representation, Principal Component Analysis (PCA), eigenfaces, dimensionality reduction, face reconstruction, and face recognition using machine learning algorithms.

### 2. Dataset
**Dataset:** AT&T ORL Faces Dataset

- Total number of images: 400
- Total number of subjects: 40
- Images per subject: 10
- Image format: PGM
- Image dimensions: 112 × 92 pixels
- Number of features per image: 10,304 pixel values

### 3. Tools and Libraries
- Python 3
- NumPy
- Pandas
- Matplotlib
- Pillow (PIL)
- Scikit-learn
- Jupyter Notebook / Anaconda

### 4. Tasks Performed
1. Loaded and inspected the ORL face dataset.
2. Converted grayscale images into numerical feature vectors.
3. Divided the dataset into training and testing sets.
4. Calculated the mean face and centered the image data.
5. Applied Singular Value Decomposition (SVD) to calculate eigenfaces.
6. Analyzed explained variance and cumulative explained variance.
7. Visualized the top eigenfaces.
8. Projected images into a lower-dimensional PCA feature space.
9. Reconstructed face images using PCA components.
10. Calculated reconstruction error using Mean Squared Error (MSE).
11. Performed face recognition using the Nearest Neighbor classifier.
12. Compared KNN, Support Vector Machine (SVM), and Logistic Regression classifiers.
13. Evaluated the effect of different numbers of PCA components on recognition accuracy.
14. Saved the results and visualization plots.

### 5. Methodology
The face images are converted into numerical vectors, with each pixel representing one feature. The dataset is divided into training and testing sets, using eight images per subject for training and two for testing.

PCA is performed using SVD on the centered training data. The resulting principal components, known as eigenfaces, represent important patterns of facial variation. Images are projected onto selected eigenfaces to reduce dimensionality.

The reduced feature representations are then used for face recognition. Different classifiers and PCA component counts are evaluated using classification accuracy.

### 6. Results and Output Files
The program saves the following files in the `outputs` directory:

- `classifier_results.csv` – Accuracy results for the evaluated classifiers.
- `pca_component_results.csv` – Recognition accuracy for different PCA component counts.
- `pca_explained_variance.png` – Cumulative explained variance plot.
- `classifier_comparison.png` – Comparison of classifier accuracy.
- `assignment_summary.txt` – Summary of dataset details and experimental results.

### 7. Conclusion
This assignment demonstrates how PCA can reduce the dimensionality of face images while retaining important facial information. Eigenfaces provide a compact representation of facial patterns, and the resulting features can be used for face recognition.

The experiments compare different classification algorithms and investigate how the number of principal components affects recognition accuracy. The results help illustrate the relationship between dimensionality reduction and face-recognition performance.

### 8. How to Run
1. Open the Jupyter Notebook in Anaconda.
2. Ensure the ORL dataset folders (`s1` through `s40`) are accessible from the notebook's working directory.
3. Install the required libraries if necessary.
4. Run the notebook cells in order.
5. Review the generated results and plots in the `outputs` directory.
