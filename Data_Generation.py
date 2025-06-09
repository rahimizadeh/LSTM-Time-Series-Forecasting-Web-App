import numpy as np
import pandas as pd

# Generate synthetic time series data
time = np.arange(0, 100, 0.1)
series = np.sin(time) + np.random.normal(0, 0.1, len(time))

# Save as CSV (for later upload testing)
df = pd.DataFrame({'value': series})
df.to_csv('timeseries_data.csv', index=False)