# model.py

from sklearn.linear_model import LinearRegression

def simple_model(df):
    df = df.dropna()

    X = df[['age']]
    y = df['recovery_days']

    model = LinearRegression()
    model.fit(X, y)

    print("\nModel trained using age to predict recovery time")