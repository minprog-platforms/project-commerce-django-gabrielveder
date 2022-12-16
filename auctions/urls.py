from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("add_comment/<int:id>", views.add_comment, name ="add_comment"),
    path("listing_page/<int:id>", views.listing_page, name="listing_page"),
    path("add_bid/<int:id>", views.add_bid, name ="add_bid"),
    path("close_auction/<int:id>", views.close_auction, name ="close_auction"),
]
