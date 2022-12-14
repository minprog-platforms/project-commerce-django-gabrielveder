from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Comment, Bid


def index(request):
    listings = Listing.objects.filter(isactive=True)
    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def new_listing(request):
    if request.method == "POST":
        url = request.POST["url"]
        title = request.POST["title"]
        description = request.POST["description"]
        start_price = request.POST["start_price"]
        user = request.user
        
        # Create bid object to link listing to
        bid = Bid(amount=int(start_price), user=user)
        bid.save()
        
        # Create listing object 
        new_listing = Listing(
            title = title,
            description = description,
            current_bid = bid,
            owner = user,
            image_url = url
            )
        new_listing.save()
        # return render(request, "auctions/index.html")
        return index(request)
    else:
        return render(request, "auctions/new_listing.html")


def listing_page(request, id):
    listing = Listing.objects.get(pk=id)
    comments = Comment.objects.filter(listing=listing)

    # Bool that checks if the visitor is the owner of the page
    visitor_is_owner = listing.owner.username == request.user.username

    # Render listing page
    return render(request, "auctions/listing_page.html",{
        "listing":listing,
        "comments":comments,
        "visitor_is_owner":visitor_is_owner
    })

@login_required
def add_comment(request, id):
    listing = Listing.objects.get(pk=id)
    user = request.user
    comment_body = request.POST['new_comment']

    # Create comment object and save to database
    comment = Comment(author=user, listing=listing, text=comment_body)
    comment.save()
    return HttpResponseRedirect(reverse("listing_page", args=(id, )))

@login_required
def add_bid(request, id):
    listing = Listing.objects.get(pk=id)
    comments = Comment.objects.filter(listing=listing)

    # Save bid amount as integer
    bid = int(request.POST["new_bid"])

    # Bool that checks if the visitor is the owner of the page
    visitor_is_owner = listing.owner.username == request.user.username
    if bid > listing.current_bid.amount:
        new_bid = Bid(user=request.user, amount=bid)
        new_bid.save()
        listing.current_bid = new_bid
        listing.save()
        return render(request, "auctions/listing_page.html",{
        "listing":listing,
        "comments":comments,
        "visitor_is_owner":visitor_is_owner
    })

@login_required
def close_auction(request, id):
    listing = Listing.objects.get(pk=id)
    comments = Comment.objects.filter(listing=listing)

    # Sets listing to inactive when listing is closed by owner
    listing.isactive = False
    listing.save()
    visitor_is_owner = listing.owner.username == request.user.username
    return render(request, "auctions/listing_page.html",{
    "listing":listing,
    "comments":comments,
    "visitor_is_owner":visitor_is_owner
    })
