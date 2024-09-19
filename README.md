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

![Launch Success](https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/9.png)
![Launch Success](https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/13.png)
![Launch Success](https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/16.png)
![Launch Success](https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/19.png)
![Launch Success](https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/22.png)
![Launch Success](https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/25.png)

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

![Launch Success](https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/27.png)
![Launch Success](https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/36.png)
![Launch Success](https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/50.png)
![Launch Success](https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/64.png)

### Key Insights:

- **Highest Success Rate Launch Site**: 🚀 **KSC-LC-39A** with a 76.9% success rate.
- **Optimal Payload Range for Success**: 📦 **2,000kg - 6,000kg** has the highest success.
- **Lowest Success Rate Payload**: ⚖️ **7,000kg - 10,000kg** range experiences lower success.
- **Most Reliable Booster Version**: 🔧 **FT version** has demonstrated the highest reliability.

EDA was performed using **Pandas**, **Matplotlib**, and **Seaborn** to visualize these insights. Additionally, we created interactive dashboards using **Plotly** and **Dash** to dynamically explore the data.

---

## 🧠 **Predictive Analysis (Machine Learning)** <a name="ml"></a>

We explored different classification models to predict launch outcomes. Our process included:

1. **Data Preprocessing**:

   → Standardization of features (payload mass, booster version, etc.).  
   → Train-test split (80%-20%) to validate model performance.  

2. **Model Development**:

   → **Support Vector Machines (SVM)**  
   → **Decision Trees**  
   → **Logistic Regression**  
   → **K Nearest Neighbors (KNN)**  

3. **Hyperparameter Tuning**:  
   We performed a grid search over key parameters for each model to ensure optimal performance.

4. **Evaluation**:  
   Models were evaluated using **accuracy** on the train set. Cross-validation was employed to mitigate overfitting.

---

## 📊 **Model Performance** <a name="performance"></a>

| Model                        | Accuracy | 
| ---------------------------- | -------- | 
| Support Vector Machine (SVM) | 0.848214   | 
| Decision Tree                | 0.876786   | 
| Logistic Regression          | 0.846429   | 
| K Nearest Neighbors (KNN)          | 0.848214   | 

**Best Performing Model**: **Decision Tree** with **0.876786 accuracy**, providing the most consistent and reliable predictions for launch success.

---

## 📌 **Conclusion** <a name="conclusion"></a>
![Launch Success](https://github.com/angelaL8a/SpaceX-CapstoneIBM/blob/main/images/70.png)
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

## 📘 Extra Study Materials <a name="extra_study"></a>

Before diving into the labs, it’s highly recommended to review previous concepts and practice them locally on your machine. This not only enhances understanding but also helps reduce the usage of cloud trial versions.

### 📊 Visualization Libraries
- **[Plotly](https://dash.plotly.com/layout)** - A versatile and powerful library for creating interactive visualizations.
- **[Folium](https://python-visualization.github.io/folium/plugins.html)** - Visualize geographical data with ease through interactive maps.

### 🌍 Folium Example Projects
- **[Folium Examples](https://nbviewer.jupyter.org/github/python-visualization/folium/tree/master/examples/)** - Explore practical examples of Folium in action for inspiration and guidance.

### 🤖 Data Science Concepts
- **[Confusion Matrix](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/)** - Master the basics of classification evaluation with this simple guide to confusion matrices.

---

## ✉️ **Contact** <a name="contact"></a>

For more information or collaboration, feel free to reach out:

[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/isonoangelapaola/)
[![GitHub Badge](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/angelaL8a/)

---

#### © 2024 [Angela Paola](https://github.com/angelaL8a) All Rights Reserved

<p align="center">
  <img src="https://yourimageurl.com/final_logo.png" alt="Final Logo" width="120">
</p>
