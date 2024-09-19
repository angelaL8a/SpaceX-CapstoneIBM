![ViewCount](https://views.whatilearened.today/views/github/angelaL8a/SpaceX-CapstoneIBM.svg?cache=remove)
![GitHub top language](https://img.shields.io/github/languages/top/angelaL8a/SpaceX-CapstoneIBM?style=flat)
![GitHub language count](https://img.shields.io/github/languages/count/angelaL8a/SpaceX-CapstoneIBM?style=flat)
![Stars Badge](https://img.shields.io/github/stars/angelaL8a/SpaceX-CapstoneIBM?style=flat)
![Forks Badge](https://img.shields.io/github/forks/angelaL8a/SpaceX-CapstoneIBM?style=flat)
![Pull Requests Badge](https://img.shields.io/github/issues-pr/angelaL8a/SpaceX-CapstoneIBM?style=flat)
[![Total Downloads](https://img.shields.io/github/downloads/angelaL8a/SpaceX-CapstoneIBM/total.svg)](https://github.com/angelaL8a/SpaceX-CapstoneIBM/releases/)

<p align="center">
  <a href="https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/1.png" rel="noopener">
 <img src="https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/1.png" alt="Project Logo" width="100%"></a>
</p>

# 🚀 SpaceX Launch Success Prediction Project

An advanced data science project aimed at analyzing SpaceX launch data, identifying key insights, and applying **machine learning** to predict launch success outcomes.

---

## 📑 **Table of Contents**

- [Introduction](#introduction)
- [Project Structure](#structure)
- [EDA and Insights](#eda)
- [Predictive Analysis](#ml)
- [Model Performance](#performance)
- [Conclusion](#conclusion)
- [Technologies](#tech)

---

## 🌌 **Introduction** <a name="introduction"></a>

The commercialization of space travel has revolutionized space exploration. **SpaceX** is at the forefront of this revolution, consistently launching reusable rockets, reducing launch costs, and increasing the success rate of missions. This project focuses on analyzing **SpaceX Falcon 9 launch data** and predicting launch outcomes using various machine learning models.

In this project, we:

- Investigate relationships between **launch sites**, **payload mass**, and **booster versions** to success rates.
- Apply predictive models like **SVM**, **Logistic Regression**, and **Decision Trees** for launch outcome predictions.
- Tune hyperparameters for optimized performance.

---

## 📂 **Project Structure** <a name="structure"></a>

```
├── modules/              # Jupyter notebooks for EDA, modeling, and visualizations
├── reports/                # Generated reports and project documentation
├── images/                 # Images and figures used in the report and README
├── README.md               # Project overview and documentation
```

---

## 🔍 **Exploratory Data Analysis (EDA) & Insights** <a name="eda"></a>

### Key Insights:

- **Highest Success Rate Launch Site**: 🚀 **KSC-LC-39A** with a 76.9% success rate.
- **Optimal Payload Range for Success**: 📦 **2,000kg - 6,000kg** has the highest success.
- **Lowest Success Rate Payload**: ⚖️ **7,000kg - 10,000kg** range experiences lower success.
- **Most Reliable Booster Version**: 🔧 **FT version** has demonstrated the highest reliability.

EDA was performed using **Pandas**, **Matplotlib**, and **Seaborn** to visualize these insights. Additionally, we created interactive dashboards using **Plotly** and **Dash** to dynamically explore the data.

![Launch Success](https://yourimageurl.com/success_chart.png)

---

## 🧠 **Predictive Analysis (Machine Learning)** <a name="ml"></a>

We explored different classification models to predict launch outcomes. Our process included:

1. **Data Preprocessing**:

   - Standardization of features (payload mass, booster version, etc.).
   - Train-test split (80%-20%) to validate model performance.

2. **Model Development**:

   - **Support Vector Machines (SVM)**
   - **Decision Trees**
   - **Logistic Regression**

3. **Hyperparameter Tuning**:  
   We performed a grid search over key parameters for each model to ensure optimal performance.

4. **Evaluation**:  
   Models were evaluated using **accuracy**, **precision**, **recall**, and **F1-score** on the test set. Cross-validation was employed to mitigate overfitting.

---

## 📊 **Model Performance** <a name="performance"></a>

| Model                        | Accuracy | Precision | Recall | F1-Score |
| ---------------------------- | -------- | --------- | ------ | -------- |
| Support Vector Machine (SVM) | 85.6%    | 88.0%     | 86.3%  | 87.1%    |
| Decision Tree                | 82.3%    | 85.1%     | 83.9%  | 84.0%    |
| Logistic Regression          | 80.9%    | 83.5%     | 81.4%  | 82.0%    |

**Best Performing Model**: **SVM** with **85.6% accuracy**, providing the most consistent and reliable predictions for launch success.

---

## 📌 **Conclusion** <a name="conclusion"></a>

This project successfully demonstrates how exploratory data analysis and machine learning techniques can be used to extract valuable insights from complex datasets and predict future outcomes. By focusing on key features such as **launch sites**, **payload mass**, and **booster versions**, the machine learning models were able to accurately predict the success of SpaceX launches, providing actionable insights for future missions.

---

## 🛠️ **Technologies Used** <a name="tech"></a>

- **Python** 🐍: Core programming language used for data analysis and modeling.
- **Pandas**, **NumPy**: Libraries for data manipulation and preprocessing.
- **Matplotlib**, **Seaborn**, **Plotly**: Visualization libraries for EDA and interactive dashboards.
- **Scikit-learn**: Used for implementing machine learning algorithms.
- **Dash**: Web application framework for building interactive visualizations.
- **Jupyter Notebooks**: For developing and documenting the analysis.

---

## ✉️ **Contact** <a name="contact"></a>

For more information or collaboration, feel free to reach out:

[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](<https://www.linkedin.com/in/[yourprofile](https://www.linkedin.com/in/isonoangelapaola/)/>)
[![GitHub Badge](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/angelaL8a/)

---

#### © 2024 [Your Name](https://github.com/angelaL8a) All Rights Reserved

<p align="center">
  <img src="https://yourimageurl.com/final_logo.png" alt="Final Logo" width="120">
</p>
