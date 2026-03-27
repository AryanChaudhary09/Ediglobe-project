# Linear Regression:

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def run_linear_regression(df):


    df = df[['age', 'contact_number', 'recovery_days']].dropna()

    
    X = df[['age', 'contact_number']]
    y = df['recovery_days']

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LinearRegression()

    
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    print("\nModel Score (R^2):", score)

    return model