from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from Api.models import Book
from Api.serializers import BookSerializer


@csrf_exempt
def CreateBook(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    bookData = JSONParser().parse(request)

    try:
        checkBook = Book.objects.get(
            Title=bookData["Title"],
            AuthorFirstName=bookData["AuthorFirstName"],
            AuthorLastName=bookData["AuthorLastName"]
        )
    except Book.DoesNotExist:
        book = BookSerializer(data=bookData)
        if book.is_valid():
            book.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    checkBook.Quantity += bookData["Quantity"]
    checkBook.save()
    return HttpResponse(status=status.HTTP_302_FOUND)


@csrf_exempt
def DeleteBookById(request, id):
    if request.method != "DELETE":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    try:
        book = Book.objects.get(Id=id)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    Book.objects.filter(Id=id).delete()
    return HttpResponse(status=status.HTTP_200_OK)


@csrf_exempt
def GetBook(request, title, authorFirstName, authorLastName):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    try:
        book = Book.objects.get(Title=title, AuthorFirstName=authorFirstName, AuthorLastName=authorLastName)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    bookData = BookSerializer(book)
    return JsonResponse(bookData.data)


@csrf_exempt
def GetBookById(request, id):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    try:
        book = Book.objects.get(Id=id)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    bookData = BookSerializer(book)
    return JsonResponse(bookData.data)


@csrf_exempt
def GetAllBooks(request):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    books = Book.objects.all().distinct()
    booksData = BookSerializer(books, many=True)
    return JsonResponse(booksData.data, safe=False)


@csrf_exempt
def EditBookById(request, id, property, newData):
    if request.method != "PATCH":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    elif property == "Id":
        return HttpResponse(status=status.HTTP_403_FORBIDDEN)

    try:
        book = Book.objects.get(Id=id)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if property == "Title":
        book.Title = newData
    elif property == "AuthorFirstName":
        book.AuthorFirstName = newData
    elif property == "AuthorLastName":
        book.AuthorLastName = newData
    elif property == "Price":
        book.Price = float(newData)
    elif property == "Quantity":
        book.Quantity = int(newData)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    book.save()
    return HttpResponse(status=status.HTTP_200_OK)


@csrf_exempt
def GetSumOfAllBookPrices(request):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    total = float()
    books = Book.objects.all().distinct()
    for book in books:
        total += book.Price * book.Quantity

    total = f"{total:.2f}"
    total = float(total)

    priceData = {
        "Total": total
    }
    return JsonResponse(priceData)


@csrf_exempt
def CreateFile(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    total = float()
    file = open("Books.txt", "a")
    title = "Title"
    author = "Author"
    unitPrice = "Unit Price"
    quantity = "Quantity"
    price = "Total Price"
    file.write(f"{title:<50s} {author:<40s} {unitPrice:<12s} {quantity:<12s} {price:<11s}\n\n")

    books = Book.objects.all().distinct().order_by("AuthorLastName")
    for book in books:
        fullName = f"{book.AuthorFirstName} {book.AuthorLastName}"
        unitPrice = book.Price
        price = unitPrice * book.Quantity
        unitPrice = f"${unitPrice:.2f}  "
        total += price
        price = f"${price:.2f}"
        file.write(f"{book.Title:<50s} {fullName:<40s} {unitPrice:>12s} {str(book.Quantity):<12s} {price:>11s}\n")
    file.write("\n")
    price = "Sum of All Books"
    file.write(f"{price:>129s}\n")
    total = f"${total:.2f}"
    file.write(f"{total:>129s}\n")
    file.close()
    return HttpResponse(status=status.HTTP_200_OK)
