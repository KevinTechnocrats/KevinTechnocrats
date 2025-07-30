"""
Data Analysis Module

This module provides utilities for creating and manipulating pandas DataFrames
with sample data. It demonstrates basic data analysis operations and serves
as a foundation for data processing workflows.

Author: Data Analysis Team
Version: 1.0.0
"""

import pandas as pd
from typing import Dict, List, Any, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_sample_data() -> Dict[str, List[Any]]:
    """
    Create sample data dictionary for DataFrame creation.
    
    This function generates a predefined dataset containing personal information
    including names and ages. The data is structured as a dictionary with
    string keys and list values, suitable for pandas DataFrame creation.
    
    Returns:
        Dict[str, List[Any]]: A dictionary containing:
            - 'Name': List of string names
            - 'Age': List of integer ages
    
    Examples:
        >>> data = create_sample_data()
        >>> print(data)
        {'Name': ['ankit', 'vinod', 'rakesh'], 'Age': [12, 34, 56]}
        
        >>> # Use with pandas DataFrame
        >>> import pandas as pd
        >>> df = pd.DataFrame(data)
        >>> print(df.head())
           Name  Age
        0  ankit   12
        1  vinod   34
        2  rakesh  56
    
    Note:
        This function returns static sample data. For dynamic data generation,
        consider using create_custom_data() function instead.
    """
    logger.info("Creating sample data dictionary")
    return {
        'Name': ['ankit', 'vinod', 'rakesh'],
        'Age': [12, 34, 56]
    }


def create_custom_data(names: List[str], ages: List[int]) -> Dict[str, List[Any]]:
    """
    Create custom data dictionary with provided names and ages.
    
    This function allows users to create their own dataset by providing
    custom lists of names and ages. It validates input lengths and creates
    a properly formatted dictionary for DataFrame creation.
    
    Args:
        names (List[str]): List of names as strings
        ages (List[int]): List of ages as integers
    
    Returns:
        Dict[str, List[Any]]: A dictionary containing the provided data
    
    Raises:
        ValueError: If names and ages lists have different lengths
        TypeError: If names contains non-string values or ages contains non-integer values
    
    Examples:
        >>> names = ['Alice', 'Bob', 'Charlie']
        >>> ages = [25, 30, 35]
        >>> data = create_custom_data(names, ages)
        >>> print(data)
        {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
        
        >>> # Error handling example
        >>> try:
        ...     data = create_custom_data(['Alice'], [25, 30])
        ... except ValueError as e:
        ...     print(f"Error: {e}")
        Error: Names and ages lists must have the same length
    """
    logger.info(f"Creating custom data with {len(names)} entries")
    
    # Validate input lengths
    if len(names) != len(ages):
        raise ValueError("Names and ages lists must have the same length")
    
    # Validate data types
    if not all(isinstance(name, str) for name in names):
        raise TypeError("All names must be strings")
    
    if not all(isinstance(age, int) for age in ages):
        raise TypeError("All ages must be integers")
    
    return {
        'Name': names,
        'Age': ages
    }


def create_dataframe(data: Optional[Dict[str, List[Any]]] = None) -> pd.DataFrame:
    """
    Create a pandas DataFrame from provided data or sample data.
    
    This function creates a pandas DataFrame using either provided data
    or default sample data. It includes basic validation and logging
    for better error handling and debugging.
    
    Args:
        data (Optional[Dict[str, List[Any]]]): Dictionary containing data for DataFrame.
            If None, uses sample data from create_sample_data().
    
    Returns:
        pd.DataFrame: A pandas DataFrame containing the specified data
    
    Raises:
        ValueError: If data dictionary is empty or contains invalid structure
        pandas.errors.ParserError: If data cannot be converted to DataFrame
    
    Examples:
        >>> # Using default sample data
        >>> df = create_dataframe()
        >>> print(df)
           Name  Age
        0  ankit   12
        1  vinod   34
        2  rakesh  56
        
        >>> # Using custom data
        >>> custom_data = {'Name': ['John', 'Jane'], 'Age': [28, 32]}
        >>> df = create_dataframe(custom_data)
        >>> print(df)
           Name  Age
        0  John   28
        1  Jane   32
        
        >>> # Get DataFrame info
        >>> print(f"Shape: {df.shape}")
        >>> print(f"Columns: {list(df.columns)}")
        Shape: (2, 2)
        Columns: ['Name', 'Age']
    """
    if data is None:
        logger.info("No data provided, using sample data")
        data = create_sample_data()
    
    # Validate data structure
    if not data:
        raise ValueError("Data dictionary cannot be empty")
    
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    
    try:
        df = pd.DataFrame(data)
        logger.info(f"DataFrame created successfully with shape {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Failed to create DataFrame: {e}")
        raise


