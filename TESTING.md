# Testing 

## Testing Tools 
 CSS validator used for CSS -[CSS](https://jigsaw.w3.org/css-validator/)
 HTML validator used for checking HTML code -[HTML](https://validator.w3.org/)
 JSHint validator for checking JS -[JS](https://jshint.com/ )
 warnings given but no errors in the Javascript code 
 



##### Home Page 

##### **Shopper/blog reader**

**Links** 
All Products  dropdown links to sort products by Category, Price, Ratings and to All Products page   tested and working
Cats and Dogs dropdown links working correctly 
All Specials is not working correctly  -- the category New Arrivals is working and displays correctly and displays in All Specials but 
the products in the Best Sellers category are not displaying on the category page or in the All Specials page 
 
**Icons** 
My Account icon has  dropdown links  to Register or  Login pages   tested and working
success message displayed when user registers or logs in.  
Cart icon   displays cart page with items in cart price total and button links to checkout form page or to all products page to continue shopping 
If a user has items in the cart -- the total purchase cost is displayed in the navbar 

**Buttons**  
button to Start Shopping links to All Product page  working 
button to Blog links to All blog post page working 

**Search Bar** functions correctly to display products by a keyword in either title or description 
The Home page is available on Desktop, tablet and mobile versions 
**Footer** 
Links to the Home page is working  Contact, About and Privacy pages not installed yet.
Links to social media , connected and  working 

   **Home Page  for registered user** 
         My Account dropdown links now include My Profile and logout   
          my profile links to profile page and logout to logout page with button to sign out/ logout 
**Home Page for admin/superuser** 
         My account icon dropdown links now include Product Management 

##### Product Page for all users

Number of items is displayed and is correct.

Sort By selection box allows user to sort items by category, price or rating, tested &  not working correctly 
this was discovered at the last minute and too late to fix. 

Product title links to product detail page for the item, tested and  is working 
 

##### **Product Detail Page for all Users** 

**Selection boxes** for Size and Quantity of the item to change the size or number of items -- tested and work
Product item details are displayed  
**Buttons** link to all products page for more shopping or Add to Cart to add the item to the cart   -- tested and working 
**Success message**  is displayed to the user when the item is added to the cart with image, item details and total with a banner display if the user is below the threshold for free delivery and a button link to the checkout page 

##### Cart Page for all users

**Text links** to Remove or Update items in the cart 
**Selection box** to add or decrease quantity of individual items  in cart
**Button**s  link to checkout page or Keep shopping returns user to the All Products page 

##### Checkout Page for all users 

Required input fields are indicated with an asterisk  if not filled in will indicate a tooltip error indicating which field must be completed
Order summary displays the cart items to be purchased with details and image 
Country input is a selection box  
CC details section will display specific errors to the user  
Button to submit payment and links to Checkout success page 
Success message is displayed when checkout is successful 

**Registered Users**  
Registered Users can use the tickbox to save their information to their profile page 



##### Checkout Success Page for all users

**User message** displays where the confirmation email will be sent 
**Order information** is displayed 
**Button** to return to shop   

##### Blog page for all users

Posts are listed 
Button "Read More" link to post detail page for the individual post  

##### Post Detail page for all users

Individual post is displayed with large image 

##### Post Detail page for registered users 

Displays a commenting section for user comments ( moderated by admin) 



##### **Register Page , Login Page  Logout Page, Password Reset Page** 

**Forms**
Each text input field has character restrictions and displays error messages to the user
**Register form** will return an error if the password is too similar to the username or if there are too few characters in the password 
when the user signs up successfully a success message is displayed to say that the user will receive an email to verify their address. 
On clicking verify the user receives a second message to say they can now log in 
The email functionality has been tested and works. 
**Text link** to login page  tested and works 
**Buttons**  linking to Login or to complete the Registration process links to the Login page  tested and works 
**Password Reset Page** 
Buttons  link to Login page and Reset My Password to  submit email 

**Login Page**
**Text link** to Register page and to Reset Password page 
**Tickbox** Remember me box for users login to be saved 
**Buttons**   link to home page and to submit data to login to site  

**Logout Page** 
Success message is displayed to the user when any of these actions is completed successfully 

##### Profile Page- registered users

If there is an order history for the user,  details will be displayed  order number, date of order, order item , order title, cost of each item, delivery cost ( if any ) and grand total
**Delivery information** for the user is displayed in input fields  phone number, street address city, postcode, county and country selector box 
**Button** to update the information if the user makes changes  

##### Admin Product Management 

Link to **Add product form** works and form fields tested Eg  to add an item an invalid price was added and the error message appears 
When an item is added successfully and submitted the product is logged to the django admin section and the image is added to the media file correctly .  


**Edit Product form** Links from both product page and product detail page work and fields on the form were tested including the image update  
**Delete Product**  links from product page and product detail page work and delete works 
messages for each action are displayed correctly. 

#####  Admin Post Management 

Add Post form   each input field was tested for invalid input and successful input 
Error message is displayed if Eg the slug field is not correctly filled 
Success message is displayed to the user on drafting or publishing a post successfully

