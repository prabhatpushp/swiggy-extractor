# Swiggy Product Extractor

## Introduction
This project provides functionality to extract product data from Swiggy's Instamart API. It generates search queries, fetches product details, and saves the results to a CSV file for further analysis.

## Features
- **Product Data Extraction**: Automatically fetches product data from Swiggy based on generated search queries.
- **Customizable Search Queries**: Generates a variety of search queries based on predefined categories and items.
- **CSV Output**: Saves the extracted product details to a CSV file for easy access and analysis.

## Tech Stack
- **Python**: The implementation is written in Python.
- **Requests**: Used for making HTTP requests to the Swiggy API.
- **CSV**: For handling CSV file operations.
- **JSON**: For processing API responses.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/prabhatpushp/swiggy-extractor
   cd swiggy-extractor
   ```
2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install requests
   ```

## Usage
To use the Swiggy extractor, you can run the `main.py` script. Here is an example:
```python
from main import generate_search_queries, fetch_swiggy_search_results, save_to_csv

# Generate search queries
queries = generate_search_queries()

# Fetch product details for each query
products = []
for query in queries:
    product_data = fetch_swiggy_search_results(query)
    products.extend(product_data)

# Save the results to a CSV file
save_to_csv(products)
```

## Development
- The main implementation is in `main.py`. You can modify or extend the functionality as needed.
- Ensure to test your changes thoroughly to maintain the integrity of the extraction process.

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes and create a pull request.

## License
This project is licensed under the MIT License. Feel free to use this project for personal or commercial purposes. 
