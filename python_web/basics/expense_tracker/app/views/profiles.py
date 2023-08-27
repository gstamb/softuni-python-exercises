from django.shortcuts import render, redirect
from app.forms import ProfileForm
from app.models import Expense, Profile


def index(request):
    users = Profile.objects.first()
    if not users:
        return create_profile(request)
    else:
        expenses = Expense.objects.all()
        context = {
            'profile': users,
            'expenses': expenses
        }
        return render(request, 'home-with-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    return persist_profile(request, profile, 'profile-edit.html')


def create_profile(request):
    return persist_profile(request, template_name='home-no-profile.html')


def profile_page(request):
    user = Profile.objects.first()
    context = {
        'profile': user
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        return render(request, 'profile-delete.html')
    else:
        profile.delete()
        return redirect('index')


def persist_profile(request, profile=None, template_name='home-no-profile.html'):
    if profile is None:
        profile = Profile()
 
    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        context = {
            'form': form,
        }
        return render(request, template_name, context)

    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.budget_left = profile.budget - sum(expense.price for expense in Expense.objects.all())
            profile.save()
            return redirect('index')
        else:
            context = {
                'form': form,
            }
            return render(request, template_name, context)


 