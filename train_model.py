import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib

print("Loading data...")
# 1. Dataset Load Karna
df = pd.read_csv('rural_crop_data.csv')

# 2. Features (Input: X) aur Target (Output: y) define karna
X = df.drop('Price_per_Quintal', axis=1)
y = df['Price_per_Quintal']

# 3. Data Preprocessing (Categorical to Numeric)
# ML models sirf numbers samajhte hain, isliye State, Region, Crop ko numbers mein badalna zaroori hai.
categorical_features = ['State', 'Region', 'Crop']
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# ColumnTransformer sirf un columns ko change karega jo humne bataye hain, baaki (Rainfall, Temp) ko waise hi chhod dega.
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features)
    ], remainder='passthrough' 
)

# 4. Machine Learning Pipeline Banana (Software Engineering Best Practice!)
# Yeh pipeline pehle data ko transform karegi, fir RandomForest model par bhejegi.
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# 5. Data ko Train (80%) aur Test (20%) mein divide karna
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training the Random Forest model...")
# 6. Model ko Train Karna
model_pipeline.fit(X_train, y_train)

# Model ki accuracy check karte hain (R-squared score)
score = model_pipeline.score(X_test, y_test)
print(f"Model Accuracy (R^2 Score) on Test Data: {round(score * 100, 2)}%")

# 7. Model Save Karna (Taaki API use kar sake)
joblib.dump(model_pipeline, 'crop_price_model.joblib')
print("Model successfully trained and saved as 'crop_price_model.joblib'!")