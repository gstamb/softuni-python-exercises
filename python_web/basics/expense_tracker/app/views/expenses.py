from django.shortcuts import get_object_or_404, render, redirect
from app.forms import ExpenseForm
from app.models import Expense, Profile
from django.db import transaction


def create_expense(request):
    return persist_expense(request)


def edit_expense(request, pk):
    return persist_expense(request, pk)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    form = ExpenseForm(instance=expense)
    for fieldname in form.fields:
        form.fields[fieldname].disabled = True
    if request.method == "GET":
        context = {
            'expense': expense,
            'form': form
        }
        return render(request, 'expense-delete.html', context)
    else:
        user = Profile.objects.get(pk=expense.fk.id)
        user.budget_left += expense.price
        user.save()
        expense.delete()
        return redirect('index')


def persist_expense(request, pk=None):
    if pk:
        expense = get_object_or_404(Expense, pk=pk)
        template = "expense-edit.html"
    else:
        expense = Expense()
        template = "expense-create.html"

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            return update_expense_and_budget(Profile.objects.first(), form)
    else:
        form = ExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, template, context)


@transaction.atomic
def update_expense_and_budget(user_profile, form):
    new_expense = form.save(commit=False)
    new_expense.fk = user_profile
    new_expense.save()
    user_profile.budget_left = user_profile.budget - sum(expense.price for expense in Expense.objects.all())
    user_profile.save()

    return redirect('index')
 