# Access POI Data with Amap

This repository contains two Python scripts for scraping building information from the Amap API and performing reverse geocoding to extract area information. 

## Requirements

Before running the scripts, make sure to install the required dependencies:

```bash
pip install pandas requests
```

## Configuration

### API Key and Parameters

- **API Key**: You must fill in your Amap API key in the scripts.
- **Number of Pages**: Specify the number of pages to crawl for building data.
- **Keyword**: Provide the keyword for the buildings you want to search.

### Scripts Overview

1. **`gaode.py`**: This script is responsible for scraping basic building data based on the specified keyword.
2. **`gaode2.py`**: This script performs reverse geocoding to fetch area information for the buildings collected in the first script.

### Usage Instructions

1. **Run `gaode.py`**: 
   - This will collect building data based on the specified keyword and save it to an Excel file named `city_buildings.xlsx`.

2. **Run `gaode2.py`**:
   - This script will read the Excel file created by `gaode.py`, perform reverse geocoding on the collected data, and append the area information to the same Excel file.

### Example

Make sure to edit the scripts to include:
- Your Amap API key.
- The desired number of pages to crawl and the keyword for searching buildings.

### Note

- Ensure that you have a valid API key from Amap.
- The scripts will create or update the `city_buildings.xlsx` file in the current directory with the scraped data and area information.

## Conclusion

This repository provides a straightforward way to collect building information and their respective areas using the Amap API. For any issues or contributions, feel free to open an issue or submit a pull request.
