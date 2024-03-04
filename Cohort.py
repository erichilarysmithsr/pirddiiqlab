import pandas as pd
import numpy as np

# Import the IDPH data
df = pd.read_csv("idph_data.csv")

# Identify the data that is relevant to the study
df = df[["race/ethnicity", "diabetes status", "location"]]

# Clean and prepare the data
df = df.dropna()
df = df.reset_index(drop=True)

# Identify a cohort of study participants
# Use random sampling
np.random.seed(12345)
df = df.sample(n=1000)

# Save the cohort of study participants
df.to_csv("cohort.csv", index=False)
