
import urllib.request,json
from .models import Blog


base_url = None

def configure_request(app):
    global base_url
    
    base_url = app.config['QUOTES_API_BASE_URL']

def get_blogs():
    
   

    with urllib.request.urlopen(base_url) as url:
        get_blogs_data = url.read()
        get_blogs_response = json.loads(get_blogs_data)


        id = blogs_details_response.get('id')
        author = blogs_details_response.get('author')
        quote= blogs_details_response.get('quote')
        

        blogs_object =Blog (id,author,quote)

    return blogs_object

