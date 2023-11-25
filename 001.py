#download a novel
import requests
import parsel

def get_response(html_url):
    headers = {
        'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
                
    }
    response = requests.get(url=html_url,headers=headers)
    return response

def get_novel_content(html_url):
    html_data = get_response(html_url).text
    selector = parsel.Selector(html_data)
    href = selector.css('#list dd a::attr(href)').getall
    
    print(href)
    
    
    
    
url = 'http://www.biquxs.com/book/15441/'
get_novel_content(html_url=url)



