from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
        html = '''
        <html><head><title>Index</title>
        <style>
        body { background: linear-gradient(120deg, #f8ffae 0%, #43c6ac 100%); min-height:100vh; margin:0; display:flex; align-items:center; justify-content:center; }
        .center-box { background:#fff; padding:40px 32px; border-radius:18px; box-shadow:0 4px 24px rgba(0,0,0,0.10); text-align:center; }
        h1 { color:#43c6ac; margin-bottom:10px; }
        p { color:#555; font-size:1.1rem; }
        </style></head><body>
        <div class="center-box">
            <h1>ICT12367 SPU</h1>
            <p>Welcome to the Django Project</p>
            <a href="/about/" style="color:#fff; background:#43c6ac; padding:10px 24px; border-radius:8px; text-decoration:none; font-weight:bold;">About</a>
        </div>
        </body></html>
        '''
        return HttpResponse(html)

def about(request):
        html = '''
        <html><head><title>About</title>
        <style>
        body { background: linear-gradient(120deg, #f093fb 0%, #f5576c 100%); min-height:100vh; margin:0; display:flex; align-items:center; justify-content:center; }
        .center-box { background:#fff; padding:40px 32px; border-radius:18px; box-shadow:0 4px 24px rgba(0,0,0,0.10); text-align:center; }
        h1 { color:#f5576c; margin-bottom:10px; }
        p { color:#555; font-size:1.1rem; }
        </style></head><body>
        <div class="center-box">
            <h1>About</h1>
            <p>รสมาริน มุมิ 68068328<br>วิชา ICT12367</p>
            <a href="/" style="color:#fff; background:#f5576c; padding:10px 24px; border-radius:8px; text-decoration:none; font-weight:bold;">Home</a>
        </div>
        </body></html>
        '''
        return HttpResponse(html)

def contact(request):
    return HttpResponse('<h1>ติดต่อ 68068328 นางสาวรสมาริน มุมิ</h1>')

def form(request):
    return render(request, 'form.html')