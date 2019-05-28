from django.conf.urls import url
from tabafi.views import farmer_views, customer_views, views

urlpatterns = [
    url(
        r'^api/v1/farmers/(?P<pk>[0-9]+)$',
        farmer_views.get_delete_update_farmer,
        name='get_delete_update_farmer'
    ),
    url(
        r'^api/v1/farmers/$',
        farmer_views.get_post_farmers,
        name='get_post_farmer'
    ),
    url(
        r'^api/v1/customers/(?P<pk>[0-9]+)$',
        customer_views.get_delete_update_customer,
        name='get_delete_update_farmer'
    ),
    url(
        r'^api/v1/customers/$',
        customer_views.get_post_customers,
        name='get_post_farmer'
    ),
    url(
        r'^api/v1/login/$',
        views.login,
        name='farmer_login'
    )
]