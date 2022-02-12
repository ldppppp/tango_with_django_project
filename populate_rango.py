from rango.models import Category, Page


def populate():
    category1 = Category.objects.create(name='Python', views=128, likes=64)
    category2 = Category.objects.create(name='Django', views=64, likes=32)
    category3 = Category.objects.create(name='Other Frameworks', views=32, likes=16)

    page1_1 = Page.objects.create(category=category1, title='Official Python Tutorial')
    page1_2 = Page.objects.create(category=category1, title='How to Think like a Computer Scientist')
    page1_3 = Page.objects.create(category=category1, title='Learn Python in 10 Minutes')

    page2_1 = Page.objects.create(category=category2, title='Official Django Tutorial')
    page2_2 = Page.objects.create(category=category2, title='Django Rocks')
    page2_3 = Page.objects.create(category=category2, title='How to Tango with Django')

    page3_1 = Page.objects.create(category=category3, title='Bottle')
    page3_2 = Page.objects.create(category=category3, title='Flask')