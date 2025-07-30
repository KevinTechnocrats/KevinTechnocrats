# Data Analysis Module - API Documentation

## Overview

The Data Analysis Module provides a comprehensive set of utilities for creating, manipulating, and analyzing pandas DataFrames. This module is designed to serve as a foundation for data processing workflows and demonstrates best practices for data analysis operations.

**Version:** 1.0.0  
**Author:** Data Analysis Team  
**Dependencies:** pandas>=2.0.0, typing-extensions>=4.0.0

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [API Reference](#api-reference)
   - [Data Creation Functions](#data-creation-functions)
   - [DataFrame Operations](#dataframe-operations)
   - [Analysis Functions](#analysis-functions)
   - [Utility Functions](#utility-functions)
4. [Examples](#examples)
5. [Error Handling](#error-handling)
6. [Best Practices](#best-practices)

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
import pandas as pd
from main import create_dataframe, display_dataframe_info, filter_dataframe_by_age

# Create a DataFrame with sample data
df = create_dataframe()
print(df)

# Display comprehensive information
display_dataframe_info(df)

# Filter data by age
adults = filter_dataframe_by_age(df, min_age=18)
print(adults)
```

## API Reference

### Data Creation Functions

#### `create_sample_data()`

Creates a predefined sample dataset for demonstration and testing purposes.

**Signature:**
```python
def create_sample_data() -> Dict[str, List[Any]]
```

**Returns:**
- `Dict[str, List[Any]]`: Dictionary containing sample data with 'Name' and 'Age' keys

**Example:**
```python
data = create_sample_data()
print(data)
# Output: {'Name': ['ankit', 'vinod', 'rakesh'], 'Age': [12, 34, 56]}
```

**Use Cases:**
- Quick prototyping and testing
- Demonstration purposes
- Initial data exploration

---

#### `create_custom_data(names, ages)`

Creates a custom data dictionary with user-provided names and ages, including comprehensive validation.

**Signature:**
```python
def create_custom_data(names: List[str], ages: List[int]) -> Dict[str, List[Any]]
```

**Parameters:**
- `names` (List[str]): List of names as strings
- `ages` (List[int]): List of ages as integers

**Returns:**
- `Dict[str, List[Any]]`: Dictionary containing the provided data

**Raises:**
- `ValueError`: If names and ages lists have different lengths
- `TypeError`: If names contains non-string values or ages contains non-integer values

**Example:**
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
data = create_custom_data(names, ages)
print(data)
# Output: {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
```

**Validation Features:**
- Length matching between names and ages
- Type validation for all elements
- Comprehensive error messages

---

### DataFrame Operations

#### `create_dataframe(data=None)`

Creates a pandas DataFrame from provided data or uses sample data as default.

**Signature:**
```python
def create_dataframe(data: Optional[Dict[str, List[Any]]] = None) -> pd.DataFrame
```

**Parameters:**
- `data` (Optional[Dict[str, List[Any]]]): Dictionary containing data for DataFrame. If None, uses sample data.

**Returns:**
- `pd.DataFrame`: A pandas DataFrame containing the specified data

**Raises:**
- `ValueError`: If data dictionary is empty or contains invalid structure
- `TypeError`: If data is not a dictionary
- `pandas.errors.ParserError`: If data cannot be converted to DataFrame

**Examples:**

*Using default sample data:*
```python
df = create_dataframe()
print(df)
#    Name  Age
# 0  ankit   12
# 1  vinod   34
# 2  rakesh  56
```

*Using custom data:*
```python
custom_data = {'Name': ['John', 'Jane'], 'Age': [28, 32]}
df = create_dataframe(custom_data)
print(df)
#   Name  Age
# 0  John   28
# 1  Jane   32
```

**Features:**
- Automatic logging of DataFrame creation
- Comprehensive error handling
- Flexible input handling

---

### Analysis Functions

#### `display_dataframe_info(df)`

Displays comprehensive information about a pandas DataFrame including statistics, data types, and structure.

**Signature:**
```python
def display_dataframe_info(df: pd.DataFrame) -> None
```

**Parameters:**
- `df` (pd.DataFrame): The DataFrame to analyze and display

**Returns:**
- `None`: This function prints information and doesn't return anything

**Raises:**
- `TypeError`: If input is not a pandas DataFrame

**Example:**
```python
df = create_dataframe()
display_dataframe_info(df)
```

**Output:**
```
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

=== No Missing Values Found ===
```

**Information Displayed:**
- DataFrame shape and structure
- Column names and data types
- First 5 rows preview
- Statistical summary
- Missing value analysis

---

#### `filter_dataframe_by_age(df, min_age, max_age=None)`

Filters DataFrame by age range with flexible range specification.

**Signature:**
```python
def filter_dataframe_by_age(df: pd.DataFrame, min_age: int, max_age: Optional[int] = None) -> pd.DataFrame
```

**Parameters:**
- `df` (pd.DataFrame): Input DataFrame containing an 'Age' column
- `min_age` (int): Minimum age (inclusive)
- `max_age` (Optional[int]): Maximum age (inclusive). If None, no upper limit

**Returns:**
- `pd.DataFrame`: Filtered DataFrame containing only rows within age range

**Raises:**
- `KeyError`: If 'Age' column doesn't exist in the DataFrame
- `ValueError`: If min_age is negative or max_age is less than min_age

**Examples:**

*Filter for adults (ages 18 and above):*
```python
df = create_dataframe()
adults = filter_dataframe_by_age(df, min_age=18)
print(adults)
#     Name  Age
# 1  vinod   34
# 2  rakesh  56
```

*Filter for specific age range:*
```python
middle_aged = filter_dataframe_by_age(df, min_age=30, max_age=50)
print(middle_aged)
#     Name  Age
# 1  vinod   34
```

*Handle empty results:*
```python
seniors = filter_dataframe_by_age(df, min_age=60)
print(f"Seniors found: {len(seniors)}")
# Output: Seniors found: 0
```

**Features:**
- Flexible age range filtering
- Automatic logging of filter operations
- Comprehensive input validation
- Returns a copy to prevent data modification

---

### Utility Functions

#### `main()`

Demonstration function showcasing the usage of all module functions with comprehensive examples.

**Signature:**
```python
def main() -> None
```

**Returns:**
- `None`: Executes demonstration code and displays results

**Example:**
```python
main()
```

**Demonstrates:**
- Sample DataFrame creation
- Custom data handling
- Information display
- Filtering operations
- Error handling patterns

---

## Examples

### Basic Usage

```python
from main import create_dataframe, display_dataframe_info

# Create DataFrame with default data
df = create_dataframe()
display_dataframe_info(df)
```

### Custom Data Processing

```python
from main import create_custom_data, create_dataframe, filter_dataframe_by_age

# Create custom dataset
names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
ages = [22, 25, 30, 35, 28]
data = create_custom_data(names, ages)

# Create DataFrame
df = create_dataframe(data)

# Filter for people in their thirties
thirties = filter_dataframe_by_age(df, min_age=30, max_age=39)
print("People in their thirties:")
print(thirties)
```

### Error Handling Example

```python
from main import create_custom_data

try:
    # This will raise a ValueError
    data = create_custom_data(['Alice'], [25, 30])
except ValueError as e:
    print(f"Error: {e}")
    # Handle the error appropriately

try:
    # This will raise a TypeError
    data = create_custom_data(['Alice', 123], [25, 30])
except TypeError as e:
    print(f"Type Error: {e}")
    # Handle the error appropriately
```

### Advanced Filtering

```python
from main import create_dataframe, filter_dataframe_by_age

# Create sample data
df = create_dataframe()

# Multiple filtering operations
minors = filter_dataframe_by_age(df, min_age=0, max_age=17)
adults = filter_dataframe_by_age(df, min_age=18, max_age=64)
seniors = filter_dataframe_by_age(df, min_age=65)

print(f"Minors: {len(minors)}")
print(f"Adults: {len(adults)}")
print(f"Seniors: {len(seniors)}")
```

## Error Handling

The module provides comprehensive error handling with specific exception types:

### Common Exceptions

1. **ValueError**: Raised for invalid parameter values
   - Mismatched list lengths in `create_custom_data()`
   - Negative ages in filtering functions
   - Empty data dictionaries

2. **TypeError**: Raised for incorrect data types
   - Non-string values in names list
   - Non-integer values in ages list
   - Non-DataFrame inputs to analysis functions

3. **KeyError**: Raised when required columns are missing
   - Missing 'Age' column in filtering operations

### Error Handling Best Practices

```python
import logging
from main import create_custom_data, filter_dataframe_by_age

# Set up logging to capture module logs
logging.basicConfig(level=logging.INFO)

try:
    # Your data processing code here
    data = create_custom_data(['Alice', 'Bob'], [25, 30])
    df = create_dataframe(data)
    filtered = filter_dataframe_by_age(df, min_age=20)
except (ValueError, TypeError, KeyError) as e:
    logging.error(f"Data processing error: {e}")
    # Handle error appropriately
except Exception as e:
    logging.error(f"Unexpected error: {e}")
    raise
```

## Best Practices

### 1. Data Validation
Always validate your input data before processing:

```python
def validate_input_data(names, ages):
    if not isinstance(names, list) or not isinstance(ages, list):
        raise TypeError("Names and ages must be lists")
    
    if len(names) != len(ages):
        raise ValueError("Names and ages must have the same length")
    
    return create_custom_data(names, ages)
```

### 2. Logging
Enable logging to track operations:

```python
import logging
logging.basicConfig(level=logging.INFO)

# Module functions will automatically log their operations
df = create_dataframe()  # This will log DataFrame creation
```

### 3. Memory Management
For large datasets, consider memory usage:

```python
# Use copy() when returning filtered DataFrames to prevent memory leaks
filtered_df = filter_dataframe_by_age(df, min_age=25)
# The function already returns a copy, but be aware of this pattern
```

### 4. Type Hints
Always use type hints for better code documentation:

```python
from typing import Dict, List, Any, Optional
import pandas as pd

def my_analysis_function(df: pd.DataFrame) -> Dict[str, Any]:
    # Your analysis code here
    return {"result": "analysis_complete"}
```

### 5. Error Recovery
Implement graceful error recovery:

```python
def safe_data_processing(names, ages):
    try:
        data = create_custom_data(names, ages)
        return create_dataframe(data)
    except (ValueError, TypeError) as e:
        print(f"Using sample data due to error: {e}")
        return create_dataframe()  # Fallback to sample data
```

## Performance Considerations

- **DataFrame Creation**: The module creates copies of filtered DataFrames to prevent unintended modifications
- **Memory Usage**: For large datasets, consider processing data in chunks
- **Logging**: Disable logging in production for better performance if needed

## Contributing

When extending this module:

1. Follow the existing docstring format
2. Include comprehensive type hints
3. Add logging statements for debugging
4. Provide usage examples in docstrings
5. Implement proper error handling
6. Write unit tests for new functions

## Version History

- **1.0.0**: Initial release with basic DataFrame operations and filtering capabilities