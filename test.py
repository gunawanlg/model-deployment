import requests

if __name__ == "__main__":
    feature1 = str(1.0)
    feature2 = str(2.0)
    feature3 = str(3.0)
    feature4 = str(4.0)
    feature5 = str(5.0)
    
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

    URL = "http://gunawangaol.pythonanywhere.com/"
    URL2 = "https://gunawangaol.pythonanywhere.com/prediction?feature1="+feature1+"&feature2="+feature2+"&feature3="+feature3+"&feature4="+feature4+"&feature5="+feature5

    # sending get request and saving the response as response object 
    # r = requests.get(url = URL, json=datum_body) 
    r = requests.get(url = URL2)
    # extracting data in json format  
    print(r.json())