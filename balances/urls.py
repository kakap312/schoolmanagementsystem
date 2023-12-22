from django.urls import path 
from .import views

urlpatterns = [
    path("dashboard/balance/single", views.single, name = 'balancesingleview'), 
    path("dashboard/balance/bulk", views.bulk, name = 'balancebulkview'),
    # path("dashboard/fee/filter", views.filter, name = 'filterfee'),
    # path("dashboard/payment/receipt/<int:id>", views.receipt),
    # path("dashboard/payment/newentry", views.add, name = 'newentrypayment'),
    # path("dashboard/payment/search", views.search,name = 'searchpayment'),
    # path("dashboard/payment/delete/<int:id>", views.delete),
    # path("dashboard/payment/edit/<int:id>", views.edit, name = 'editpayment')
]


