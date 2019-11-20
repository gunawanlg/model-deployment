# model-deployment
Example model deployment at DSA HCID Iykra training 2019.

## API Testing
Example payload

```
payload = {
  "body":
  [
    {
      "feat1": 1.0,
      "feat2": 2.0,
      "feat3": 3.0,
      "feat4": 4.0,
      "feat5": 5.0,
    },
    {
      "feat1": 1.0,
      "feat2": 2.0,
      "feat3": 3.0,
      "feat4": 4.0,
      "feat5": 5.0,
    },
    ...
  ]
}
```

Body is an array of dictionary, with minimum size of 1, will return error code 400 if empty. Sample test using requests module in python

```python
import requests

url = "https://gunawangaol.pythonanywhere.com/"
r = request.get(url, payload)
print(r.json())
```

## Single Data Formlike User Testing
Visit [arc-rendezvous.github.io/model-deployment]()
