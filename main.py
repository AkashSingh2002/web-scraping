import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode for better performance
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

# Initialize the Chrome driver with webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# List of search queries
search_queries = [
    'POUF WITH FILLER', 'CUSHION WITH FILLER', "MEN'S FULL SLEEVE SHIRT", 'TUFTED THROW',
    'COTTON THROW', 'BEADED SOCKS', 'BEADED VELVET SOCKS', 'BATH MAT', 'EMBROIDERED RUNNER',
    'FLOOR LAMP WITH SHADE SET', 'TABLE LAMP WITH SHADE', 'LADIES MAXI DRESS', 'LADIES MIDI DRESS',
    'LADIES DRESS', 'LADIES SMOCKED DRESS', 'LADIES SCHIFFLI MAXI DRESS', 'LADIES OFF SHOULDER DRESS',
    "MEN'S SHORT SLEEVE SHIRT", "MEN'S BEACH PANT", "MEN'S BEACH ELASTICATED WAIST SHORTS", 'JUTE BASKET',
    'HAIRON LEATHER PHOTOFRAME', 'HAIRON LEATHER BOX', 'BONE PHOTO FRAME', 'DECORATIVE BOX',
    'DECORATIVE PIECES', 'WOODEN BOX WITH LID', 'BONE CONE', 'WALL HANGING',
    'TUFTED CUSHION WITH FILLER', 'TUFTED CUSHION', 'BABY GIRL PANT', 'BABIES JUMPSUIT', 'BABY GIRL DRESS',
    'BABIES ROMPER', 'BABIES SHORTS', 'COTTON POUF', 'BABIES HOODED T-SHIRT', 'FLOOR CUSHION WITH FILLER',
    'SOAP DISPENSER', 'PUMP SOAP DISPENSER', 'WOODEN TRAY', 'COTTON BASKET', 'TUFTED BATH MAT',
    'LADIES SHORT SLEEVE BLOUSE', 'LADIES SKIRT', 'LADIES TOP', 'LADIES SHIRT', 'LADIES RUFFLE SLEEVE MIDI DRESS',
    'LADIES SLEEVELESS BLOUSE', 'LADIES SHORTS', 'BATH TUMBLER', 'COTTON PLACEMAT', 'COTTON LUREX RUNNER',
    'TABLE NAPKIN', 'TABLE CLOTH', 'KIDS CARPET', 'CHARGER PLATE', 'COTTON BOX', 'WOODEN TUMBLER',
    'COTTON CARPET', 'FLOOR CARPET', 'BABY GIRL SLEEVELESS TOP', 'MOP PLACE MAT', 'BEADED PLACE MAT',
    'JUTE PLACE MAT', 'COTTON NAPKIN', 'FLOWER EMBROIDERY PLACE MAT', 'BEADED BOX', 'CUTLERY SET',
    'DECORATIVE PINEAPPLE', 'TABLE LAMP', 'EMBROIDERY STOOL', 'CAKE STAND', 'BEADED COASTERS',
    'NAPKIN RING', 'TEA BOX', 'MDF COASTER', 'SERVING TRAY', 'DRINKING GLASS', 'CHRISTMAS GARLAND',
    'GARDEN PLANTER', 'DECORATIVE VASE', 'METAL PLANTER', 'WATERING CAN', 'BABY BOY SWEATSHIRT',
    'BABIES LONG SLEEVE SHIRT', 'BABIES JACKET', 'BABIES HOODIE', 'BABIES SWEATER', 'BABIES SWEATSHIRT',
    'BABY BOY SWEATER', 'BABIES T-SHIRT', 'BABIES KNITTED TOP', 'BABY GIRLS SWEATER', 'BABY GIRL SKIRT',
    'BABIES JUMPER', 'BABIES BLOUSE', 'COTTON RUG', 'JUTE RUG', 'DECORATIVE PIECE', 'CHRISTMAS ORNAMENT',
    'CHRISTMAS STOCKING', 'CHRISTMAS TREE', 'WOODEN TREE COLLAR', 'BEADED RUNNER', 'CRYSTAL ORNAMENT',
    'BEADED SNOW FLAKE', 'TABLE TREE', 'TREE COLLAR', 'TREE SKIRT', 'BEADED TREE SKIRT', 'WOODEN REINDEER',
    'BEADED TREE TOPPER', 'EMBROIDERED TREE SKIRT', '3PC BEACHWEAR SET', 'WOODEN PHOTO FRAME',
    'MDF PHOTO FRAME', 'RESIN PHOTO FRAME', 'WOODEN SCULPTURE', 'MANGO WOOD SCULPTURE', 'LADIES BLOUSE',
    'GLASS VASE', 'ALUMINIUM VASE', 'STEEL VASE', 'X&O GAME DECOR PIECE', 'STEEL LANTERN',
    'LADIES RUFFLED SWEATER', 'METAL SCULPTURE', 'TABLE CLOCK', 'DECORATIVE APPLE', 'BABY BOY CARDIGAN',
    'LADIES VEST', 'LADIES JACKET', 'MIRROR', 'DINING TABLE', 'CONSOLE TABLE', 'MEDIA TV UNIT',
    'SIDE BOARD TABLE', 'WOODEN CHAIR', 'WOODEN BENCH', 'COFFEE TABLE', 'COUNTER TABLE', "MEN'S VEST",
    "MEN'S JOGGERS", "MEN'S ZIPPER JACKET", "MEN'S JACKET", "MEN'S HOODED JACKET", "MEN'S SWEATSHIRT",
    'BABIES SHIRT', 'BEADED COASTER', '4 PC BEDSHEET SET', 'BABIES PYJAMA SET', 'RATAN POT',
    'RATAN COASTER', 'DECORATIVE PUMPKIN', 'JEWELLERY BOX', 'BATH TOWEL SET OF 6', 'HAND TOWEL',
    'FACIAL TOWEL', 'MANGO WOOD BOX', 'JEWELLERY TRAY', 'LADIES CARDIGAN', 'LADIES LOUNGEWEAR',
    'LADIES SWEATER', 'MENS LONG SLEEVE SWEATER', "MEN'S SWEATER", 'NAPKIN HOLDER', 'SALT & PEPPER SHAKER',
    'MARBLE COASTER', 'STORAGE BASKET', 'WOODEN COASTER', 'SERVING SPOON', 'DECORATIVE BOWL',
    'COTTON RUNNER', 'LADIES HANDBAG', "WOMEN'S BUCKET BAG", 'LADIES BAG', 'LADIES SLING BAG',
    'LAZY SUSAN', 'COTTON COASTER', 'MARBLE CHEESE SET', 'LADIES UTILITY BAG', 'SALT & PEPPER POT',
    'LADIES HANDBAG', 'MARBLE PINCH POT', 'GLASS TUMBLER', 'RESIN TUMBLER', 'HAIRPIN LEG BENCH',
    'BEADED PHOTO FRAME', 'COTTON PLACE MAT', 'CANDLE STAND', 'MULTICOLOR PLACE MAT',
    'MULTICOLORED RUNNER', 'CHINDI RUG', 'TUFTED CARPET', 'ROUND CARPET', 'JUTE CARPET',
    'TABLE PLACE MAT', 'WOODEN LANTERNS', 'T-LIGHT HOLDER', 'WOODEN BOX', 'TABLE RUNNER',
    'FABRIC PLACE MAT', 'TOY SMALL FISHING', 'SILK SOLID DYED', 'LADIES JUTE BAG', 'MAGNIFYING GLASS',
    'WALL CLOCK', 'BAR STOOL', 'ROUND DINING TABLE', 'WOODEN COFFEE TABLE', 'WOODEN SIDE TABLE',
    'ROUND SIDE TABLE', 'RATAN BASKET', 'ACETATE PRINTED FABRICS', 'GIRLS SKIRT',
    'POLYESTER PRINTED FABRICS', 'PROJECTION TOY GUN', 'KIDS TORCH', 'WOODEN SOAP DISPENSER',
    'TOY MIKE PROJECTOR', 'OMBRE CHIFFON SOLID DYED', "MEN'S PANT", 'ORGANZA SOLID DYED',
    'VISCOSE BLEND PRINTED FABRICS', 'TOY GUN', 'SILK PRINTED FABRICS', 'TOY LAPTOP',
    'BOYS SHORT', 'TOY RING TOSS', 'LINEN PRINTED FABRICS', 'HOVER BALL', 'BLAZE STROM',
    'VISCOSE PRINTED FABRICS', 'PLASTIC TOY CUBE', 'COTTON PRINTED FABRICS', 'LADIES PANT',
    'SATIN SOLID DYED', "MEN'S SHIRT", 'BLAST GUN', "GIRL'S CAP", 'BABIES JACKET', 'TOY SHOES',
    'LADIES SAREE', 'POLYESTER PANT', 'BABIES DRESS', 'PLASTIC TOY TRAIN', "GIRL'S SKIRT",
    'PLASTIC TOY TOOLS', 'GIRLS T-SHIRT', 'COTTON DYED FABRICS', 'COTTON SHIRT', 'BOYS T-SHIRT',
    'SILK PRINTED', 'WALL STICKER', 'PLASTIC TOY SET', 'TOY ROBOT', 'TOY HAMMER', 'BABY CAP',
    'GIRLS PANT', 'COTTON SCARF', 'KIDS SWEATSHIRT', 'COTTON GIRL DRESS', 'BABY GIRL PANT',
    'BABY DRESS', 'PLASTIC TOY VEHICLE', 'TOY TRAIN', 'TOY ARMY SET', 'TOY TOOL SET', 'TOY CAR',
    'TOY GUN', 'PLASTIC TOY WRENCH', 'TOY VAN', 'TOY HAMMER', 'TOY SMALL VEHICLE', 'BABY JACKET',
    'BABY SWEATER', 'BABY TOP', 'BABY SHIRT', 'BABY DRESS'
]

