import requests
import csv
import json
from typing import List, Dict
import itertools
import time
import random
import string
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

seen_ids = set()

def generate_search_queries() -> List[str]:
    """
    Generate search queries
    """
    chars = string.ascii_lowercase + string.digits
    categories = [
    "Fresh Vegetables",
    "Fresh Fruits",
    "Dairy, Bread and Eggs",
    "Cereals and Breakfast",
    "Atta Rice and Dals",
    "Oils and Ghee",
    "Masalas and Dry Fruits",
    "Bakery",
    "Biscuits and Cakes",
    "Tea, Coffee and More",
    "Kitchen and Dining",
    "Meat and Seafood",
    "Chips and Namkeens",
    "Ice Cream and Frozen Desserts",
    "Chocolates and Sweets",
    "Cold Drinks and Juices",
    "Noodles, Pasta, Vermi",
    "Frozen Food",
    "Sauces and Spreads",
    "Paan Corner",
    "Bath and Body",
    "Hair Care",
    "Skincare and Beauty",
    "Oral Care",
    "Feminine Hygiene",
    "Health Care",
    "Baby Care",
    "Pet Supplies",
    "Cleaning Essentials",
    "Home and Fashion",
    "Electrical and Electronics",
    "Toys and Stationery"
    ]
    
    items = [
    "Tomatoes",
    "Potatoes",
    "Onions",
    "Carrots",
    "Spinach",
    "Bananas",
    "Apples",
    "Mangoes",
    "Grapes",
    "Pineapple",
    "Amul Butter",
    "Mother Dairy Milk",
    "Britannia Bread",
    "Lays Chips",
    "Parle-G Biscuits",
    "Maggi Noodles",
    "Aashirvaad Atta",
    "India Gate Basmati Rice",
    "Tata Sampann Dal",
    "Fortune Sunflower Oil",
    "Amul Ghee",
    "Everest Garam Masala",
    "Badam (Almonds)",
    "Britannia Cake",
    "Hide & Seek Cookies",
    "Tata Tea Gold",
    "Nescafe Classic Coffee",
    "Milton Water Bottle",
    "Butter Chicken Masala",
    "Venky's Chicken Nuggets",
    "Haldiram's Namkeen",
    "Kwality Wall's Ice Cream",
    "Cadbury Dairy Milk",
    "Frooti Mango Drink",
    "Coca-Cola",
    "Kissan Jam",
    "Amul Cheese Spread",
    "Closeup Toothpaste",
    "Colgate Toothbrush",
    "Dove Soap",
    "Lifebuoy Handwash",
    "Pantene Shampoo",
    "Clinic Plus Conditioner",
    "Lakme Face Cream",
    "Nivea Lip Balm",
    "Stayfree Sanitary Pads",
    "Dettol Antiseptic",
    "Himalaya Baby Powder",
    "Johnson's Baby Oil",
    "Pedigree Dog Food",
    "Surf Excel Detergent",
    "Vim Dishwash Liquid",
    "Havells LED Bulbs",
    "Philips Mixer Grinder",
    "Classmate Notebook",
    "Funskool Toys",
    "Godrej Air Freshener",
    "Amul", "Mother Dairy", "Britannia", "Aashirvaad", "India Gate", "Tata Sampann", "Fortune", "Everest", 
    "Haldiram's", "Kwality Wall's", "Cadbury", "Frooti", "Coca-Cola", "Kissan", "Nescafe", "Tata Tea", 
    "Venky's", "Parle-G", "Lays", "Hide & Seek", "Closeup", "Colgate", "Dove", "Lifebuoy", "Pantene", 
    "Clinic Plus", "Lakme", "Nivea", "Stayfree", "Dettol", "Himalaya", "Johnson's", "Pedigree", "Surf Excel", 
    "Vim", "Havells", "Philips", "Funskool", "Classmate", "Godrej", "Nestle", "Maggi", "Pepsi", "Sprite", 
    "Thums Up", "Limca", "Appy Fizz", "Bisleri", "Kinley", "Aquafina", "Bournvita", "Horlicks", "Complan", 
    "Boost", "Red Bull", "Monster", "Real", "Tropicana", "Paper Boat", "Paperkraft", "Safari", "Wildcraft", 
    "Allen Solly", "Raymond", "Van Heusen", "Peter England", "Louis Philippe", "Jockey", "Hanes", "Adidas", 
    "Nike", "Puma", "Reebok", "Woodland", "Bata", "Liberty", "Paragon", "Relaxo", "Metro Shoes", "Catwalk", 
    "Action Shoes", "Hidesign", "Fastrack", "Titan", "Sonata", "Casio", "Timex", "Samsung", "Apple", "Sony", 
    "LG", "OnePlus", "Xiaomi", "Vivo", "Oppo", "Realme", "Dell", "HP", "Lenovo", "Acer", "Asus", "Canon", 
    "Nikon", "Epson", "Brother", "Panasonic", "Voltas", "Hitachi", "Daikin", "Blue Star", "Whirlpool", 
    "Godrej Appliances", "IFB", "Haier", "Bosch", "Karcher", "Prestige", "Hawkins", "Bajaj Electricals", 
    "Philips Lighting", "Usha", "Crompton", "Orient", "Syska", "Luminous", "Exide", "Amaron", "Hero", 
    "Bajaj", "TVS", "Honda", "Yamaha", "Royal Enfield", "Suzuki", "Tata Motors", "Mahindra", "Maruti Suzuki", 
    "Hyundai", "Kia", "Toyota", "MG Motors", "Volkswagen", "Ford", "Renault", "Nissan", "Bosch Automotive", 
    "Castrol", "Shell", "Gulf", "Indigo Paints", "Asian Paints", "Berger Paints", "Nerolac", "Fevicol", 
    "Pidilite", "3M", "Johnson Tiles", "Kajaria", "Somany", "Jaquar", "Hindware", "Cera", "Parryware", 
    "Duroflex", "Kurlon", "Sleepwell", "Centuary Mattresses", "Godrej Interio", "Durian", "Nilkamal", 
    "Urban Ladder", "Pepperfry", "Home Centre", "Prestige Cookware", "Vinod Cookware", "Havells Kitchen", 
    "KitchenAid", "IFB Kitchen", "Wonderchef", "Borosil", "Cello", "Milton", "Tupperware", "Pigeon", 
    "HIT", "Mortein", "All Out", "Good Knight", "Odonil", "Ambipur", "Axe", "Wild Stone", "Park Avenue", 
    "Nivea Men", "Old Spice", "Gillette", "Veet", "Engage", "Fogg", "Set Wet", "KS", "BBlunt", "Biotique", 
    "Lotus Herbals", "Forest Essentials", "The Body Shop", "Mamaearth", "Wow Skin Science", "Plum","Boat",
    "Redmi", "OnePlus", "Samsung", "Nokia", "Oppo", "Vivo", "Realme", "OnePlus", "Samsung", "Nokia", "Oppo", "Vivo", "Realme", 
    "Apple", "Google", "Microsoft", "Amazon", "Meta", "Tesla", "SpaceX", "Nasa", "NASA", "SpaceX", "Tesla", "Amazon", "Google", "Microsoft", "Meta","Nu Republic",
    "ambrane", "jbl"
    ]

    search_terms = [] + categories + items
    
    # Generate 1-character terms
    for c in chars:
        search_terms.append(c)
        
    # Generate 2-character terms
    for c1 in chars:
        for c2 in chars:
            search_terms.append(c1 + c2)
            if(len(search_terms)>200):
                break
    
    # Generate 3-character terms
    # for c1 in chars:
    #     for c2 in chars:
    #         for c3 in chars:
    #             search_terms.append(c1 + c2 + c3)
    
    # Generate 4-character terms
    # for c1 in chars:
    #     for c2 in chars:
    #         for c3 in chars:
    #             for c4 in chars:
    #                 search_terms.append(c1 + c2 + c3 + c4)
    
    return search_terms

