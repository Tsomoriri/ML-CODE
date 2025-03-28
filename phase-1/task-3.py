"""
Task 1.3: Pandas DataFrame Fluency: Master data loading (pd.read_csv), cleaning (.fillna, .dropna), filtering (.loc, .iloc), transformation (.apply, .map), grouping (.groupby, .agg), merging (pd.merge, pd.concat) from memory.

    Goal: Make DataFrame manipulation second nature. Memorize the core API.
Task 1.3: Pandas DataFrame Fluency: Master data loading (pd.read_csv), cleaning (.fillna, .dropna), filtering (.loc, .iloc), transformation (.apply, .map), grouping (.groupby, .agg), merging (pd.merge, pd.concat) from memory.

    Goal: Make DataFrame manipulation second nature. Memorize the core API.
"""
"""
Scenario: Assume you are working with two datasets:

    sales.csv: Contains sales transaction data. Columns: OrderID, Product, Category, Price, Quantity, Date (YYYY-MM-DD format), CustomerID. Might contain missing values.
    customers.csv: Contains customer information. Columns: CustomerID, CustomerName, City, JoinDate.

(Suggestion: Create small, sample CSV files with these structures to actually run the code.)

Task 1.3: Pandas DataFrame Fluency Questions

    Loading Data (pd.read_csv):
        Load sales.csv into a Pandas DataFrame called sales_df. Ensure the Date column is correctly parsed as datetime objects during loading.
        Load customers.csv into a DataFrame called customers_df.
        Display the first 5 rows (.head()), the last 3 rows (.tail()), and the data types (.info()) of sales_df.

    Inspecting Data (.describe, .shape, .columns):
        Get summary statistics for the numerical columns in sales_df (.describe()).
        What are the dimensions (rows, columns) of sales_df (.shape)?
        List the column names of customers_df (.columns).

    Handling Missing Values (.isnull, .sum, .dropna):
        Check how many missing values (NaN) exist in each column of sales_df (.isnull().sum()).
        Create a new DataFrame sales_cleaned_df by dropping rows from sales_df where either Price or Quantity is missing (.dropna()).

    Handling Missing Values (.fillna):
        In the original sales_df, fill any missing CustomerID values with the integer 0.
        Fill any remaining missing Price values with the mean price of all products in sales_df.

    Filtering with Boolean Indexing (.loc):
        Select all rows from sales_cleaned_df where the Category is 'Electronics'.
        Select all rows where Quantity is greater than 5.

    Filtering with .loc (Labels & Conditions):
        Select rows where OrderID is one of [1001, 1005, 1010] AND Quantity is greater than 1. Show only the Product and Price columns for these rows. (Requires OrderID to be suitable for direct selection or use .isin()).
        Select all columns for rows where the index (assume default integer index) is between 50 and 60 (inclusive).

    Filtering with .iloc (Integer Position):
        Select the first 5 rows and the first 4 columns of sales_cleaned_df.
        Select the row at integer position 10 and the column at integer position 2.
        Select the last 3 rows and the last 2 columns.

    Column Creation (Direct Assignment):
        In sales_cleaned_df, create a new column called TotalSale which is the product of the Price and Quantity columns.

    Transformation (.map):
        You have a dictionary mapping product categories to a rating: category_rating = {'Electronics': 5, 'Clothing': 4, 'Groceries': 3, 'Books': 4}. Create a new CategoryRating column in sales_cleaned_df by applying this mapping to the Category column using .map(). Assign a default rating of 2 for categories not in the dictionary.

    Transformation (.apply):
        Write a Python function discount_price(price, threshold=100, discount_factor=0.9) that applies a 10% discount if the price is above a threshold.
        Create a new DiscountedPrice column in sales_cleaned_df by applying this function to the Price column using .apply().

    Type Conversion (.astype):
        Assume the CustomerID column in sales_cleaned_df is currently a float (due to NaNs before filling). Convert it to an integer type.
        Convert the Price column to a string type.

    Grouping and Aggregation (.groupby, .agg - Single):
        Group sales_cleaned_df by Category and calculate the total Quantity sold within each category.
        Find the average Price for each Product.

    Grouping and Aggregation (.groupby, .agg - Multiple):
        Group sales_cleaned_df by Category and calculate:
            The sum of TotalSale.
            The average Price.
            The number of unique Products within that category.
        Use .agg() and provide meaningful names for the resulting aggregated columns (e.g., using a dictionary like {'TotalSale': 'sum', 'Price': 'mean', 'Product': 'nunique'}).

    Grouping (.size, .count):
        Calculate the number of sales transactions per CustomerID using .groupby().size().
        Calculate the number of non-null Price entries for each Category using .groupby().count().

    Merging DataFrames (pd.merge - Inner Join):
        Merge sales_cleaned_df with customers_df based on the CustomerID column. Only include rows where the CustomerID exists in both DataFrames. Store the result in merged_inner_df.

    Merging DataFrames (pd.merge - Left Join):
        Merge sales_cleaned_df (left) with customers_df (right) based on CustomerID. Include all rows from sales_cleaned_df and the corresponding customer info if available, otherwise NaN for customer columns. Store the result in merged_left_df. Check for NaNs in the columns originating from customers_df.

    Concatenating DataFrames (pd.concat):
        Imagine you have a second DataFrame sales_new_df (create a small sample) with the same columns as sales_cleaned_df. Create a combined_sales_df by stacking sales_cleaned_df and sales_new_df vertically. Ensure the index is reset appropriately (ignore_index=True).

    Handling Duplicates (.duplicated, .drop_duplicates):
        Check if there are any completely duplicate rows in combined_sales_df (.duplicated().sum()).
        Create a new DataFrame unique_sales_df by removing duplicate rows, keeping the first occurrence (.drop_duplicates()).

    String Manipulation (.str accessor):
        In unique_sales_df, ensure the Product column has no leading/trailing whitespace (.str.strip()).
        Find all sales records where the CustomerName (in merged_left_df) starts with the letter 'A' (.str.startswith()).
        Create a boolean column IsElectronics which is True if the Category column contains the word 'Electronics' (case-insensitive, .str.contains()).

    Date/Time Operations (.dt accessor):
        In unique_sales_df (ensure 'Date' is datetime type), create new columns: SaleYear, SaleMonth, SaleDayOfWeek using the .dt accessor.
        Filter unique_sales_df to show only sales that occurred after '2024-01-01'. Use the 'Date' column for comparison.
    """
