from django.shortcuts import render

# xFPnqF8LrRgfK1bzK4zj8A==cJaME9eRe3kEhT8x API key
# Create your views here.

def home(request):
    import json
    import requests

    if request.method == 'POST':
        query = request.POST['query']
        activityType1 = 'lifting'
        activityType2 = 'run'
        activityType3 = 'yoga'
        activityType4 = 'brisk'

        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_url_act = 'https://api.api-ninjas.com/v1/caloriesburned?activity='
        api_request1 = requests.get(api_url + query, headers={'X-Api-Key': 'xFPnqF8LrRgfK1bzK4zj8A==cJaME9eRe3kEhT8x'})
        api_request2 = requests.get(api_url_act + activityType1, headers={'X-Api-Key': 'xFPnqF8LrRgfK1bzK4zj8A==cJaME9eRe3kEhT8x'})
        api_request3 = requests.get(api_url_act + activityType2, headers={'X-Api-Key': 'xFPnqF8LrRgfK1bzK4zj8A==cJaME9eRe3kEhT8x'})
        api_request4 = requests.get(api_url_act + activityType3, headers={'X-Api-Key': 'xFPnqF8LrRgfK1bzK4zj8A==cJaME9eRe3kEhT8x'})
        api_request5 = requests.get(api_url_act + activityType4, headers={'X-Api-Key': 'xFPnqF8LrRgfK1bzK4zj8A==cJaME9eRe3kEhT8x'})
        try:
            api1 = json.loads(api_request1.content)
            api2 = json.loads(api_request2.content)
            api3 = json.loads(api_request3.content)
            api4 = json.loads(api_request4.content)
            api5 = json.loads(api_request5.content)
            print(api_request1.content)
            print(api_request2.content)
            print(api_request3.content)
            print(api_request4.content)
            print(api_request5.content)
        except Exception as e:
            api1 = "There was an error with api1!"
            api2 = "There was an error with api2!"
            api3 = "There was an error with api3!"
            api4 = "There was an error with api4!"
            api5 = "There was an error with api5!"
            print(e)
        return render(request, 'home.html', {'api1': api1, 'api2': api2, 'api3': api3, 'api4': api4, 'api5': api5})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
