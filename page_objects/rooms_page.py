

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class RoomsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Increased timeout



    @property
    def rooms_section (self):
        """Get the Our Rooms title element"""
        return self.driver.find_element(By.XPATH, "//section[@id='rooms']//div[@class='container']")
    def scroll_to_our_rooms_section(self):
        """Scroll to the Our Rooms section"""
        try:
            self.driver.execute_script("window.scrollBy(0, 600);")
            time.sleep(1)
            element = self.rooms_section
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            time.sleep(2)
            print("✅ Scrolled to Our Rooms section")
        except Exception as e:
            print(f"⚠️ Error scrolling: {e}")

    @property
    def rooms_title(self):
        """Get the Our Rooms title element"""
        return self.driver.find_element(By.XPATH, "//h2[normalize-space()='Our Rooms']")

    @property
    def rooms_subtitle(self):
        """Get the Our Rooms description element"""
        return self.driver.find_element(By.XPATH, "//p[contains(text(),'Comfortable beds')]")

    @property
    def verify_room_count(self):
        """Verify there are exactly 3 rooms"""
        return len(self.room_cards) == 3

    @property
    def room_cards(self):

        cards = []
        try:
            cards = self.driver.find_elements(By.CLASS_NAME, "col-md-6 col-lg-4")
            if len(cards) >= 3:
                print(f"✅ Found {len(cards)} cards using col-md-6 col-lg-4")
                return cards[:3]
        except:
               pass


    def get_all_room_images(self):
        """Get all room images"""
        images = []
        cards = self.room_cards  # This should now be a list

        # print(f"📦 Found {len(cards)} room cards")
        # print(f"📦 Type of cards: {type(cards)}")

        # Safety check: ensure cards is a list
        if not isinstance(cards, list):
            print("❌ ERROR: room_cards is not a list!")
            cards = [cards]  # Convert single element to list

        for i, card in enumerate(cards):
            try:
                img = card.find_element(By.TAG_NAME, "img")
                img_src = img.get_attribute("src")
                images.append(img_src)
                print(f"  ✅ Room {i + 1} image: {img_src[:60]}...")
            except Exception as e:
                print(f"  ❌ Room {i + 1} image error: {e}")
                images.append(None)

        return images


    def get_all_room_titles(self):
        """Get all room titles as a list"""
        titles = []
        cards = self.room_cards
        print(f"📦 Found {len(cards)} room cards")
        if not isinstance(cards, list):
            cards = [cards]

        for i, card in enumerate(cards):
            try:
                title = None
                for selector in ["(//div[@class='col-md-6 col-lg-4'])[1]", "(//div[@class='col-md-6 col-lg-4'])[2]", "(//div[@class='col-md-6 col-lg-4'])[3]",]:
                    try:
                        title_elem = card.find_element(By.XPATH, selector)
                        title = title_elem.text
                        if title:
                            break
                    except:
                        continue

                titles.append(title)
                print(f"  ✅ Room {i + 1} title: {title}")
            except Exception as e:
                print(f"  ❌ Room {i + 1} title error: {e}")
                titles.append(None)

            return titles


    def get_all_room_descriptions(self):
        """Get all room descriptions (the Latin text under each room)"""
        descriptions = []
        cards = self.room_cards
        if not isinstance(cards, list):
            cards = [cards]

        for i, card in enumerate(cards):
            try:
                paragraphs = card.find_elements(By.CLASS_NAME, "card-text")
                # Get the first substantial paragraph
                desc = None
                for p in paragraphs:
                    text = p.text
                    if len(text) > 20:  # Substantial text
                        desc = text
                        break

                descriptions.append(desc)
                print(f"  ✅ Room {i + 1} desc: {desc[:40] if desc else 'None'}...")
            except Exception as e:
                print(f"  ❌ Room {i + 1} desc error: {e}")
                descriptions.append(None)

            return descriptions

    def get_all_room_features(self):
        """Get all room features (Wi-Fi, TV, Safe, etc.) for all rooms"""
        all_features = []
        cards = self.room_cards
        if not isinstance(cards, list):
            cards = [cards]
        for i, card in enumerate (cards):
            try:
                features_elements = card.find_elements(By.CLASS_NAME, "d-flex gap-3 mb-3 flex-wrap")
                features = [feat.get_attribute("title") or feat.text for feat in features_elements if
                            feat.text or feat.get_attribute("title")]
                all_features.append(features)
            except Exception as e:
                print(f"  Room { i +1}: {e}")
                all_features.append([])
        return all_features

    def get_room_features_by_index(self, index):
        """Get features for a specific room by index (0=Single, 1=Double, 2=Suite)"""
        try:
            card = self.room_cards[index]
            features_elements = card.find_elements(By.CLASS_NAME, "d-flex gap-3 mb-3 flex-wrap")
            features = [feat.get_attribute("title") or feat.text for feat in features_elements if
                        feat.text or feat.get_attribute("title")]
            return features
        except:
            return []

    def get_all_room_prices(self):
        """Get all room prices as a list"""
        prices = []
        cards = self.room_cards
        if not isinstance(cards, list):
            cards = [cards]
        for i, card in enumerate(cards):
            try:
                price = card.find_element(By.CLASS_NAME, "fw-bold fs-5").text
                prices.append(price)
                print(f"  Room {i + 1}: {price}")
            except Exception as e:
                print(f"  Room {i + 1}: Error getting title - {e}")
        return prices

    def get_room_price_by_index(self, index):
        """Get price for specific room by index"""
        try:
            card = self.room_cards[index]
            price = card.find_element(By.CLASS_NAME, "fw-bold fs-5").text
            return price
        except:
            return None

    def click_book_now_by_index(self, index):
        """Click Book Now button for specific room (0=Single, 1=Double, 2=Suite)"""
        try:
            cards = self.driver.find_element(By.CLASS_NAME, "col-md-6 col-lg-4")
            card = cards[index]
            # card = self.room_cards[index]
            book_button = card.find_element(By.LINK_TEXT, "Book now")
            book_button.click()
            time.sleep(2)
            print(f"✅ Clicked Book Now for room at index {index}")
        except Exception as e:
            print(f"❌ Error clicking Book Now: {e}")
            raise

    def click_book_now_for_single(self):
        """Click Book Now for Single room"""
        self.click_book_now_by_index(0)

    def click_book_now_for_double(self):
        """Click Book Now for Double room"""
        self.click_book_now_by_index(1)

    def click_book_now_for_suite(self):
        """Click Book Now for Suite"""
        self.click_book_now_by_index(2)

    def is_on_reservation_page(self):
        """Check if redirected to reservation page"""
        current_url = self.driver.current_url
        return "reservation" in current_url

    def get_current_reservation_room_id(self):
        """Get the room ID from reservation page URL"""
        current_url = self.driver.current_url
        if "reservation/" in current_url:
            # Extract room ID from URL like /reservation/1 or /reservation/2
            parts = current_url.split("reservation/")
            if len(parts) > 1:
                room_id = parts[1].split("?")[0].split("/")[0]
                return room_id
        return None



