# main.py

from src.cleaning import load_data, clean_data, add_recovery_days
from src.analysis import *
from src.plots import *
from src.model import simple_model

# load data
df = load_data()

# clean data
df = clean_data(df)
df = add_recovery_days(df)

# analysis
show_basic_info(df)
gender_analysis(df)
region_analysis(df)
recovery_analysis(df)

# plots
plot_gender(df)
plot_age(df)
plot_region(df)
plot_recovery(df)

# model
simple_model(df)