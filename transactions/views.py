from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from .models import Transaction
from .forms import TransactionForm

def dashboard(request):
    """Main dashboard showing profit/loss overview and recent transactions"""
    # Get all transactions
    transactions = Transaction.objects.all()
    
    # Calculate totals
    total_income = transactions.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = transactions.filter(transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    net_profit = total_income - total_expenses
    
    # Get recent transactions (last 10)
    recent_transactions = transactions[:10]
    
    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_profit': net_profit,
        'recent_transactions': recent_transactions,
        'is_profit': net_profit >= 0,
    }
    return render(request, 'transactions/dashboard.html', context)

def transaction_list(request):
    """Show all transactions with filtering options"""
    transactions = Transaction.objects.all()
    
    # Filter by type if specified
    transaction_type = request.GET.get('type')
    if transaction_type in ['income', 'expense']:
        transactions = transactions.filter(transaction_type=transaction_type)
    
    context = {
        'transactions': transactions,
    }
    return render(request, 'transactions/transaction_list.html', context)

def add_transaction(request):
    """Add a new transaction"""
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # The date will be automatically set by auto_now_add=True in the model
            transaction = form.save(commit=False)
            transaction.save()
            messages.success(request, 'Transaction added successfully!')
            return redirect('transactions:dashboard')
    else:
        # Pre-select transaction type if provided in URL
        initial_data = {}
        transaction_type = request.GET.get('type')
        if transaction_type in ['income', 'expense']:
            initial_data['transaction_type'] = transaction_type
        
        form = TransactionForm(initial=initial_data)
    
    context = {
        'form': form,
        'pre_selected_type': request.GET.get('type'),
    }
    return render(request, 'transactions/add_transaction.html', context)

def edit_transaction(request, pk):
    """Edit an existing transaction"""
    transaction = Transaction.objects.get(pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transaction updated successfully!')
            return redirect('transactions:transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    
    context = {
        'form': form,
        'transaction': transaction,
    }
    return render(request, 'transactions/edit_transaction.html', context)

def delete_transaction(request, pk):
    """Delete a transaction"""
    transaction = Transaction.objects.get(pk=pk)
    if request.method == 'POST':
        transaction.delete()
        messages.success(request, 'Transaction deleted successfully!')
        return redirect('transactions:transaction_list')
    
    context = {
        'transaction': transaction,
    }
    return render(request, 'transactions/delete_transaction.html', context)