def scrape_amazon_data(search_query):
    # Clean and format the search query for file naming
    safe_query = ''.join(c for c in search_query if c.isalnum() or c in (' ', '_')).replace(' ', '_')
    file_name = f'{safe_query[:50]}.csv'

    try:
        driver.get("https://www.amazon.in")
    except WebDriverException as e:
        print(f"Error accessing Amazon: {e}")
        return

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(3)
    
    products = []
    
    for page in range(1, 4):
        try:
            product_elements = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div.s-result-item")

            for product in product_elements:
                try:
                    # Extract product information
                    name = product.find_element(By.CSS_SELECTOR, "h2 a span").text
                    price = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
                    rating = product.find_element(By.CSS_SELECTOR, "span.a-icon-alt").text
                    link = product.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")
                    products.append([name, price, rating, link])
                except Exception as e:
                    print(f"Error extracting data: {e}")
                    continue

            try:
                # Go to the next page
                next_page_button = driver.find_element(By.CLASS_NAME, "s-pagination-next")
                next_page_button.click()
                time.sleep(3)
            except:
                break
        
        except WebDriverException as e:
            print(f"Error on page {page}: {e}")
            break
    
    # Write data to CSV file
    if products:
        os.makedirs('scraped_data', exist_ok=True)  # Create a directory for CSV files if it doesn't exist
        with open(f'scraped_data/{file_name}', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Product Name', 'Price', 'Rating', 'URL'])
            writer.writerows(products)
    else:
        print(f"No products found for query: {search_query}")

# Process each search query from the list
for query in search_queries:
    scrape_amazon_data(query)

driver.quit()
