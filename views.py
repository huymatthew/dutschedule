from django.shortcuts import render
from TKB.generator import generator
from django.http import HttpResponse
import io
# Create your views here.
def generator(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        # Process the data as needed
        image = generator(data)
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')
        buffer.seek(0)
        
        return HttpResponse(buffer, content_type='image/png')
    return HttpResponse('NO POST DATA!!')