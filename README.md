# model-deployment
Example model deployment at DSA HCID Iykra training 2019.

## API Testing
Example payload

```python
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

Body is an array of dictionary, with minimum size of 1, will return error code 400 if empty. 

Sample test using requests module in python.

```python
import requests

url = "https://gunawangaol.pythonanywhere.com/"
r = requests.get(url, json=payload)
print(r.json())
```

## Single Data Formlike User Testing
Visit [this link](https://arc-rendezvous.github.io/model-deployment/).

<hr>

Copyright &copy; 2020 Gunawan Lumban Gaol

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language overning permissions and limitations under the License.
