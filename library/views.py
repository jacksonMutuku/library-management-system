from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Member, Transaction
from datetime import date
from django.utils import timezone
from django.http import HttpResponse

def index(request):
    return render(request, 'library/base.html')

def transaction_list(request):
    transactions = Transaction.objects.all()
    for transaction in transactions:
        print(f"Transaction ID: {transaction.id}")
    return render(request, 'library/transaction_list.html', {'transactions': transactions})

def book_list(request):
    # Always define `books` before using it
    books = Book.objects.all()  # Fetch all books from the database
    print("Books:", books) 
    return render(request, 'library/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        stock = request.POST['stock']
        Book.objects.create(title=title, author=author, stock=stock)
        return redirect('book_list')
    return render(request, 'library/book_form.html')

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.stock = request.POST['stock']
        book.save()
        return redirect('book_list')
    return render(request, 'library/book_form.html', {'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

# Similar views for Members
# Member CRUD
def member_list(request):
    members = Member.objects.all()
    print("members", members)
    return render(request, 'library/member_list.html', {'members': members})

def member_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        outstanding_debt_str = request.POST.get('outstanding_debt', '0.0')

        try:
            outstanding_debt = float(outstanding_debt_str)
            if outstanding_debt < 0:
                outstanding_debt = 0.0  # Default to 0.0 if the value is negative
        except ValueError:
            outstanding_debt = 0.0  # Default to 0.0 if conversion fails

        Member.objects.create(name=name, email=email, outstanding_debt=outstanding_debt)
        return redirect('member_list')
    
    return render(request, 'library/member_form.html', {'member': None})

def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.name = request.POST['name']
        member.email = request.POST['email']
        member.outstanding_debt = request.POST['outstanding_debt']
        member.save()
        return redirect('member_list')
    return render(request, 'library/member_form.html', {'member': member})

def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()
    return redirect('member_list')

def issue_book(request):
    if request.method == 'POST':
        member_id = request.POST.get('member')
        book_id = request.POST.get('book')

        try:
            member = Member.objects.get(id=member_id)
            book = Book.objects.get(id=book_id)

            # Check if the book is available in stock
            if book.stock > 0:
                # Create a transaction and reduce the stock
                transaction = Transaction.objects.create(
                    member=member,
                    book=book,
                    issue_date=timezone.now(),
                    return_date=None
                )
                book.stock -= 1
                book.save()
                return redirect('transaction_list')  # Redirect after successful issue
            else:
                return HttpResponse("Book is out of stock.")  # Handle case where book is not in stock
        except Member.DoesNotExist:
            return HttpResponse("Member does not exist.")
        except Book.DoesNotExist:
            return HttpResponse("Book does not exist.")
    
    # GET request - Display the form
    members = Member.objects.all()
    books = Book.objects.all()
    return render(request, 'library/issue_book.html', {'members': members, 'books': books})


def search_books(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})



def return_book(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)

    # Check if the book has already been returned
    if not transaction.return_date:
        transaction.return_date = date.today()  # Mark the return date
        days_issued = (transaction.return_date - transaction.issue_date).days

        # Rent fee (you can define how much to charge per day)
        rent_fee_per_day = 50
        transaction.fee = days_issued * rent_fee_per_day

        transaction.book.stock += 1  # Increase the stock when the book is returned
        transaction.book.save()
        transaction.save()

    return redirect('transaction_list')


# return render(request, 'library/member_form.html')