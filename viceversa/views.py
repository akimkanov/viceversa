from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    reverse_text = user_text[::-1]
    text_len = len(user_text.split())
    
    return render(request, 'reverse.html', {'usertext':user_text, 'reversed_text':reverse_text, 'len_text':text_len} )
