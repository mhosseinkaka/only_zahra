import requests
from django.shortcuts import render

def get_random_poem(request):
    api_url = "http://c.ganjoor.net/beyt-json.php"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        poem_data = response.json()
        context = {
            'm1': poem_data.get('m1', ''),
            'm2': poem_data.get('m2', ''),
            'poet': poem_data.get('poet', ''),
            'url': poem_data.get('url', ''),
        }
        return render(request, 'poem_display/poem.html', context)
    except requests.exceptions.RequestException as e:
        context = {'error': f"خطا در دریافت شعر: {e}"}
        return render(request, 'poem_display/error.html', context)
    except ValueError:
        context = {'error': "فرمت داده دریافتی از API نامعتبر است."}
        return render(request, 'poem_display/error.html', context)
    

def get_poem_with_param(request, poem_id=None):
    api_url = "http://c.ganjoor.net/beyt-json.php?p="
    params = {}
    if poem_id is not None:
        params['p'] = poem_id 

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        poem_data = response.json()

        if not poem_data.get('m1') and not poem_data.get('m2'):
            context = {'error': f"شعری با شناسه {poem_id} یافت نشد یا داده‌ها نامعتبر است."}
            return render(request, 'poem_display/error.html', context)

        context = {
            'm1': poem_data.get('m1', ''),
            'm2': poem_data.get('m2', ''),
            'poet': poem_data.get('poet', ''),
            'url': poem_data.get('url', ''),
            'poem_id_requested': poem_id 
        }
        return render(request, 'poem_display/poem_with_param.html', context)

    except requests.exceptions.RequestException as e:
        context = {'error': f"خطا در دریافت شعر: {e}"}
        return render(request, 'poem_display/error.html', context)
    except ValueError:
        context = {'error': "فرمت داده دریافتی از API نامعتبر است."}
        return render(request, 'poem_display/error.html', context)
