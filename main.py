import pandas as pd
from AnalysisFactory import AnalysisFactory

import pandas as pd

# Load dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        if data.empty:
            print("Error: The dataset is empty.")
            return None
        print("Data loaded successfully.")  # Success message when data is loaded correctly
        return data
    except Exception as e:
        print(f"Error: Could not load the data. {e}")  # Error message if loading fails
        return None


def main():
    data = load_data("supermarket_sales.csv")  # Load data here
    
    if data is None:
        print("Exiting the system due to data load failure.")
        return
    
    while True:
        print("\n=== Sales Data Analysis System ===")
        print("1. Best Selling Products Analysis")
        print("2. Customer Behavior Analysis")
        print("3. Product Performance Analysis")
        print("4. Regional Sales Analysis")
        print("5. Exit")
        
        choice = input("Enter the number corresponding to the analysis you want: ")

        analysis_names = {
            '1': "Best Selling Products Analysis",
            '2': "Customer Behavior Analysis",
            '3': "Product Performance Analysis",
            '4': "Regional Sales Analysis"
        }

        if choice in analysis_names:
            print(f"\n=== {analysis_names[choice]} ===")
            analysis = AnalysisFactory.get_analysis(choice)
            results = analysis.analysis(data)
            print("\n=== Analysis Results ===")
            print(results)
            print("\nReturning to the main menu...")
        elif choice == '5':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
