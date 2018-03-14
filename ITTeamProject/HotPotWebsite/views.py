from django.shortcuts import render

# Create your views here.
def index(request):

    # Return a rendered response to send to the client
    # We make use of the shortcut function to make our lives easier
    # Note that the first parameter is the template we wish to use
    response = render(request, 'HotPotWebsite/index.html')
    return response

def message_board(request):
    return render(request, 'HotPotWebsite/message_board.html')

def book(request):
    return render(request, 'HotPotWebsite/message_board.html')

def menu(request):
    return render(request, 'HotPotWebsite/message_board.html')

def about(request):
    return render(request, 'HotPotWebsite/about.html')
