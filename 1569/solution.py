import string
import random

class URLShortener:
  def __init__(self):
    self.url_to_short = {}
    self.short_to_url = {}
    self.characters = string.ascii_letters + string.digits
  
  def shorten(self, url):
    if url in self.url_to_short:
      return self.url_to_short[url]
    
    short_code = self.generate_short_code()
    while short_code in self.short_to_url:
      short_code = self.generate_short_code()
    self.short_to_url[short_code] = url
    self.url_to_short[url] = short_code
    return short_code
    
  def restore(self, short):
    return self.short_to_url.get(short, None)

  def generate_short_code(self):
    return ''.join(random.choices(self.characters, k=6))
    

if __name__ == "__main__":
  # Example usage:
  url_shortener = URLShortener()
  original_url = "https://www.example.com"
  shortened_url = url_shortener.shorten(original_url)
  print(f"Shortened URL: {shortened_url}")
  restored_url = url_shortener.restore(shortened_url)
  print(f"Restored URL: {restored_url}")

  # Test case when entering the same URL twice
  same_original_url = "https://www.example.com"
  same_shortened_url = url_shortener.shorten(same_original_url)
  print(f"Shortened URL for the same original URL: {same_shortened_url}")