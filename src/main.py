import os
from dotenv import load_dotenv
from api import OSRSApiClient
from models import Item

load_dotenv()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n" + "=" * 35)
    print("      OSRS LIVE PRICE CHECKER      ")
    print("=" * 35)
    print("[1] Search for an Item Price")
    print("[0] Exit Program")
    print("=" * 35)

def main():
    client = OSRSApiClient()
    clear_screen()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                clear_screen()
                item_query = input("What are you looking for?: ").strip()
                if not item_query:
                    print("Search cannot be empty.")
                    input("\nPress Enter to continue...")
                    clear_screen()
                    continue
                
                matches = client.search_items_by_name(item_query)

                if not matches:
                    print("\n❌ No items found matching that name.")
                    input("\nPress Enter to continue...")
                    clear_screen()
                    continue
                
                selected_item = None

                if len(matches) == 1:
                    selected_item = matches[0]
                else:
                    clear_screen()
                    print(f"Found multiple items matching your query ({len(matches)} total):")
                    
                    start_index = 0
                    while True:
                        visible_matches = matches[start_index : start_index + 10]
                        
                        print("\n" + "-" * 35)
                        print(f"    RESULTS PAGE {int(start_index/10) + 1}")
                        print("-" * 35)
                        for index, match_item in enumerate(visible_matches, 1):
                            print(f"[{index}] {match_item['name']} (ID: {match_item['id']})")
                        print("-" * 35)
                        
                        has_more = (start_index + 10) < len(matches)
                        if has_more:
                            print("[M] Show More Results")
                        print("[0] Cancel Search")
                        
                        selection = input("\nSelect an item number, 'M' for more, or '0' to cancel: ").strip().lower()
                        
                        if selection == '0':
                            print("Selection cancelled.")
                            input("\nPress Enter to continue...")
                            clear_screen()
                            break  
                            
                        if selection == 'm' and has_more:
                            start_index += 10
                            clear_screen()  
                            continue
                            
                        try:
                            selection_idx = int(selection)
                            if 1 <= selection_idx <= len(visible_matches):
                                selected_item = visible_matches[selection_idx - 1]
                                break  
                            else:
                                print("Number out of range for this page. Try again.")
                        except ValueError:
                            print("Invalid entry. Enter a number or 'M'.")

                if not selected_item:
                    continue

                clear_screen()
                print(f"Fetching live prices for {selected_item['name']}...")

                price_data = client.fetch_item_prices(selected_item['id'])
                if not price_data:
                    price_data = {}

                item_object = Item(
                    selected_item['id'],
                    selected_item['name'],
                    price_data.get('high', 0),
                    price_data.get('low', 0)
                )
                
                clear_screen()
                print(item_object.formatted_info())
                
                input("\nPress Enter to continue back to menu...")
                clear_screen()

            case "0":
                print("Exiting.")
                break

            case _:
                print("Invalid choice. Please try again.")
    


    
    
if __name__ == "__main__":
    main()
