import pytest
import pandas as pd

from Best_selling_analysis import Best_selling_analysis
from Customer_behavior_analysis import Customer_behavior_analysis
from Product_performance_analysis import Product_performance_analysis
from Regional_sales_analysis import Regional_sales_analysis

# Fixture to load data
@pytest.fixture
def actual_data():  
    return pd.read_csv("supermarket_sales.csv")

class TestAnalysis:   
    def test_best_selling_products(self, actual_data):
        analysis = Best_selling_analysis()
        actual_result = analysis.analysis(actual_data)
        expected_result = (
            actual_data.groupby("ProductName")["Quantity"].sum().nlargest(10)
        )

        pd.testing.assert_series_equal(
            actual_result, expected_result, check_dtype=False,
            obj="BestSellingProductsAnalysis"
        )
    
    def test_customer_behavior(self, actual_data):
        analysis = Customer_behavior_analysis()
        actual_result = analysis.analysis(actual_data)
        actual_data['Date'] = pd.to_datetime(actual_data['Date'], format='%m/%d/%Y', errors='coerce')
        actual_data['Year'] = actual_data['Date'].dt.year
        expected_result = (
            actual_data.groupby(['CustomerID', 'ProductName', 'Year'])['Quantity']
            .sum().reset_index().sort_values(by='Quantity', ascending=False).head(10)
        )

        pd.testing.assert_frame_equal(
            actual_result.reset_index(drop=True),
            expected_result.reset_index(drop=True),
            check_dtype=False,
            obj="CustomerBehaviourAnalysis"
        )
    
    def test_product_performance(self, actual_data):
        analysis = Product_performance_analysis()
        actual_result = analysis.analysis(actual_data)
        actual_data['Date'] = pd.to_datetime(actual_data['Date'], format='%m/%d/%Y', errors='coerce')
        expected_result = (
            actual_data.groupby([pd.Grouper(key='Date', freq='ME'), 'ProductName'])['Quantity']
            .sum().reset_index().sort_values(['Date', 'ProductName']).reset_index(drop=True)
        )

        pd.testing.assert_frame_equal(
            actual_result.reset_index(drop=True),
            expected_result.reset_index(drop=True),
            check_dtype=False,
            obj="ProductPerformanceAnalysis"
        )
    
    def test_regional_sales(self, actual_data):
        analysis = Regional_sales_analysis()
        actual_result = analysis.analysis(actual_data)
        expected_result = (
            actual_data.groupby('Region')['TotalPrice'].sum()
            .reset_index().sort_values(by='TotalPrice', ascending=False).reset_index(drop=True)
        )

        pd.testing.assert_frame_equal(
            actual_result.reset_index(drop=True),
            expected_result.reset_index(drop=True),
            check_dtype=False,
            obj="RegionalSalesAnalysis"
        )
