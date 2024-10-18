import requests
import pandas as pd

# Sample data scraping from a mock API
url = 'https://www.kaggle.com/datasets/prasad22/retail-transactions-dataset'
response = requests.get(url)
data = response.json()

# Convert the scraped data into a DataFrame
df = pd.DataFrame(data)
print(df.head())  # Inspect the data



