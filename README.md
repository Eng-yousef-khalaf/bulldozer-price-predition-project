# 🚜 Bulldozer Price Prediction using Linear Regression

A machine learning regression project that predicts the **actual sale price** of bulldozers using historical auction data. This project utilizes a **Linear Regression** model to estimate bulldozer prices based on several machine attributes.

---

## 📌 Objective

The goal of this project is to predict the real-world auction price of bulldozers based on features such as manufacturing year, usage, and product size. Accurate price prediction helps in better valuation and decision-making during auctions or resale.

---

## 🧰 Tools & Technologies Used

- **Python**
- **Pandas** and **NumPy** for data manipulation
- **Scikit-learn** for model building and evaluation

---

## 📊 Dataset

The dataset `bulldozer_data.csv` contains historical information on bulldozer auctions, including:

- `YearMade` – Manufacturing year  
- `MachineHoursCurrentMeter` – Total usage hours  
- `UsageBand` – Usage category (Low, Medium, High)  
- `ProductSize` – Size classification of the bulldozer  
- `SalePrice` – The actual target price to predict  

---

## 🧪 Project Workflow

1. **Data Loading & Cleaning**  
   Load CSV file and handle missing values

2. **Feature Engineering**  
   Convert categorical features using one-hot encoding

3. **Train-Test Split**  
   Use 80% for training and 20% for testing

4. **Model Building**  
   Train a `LinearRegression` model

5. **Evaluation**  
   Calculate the **Mean Squared Error (MSE)** as a performance metric

---

## ✅ Results

The model predicts continuous sale prices for bulldozers based on historical data. The mean squared error (MSE) is printed as a basic performance indicator.

---

## 📦 How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/Eng-yousef-khalaf/bulldozer-price-regression-project.git
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn
   ```
3. Make sure `bulldozer_data.csv` is in the project folder.
4. Run the Python script:
   ```bash
   python bulldozer_price_prediction.py
   ```

---

## 📄 License

This project is licensed under the MIT License.
