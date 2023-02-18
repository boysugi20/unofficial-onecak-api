from flask import Flask, jsonify
import requests
import datetime
import time
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/get-post/<int:post_id>')
def get_post(post_id):

    r = requests.get('https://1cak.com/' + str(post_id))
    html_content = r.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    posts = soup.select('[id^="posts"]')
    
    response = {}

    for post in posts:
        nsfw_flag = False

        img_elements = post.find_all('img')

        for img in img_elements:
            if("title" in img.attrs):
                if(img['title'] == 'Not safe for work'):
                    nsfw_flag = True
                
        for img in img_elements:
            source = str(img['src'])
            if(source.startswith('/posts')):
                response = {
                    'id': post_id,
                    'title': img['title'],
                    'link' : 'https://1cak.com/' + str(post_id),
                    'image': 'https://1cak.com' + source,
                    'nsfw' : nsfw_flag
                }
                
    return jsonify(response)

@app.route('/random')
def get_post_random():

    r = requests.get('https://1cak.com/shuffle')
    html_content = r.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    posts = soup.select('[id^="posts"]')
    
    response = {}
    
    for post in posts:
        
        nsfw_flag = False
        
        post_id = post['id'][5:] # remove "posts" prefix
        img_elements = post.find_all('img')
        
        for img in img_elements:
            if("title" in img.attrs):
                if(img['title'] == 'Not safe for work'):
                    nsfw_flag = True
                
        for img in img_elements:
            source = str(img['src'])
            if('/posts/' in source):
                response ={
                    'id': post_id,
                    'title': img['title'],
                    'link' : 'https://1cak.com/' + str(post_id),
                    'image': str(source),
                    'nsfw' : nsfw_flag
                }
                
    return jsonify(response)
    
@app.route('/get-categorized/<category>/<int:hours>')
def get_post_categorized(category, hours):
    
    now = datetime.datetime.now()
    start = now - datetime.timedelta(hours=hours)
    end = now - datetime.timedelta(minutes=2)
    
    unix_from = int(time.mktime(start.timetuple()))
    unix_to = int(time.mktime(end.timetuple()))
    
    if(category == 'lol'):
        url = 'https://1cak.com/lol-' + str(unix_from)
    elif(category == 'trending'):
        url = 'https://1cak.com/trending-' + str(unix_from)
    elif(category == 'recent'):
        url = 'https://1cak.com/recent-0-' + str(unix_from)
    elif(category == 'legendary'):
        url = 'https://1cak.com/legendary-0-' + str(unix_from)
    else:
        raise ValueError('Category not valid!')
    
    r = requests.get(url)
    html_content = r.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    posts = soup.select('[id^="posts"]')
    
    temp = []
    
    for post in posts:
        
        nsfw_flag = False
        
        post_id = post['id'][5:] # remove "posts" prefix
        img_elements = post.find_all('img')
        
        for img in img_elements:
            if("title" in img.attrs):
                if(img['title'] == 'Not safe for work'):
                    nsfw_flag = True
                
        for img in img_elements:
            source = str(img['src'])
            if(source.startswith('/posts')):
                temp.append({
                    'id': post_id,
                    'title': img['title'],
                    'link' : 'https://1cak.com/' + str(post_id),
                    'image': 'https://1cak.com' + source,
                    'nsfw' : nsfw_flag
                })
                
    response = {'category':category, 'posts': temp}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False)