from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


@login_required
def scraper_view(request):
    data = None

    if request.method == 'POST':
        url = request.POST.get('url')

        try:
            headers = {
                "User-Agent": "Mozilla/5.0"
            }

            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # mostramos el HTML tal cual
            data = response.text

        except Exception as e:
            data = f"❌ Error al scrapear: {str(e)}"

    return render(request, 'scraper/scraper.html', {'data': data})
