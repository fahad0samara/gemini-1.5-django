from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import google.generativeai as genai
from django.conf import settings
from django.shortcuts import render

@csrf_exempt
@require_POST
def generate_text_only(request):
    prompt = request.POST.get('prompt', '')
    if not prompt:
        return JsonResponse({'error': 'Prompt is required'}, status=400)

    try:
        # Set the API key from settings
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return JsonResponse({'text': response.text})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def text_form(request):
    return render(request, 'generate_text.html')
