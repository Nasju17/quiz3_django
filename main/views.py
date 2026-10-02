from django.shortcuts import render

def student_list(request):
    student = [
        {"name": "Imee Boo", "course": "BSPA","age": 20, "email": "imeeboo123@gmail.com"},
        {"name": "John Michael Mamac", "course": "BSIT", "age": 19, "email": "jm334@gmail.com"},
        {"name": "Vincel Alcantara", "course": "BSAIS", "age": 21, "email": "vinz888@gmail.com"},
        {"name": "Ericka Cantos", "course": "BSE", "age": 20, "email": "cantos6767@gmail.com"},
        {"name": "Shey Paz", "course": "DHRS", "age": 22, "email": "sheypaz@gmail.com"},
    ]

    return render(request, "main/home.html", {"student": student})