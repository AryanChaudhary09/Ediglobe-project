# Main File

from src.cleaning import load_data, clean_data, add_recovery_days
from src.analysis import *
from src.plots import *
from src.model import simple_model

# Loading data
df = load_data()

# Cleaning data
df = clean_data(df)
df = add_recovery_days(df)

# Analysis
show_basic_info(df)
gender_analysis(df)
region_analysis(df)
recovery_analysis(df)

# Plots
plot_gender(df)
plot_age(df)
plot_region(df)
plot_recovery(df)

# Model
simple_model(df)

#Linear Regression
from src.model import run_linear_regression
run_linear_regression(df)