# import requests
# from bs4 import BeautifulSoup

# def extract_price_and_title(url, price_selector):
#     try:
#         headers = {
#             "User-Agent": (
#                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                 "AppleWebKit/537.36 (KHTML, like Gecko) "
#                 "Chrome/114.0.0.0 Safari/537.36"
#             ),
#             "Accept-Language": "en-US,en;q=0.9",
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#             "Referer": "https://www.google.com/",
#             "DNT": "1",
#             "Connection": "keep-alive",
#         }

#         response = requests.get(url, headers=headers, timeout=10)
#         response.raise_for_status()

#         soup = BeautifulSoup(response.text, "html.parser")

#         title_tag = soup.find("title")
#         title = title_tag.text.strip() if title_tag else "No Title Found"

#         price_element = soup.select_one(price_selector)
#         if not price_element:
#             return {"success": False, "error": "Price selector not found"}

#         price_text = price_element.text.strip()
#         price = float(''.join([c for c in price_text if c.isdigit() or c == '.']))

#         return {
#             "success": True,
#             "title": title,
#             "price": price
#         }

#     except Exception as e:
#         return {"success": False, "error": str(e)}
