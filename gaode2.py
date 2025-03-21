import requests
import pandas as pd

# The base URL of the inverse geocoding API
regeo_url = "https://restapi.amap.com/v3/geocode/regeo"

api_key = ''
df = pd.read_excel('city_buildings.xlsx')

# Check if the DataFrame already has an 'area' column, if not, add it
if 'AOI点面积' not in df.columns:
    df['AOI点面积'] = None

for index, row in df.iterrows():
    # Check whether the current cell in the 'AOI Point Area 'column already has content, and skip it if it does
    if pd.notnull(row['AOI点面积']):
        continue
    params = {
        "key": api_key,
        "location": f"{row['经度']},{row['纬度']}",
        "extensions": "all"  # Be sure to return all information, including AOI
    }
    print(params)

    response = requests.get(regeo_url, params=params)
    print(response)

    if response.status_code == 200:
        result = response.json()

        # Check for inverse geocoding data
        if result['status'] == '1' and 'regeocode' in result:
            # AOI point area was extracted
            try:
                area = result['regeocode']['aois'][0].get('area', '未知')
                # Update the 'AOI point area' column in the DataFrame
                df.at[index, 'AOI点面积'] = area
            except:
                pass
        else:
            print(f"Reverse geocoding request failed:{result['info']}")
    else:
        print(f"Failed to request Amap API, status code:{response.status_code}")

df.to_excel('city_buildings.xlsx', index=False)
print("AOI point area information has been added to the original Excel file.")