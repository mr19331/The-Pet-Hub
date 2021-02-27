# The Pet Hub 

The Pet Hub site is an ecommerce site for pet owners supplying  essential and non-essential pet items.  The site provides a platform for local pet services to advertise and promote their services to website visitors and it has a  blog featuring articles by  local  dog and cat service owners Eg dog-daycare, owners, local vets, local kennel and cattery service owners, dog groomers ,dog walkers etc.
Revenue  to the website owner can be earned through commission on items sold and from selling advertising space.  

The blog is a vital part of the ecommerce site because it  can generate traffic and customers. To achieve organic ranking and get traffic for a website is often difficult, slow and costly. A blog is an excellent way to cut advertising costs and boost the ranking of an online store quickly in a way that search engines approve. 
Blog posts allow the use of  relevant, search engine optimized keywords inserted as slugs in the blog title.
Blog articles can feature and review products in the store, and can link to those items.
Product descriptions for items in an ecommerce store have to be short and specific, a blog article can can use targeted keywords and lengthy descriptions. Carefully written posts are indexed by  search engines and will rank in the organic search results and generate traffic to the site with no advertising costs.
Product descriptions for items in an ecommerce store have to be short and specific, a blog article can  

Blog posts featuring products for sale can also be posted on social media  platforms for free advertising to generate traffic and customers by means of backlinks to the product item.
Blogging allows the business owner to write tips, user guides, comparison articles, etc. These articles can  create  more traffic and more interest without "hard selling"  and can demonstrate the strengths of store products compared to those of competitors. 

The regular addition of blog articles creates fresh content for the site, as do the  comments added by  blog readers. Search engines consider fresh content addition to a site as positive ranking feature. 
Shoppers may buy items from the website without creating an account but visitors are encouraged to register and create an account so they can store their shipping and purchasing information and so that the website can market to them through email. 

**Rationale for the Project** 
 The pet sector is flourishing and pet owners like to buy the latest pet gadgets and gear and are interested in pet items that are useful and fun. Django and Stripe technologies can create a very effective website that can be commercially viable and not difficult or time consuming to operate. I want  to develop this project and make it a reality.

