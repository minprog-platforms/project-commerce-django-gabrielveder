# Commerce website

During this project, I will be building an online auction website. Here, users can create an account, create new auction listings, bid on existing listings and comment on listings. The default page will display an overview of all the current auction listings and information about these listings. A user can add a photo to their own listing, write a description for their listing and set a minumum bidding price. They will also be able to close their auctions, in which case, the highest bidder will be the winner of the auction and the auction will no longer be listed. If the winner is logged in and visits the auction page, the page will notify them of being the winner of the auction. Some parts of the web page will of course only work for those who are logged in. Users that have not logged into an account will not be able to place bids or comments on active listings. 


## Getting Started

#### Models

At least three models will have to be created in Django. A model for auction listings, a model for bids and a model for comments on these listings. These models will be made by creating classes in the models.py file. 

#### New Listings

Logged in users should be able to visit a page where they will be able to create a new listing. They should be able to give a title, a description, a minumum bidding price and a url for an image associated with the listing. To make this work, a listing model will have to be created, as well as a new views entry and a new URL in urls.py. Also, a page will have to be created in HTML. 

#### Active listings

The default route of the website will route users to a page where all the listings will be displayed. This page will roughly be the same for logged in users and not logged in users. The auction's image will be displayed, the title of the listing, a (short) description as well as the current highest bid.

#### Listing Page

When a logged in user clicks on a listing, they should see a page where they can leave a comment, make a bid on the listing (at least as high as the current bid), add the listing to their watchlist and read the comments that other users have placed on the listing. 

#### What this will look like

This is a render of what the default route will look like:

![Default route](sketches/start_page.png)

This is a sketch of what a listing will look like:

![Listing entry](sketches/listing_entry.png)

And here is a sketch of the add listing page:

![New listing](sketches/new_listing.png)