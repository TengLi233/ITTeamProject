from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from HotPotWebsite.models import MenuCategory
from HotPotWebsite.models import Dish
from HotPotWebsite.forms import UserForm, UserProfileForm
from datetime import datetime
# Create your views here.


def index(request):
    response = render(request, 'HotPotWebsite/index.html')
    return response


def message_board(request):
    return render(request, 'HotPotWebsite/message_board.html')


def book(request):
    return render(request, 'HotPotWebsite/book.html')


def menu(request):
    category_list = MenuCategory.objects.all
    context_dict = {'categories': category_list}

    return render(request, 'HotPotWebsite/menu.html', context_dict)


def show_category(request, category_name_slug):
    context_dic = {}
    try:
        menucategory = MenuCategory.objects.get(slug=category_name_slug)
        dishes = Dish.objects.filter(category=menucategory)
        context_dic['dishes'] = dishes
        context_dic['menucategory'] = menucategory
    except MenuCategory.DoesNotExist:
        context_dic['pages'] = None
        context_dic['category'] = None

    return render(request, 'HotPotWebsite/category.html', context_dic)


def about(request):
    return render(request, 'HotPotWebsite/about.html')


def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.headpicture = request.FILES['picture']
			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'HotPotWebsite/register.html',
				  {
					  'user_form': user_form,
					  'profile_form': profile_form,
					  'registered': registered
				  })

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your Hot-Pot Website account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'HotPotWebsite/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