- [The Pet Hub](#the-pet-hub)
  * [UX](#ux)
    + [Strategy & Scope](#strategy---scope)
        * [Visitor Goals](#visitor-goals)
        * [**The Pet Hub Club meets these needs with:**](#--the-pet-hub-club-meets-these-needs-with---)
        * [User Goals](#user-goals)
        * [**The Pet Hub Club meets these needs :**](#--the-pet-hub-club-meets-these-needs----)
        * [Business Goals](#business-goals)
        * [**The Pet Hub Club meets these needs by:**](#--the-pet-hub-club-meets-these-needs-by---)
    + [**Structure**](#--structure--)
      - [**Skeleton**](#--skeleton--)
      - [**Surface**](#--surface--)
  * [**User Stories**](#--user-stories--)
    + [**As a   shopper/blog reader **](#--as-a---shopper-blog-reader---)
    + [**As a registered shopper/blog reader:**](#--as-a-registered-shopper-blog-reader---)
    + [**As the website owner/admin (superuser):**](#--as-the-website-owner-admin--superuser----)
  * [Defensive Design](#defensive-design)
  * [Features of the website](#features-of-the-website)
    + [Existing Features](#existing-features)
        * [All Pages](#all-pages)
        * [**Home Page**](#--home-page--)
    + [Features Left to Implement](#features-left-to-implement)
  * [Technologies Used](#technologies-used)
  * [Deployment](#deployment)
      - [Steps to Heroku Deployment :](#steps-to-heroku-deployment--)
  * [Steps to Run App Locally](#steps-to-run-app-locally)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
      - [**Code**](#--code--)





  

## UX

### Strategy & Scope

##### Visitor Goals 

- Pet owners who want to buy useful items for their pets, for training or amusement, or general pet care 

-  Pet owners who want to read useful articles on pet care, health , nutrition and training. 

-  People who are considering getting a pet who want to read articles on pet care. 

-  Pet owners searching for pet services in their area that are advertising on The Pet Hub site( Groomers, Dog -DayCare, Dog Walkers, Cat & Dog Sitters, Vets, Dog Trainers, Kennels,  Catteries) 

-  Pet owners who want to ask questions and comment on the articles they read on the Pet Hub Blog 

  ##### **The Pet Hub Club meets these needs with:**
  
  A home page that is easy to navigate and clearly conveys the offerings of the site. 
  
  Purchases and reading the blog do not require user registration

  Pet items for sale that are good quality and popular
  Publishing frequent blog articles  relevant content and optimized for SEO to generate traffic and cut advertising costs
  Advertising space for local pet services
  Allowing  users to add comments or questions on the blog posts  
  
  The display banner offers free shipping as an enticement to buy 
   The menu links are clearly indicated and blog posts are shown on the home page. 
   Menu links have dropdowns for easy user access and icons when the site is on the mobile and tablet versions. 
  
  

#####  User Goals 

-  Repeat purchasers who want to store their purchasing  and shipping information, so they can buy  quickly giving just their name and email and CC number 

- People who like to read the blog articles and ask questions or comment . 

-  People who like to buy online with their credit card and make secure purchases at any time night or day. 

- Those who like to buy on their phone and have all the details of the purchase confirmed in an email immediately 

- Those who want to find and buy pet items that have been reviewed or compared or endorsed in some way 

   ##### **The Pet Hub Club meets these needs :**
  
  Registered users have the option to save purchasing and shipping information
  Payment for pet items purchased is secure and easy with the Stripe integration system. 
  
  Users can comment on the blog articles or ask questions 
The site uses Stripe payments which are secure and automatic
  A confirmation email is generate automatically to shoppers with details of their purchase.
  Providing relevant articles that review, compare or endorse products on the site
  
   

##### Business Goals

- Maximise revenue from purchases by pet owners 

-  Earn income  from selling advertising space on the website to local pet services

- Keep advertising costs for the website to a minimum with  blog posts on Social Media

-  Generate traffic to the Pet Hub shop and to the pet services advertising on the website by ranking the site in the organic searches using blog posts

-  Meet visitor and user expectations with an attractive and easily navigated website.  

- Meet visitor and user  expectations with  good quality and useful pet products that sell well

-  Meet visitor and user expectations with relevant informative articles on pet care that generate traffic to the website. 

-  Provide purchasing security for online shoppers

-  Have an online shop that takes automatic payments 

   ##### **The Pet Hub Club meets these needs by:**
  
  Stocking good quality useful items that are popular to avoid poor product reviews and negative feedback
  Designing a website that is attractive and easily navigated and understood with constantly updated content for shop and blog
  Using Stripe payment system with inbuilt and effective security and automation
  
  

 

### **Structure**

**Information Architecture**

The dropdown link and button options are the conventional and well understood means for a user to find what they need onsite.

 Pet products can sorted or searched for quickly and simply by category, rating or price. The search bar searches for items by keyword in the item description or in the item title. 

Information architecture is designed to keep to a minimum the user steps to purchasing a pet item
 To make a purchase users are not required to register or login, a user can select an item, add it to their cart and receive confirmation of purchase and checkout in a matter of minutes. 

The information architecture is that which will enable all user goals to be fulfilled as quickly and as simply as possible. 

Images are stored in 

#### **Skeleton** 

The home page is designed to encourage the visitor to buy pet items and to read the blog posts.  

 

#### **Surface** 

Appearance, images, colour choices and fonts were all chosen for a clean, minimal appearance 

Basic bootstrap buttons, colours and messages  were used in design.  primary versus secondary actions/notification was adhered to. 

Modern design conventions were followed.

Crispy forms were used to create simple forms with as few input fields as possible, the emphasis was on keeping user effort to a minimum. 

Fonts are those easy to read. 


 .

1. **Wireframes**
[Wireframes for the  Pet Hub](https://github.com/mr19331/the-pet-hub/blob/master/WIREFRAMES.md)

   



## **User Stories**

###           **As a   shopper/blog reader ** 

​          

- I expect to be able to access the information that I want easily using conventional  image and link clicking methods
- I want to view the products that this site is offering  quickly and easily
- I want to view the total for my products at any time
- I want to be able to filter products by category  to save me time,  as well as searching by name
- I want to be able to visit the site easily on my phone and tablet as well as desktop
- I  don't want to be spammed because I have visited the site 
- I don't want to be forced sign up for anything or  to give out my information unless I get value in return. 
- I  want to buy good quality pet products and pay securely with my credit card 
- I want to buy pet products that are endorsed or recommended by different pet experts.
- I want to be able to leave a comment on a blog post
- I would like to read a review of some of the products or a comparison with competitor products 
- I want to see some information on the website owners so that I can decide if the site is reputable ( Contact information, privacy policy, About us)
- I expect to be able to connect with the social platforms that the brand is using so I can get further reassurance that they are reputable

### **As a registered shopper/blog reader:**

- I want to be able to register quickly and give a minimum of personal information
- I want to recover my password in case I forget it
- If I make an error logging in I want to be alerted to my mistake
- I want to receive an email confirming a purchase 
- I expect any information I give to be secure and confidential 
- I expect to be able to login and logout easily and  to be able to find those links quickly
- I want to be able to store my purchasing information and store my orders
- I want to be able to be able to delete and update items to buy and I don't want the process to be complicated 
- I want to receive messages to clarify any errors I make when I am paying by credit card
- I want to see confirmation when I have successfully complete any of these actions 
- I want to see what I have searched for and the number of results
- I want to be able to sort a specific category of product, and multiple categories of products
  

### **As the website owner/admin (superuser):**

-   I want to generate traffic to the site and persuade visitors to buy products so that I can earn  revenue 
-  I want to  sell advertising space to local pet services
-  I want to be able to create blog articles that review the products for sale and publish posts that have valuable and relevant content for site visitors. 
- I want  the website to  provide valuable information for users so that they return frequently
- I want to use social media platforms to create brand awareness to generate traffic and cut advertising costs
- I want users to stay on the site for as long as possible and to contribute fresh content to the site. 
- I want the personal information provided by users to be secure and private
- I expect the users of the site to be able to contact admin if they wish. 
- I expect admin sections of the site to be secure and have  protected access
- I want to be able to login and logout and to be able to easily and quickly add, edit or delete the products for sale and I want to be able to add posts to the blog.
- I want the site to be stable and robust and function without problems 

## Testing 
[Testing for the  Pet Hub](https://github.com/mr19331/the-pet-hub/blob/master/TESTING.md)

## Defensive Design 

**User information**

User  messages at the top right of the users page inform the user when actions are successful and when an error is present.
Eg when an item is added to the cart or when a user registers or logs in.  
Form validation is present on each input field for every form.
User is informed when data is not appropriate or in error 
Eg  when registering   if the password is too similar to the username entered or when too few characters ( less than 8 ) are used in a pw 

**Authentication**

A user must validate their email before they can successfully register 
Registered users are not shown the register link in the My account dropdown link 

Users can only access the links to registered user areas if they are logged in.

Super users only  are able to access the full Django admin site.

Super users only can see the link to Product management in the My account link  and can  access the  add-Product, Edit Product and Delete-Product forms and actions
Super users only can see the link to Post management in My account link and can access the Add Post form.

Decorators have been added to enforce authorization measures as a result Django checks first whether a user/superuser is logged in before executing a view and will redirect  the user to the home page if not authorized after displaying an appropriate message. 

**Products**

The  'add to cart' button is disabled  for a quantity of 0.

If an product does not have an accompanying image a no-image.png is shown 


**Cart** 

Items are removed from basket if the quantity is changed to 0.

An empty cart  will show a message and a button to redirect the user.

**Checkout**

A registered user can use the save-information checkbox to use their  default delivery information  to pre-fill the form on the checkout page.

if a user quits the checkout process before it has finished loading their information or if there is a delay so that the checkout process is interrupted, the webhook handler from Stripe will ensure that the payment intent succeeds, checkout will be successful and their delivery information will be saved. 
To prevent a user's order being duplicated Eg during a delayed order process the webhook handler will make 5 attempts before creating the order.
 To ensure the same order by a user is fulfilled, each order contains the stripe intent id wihich is unique.
Country selection is by dropdown to avoid user confusion 

Validation messages give specific messages if the input data fields are not filled correctly 

Stripe error messages inform the user specifically when there is an error with the information entered to do with their credit card Eg card declined, card invalid, card number not correct, invalid CVC, invalid expiry year

A spinning overlay appears during CC processing to inform the user that the process is completing 

Stripe verification asks the user to verify payment before the process completes .

The  user is shown the checkout success page and a thank you message with their order information and a message to say they will receive an email confirmation of their purchase  as soon as the payment and order is successfully placed.

**Profile** 
Registered users that check the save to profile box on the checkout page  save their default delivery and order history to their profile page

 **Blog**

**Blog detail pag**e displays an individual blog with large image. All users can read the blog but only registered users can access the a commenting section below a post to post a comment. 
User comments must be moderated by admin before being added
After adding a comment the user is notified that their comment is awaiting moderation  

**Add Blog page**  is only available to superusers and is a form with input fields each of which must be filled in and an image field to upload an image to the blog post 





## Features of the website 

### Existing Features

##### All Pages

**<u>Nav Bar</u>**

Navbar is displayed on all pages  
My Account icon with  user  links to  login, register pages 
registered users to log out and My Profile pages 
superusers to Product Management page  
Cart icon ( color change on adding item and monetary total) -- users can see item has been added and total cost 
Product menu links with dropdown, allows user to sort items by category, price and rating  
Blog link allows user to see all blog articles 
Logo link to  return to home page
Banner  displays a message - encourages users to shop to earn free shipping 
**Footer** 

Website contact information, email & phone number 
Social platform links 
Link back to home, about, contact and privacy pages 
Link to Blog 
Link to Shop 

##### **Home Page**

  Hero image with 2 large buttons Shop Now and Read our Blog 

 **All Products page** 
 Products displayed total 
 Image of individual product item  and description, category, price, rating  
 Each image links to product detail page 
 Title links to product detail page and displays change of state on hover
**Admin users** have text links that allow edit or deletion of item and alert messages show for each action. 

**Product Detail Page** 
 Large image of product
 Size selector 
 Quantity selector 
 Button to return to All Products page ( Keep Shopping) 
 Button to add item to cart  (Add to Cart) 
 if the add to Cart button is used  User  Success Message is displayed
 **Admin users** have text links for edit or deletion of item and alert messages show for each action

**Cart** 
 Cart icon has color change when item is added to it 
 When clicked it displays the cart page with list of items selected for purchase 
 Each item has image, price, quantity 
 Text links below item are Remove and Update Remove item will remove the item from cart and update the grand total
Remove and Update actions trigger user messages 

**Secure Checkout page** 

Form for customer information requiring full name, email and physical address 
Summary of the customer order 
Card detail section

**Checkout Success page** 

Displays purchase summary including order number 
Message is displayed informing of email confirmation will be emailed to purchaser 
Button for "Keep Shopping"

**Blog Page** (all users)
Displays the navbar and footer with a list of blog posts and thumbnail image for each  Read More button links to complete post and large image

**Post Details Page**(all users ) 
Full blog article is displayed 
Button for  return to blog page
Sidebar to contain advertising for local pet services with a link to a website 



**Commenting section** on Post Detail page below each post ( registered users only ) 



**My Account icon and dropdown** 

**Signup /Register Page** (all users)

Text link to Login page 
Form with input fields for email username and password 
Buttons to submit registration or to go to Login page 

**Login Page** ( all users)

Text links to Register/sign up page  and to Password Reset page 
Buttons to Home page and to submit Login 
Checkbox for user to tick "Remember me" 
Input fields for Email/ Username  and Password 

**Logout** ( logged in users only)
Buttons to Cancel or Logout to give user option to stay logged in or complete the action
Message is given to user " You  have logged out"

**My Profile** (  logged in users only )
Stores the profile page that contains Order History and default delivery information so that the user has a record of purchases and can edit their deliver information that will prefill a checkout form for future purchases. 

**Product Management** (   logged in super/admin users only)
 Links to the  Add Product form  - a new product can be added with all fields name, sku, description, image etc
Admin/super users can edit or delete a store item using text links on product page or product-detail page.

**Post Management** (   logged in super/admin users only)
Add Post form with input fields and image upload 
Each field has validation
Success message displays to the user when the post is saved to draft or published 
Error message displays if a field is left blank or filled incorrectly Eg slug



### Features Left to Implement

 Long term goals of the site are
To increase  user registration and increase revenue by 

Providing an image profile for  registered  users where they can upload a picture of their pet
Allow users to post reviews for products purchased 
Introducing Zoom sessions  where local experts in various pet fields answer user questions,
which can be recorded and uploaded to the website  
Marketing new products and popular items to registered users using email marketing 
Selling  advertising sections to local pet services - vets, groomers, dog walkers, dog daycare, dog trainers etc  to create revenue
Upload videos to the blog  by local pet experts in various fields on pet nutrition, care of pets , dog training, puppy and kitten care etc 
Introduce  a pet forum where registered users can ask questions and interact on the site  ( like mumsnet )  



.

## Technologies Used



​        HTML
​        CSS
​        JavaScript 
​        

- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.

- [Stripe](https://stripe.com/gb) as payment platform to validate and accept credit card payments securely.

- [AWS S3 Bucket](https://aws.amazon.com/) to store static files and images entered into the database.

- [Autopep8](https://pypi.org/project/autopep8/)a tool for automatically formatting Python code to conform to pep8 style guide 

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms.

- [Heroku](https://www.gitpod.io/) Heroku for deployment

- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.

- [Gunicorn](https://pypi.org/project/gunicorn/)WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.

- [Pillow](https://pillow.readthedocs.io/en/stable/)  the  python imaging library used for processing image files to store in database.

- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.

- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.

- [Github](https://github.com/) to store and share all project code remotely.

- [GMail](https://www.google.mail.com/) for emails 

- [Canva](https://www.canva.com/) to edit and crop images.

- [Cacoo](https://cacoo.com/) was used to create the wireframes for this project.







  

## Deployment 

#### Steps to Heroku Deployment :

 **Setting up the Heroku App** 

1. Go to Heroku.com and click on New and then create new app 
2. Name app and choose region. 
3. Use the Resources tab and provision a new Postgres database ( instead of Sqlite ) 

 To use Postgres as the database 2  installations are required in gitpod 
    dj_database_url   Use pip3 install dj_database_url     
    psycopg2-binary    Use pip3 install psycopg2-binary  

Now freeze the requirements.txt using pip3 freeze > requirements.txt ( this ensures Heroku installs all app requirements when the app is deployed) 

4. In settings.py  import dj_database_url 
5.  In settings.py under the databases setting add the database URL from Heroku – which is found in the config variables in the Heroku app settings tab ( or from the command line using Heroku config) 
6. Run the migrations command  to apply all the migrations and set up the database using
    python3 manage.py makemigrations –dry-run
    python 3 manage.py makemigrations 
    python 3 manage.py migrate --plan 
    python3 manage.py migrate

7. The data must now be imported by loading product data, category data and blog data 
8.  Create a superuser pw and username to log in with Using python3 manage.py createsuperuser
9. Remove the Heroku database config. and uncomment the original so the database URL doesn't end up in version control
10. Commit all changes and push to git hub 
11.  Import the categories data using python3 manage.py loaddata categories 
     and then the products using python3 manage.py loaddata products 
12.  Create a superuser username and pw to login  with python3 manage.py createsuperuser
13.  Remove the Heroku database configuration and restore ( uncommit ) the original setting so the database URL does not end up in version control. 
14. Commit the changes and push to git hub 

<u>Setting up alternative database URL environments</u>

Create an if statement in settings.py so that when the app is running on Heroku the database URL environment variable will be defined the connection is with Postgres and otherwise we connect to SQLite.  If the database URL is in os.environ we will generate its value using dj_database_url.parse and use that as the database setting – otherwise the default configuration will be used

![image-20210208181619997](C:\Users\Maria\AppData\Roaming\Typora\typora-user-images\image-20210208181619997.png)

15.Requirements to be  installed before final deployment to Heroku

 Add gunicorn   use the command pip3 install gunicorn 
 Add into the requirements.txt file using pip3 freeze > requirements.txt
 Add a Procfile  ( this tells Heroku to create a web dyno that will run both gunicorn and serve the Django app 

16.Ensure that you are logged into Heroku.com 

17.Temporarily disable collectstatic using the command  
Heroku config set disable collectstatic = 1 - - app (add host name of Heroku app here ) 

18 In settings.py add the hostname of Heroku app to allowed hosts AND add localhost so gitpod will still work

19.Now attempt deployment by adding and committing these changes and push to git hub
 Then deploy to Heroku  using       git push Heroku master

NB if this triggers an error message then you may have to initialize your Heroku git remote if the app was created on the website rather than in the CLI 

Use the command Heroku git:remote -a  app-name-here  
 then git push Heroku master 

## Steps to Run App Locally 

**Requirements** 
An IDE  ( gitpod, VSCode, PyCharm)

PIP  to install packages such as Django , Pillow etc. 
Python3 

Git  for easy version control 

**Access the github repository.** Download or Clone 

Download a zip file.

- On the GitHub project page, click ‘code’ tab  to download a zip file.
- Extract the files to a  folder on the desktop.

Clone the repository 

1.  On the GitHub project pag click to copy the url for your repository.
2. Either open Git Bash on your local computer or open the command line on your IDE and     ensure you are in the right directory. Then run the following command:

git clone  https://github.com/mr19331/the-pet-hub.git        Select a file destination for the directory

Ensure you have pip installed on the machine:  py -3 -m pip --version

Use a virtual environment for the Python interpreter. Python's  built-in environment can can be used with the command  : python -m .venv <path for venv>

Activate the environment  using the command:  .venv\Scripts\activate

Download the requirements for the project using the command:   pip -r requirements.txt

Set up the environment variables in an env.py file 

- SECRET_KEY
- DATABASE_URL*
- EMAIL_HOST_PASSWORD
- EMAIL_HOST_USER
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- STRIPE_WH_SECRET

EMAIL_HOST_PASSWORD  Can be found in the security settings of your email host.

The EMAIL_HOST_USER is  the email address from which you want your emails to be sent from.

Before you can start the local server,  apply all the migrations and set up the database using
python3 manage.py makemigrations –dry-run
python 3 manage.py makemigrations 
python 3 manage.py migrate --plan 
python3 manage.py migrate

This will create a database of all of your models. Use the following code for each fixture in the project,  to “fill” the databases.

python3 manage.py loaddata <fixturename.json>

Once the data is loaded you can then run your server locally.    python3 manage.py runserver 

This will open a port (which may be different depending on your IDE) .




## Credits

### Content

[Table of contents](http://ecotrust-canada.github.io/markdown-toc)  

Content  for blog posts was taken from the [PDSA website](https://pdsa.org.uk ) 
Descriptions for pet products was taken from [Pet Planet website](https://petplanet.co.uk)



### Media
Images in the blog posts are from  
Puppies from  [ pexels.com]( https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
Suitcase image from [espares blog](https://blog.espares.co.uk/)

Cat images from [aspca.org](https://www.aspca.org/) and from  [pets.webmd.com](https://pets.webmd.com/cats/default.htm)

Main hero image on home page [Anna Dudkova on Unsplash](https://unsplash.com/photos/urs_y9NwFcc)

Pet product images from [Pet Planet website.](https://petplanet.co.uk.)

#### **Code** 

Blog post gallery on home page adapted  from 
[mdbootstrap.com](https://mdbootstrap.com/)
[bootstrap](https://getbootstrap.com/)

Blog application code was derived from the following sources 
[django central.com](https://djangocentral.com/building-a-blog-application-with-django)

the ebook by [Will Vincent](https://wsvincent.com/best-django-books/#django-for-beginners) 

[Pythonistaplanet.com](https://www.pythonistaplanet.com/how-to-create-blog-using-django/)

[Djangocentral.com]( https://djangocentral.com/building-a-blog-application-with-django/)

The commenting section in the blog was adapted from 

[djangocentral.com](https://djangocentral.com/creating-comments-system-with-django/)

Help with uploading images from
[Geeksforgeeks.com]((https://www.geeksforgeeks.org/python-uploading-images-in-django/)) 

