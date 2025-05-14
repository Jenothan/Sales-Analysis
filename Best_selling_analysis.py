from Read_Data import ReadData

class Best_selling_analysis(ReadData):
    """Class to analyze best-selling products."""

    def analysis(self, data):
        """Returns top 10 best-selling products."""
        product_analysis = data.groupby('ProductName')['Quantit'].sum().nlargest(10)
        return product_analysis
    

    