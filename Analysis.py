# analysis.py

def show_basic_info(df):
    print("First 5 rows:")
    print(df.head())

    print("\nMissing values:")
    print(df.isnull().sum())


def gender_analysis(df):
    print("\nGender count:")
    print(df['sex'].value_counts())


def region_analysis(df):
    print("\nTop regions:")
    print(df['region'].value_counts().head())


def recovery_analysis(df):
    print("\nAverage recovery time:")
    print(df['recovery_days'].mean())