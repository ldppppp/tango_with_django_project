from rango.models import Category, Page


def populate():
    category1 = Category.objects.create(name='Python', views=128, likes=64)
    category2 = Category.objects.create(name='Django', views=64, likes=32)
    category3 = Category.objects.create(name='Other Frameworks', views=32, likes=16)

    page1_1 = Page.objects.create(category=category1, title='Official Python Tutorial',
                                  url='http://docs.python.org/3/tutorial/', views=category1.views)
    page1_2 = Page.objects.create(category=category1, title='How to Think like a Computer Scientist',
                                  url='http://www.greenteapress.com/thinkpython/', views=category1.views)
    page1_3 = Page.objects.create(category=category1, title='Learn Python in 10 Minutes',
                                  url='http://www.korokithakis.net/tutorials/python/', views=category1.views)

    page2_1 = Page.objects.create(category=category2, title='Official Django Tutorial',
                                  url='https://docs.djangoproject.com/en/2.1/intro/tutorial01/', views=category2.views)
    page2_2 = Page.objects.create(category=category2, title='Django Rocks',
                                  url='http://www.djangorocks.com/', views=category2.views)
    page2_3 = Page.objects.create(category=category2, title='How to Tango with Django',
                                  url='http://www.tangowithdjango.com/', views=category2.views)

    page3_1 = Page.objects.create(category=category3, title='Bottle',
                                  url='http://bottlepy.org/docs/dev/', views=category3.views)
    page3_2 = Page.objects.create(category=category3, title='Flask',
                                  url='http://flask.pocoo.org', views=category3.views)
