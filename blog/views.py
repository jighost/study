from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html', {})

def wc_board(request):
    return render(request, 'blog/wc_board.html', {})

def im(request):
    return render(request, 'blog/im.html', {})

