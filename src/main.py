import os
from dotenv import load_dotenv
import requests
from api import OSRSApiClient
from models import Item

load_dotenv()

def main():
    client = OSRSApiClient()
    item = input("Enter the name of the item you want to search for: ")
    result = client.get_item_by_name(item)
    
    if result == None:
        print(f"Item '{item}' not found.")
        return

    #turn item into an Item object
    item_obj = Item(result['id'], result['name'], result['high'], result['low'])

    print(item_obj.formatted_info())

if __name__ == "__main__":
    main()
