from django.conf.urls import url
from tabafi.views import farmer_views, customer_views, views
from tabafi.views.farmer_views import RequestList

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
    ),
    url(
        r'^api/v1/products/(?P<pk>[0-9]+)$',
        farmer_views.get_post_products,
        name='farmer_get_post_products'
    ),
    url(
        r'^api/v1/farmers/(?P<uuid>[0-9]+)/product/(?P<pk>[0-9]+)$',
        farmer_views.get_delete_update_product,
        name='farmer_get_delete_update_product'
    )
    # get, edit and delete product of a farmer by id.
    ,
    # url(
    #     r'^api/v1/product/(?P<pid>[0-9]+)$',
    #     UploadProductImage.as_view(),
    #     name='farmer_get_delete_update_product'
    # )
    # # post farmer's product image.
    # ,
    url(
        r'^api/v1/image/product/(?P<pid>[0-9]+)/add/$',
        farmer_views.post_product_image,
        name='farmer_post_product_image'
    )
    # post farmer's product image.
    ,
    url(
        r'^api/v1/image/product/(?P<pid>[0-9]+)/remove/$',
        farmer_views.delete_product_image,
        name='farmer_delete_product_image'
    )
    # delete farmer's product image.
    ,
    url(
        r'^api/v1/image/avatar/(?P<pid>[0-9]+)$',
        farmer_views.post_delete_farmer_avatar,
        name='farmer_delete_product_image'
    )
    # delete farmer's product image.
    ,
    url(
        r'^api/v1/requests/$',
        RequestList.as_view(),
        name='farmer_get_requests'
    )
    # delete farmer's product image.
    ,

]
