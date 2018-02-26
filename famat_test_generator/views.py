from django.shortcuts import render


def add_question(request):
    if request.method == "GET":
        return render(request, 'famat_test_generator/index.html')
    elif request.method == "POST":
        pass
