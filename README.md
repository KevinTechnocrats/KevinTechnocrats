# Data Analysis Module

A comprehensive Python module for creating, manipulating, and analyzing pandas DataFrames with built-in validation, logging, and error handling.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/pandas-2.0.0+-green.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- **Easy DataFrame Creation**: Create DataFrames from sample or custom data
- **Comprehensive Validation**: Input validation with detailed error messages
- **Data Analysis Tools**: Built-in functions for data exploration and filtering
- **Logging Support**: Automatic logging for debugging and monitoring
- **Type Safety**: Full type hints for better IDE support and code quality
- **Error Handling**: Robust error handling with specific exception types
- **Extensible Design**: Clean architecture for easy extension and customization

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Functions](#core-functions)
- [Usage Examples](#usage-examples)
- [Documentation](#documentation)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pandas 2.0.0 or higher

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Verify Installation

```python
python main.py
```

This will run the demonstration showing all module capabilities.

## ⚡ Quick Start

```python
from main import create_dataframe, display_dataframe_info, filter_dataframe_by_age

# Create a DataFrame with sample data
df = create_dataframe()
print(df)
#    Name  Age
# 0  ankit   12
# 1  vinod   34
# 2  rakesh  56

# Display comprehensive information
display_dataframe_info(df)

# Filter data by age
adults = filter_dataframe_by_age(df, min_age=18)
print(adults)
#     Name  Age
# 1  vinod   34
# 2  rakesh  56
```

## 🔧 Core Functions

### Data Creation
- `create_sample_data()` - Generate predefined sample data
- `create_custom_data(names, ages)` - Create custom datasets with validation
- `create_dataframe(data=None)` - Convert data to pandas DataFrame

### Data Analysis
- `display_dataframe_info(df)` - Comprehensive DataFrame analysis
- `filter_dataframe_by_age(df, min_age, max_age=None)` - Age-based filtering

### Utilities
- `main()` - Complete demonstration of all features

## 📚 Usage Examples

### Creating Custom Data

```python
from main import create_custom_data, create_dataframe

# Define your data
names = ['Alice', 'Bob', 'Charlie', 'Diana']
ages = [25, 30, 35, 28]

# Create and validate data
data = create_custom_data(names, ages)
df = create_dataframe(data)
print(df)
```

### Advanced Filtering

```python
from main import create_dataframe, filter_dataframe_by_age

df = create_dataframe()

# Filter by minimum age
adults = filter_dataframe_by_age(df, min_age=18)

# Filter by age range
young_adults = filter_dataframe_by_age(df, min_age=18, max_age=30)

# Handle edge cases
seniors = filter_dataframe_by_age(df, min_age=65)
print(f"Found {len(seniors)} seniors")
```

### Error Handling

```python
from main import create_custom_data

try:
    # This will raise a ValueError due to length mismatch
    data = create_custom_data(['Alice'], [25, 30])
except ValueError as e:
    print(f"Validation Error: {e}")
    # Handle error gracefully

try:
    # This will raise a TypeError due to invalid data types
    data = create_custom_data(['Alice', 123], [25, 30])
except TypeError as e:
    print(f"Type Error: {e}")
    # Handle error gracefully
```

### Working with Logging

```python
import logging
from main import create_dataframe

# Enable logging to see internal operations
logging.basicConfig(level=logging.INFO)

# Create DataFrame (will log creation details)
df = create_dataframe()
# Output: INFO:__main__:No data provided, using sample data
# Output: INFO:__main__:DataFrame created successfully with shape (3, 2)
```

## 📖 Documentation

For comprehensive API documentation, including detailed function signatures, parameters, return values, and advanced examples, see:

- **[API Documentation](API_DOCUMENTATION.md)** - Complete API reference
- **[Function Docstrings](main.py)** - Inline documentation with examples

### Key Documentation Sections

1. **[Installation Guide](API_DOCUMENTATION.md#installation)** - Setup and dependencies
2. **[API Reference](API_DOCUMENTATION.md#api-reference)** - Complete function documentation
3. **[Examples](API_DOCUMENTATION.md#examples)** - Practical usage scenarios
4. **[Best Practices](API_DOCUMENTATION.md#best-practices)** - Recommended patterns
5. **[Error Handling](API_DOCUMENTATION.md#error-handling)** - Exception handling guide

## 🔍 Data Analysis Features

### DataFrame Information Display

The `display_dataframe_info()` function provides comprehensive analysis:

```python
df = create_dataframe()
display_dataframe_info(df)
```

**Output includes:**
- DataFrame shape and structure
- Column data types
- Statistical summary
- Missing value analysis
- Sample data preview

### Flexible Filtering

Age-based filtering with multiple options:

```python
# Minimum age only
adults = filter_dataframe_by_age(df, min_age=18)

# Age range
working_age = filter_dataframe_by_age(df, min_age=18, max_age=65)

# Handle empty results gracefully
result = filter_dataframe_by_age(df, min_age=100)
if result.empty:
    print("No records found in age range")
```

## ⚠️ Error Handling

The module provides robust error handling with specific exception types:

### Common Exceptions

- **ValueError**: Invalid parameter values (e.g., mismatched list lengths)
- **TypeError**: Incorrect data types (e.g., non-string names)
- **KeyError**: Missing required columns (e.g., no 'Age' column)

### Best Practices

```python
import logging
from main import create_custom_data, create_dataframe

logging.basicConfig(level=logging.INFO)

try:
    data = create_custom_data(['Alice', 'Bob'], [25, 30])
    df = create_dataframe(data)
except (ValueError, TypeError) as e:
    logging.error(f"Data validation error: {e}")
    # Fallback to sample data
    df = create_dataframe()
except Exception as e:
    logging.error(f"Unexpected error: {e}")
    raise
```

## 🧪 Testing

Run the main function to test all functionality:

```bash
python main.py
```

This executes a comprehensive demonstration including:
- Sample data creation
- Custom data validation
- DataFrame operations
- Filtering examples
- Error handling scenarios

## 🚀 Performance Tips

1. **Memory Management**: Functions return DataFrame copies to prevent unintended modifications
2. **Logging**: Disable logging in production for better performance
3. **Large Datasets**: Consider processing data in chunks for memory efficiency
4. **Type Validation**: Input validation prevents runtime errors but adds overhead

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Install dependencies: `pip install -r requirements.txt`
4. Make your changes with proper documentation
5. Test your changes: `python main.py`
6. Submit a pull request

### Code Standards

- Follow existing docstring format (Google style)
- Include comprehensive type hints
- Add logging for debugging purposes
- Provide usage examples in docstrings
- Implement proper error handling
- Write unit tests for new functions

### Documentation Requirements

- Update API documentation for new functions
- Include practical examples
- Document error conditions and exceptions
- Update version history

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔄 Version History

- **1.0.0** (Current)
  - Initial release
  - Basic DataFrame operations
  - Age-based filtering
  - Comprehensive documentation
  - Error handling and validation
  - Logging support

## 📞 Support

For questions, issues, or feature requests:

1. Check the [API Documentation](API_DOCUMENTATION.md)
2. Review existing [examples](#usage-examples)
3. Create an issue for bugs or feature requests
4. Contribute improvements via pull requests

## 🎯 Roadmap

Future enhancements being considered:

- [ ] Additional filtering options (name-based, multi-column)
- [ ] Export functionality (CSV, JSON, Excel)
- [ ] Data visualization integration
- [ ] Performance optimizations for large datasets
- [ ] Additional data validation rules
- [ ] Unit test suite
- [ ] Continuous integration setup

---

**Happy Data Analysis!** 🐍📊