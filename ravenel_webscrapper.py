# Environment set up
import requests
import pandas as pd

def get_json(url): # for requesting url ard transforming json file
  response = requests.get(url)
  if not response.ok:   # .status_code == 200
    print(f'Code: {response.status_code}, url: {url}')
  return response.json()

def get_lots_data(json): #scraping data from the json dictionary
  ret = []
  for item in json["data"]:
    artists = ', '.join([artist['name'] for artist in item['artistList']])
  
    data = {
        'auction': item.get('lastAuction'),
        'name': item.get('name'),
        'artist': artists,
        'year': item.get('year'),
        'material': item.get('material'),
        'dimention': item.get('dimension'),
        'es_price': item.get('esPriceTw'),
        'fin_price': item.get('fiPriceTw'),
        'cover': 'https://ravenel.com/' + item.get('coverUrl')
        }
    ret.append(data)
  return ret

def main(): # the main application
  urls = []
  page_index = 0
  url = f'https://ravenel.com/rest/cata/lots/search/882f4163-b8e5-458a-9e35-662911d540b8?fuzzyKeyword=%E7%BE%85%E8%8A%99%E5%A5%A7%E5%8F%B0%E5%8C%972022%E7%A7%8B%E5%AD%A3%E6%8B%8D%E8%B3%A3%E6%9C%83&artistName=&orderBy=auctionShowDateDESC&auctionYear=2022&pageIndex={page_index}&pageSize=20&language=zh-TW'
  
  while get_json(url)['data']:
    urls.append(url)
    page_index += 1
    url = f'https://ravenel.com/rest/cata/lots/search/882f4163-b8e5-458a-9e35-662911d540b8?fuzzyKeyword=%E7%BE%85%E8%8A%99%E5%A5%A7%E5%8F%B0%E5%8C%972022%E7%A7%8B%E5%AD%A3%E6%8B%8D%E8%B3%A3%E6%9C%83&artistName=&orderBy=auctionShowDateDESC&auctionYear=2022&pageIndex={page_index}&pageSize=20&language=zh-TW'
 
  data = []
  for url in urls:
    data += get_lots_data(get_json(url))
  df = pd.DataFrame(data, )
  df.to_csv('result.csv', index=False)

if __name__ == "__main__":
  main()
