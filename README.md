
# FaceArt
One of the main goals of the website is to give people an idea of using technology as art. The primary goal of the website is to show products people can buy when using their own facial landmarks as a painting. This is the first version and will be a first step in integrating an automated facial analysis module to automate the production of Personalized portraits using facial landmarks.


## UX
The main layout is taken form the Boutique Ado project from Code Institute. It has been adjusted for this current project. Mainly the color scheme used is dark, this to enhance the mystery around the technology used and the creation of anonimity with the use of facial landmarks for portraits.

The reason to use the template of Code Institute is that Code Insitute has a long history of trail and error, and thus should come up with the most efficient lay out of the webshop. 

The Landing page is a common image of a landmarked face and should give people an idea of what their wall decoration would look like in close-up.

# User Stories
During the development i used user stories as a guideline in funtionalities. Below you can find the stories used.

User story ID	|  As an/a	|  I want to be able to…	|  So that I can…
------------ | ------------- | ------------ | ------------- 
1	| Shopper |	have a nice first impression |	have an idea of the product thats is sold
2	| Shopper	| view all products |	make an informed decision on which product to buy
3	| Shopper	| see all categories (materials) | To know whats material the waal decoration is made of
4	| Shopper	| see if i have something in my shoppingbag |	know if i have to stop shopping 
 ||| Searching and sorting | 
6	| Interested shopper	|specify my search criteria	|only see the things i am interested in
7	| Interested shopper|	search through all products |	and decide on size, material and price
8	| Interested shopper	|if i found right material, choose size	|when the preferece is material
9	| Interested shopper	| if i found right size, choose material|when the preferece is size
||| Registration and user account | 
12|	Client |	register |	So i don't have to fill it in each time i order something
13|	Client |	see my order history	|I case i want to re-order or something goes wrong
14|	Client |View my acount and settings|	To check if the info is up-to-date
||| Check Out | 
15	|Paying client|	I want to pay easily without to many hurdles	|So the chances are that i will execute the payment
16	|Paying client|	know if all payments were done correctly|	So i feel safe that the payments are transfered correctly

# Features
The first part is the productspage. Here you can find all products. When clicking on different categories in the menu you can select products you are interesed in. There are three different sizes for the wall decorations. Small Medium and Large. In addition there are four different materials you can choose from: Canvas, Wood, Aluminium and Plexiglass.

The images give you a nice idea of the size compared to a living room.

In addition to the wall decorations you can also buy a cup and a glass with facial landmarks engraved. The specials are two different faces combined into a diptych also possible in the materials above and differnt sizes.

Current users can login and create an account, see their past orders and their profile information.

In previous versions of the Project the index page was a example painting with the text 'Shop New Tech' on it. I have decided to change this so people would have a better understanding of the product, instead of just a overview in a random livingroom.

# Features left to Implement
The next main implementation would be letting customers upload their image to be analyzed to get an idea what their face would look like on the products ordered.

## Technology used
* HTML5
* CSS3
* Bootstrap4
* JavaScript
* Python3
* JSON

# Used Plaforms
* Coding: GitHub/GitPod
* Fonts: Google Fonts
* Icons: Font Awesome
* Payments: Stripe
* Media hosting: Amazon Web Services
* Deployment: Heroku

# Testing
During the whole period of development the site was tested. after deployment it was tested using Lighthouse, you can find the outcome of this report below:

Device| Performance	|  Accessibility	| Best Practice	|  SEO
------------ | ------------- | ------------ | ------------- 
Mobile  | 75	| 89 |	100 |	92
Computer  | 92	| 89 |	100 |	90

# Deployment
All coding was done in GitPod and commited to GitHub. After this the deployment was done on HEROKU, with the media files and static files stored on AMAZON WEB SERVICES.

Deployment was a pain. Since it was a cloned verion of the original, a zip file was put instead of a Project folder. This cause the commits and pushes of any change in the project folder not go to GitHub. During testing this didn't cause any trouble, since it is all stored at Gitpod, however, this did caused trouble during deployment. Eventually a different file was made, and all references were changed to that file. Commits were done and Folders were read.
And all was deployed well.

## Settings
- Path routing is defined 
- Debug is still set on True
- Secret key setting is defines for Django
- Installed apps include Allauth, Django and local apps
- Middelware and security is defined
- Crispy forms is defined
- Templates are defined including Crispy
- User settings are defined, including email  verification
- DJ database is used if database is set in environment, if not use Django database
- Password validators are set
- Location settings are set, currently set on Europe
- Database location of static files and Media files are set
- Stripe Settings are initiated.

# Extra
The main font I have been using is the 'Oswald' and during one of my distraction I came accross the website of the designer of the font, Vernon Adams, who died on August 24 2016. Even though Vernon designed a lot of the Fonts we use today his family doesn't receive (financial support).

http://sansoxygen.com/

# Personal Note

This is my own project, eversince i've woked for a Computer Vision company i wanted to have a landmarked portrait. Code Insiti=ute has given me the option to create this. And all support have been so very very nice, tutors, Student Care and Mentors. Thank you!!

https://www.geeksforgeeks.org/try-except-vs-if-in-python/
https://www.tutorialrepublic.com/faq/how-to-launch-bootstrap-modal-on-page-load.php