import os
import requests

class OSRSApiClient:
    def __init__(self):
        self.base_url = "https://prices.runescape.wiki/api/v1/osrs/"
        self.headers = {"User-Agent": os.environ["USER_AGENT"]}

    # Fetch the latest prices from the OSRS Wiki API
    def fetch_latest_prices(self):
        price_url = f"{self.base_url}/latest"
        response = requests.get(price_url, headers=self.headers)
        return response.json()
    
    # Fetch the item mapping from the OSRS Wiki API
    def fetch_item_info(self):
        info_url = f"{self.base_url}/mapping"
        response = requests.get(info_url, headers=self.headers)
        return response.json()

    
    # Fetch the price data for a specific item by its ID
    def fetch_item_prices(self, item_id):
        market_price = self.fetch_latest_prices()
        return market_price['data'].get(str(item_id), None)
    
    #Fuzzy search for items by name, returning a list of matches
    def search_items_by_name(self, target_name):
        catalog = self.fetch_item_info()
        matches = []

        for item in catalog:
            if target_name.lower() in item['name'].lower():
                matches.append(item)
        return matches
    
    # Get item details by name, including its ID and price data
    def get_item_by_name(self, target_name):
        
        #Grab the full list of items from the mapping endpoint
        catalog = self.fetch_item_info() 
        
        target_id = None
        item_clean_name = None
        
        #Look through the catalog list for a name match (case-insensitive)
        for item in catalog:
            if item['name'].lower() == target_name.lower():
                target_id = item['id']
                item_clean_name = item['name']
                break 

        # If the item wasn't found in the catalog, return None
        if not target_id:
            return None

        # Fetch the prices using the ID we just uncovered
        price_data = self.fetch_item_prices(target_id)

        # Return a clean, unified dictionary package
        return {
            "id": target_id,
            "name": item_clean_name,
            "high": price_data.get('high', 0),
            "low": price_data.get('low', 0)
        }