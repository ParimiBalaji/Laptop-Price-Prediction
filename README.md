#  Laptop Price Prediction (Machine Learning Project)

##  Problem Statement

Laptop prices vary significantly based on specifications like RAM, CPU, GPU, storage, and display features.
This project aims to **predict the price of a laptop** based on its configuration using Machine Learning.

---

##  Objective

To build an end-to-end ML system that:

* Takes laptop specifications as input
* Performs feature engineering
* Predicts price accurately
* Provides an interactive user interface

---

##  Live Demo

 *(Add your deployed link here after deployment)*

---

##  Machine Learning Pipeline

The project uses a **Scikit-learn Pipeline** that includes:

1. **Data Preprocessing**

   * Handling missing values
   * Encoding categorical features

2. **Feature Engineering**

   * Calculated **PPI (Pixels Per Inch)** from screen resolution and size
   * Extracted CPU & GPU brands
   * Converted categorical variables

3. **Model Training**

   * Regression model trained on processed dataset
   * Target variable is **log-transformed** for better performance

4. **Prediction**

   * Final output is exponentiated to get actual price

---

##  Model Performance

| Metric   | Value            |
| -------- | ---------------- |
| R² Score | *Add your score* |
| MAE      | *Add your value* |
| RMSE     | *Add your value* |

>  Note: Performance may vary depending on dataset quality and preprocessing.

---

##  Input Features

* Brand (Company)
* Type (Notebook, Gaming, etc.)
* RAM (GB)
* Weight
* Touchscreen (Yes/No)
* IPS Display (Yes/No)
* Screen Size (inches)
* Resolution
* CPU Brand
* HDD / SSD (GB)
* GPU Brand
* Operating System

---

##  Tech Stack

* **Python**
* **Pandas & NumPy**
* **Scikit-learn**
* **Streamlit**
* **Pickle**

---



## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ParimiBalaji/Laptop-Price-Prediction.git
cd Laptop-Price-Prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

---

##  Future Improvements

*  Deploy on cloud (Streamlit Cloud / Render)
*  Add model comparison (Random Forest, XGBoost)
*  Improve UI/UX
*  Add feature importance visualization
*  Use real-time laptop data

---

## Author

**Parimi Gandhi Balaji**
B.Tech CSE | Aspiring Data Scientist

---

##  Support

If you found this project useful:

* ⭐ Star this repository
*  Fork it
*  Use it for learning

---

##  Disclaimer

This project is for educational purposes. Predictions are approximate and may not reflect real market prices.
