import pandas as pd
import random

states = ['Uttar Pradesh', 'Madhya Pradesh', 'Punjab', 'Maharashtra', 'Bihar']
regions = ['Azamgarh', 'Lucknow', 'Varanasi', 'Kanpur', 'Pune', 'Patna', 'Bhopal'] 
crops = ['Wheat', 'Rice', 'Sugarcane', 'Mustard', 'Potato']

data = []

print("Generating 1000 records of rural crop data...")

for _ in range(1000):
    state = random.choice(states)
    region = random.choice(regions)
    crop = random.choice(crops)
    
    rainfall = round(random.uniform(50.0, 200.0), 2)
    temperature = round(random.uniform(15.0, 40.0), 2)
    
    base_price = random.randint(1500, 3500)
    price = base_price + (temperature * 12) - (rainfall * 3)
    
    data.append([state, region, crop, rainfall, temperature, round(price, 2)])

df = pd.DataFrame(data, columns=['State', 'Region', 'Crop', 'Rainfall_mm', 'Temperature_C', 'Price_per_Quintal'])
df.to_csv('rural_crop_data.csv', index=False)

print("Data successfully generated and saved as 'rural_crop_data.csv'!")