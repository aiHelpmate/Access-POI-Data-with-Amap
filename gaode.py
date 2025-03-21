import requests
import pandas as pd
import os

# Amap API Key
base_url = "https://restapi.amap.com/v3/place/text"
api_key = ''

# The number of pages crawled
page_num = 1

# Crawl keyword
bulid_keyword = "茶颜悦色"

# Check whether the Excel file exists
excel_file_exists = os.path.isfile('city_buildings.xlsx')

'''
Configuration item End
'''
for i in range(1, page_num+1):
    params = {
        "key": api_key,
        "keywords": bulid_keyword,
        "city": "430100",  # City codes, such as "430100" for Beijing
        "page": i,
        "output": "json",
        "extensions": "all"
    }

    # Issue a request
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Parse the returned JSON data
        result = response.json()

        # Check for POI data
        if result['status'] == '1' and 'pois' in result:
            pois = result['pois']
            print(len(pois))
            print(pois[0])

            buildings_data = []

            # Iterate through the POI list, extracting only the required fields
            for poi in pois:
                # Check whether the floor information is an empty list. If yes, set the floor to 1
                floor = poi.get('indoor_data', {}).get('floor', [])
                if floor == []:
                    floor = 1
                poi_data = {
                    'id': poi.get('id'),  # Use the "get" method to avoid "KeyError"
                    '名称': poi.get('name'),
                    '楼层': floor,
                    '经度': poi.get('location', '').split(',')[0] if 'location' in poi else '',
                    '纬度': poi.get('location', '').split(',')[1] if 'location' in poi else '',
                    '类型': poi.get('type')
                }
                buildings_data.append(poi_data)

            # Convert the data list to a DataFrame
            df = pd.DataFrame(buildings_data)

            if excel_file_exists:
                existing_df = pd.read_excel('city_buildings.xlsx')
                new_df = pd.concat([existing_df, df], ignore_index=True)
                new_df.to_excel('city_buildings.xlsx', index=False)
            else:
                df.to_excel('city_buildings.xlsx', index=False)

            print("Interested building information has been appended to the Excel file.")
            excel_file_exists = True

        else:
            print("No matching building information was found or the request failed.")
    else:
        print("Failed to request Amap API, status code:", response.status_code)
