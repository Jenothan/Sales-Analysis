import pandas as pd
from Read_Data import ReadData

class Customer_behavior_analysis(ReadData):
    """Class to analyze customer behavior based on purchases."""

    def analysis(self, data):
        """Tracks customer product preferences over years."""
        data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y', errors='coerce')
        data['Year'] = data['Date'].dt.year
        customer_product_tracking = (data.groupby(['CustomerID', 'ProductName', 'Year'])['Quantity']
                                     .sum().reset_index().sort_values(by='Quantity', ascending=False).head(10))
        return customer_product_tracking
    

    