def fetch_swiggy_search_results(query: str, store_id: str = "YOUR_STORE_ID_HERE") -> Dict:
    """
    Fetch search results from Swiggy Instamart API
    """
    url = "https://www.swiggy.com/api/instamart/search"
    
    cookies = {
        '__SW': 'YOUR_SW_COOKIE_HERE',
        '_device_id': 'YOUR_DEVICE_ID_HERE',
        '_swuid': 'YOUR_SWUID_HERE',
        '_fbp': 'YOUR_FBP_HERE',
        '_ga_4BQKMMC7Y9': 'YOUR_GA_HERE',
        '_sid': 'YOUR_SID_HERE',
        '_gcl_au': 'YOUR_GCL_AU_HERE',
        '_gid': 'YOUR_GID_HERE',
        '_session_tid': 'YOUR_SESSION_TID_HERE',
        '_ga_34JYJ0BCRN': 'YOUR_GA_34JYJ0BCRN_HERE',
        'AMP_TOKEN': 'YOUR_AMP_TOKEN_HERE',
        'YOUR_SESSION_TOKEN_HERE': 'YOUR_SESSION_TOKEN_HERE',
        'YOUR_COOKIE_HERE': 'YOUR_COOKIE_HERE',
        'deviceId': 'YOUR_DEVICE_ID_HERE',
        'tid': 'YOUR_TID_HERE',
        'sid': 'YOUR_SID_HERE',
        'lat': 'YOUR_LATITUDE_HERE',
        'lng': 'YOUR_LONGITUDE_HERE',
        'address': 'YOUR_ADDRESS_HERE',
        'addressId': 'YOUR_ADDRESS_ID_HERE',
        'LocSrc': 'YOUR_LOC_SRC_HERE',
        'isImBottomBarXpEnabled': 'YOUR_IS_IM_BOTTOM_BAR_XP_ENABLED_HERE',
        '_ga_X3K3CELKLV': 'YOUR_GA_X3K3CELKLV_HERE',
        '_ga': 'YOUR_GA_HERE',
        'userLocation': 'YOUR_USER_LOCATION_HERE',
        'imOrderAttribution': 'YOUR_IM_ORDER_ATTRIBUTION_HERE',
        '_ga_8N8XRG907L': 'YOUR_GA_8N8XRG907L_HERE',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': 'YOUR_COOKIE_HERE',
    }
    
    payload = {
        "facets": {},
        "sortAttribute": ""
    }
    
    params = {
        "pageNumber": 1,
        "searchResultsOffset": 0,
        "limit": 4000,
        "query": query,
        "ageConsent": "false",
        "layoutId": 2671,
        "pageType": "INSTAMART_AUTO_SUGGEST_PAGE",
        "isPreSearchTag": "false",
        "highConfidencePageNo": 0,
        "lowConfidencePageNo": 0,
        "voiceSearchTrackingId": "",
        "storeId": store_id,
        "primaryStoreId": store_id,
        "secondaryStoreId": ''
    }
    
    try:
        response = requests.post(url, headers=headers, params=params, json=payload, cookies=cookies)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching results for {query}: {e}")
        return {}

    
