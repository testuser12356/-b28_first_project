import main.models as models


def my_variables(request):
    category_list = models.Category.objects.all()
    context = {
        "category_list": category_list
    }
    return context
