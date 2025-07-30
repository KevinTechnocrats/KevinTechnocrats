# Function Reference Guide

Quick reference for all public functions in the Data Analysis Module.

## Data Creation Functions

### `create_sample_data()`
```python
def create_sample_data() -> Dict[str, List[Any]]
```
**Purpose:** Creates predefined sample data dictionary  
**Returns:** Dictionary with 'Name' and 'Age' keys  
**Use Case:** Testing, demonstrations, prototyping

### `create_custom_data(names, ages)`
```python
def create_custom_data(names: List[str], ages: List[int]) -> Dict[str, List[Any]]
```
**Purpose:** Creates custom data dictionary with validation  
**Parameters:**
- `names`: List of string names
- `ages`: List of integer ages  
**Returns:** Validated data dictionary  
**Raises:** ValueError, TypeError

## DataFrame Operations

### `create_dataframe(data=None)`
```python
def create_dataframe(data: Optional[Dict[str, List[Any]]] = None) -> pd.DataFrame
```
**Purpose:** Creates pandas DataFrame from data or sample data  
**Parameters:**
- `data`: Optional data dictionary (uses sample if None)  
**Returns:** pandas DataFrame  
**Raises:** ValueError, TypeError, pandas.errors.ParserError

## Analysis Functions

### `display_dataframe_info(df)`
```python
def display_dataframe_info(df: pd.DataFrame) -> None
```
**Purpose:** Displays comprehensive DataFrame information  
**Parameters:**
- `df`: pandas DataFrame to analyze  
**Returns:** None (prints information)  
**Raises:** TypeError

### `filter_dataframe_by_age(df, min_age, max_age=None)`
```python
def filter_dataframe_by_age(df: pd.DataFrame, min_age: int, max_age: Optional[int] = None) -> pd.DataFrame
```
**Purpose:** Filters DataFrame by age range  
**Parameters:**
- `df`: Input DataFrame with 'Age' column
- `min_age`: Minimum age (inclusive)
- `max_age`: Maximum age (inclusive, optional)  
**Returns:** Filtered DataFrame copy  
**Raises:** KeyError, ValueError

## Utility Functions

### `main()`
```python
def main() -> None
```
**Purpose:** Demonstrates all module functionality  
**Returns:** None (executes demo code)  
**Use Case:** Testing, learning, validation

## Quick Usage Patterns

### Basic DataFrame Creation
```python
# Sample data
df = create_dataframe()

# Custom data
data = create_custom_data(['Alice', 'Bob'], [25, 30])
df = create_dataframe(data)
```

### Data Analysis
```python
# Information display
display_dataframe_info(df)

# Age filtering
adults = filter_dataframe_by_age(df, min_age=18)
seniors = filter_dataframe_by_age(df, min_age=65)
working_age = filter_dataframe_by_age(df, min_age=18, max_age=65)
```

### Error Handling
```python
try:
    data = create_custom_data(names, ages)
    df = create_dataframe(data)
    filtered = filter_dataframe_by_age(df, min_age=20)
except (ValueError, TypeError, KeyError) as e:
    # Handle specific errors
    pass
```

## Common Exceptions

| Exception | When Raised | Functions |
|-----------|-------------|-----------|
| `ValueError` | Invalid parameter values | `create_custom_data`, `filter_dataframe_by_age` |
| `TypeError` | Wrong data types | `create_custom_data`, `display_dataframe_info` |
| `KeyError` | Missing required columns | `filter_dataframe_by_age` |

## Import Statements

```python
# Individual functions
from main import create_dataframe, display_dataframe_info, filter_dataframe_by_age

# All functions
from main import *

# For type hints
from typing import Dict, List, Any, Optional
import pandas as pd
```