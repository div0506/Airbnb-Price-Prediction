
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv('listings.csv')

# Clean and select columns
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
df = df[['neighbourhood_group', 'room_type', 'price',
         'minimum_nights', 'number_of_reviews',
         'reviews_per_month', 'calculated_host_listings_count',
         'availability_365']]
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
df = df[(df['price'] > 10) & (df['price'] < 1000)]
df = pd.get_dummies(df, columns=['neighbourhood_group', 'room_type'], drop_first=True)

X = df.drop('price', axis=1)
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save column order
with open('model_columns.pkl', 'wb') as f:
    pickle.dump(X.columns.tolist(), f)
