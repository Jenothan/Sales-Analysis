import pandas as pd
from Read_Data import ReadData

class Product_performance_analysis(ReadData):
    """Class to analyze product performance over time."""

    def analysis(self, data):
        data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y', errors='coerce')
        product_performance = data.groupby([pd.Grouper(key='Date', freq='ME'), 'ProductName'])['Quantity'].sum().reset_index()
        return product_performance.sort_values(['Date', 'ProductName']).reset_index(drop=True)