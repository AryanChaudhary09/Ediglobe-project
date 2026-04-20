# plots.py

import matplotlib.pyplot as plt

def plot_gender(df):
    df['sex'].value_counts().plot(kind='bar')
    plt.title("Gender Distribution")
    plt.show()


def plot_age(df):
    df['age'].plot(kind='hist')
    plt.title("Age Distribution")
    plt.show()


def plot_region(df):
    df['region'].value_counts().head().plot(kind='bar')
    plt.title("Top Regions")
    plt.show()


def plot_recovery(df):
    df['recovery_days'].plot(kind='hist')
    plt.title("Recovery Time")
    plt.show()