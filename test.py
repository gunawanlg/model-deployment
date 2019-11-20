import requests

if __name__ == "__main__":
    URL = "http://gunawangaol.pythonanywhere.com/"
    
    datum_body = {
        "body": [
            {
                "feat1": 1.0,
                "feat2": 2.0,
                "feat3": 3.0,
                "feat4": 4.0,
                "feat5": 5.0
            },
            {
                "feat1": 1.0,
                "feat2": 2.0,
                "feat3": 3.0,
                "feat4": 4.0,
                "feat5": 5.0
            }
        ]
    }

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, json=datum_body) 
    
    # extracting data in json format  
    print(r.json())