def extract_product_details(data: Dict) -> List[Dict]:
    """
    Extract relevant details from search results
    """
    if not data or 'data' not in data or 'widgets' not in data['data']:
        return []
    
    products = []
    
    for widget in data['data']['widgets']:
        if widget.get('type') == 'PRODUCT_LIST':
            for item in widget.get('data', []):
                product_id = item.get('product_id')
                
                if not product_id:
                    continue
                for variation in item.get('variations', []):
                    # Skip if product ID already seen
                    if variation.get('id') in seen_ids:
                        continue
                    
                    product_details = {
                        'ID': variation.get('id', ''),
                        "Product Id": product_id,
                        'Store ID': variation.get('store_id', ''),
                        'Name': variation.get('display_name', ''),
                        'Brand': variation.get('brand', 'N/A'),
                        'Category': variation.get('category', ''),
                        'Price (MRP)': variation.get('price', {}).get('mrp', ''),
                        'Store Price': variation.get('price', {}).get('store_price', ''),
                        'Offer Price': variation.get('price', {}).get('offer_price', ''),
                        'Discount': variation.get('price', {}).get('offer_applied', {}).get('listing_description', '').split('%')[0].strip(),
                        'Quantity': variation.get('quantity', ''),
                        'Inventory Total': variation.get('inventory', {}).get('total', ''),
                        # 'Sourced From': variation.get('sourced_from', ''),
                    }
                    
                    products.append(product_details)
                    seen_ids.add(variation.get('id'))
    
    return products

def process_query(query: str) -> List[Dict]:
    """
    Process a single search query and return product details
    """
    try:
        print(f"Processing query: {query}")
        results = fetch_swiggy_search_results(query)
        if results:
            return extract_product_details(results)
        return []
    except Exception as e:
        print(f"Error processing query '{query}': {str(e)}")
        return []

def save_to_csv(products: List[Dict], filename: str = 'swiggy_products.csv'):
    """
    Save products to a CSV file
    """
    if not products:
        print("No products to save.")
        return
    
    # Remove duplicates
    seen_ids = set()
    unique_products = []
    for product in products:
        if product['ID'] not in seen_ids:
            unique_products.append(product)
            seen_ids.add(product['ID'])
    
    keys = unique_products[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(unique_products)
    
    print(f"Saved {len(unique_products)} unique products to {filename}")

def main():
    """
    Main function to coordinate the scraping process
    """
    search_terms = generate_search_queries()
    all_products = []
    
    # Number of processes to run in parallel (adjust based on your CPU cores)
    num_processes = multiprocessing.cpu_count() - 1  # Leave one core free
    
    print(f"Starting scraping with {num_processes} processes...")
    start_time = time.time()
    
    # Use ProcessPoolExecutor to handle multiple requests in parallel
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        # Map the process_query function to all search terms
        results = list(executor.map(process_query, search_terms))
        
        # Flatten the results list
        all_products = [product for sublist in results if sublist for product in sublist]
    
    end_time = time.time()
    print(f"Scraping completed in {end_time - start_time:.2f} seconds")
    print(f"Total products found: {len(all_products)}")
    
    # Save results to CSV
    save_to_csv(all_products)
    print("Results saved to swiggy_products.csv")

if __name__ == "__main__":
    main()