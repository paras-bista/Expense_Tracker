from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CurrentBalance, TrackingHistory

def index(request):
    if request.method == "POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')

        # Validate amount
        if not amount or float(amount) == 0:
            messages.error(request, "Amount cannot be zero") 
            return redirect('/')

        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)

        expense_type = "CREDIT"
        if float(amount) < 0:
            expense_type = "DEBIT"

        # Create new transaction
        tracking_history = TrackingHistory.objects.create(
            amount=float(amount),
            expense_type=expense_type,
            current_balance=current_balance,
            description=description
        )

        # Update current balance
        current_balance.current_balance += float(tracking_history.amount)
        current_balance.save()

        return redirect('/')

    # GET request - show data
    current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
    income = 0
    expense = 0
    
    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expense_type == "CREDIT":
            income += tracking_history.amount
        else:
            expense += tracking_history.amount

    context = {
        'income': income,
        'expense': expense, 
        'transactions': TrackingHistory.objects.all(),
        'current_balance': current_balance
    }
    return render(request, 'index.html', context)


# in views.py
def delete_transaction(request, id):
    tracking_history = TrackingHistory.objects.filter(id = id)

    if tracking_history.exists():
        current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
        tracking_history = tracking_history[0]
        
        current_balance.current_balance = current_balance.current_balance - tracking_history.amount

        current_balance.save()


    tracking_history.delete()
    return redirect('/')