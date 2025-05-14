from Read_Data import ReadData

class Regional_sales_analysis(ReadData):
    """Class to analyze sales by region."""

    def analysis(self, data):
        regional_sales = data.groupby('Region')['TotalPrice'].sum().reset_index().sort_values(by='TotalPrice', ascending=False)
        return regional_sales