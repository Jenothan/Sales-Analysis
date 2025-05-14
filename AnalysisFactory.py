from Best_selling_analysis import Best_selling_analysis
from Customer_behavior_analysis import Customer_behavior_analysis
from Product_performance_analysis import Product_performance_analysis
from Regional_sales_analysis import Regional_sales_analysis

class AnalysisFactory:
    @staticmethod
    def get_analysis(analysis_type):
        if analysis_type == '1':
            return Best_selling_analysis()
        elif analysis_type == '2':
            return Customer_behavior_analysis()
        elif analysis_type == '3':
            return Product_performance_analysis()
        elif analysis_type == '4':
            return Regional_sales_analysis()
        else:
            return None
        

        