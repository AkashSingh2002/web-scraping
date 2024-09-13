### `README.md`

This file provides instructions on how to set up and run the script.

```markdown
# Amazon Scraper

This script scrapes product data from Amazon.in based on a list of search queries. It extracts product information from the first three pages of search results and saves the data into CSV files named according to the search query.

## Requirements

Before running the script, you need to install the required Python packages. You can do this by using the `requirements.txt` file provided.

### Installation

1. **Clone the Repository** (or download the script files):
   ```sh
   git clone https://github.com/AkashSingh2002/web-scraping.git
   cd web-scraping
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```sh
   pip install -r requirements.txt
   ```

### Configuration

1. **Edit the Search Queries**:
   - Open the `main.py` file.
   - Update the `search_queries` list with the search queries you want to use.

### Running the Script

To run the script, use the following command:

```sh
python main.py
```

### Output

- The script will create a directory named `scraped_data` in the current working directory.
- CSV files will be saved in the `scraped_data` directory, with names derived from the search queries.

### Notes

- Ensure you have Chrome installed on your system as the script uses ChromeDriver to interact with the browser.
- The script runs in headless mode by default, which means the browser window will not be visible during execution. You can remove `--headless` from the `chrome_options` if you want to see the browser window.

### Troubleshooting

- **No such element**: If you encounter errors related to element location, it may be due to changes in Amazon's website structure. Check and update the CSS selectors in the script accordingly.
- **WebDriverException**: Ensure you have the latest version of ChromeDriver and Chrome. Update them if necessary.


### How to Use

1. **Save the `requirements.txt`** and **`README.md`** files in the same directory as your `main.py` script.

2. **Follow the instructions in the README.md** file to set up your environment, install dependencies, and run the script.
