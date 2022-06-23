import requests

def connect_post(url, head, data, redirects):
    r = None
    if(data and head and redirects==False):
        r = requests.post(
            url = url,
            headers = head,
            data = data,
            allow_redirects = redirects,
            )
    elif(data and head):
        r = requests.post(
            url = url,
            headers = head,
            data = data,
            )
    elif(data and redirects==False):
        r = requests.post(
            url = url,
            data = data,
            allow_redirects = redirects,
            )
    elif(head and redirects==False):
        r = requests.post(
            url = url,
            headers = head,
            allow_redirects = redirects,
            )        
    elif(data):
        r = requests.post(
            url = url,
            data = data
            )
    elif(head):
        r = requests.post(
            url = url,
            headers = head
            )
    return r
    
def connect_get(url, head):
    r = requests.get(
            url = url,
            headers = head
            )
    return r
    
def connect_put(url, head, data):
    if(data and head):
        r = requests.put(
            url = url,
            headers = head,
            data = data,
            )
    elif(data):
        r = requests.put(
            url = url,
            data = data,
            )
    return r