def display_dataframe_info(df: pd.DataFrame) -> None:
    """
    Display comprehensive information about a pandas DataFrame.
    
    This function prints detailed information about a DataFrame including
    basic statistics, data types, shape, and sample data. Useful for
    data exploration and debugging.
    
    Args:
        df (pd.DataFrame): The DataFrame to analyze and display
    
    Returns:
        None: This function prints information and doesn't return anything
    
    Examples:
        >>> df = create_dataframe()
        >>> display_dataframe_info(df)
        === DataFrame Information ===
        Shape: (3, 2)
        Columns: ['Name', 'Age']
        Data Types:
        Name    object
        Age      int64
        dtype: object
        
        === First 5 Rows ===
           Name  Age
        0  ankit   12
        1  vinod   34
        2  rakesh  56
        
        === Basic Statistics ===
               Age
        count   3.0
        mean   34.0
        std    22.0
        min    12.0
        25%    23.0
        50%    34.0
        75%    45.0
        max    56.0
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    print("=== DataFrame Information ===")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("Data Types:")
    print(df.dtypes)
    
    print("\n=== First 5 Rows ===")
    print(df.head())
    
    print("\n=== Basic Statistics ===")
    print(df.describe())
    
    # Check for missing values
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("\n=== Missing Values ===")
        print(missing_values[missing_values > 0])
    else:
        print("\n=== No Missing Values Found ===")


def filter_dataframe_by_age(df: pd.DataFrame, min_age: int, max_age: Optional[int] = None) -> pd.DataFrame:
    """
    Filter DataFrame by age range.
    
    This function filters the input DataFrame to include only rows where
    the age falls within the specified range. Useful for demographic
    analysis and data segmentation.
    
    Args:
        df (pd.DataFrame): Input DataFrame containing an 'Age' column
        min_age (int): Minimum age (inclusive)
        max_age (Optional[int]): Maximum age (inclusive). If None, no upper limit
    
    Returns:
        pd.DataFrame: Filtered DataFrame containing only rows within age range
    
    Raises:
        KeyError: If 'Age' column doesn't exist in the DataFrame
        ValueError: If min_age is negative or max_age is less than min_age
    
    Examples:
        >>> df = create_dataframe()
        >>> # Filter for ages 20 and above
        >>> adults = filter_dataframe_by_age(df, min_age=20)
        >>> print(adults)
           Name  Age
        1  vinod   34
        2  rakesh  56
        
        >>> # Filter for ages between 30 and 50
        >>> middle_aged = filter_dataframe_by_age(df, min_age=30, max_age=50)
        >>> print(middle_aged)
           Name  Age
        1  vinod   34
        
        >>> # Handle empty results
        >>> seniors = filter_dataframe_by_age(df, min_age=60)
        >>> print(f"Seniors found: {len(seniors)}")
        Seniors found: 0
    """
    if 'Age' not in df.columns:
        raise KeyError("DataFrame must contain an 'Age' column")
    
    if min_age < 0:
        raise ValueError("Minimum age cannot be negative")
    
    if max_age is not None and max_age < min_age:
        raise ValueError("Maximum age cannot be less than minimum age")
    
    # Apply age filter
    if max_age is None:
        filtered_df = df[df['Age'] >= min_age]
        logger.info(f"Filtered DataFrame for ages >= {min_age}: {len(filtered_df)} rows")
    else:
        filtered_df = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]
        logger.info(f"Filtered DataFrame for ages {min_age}-{max_age}: {len(filtered_df)} rows")
    
    return filtered_df.copy()


def main() -> None:
    """
    Main function demonstrating the usage of all module functions.
    
    This function serves as an example of how to use all the functions
    in this module. It creates sample data, converts it to a DataFrame,
    displays information, and performs filtering operations.
    
    Examples:
        >>> # Run the main function
        >>> main()
        # This will execute all demonstration code and display results
    """
    try:
        print("=== Data Analysis Module Demo ===\n")
        
        # Create and display sample DataFrame
        print("1. Creating sample DataFrame:")
        df = create_dataframe()
        print(df)
        print()
        
        # Display DataFrame information
        print("2. DataFrame Information:")
        display_dataframe_info(df)
        print()
        
        # Demonstrate custom data creation
        print("3. Creating custom DataFrame:")
        custom_names = ['Alice', 'Bob', 'Charlie', 'Diana']
        custom_ages = [25, 30, 35, 28]
        custom_data = create_custom_data(custom_names, custom_ages)
        custom_df = create_dataframe(custom_data)
        print(custom_df)
        print()
        
        # Demonstrate filtering
        print("4. Filtering by age (>= 30):")
        filtered_df = filter_dataframe_by_age(custom_df, min_age=30)
        print(filtered_df)
        print()
        
        print("5. Filtering by age range (25-32):")
        range_filtered_df = filter_dataframe_by_age(custom_df, min_age=25, max_age=32)
        print(range_filtered_df)
        
    except Exception as e:
        logger.error(f"Error in main function: {e}")
        raise


if __name__ == "__main__":
    main()