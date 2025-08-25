# Car Price Prediction using Ridge Regression

This project predicts **car prices** based on features like mileage, engine size, horsepower, weight, and luxury index.  
The focus is on comparing **Ridge Regression** (with cross-validation for alpha tuning) vs **Ordinary Least Squares (OLS)** to handle **multicollinearity** among predictors.


App Link : https://carpriceprediction-jzxwzzzekwgyee9uhwexap.streamlit.app/


---

## 📌 Features Used
- **mileage** (km driven)  
- **engine_size** (liters)  
- **horsepower**  
- **torque**  
- **doors**  
- **airbags**  
- **weight** (kg)  
- **fuel_efficiency** (km/l or mpg)  📈 Key Learning

OLS may overfit when predictors are correlated.

Ridge reduces variance and improves generalization by applying an L2 penalty.

Cross-validation helps find the optimal regularization strength.

📌 Next Steps

Extend with Lasso and ElasticNet for feature selection.

Add a plot of R² vs alpha to visualize the bias–variance tradeoff.

Deploy as a simple web app (Streamlit/Flask) for interactive predictions.
- **brand_score** (reputation index)  
- **luxury_index** (luxury factor score)  

**Target:** `price_k` (car price in thousands)
📊 Output

When you run the script, you’ll see:

Ridge Regression Results:

Optimal alpha (λ) chosen by cross-validation

Intercept and feature coefficients

Test R² score

OLS Regression Results:

Coefficients (no regularization)

Test R² score

Bar Plot:

Visual comparison of Ridge vs OLS coefficients

---
Manoj K
Project repo: car_price_prediction
