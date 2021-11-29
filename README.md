<h1 align="center">Merge Store</h1>

<h2 align="center">An e-commerce site for tech lovers</h2>

[Visit Merge Store](https://merge-store.herokuapp.com/)
<br>

I have created a web application that showcases an e-commerce store that sells a curated collection of highly-rated tech. Tech websites inspire Merge Store. Its clean interface and easy to navigate store has an urban and modern feeling aesthetic to it. I created a clean and approachable website that is a centrepiece for potential shoppers to interact with. The website consists of easily readable information pertaining to the products it provides with necessary images and product information. The key features of the website include a working shopping bag and checkout system.<br>

<h2 align="center" style="width:1200px;"><img src="https://user-images.githubusercontent.com/41737293/139531565-69c11160-6ce9-4d58-88ba-f919da33d474.png"></h2>


### Project Specifications

| CRITERIA | MEETS SPECIFICATIONS
|---|:---
| Home page | The User, is greeted with a home page which is the website's foundation that introduces the store with a shopping banner to entice potential shoppers to view the new collection available.
| Products | The Website has separate pages with information on products the firm provides.
| User Authentication | The User can register an account that allows them to log in and log out, add delivery information, and products added to the bag or ordered are assigned to the logged-in User.
| Shopping | Users can add items to the bag, increase and decrease the number of items through the easy to use shopping bag page.
| Checkout | Once registered and logged in, users can add items to the bag and checkout using the Stripe checkout system.
| Customer Reviews | Once registered and logged in, users can add reviews to products; anyone can view reviews under products.
| Contact Us | Any user can submit a contact form.


## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to be pulled in by the presentation of the website.
        2. As a First Time Visitor, I want to view a list of products.
        3. As a First Time Visitor, I want to view individual products in detail.
        4. As a First Time Visitor, I want to view the total of my purchases at any time
        5. As a First Time Visitor, I want to easily register for an account, log in and log out, recover my password, and view my profile.
        6. As a First Time Visitor, I want to be able to filter and sort products by category, price and rating.
        7. As a First Time Visitor, I want to be able to search for a product by name or description and see results.
        8. As a First Time Visitor, I want to select the quantity of a product easily, add to checkout, and process an order.
        9. As a First Time Visitor, I want to be able to contact the site admins for help regarding a product or order issue.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to view my shopping bag to see what I have added to the bag.
        2. As a Returning Visitor, I want to view my profile to check my order history once I have made an order.
        

    -   #### Frequent User Goals
        1. As a Frequent User, I want to check to see if I can log into my account without issue.
        2. As a Frequent User, I want to check to see if new products are added to the website.
        3. As a Frequent User, I want to navigate the website and find things where they are supposed to be.
        4. As a Frequent User, I want to navigate the website and be able to create and view reviews for products.

-   ### Design
    -   #### Colour Scheme
        The two main colours represent the dark, chic aesthetic as intended. I have used a contrast of dark colours and white to make the website visually appealing.
    -   #### Typography
        -   The Helvetica font is the main font used throughout the whole website. Helvetica is standardised and used to achieve readability and professionalism; it is attractive and appropriate for tech-related websites.
    -   #### Imagery
        -   Imagery is vital. The background hero images on the home page are designed to create an urban, modern feel to capture potential shoppers interests. All images for products show professional markups of the products, which are apparent to the User.

*   ### Wireframes <br>
    
    <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139533448-122d080b-a4ef-4440-af74-cb5a4fa73ddf.JPG"></h2>

   
## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

- [Django](https://www.djangoproject.com/) was used as the principal framework for the project.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used for all forms on the site.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication on the site.
- [Stripe](https://stripe.com/) was used to handle payments on the site.
- [Bootstrap 4](https://getbootstrap.com/) was used to aid responsive design.
- [Amazon Web Services](https://aws.amazon.com/) S3 was used to store all static CSS and Javascript files and images.
- [SQLite3](https://www.sqlite.org/index.html) was used during development.
- [PostgreSQL](https://www.postgresql.org/) was used in the final deployed site.
- [Heroku](https://www.heroku.com/) hosts the Merge store website.
- [JQuery](https://jquery.com/) was used extensively throughout the site in order to provide functionality for Bootstrap elements and for Stripe. 
- [GitPod](https://gitpod.io/) was used as an IDE for this project. 
- [GitHub](https://github.com/) is where the Merge store project is stored. Regular commits were made throughout, and code was pushed to GitHub from GitPod.
- [Font Awesome](https://fontawesome.com/) was used for icons on the site.
- [Balsamiq:](https://balsamiq.com/) - Balsamiq was used to create the [wireframes](https://user-images.githubusercontent.com/41737293/126455811-def56c72-13dd-4e5a-8e68-b0bd971de246.JPG) during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every project page to ensure no syntax errors.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - Validated with no errors
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - Validated with no errors
-   [PEP8 Validation](http://pep8online.com/) - Validated with no errors

- The page is fully responsive and has been tested using the Developer console.
 - Tested bag, checkout, contact, home, review and products pages in all devices. All are working as intended.
 - All the codes were formatted using Gitpod's built-in formatting system.
 - Tested every functionality like Stripe, add/edit/delete products, email, contact, check out, and confirmation email. All is working fine.
 - Grammarly checked to avoid typos.

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    As a First Time Visitor, I want to be pulled in by the presentation of the website.

    Upon entering the site, users are automatically greeted with a clean and inviting home page introducing the products. There is a Hero Image that has a modern urban look with the intention of captivating the shopper.

    There is a delivery banner informing the User of a deal, and the homepage indicates a new curated collection of items.
        
    <h2 align ="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139528510-9fa06baf-e881-4119-82c8-c9c56ea1fabd.JPG"></h2>

    2. As a First Time Visitor, I want to view a list of products.

        A navigation bar is available for the User categorising the product line into easy sections for the User to access what they wish to see.
       

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139528561-10cf0cac-da19-48be-b37d-8b7072465c30.JPG"></h2>

        <h2 align="center" style="width:500px;" ><img src="https://user-images.githubusercontent.com/41737293/139528538-42be1b78-70f8-4c00-a4ed-ec0435a03fcc.JPG"></h2>


    3. As a First Time Visitor, I want to view individual products in detail.

        I can select a product that takes me to the product page, which gives me more information on the item.
        

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139528567-feca0514-9092-4642-b10c-c77b95e406a0.JPG"></h2>

    4. As a First Time Visitor, I want to view the total of my purchases at any time

        I can see the total of my orders on the shopping bag icon, or I can see the full detail of the bag by clicking the shopping bag icon on the top right corner of the website.
        

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139528614-9c8849cb-61ea-4f8d-be65-c8c97cd3097b.JPG"></h2>
    
    5. As a First Time Visitor, I want to easily register for an account, be able to log in and log out and recover my password and view my profile.

        User authentication options are all available via the My Account tab on the navigation bar.
        
        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139528729-c5526223-eec9-4a7a-a76e-e0afe5313367.JPG"></h2>

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139528747-6032930b-ecad-4a36-84b3-ef8a96f898fc.JPG"></h2>

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139528760-85362e5b-4b16-4966-9668-4766355c570f.JPG"></h2>

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139528783-b96944a9-dee4-4841-88d0-01260e5c57e7.JPG"></h2>

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139528798-51809a7f-166f-4cdd-9018-afd01606f26f.JPG"></h2>

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139528846-2f48e7b1-85f0-4039-9efe-f5e972e92268.JPG"></h2>

    6. As a First Time Visitor, I want to be able to filter and sort products by category, price and rating.

        Sort dropdown is provided on the products page to filter by standard sorting parameters.
        
        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139528887-49d7004e-0565-49ac-b3d2-e13cd406c605.JPG"></h2>

    7. As a First Time Visitor, I want to be able to search for a product by name or description and see results.

        Search functions are available on the navigation bar, allowing users to search by product name or description.
        
        <h2 align="center" style="width:500px;" ><img src="https://user-images.githubusercontent.com/41737293/139528967-99511e92-85b0-4e95-be01-6e1cfa7cdea2.JPG"></h2>

    8. As a First Time Visitor, I want to easily select the quantity of a product, add to checkout, and process an order.

        Users can select the quantity of an item, add it to the shopping bag and finish checking out using the Stripe checkout system. 
        
        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139529047-12b067f6-b1a7-4ee2-8438-1221168d9e1f.JPG"></h2>

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139529028-328ba6ff-deb9-40fe-bda5-f1b8a7da01e1.JPG"></h2>

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139529054-86f1d1c5-06fe-4cf6-8731-780cc964b115.JPG"></h2>

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139529065-83791d55-bd3e-48d8-adc8-938fa59a962a.JPG"></h2>

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139529076-34254108-2b09-427a-af73-5db3bc873ab1.JPG"></h2>

    9. As a First Time Visitor, I want to be able to contact the site admins for help regarding a product or order issue.

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139529076-34254108-2b09-427a-af73-5db3bc873ab1.JPG"></h2>

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to view my shopping bag to see what I have added to the bag.
        
        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139529117-9b183b7a-76e3-4264-a245-ba98a2737894.JPG"></h2>

    2. As a Returning Visitor, I want to view my profile to check my order history once I have made an order.

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139529138-f94af269-0d08-4f8a-b918-9d80fadc79fd.JPG"></h2>


-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if I can log into my account without issue.

        The User can log in without issue as long as the username and password are correct. Password can be reset, and confirmation emails are received upon creating an account and verifying the account.

    2. As a Frequent User, I want to check to see if there are new products added to the website.

        Admin users can update product pages to add items to the product line so normal users can frequent the website to look for new products.

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/139529232-88e801c4-4294-41e5-925b-c9823d742175.JPG"></h2>

    3. As a Frequent User, I want to navigate the website and find things where they are supposed to be.

        The navigation bar is simple and straightforward. 
        Finding what you need is not difficult as everything is placed visibly and makes sense.

    4. As a Frequent User, I want to navigate the website and be able to create and view reviews for products

         Anyone can view product reviews under the product pages; logged in users can submit one review for each product using the form provided.

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/143865918-b4681012-6492-44f6-b889-2c71869ce8fc.JPG"></h2>

        <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/143863474-c13f5de5-a580-4d50-9d67-c430b54196e2.JPG"></h2>


    
## Information Architechture:

### Database Choice:

- SQLite was used during development, as it comes pre-installed with Django.

 <h2 align="center" style="width:500px;"><img src="https://user-images.githubusercontent.com/41737293/143863832-d98ff597-486a-4a3a-915e-7221db59a96f.JPG"></h2>


- PostgreSQL was used for the deployed site, as it is offered as an optional add-on by Heroku.


  
### Further Testing

-   The live project has been tested  on a variety of devices such as Desktop and Samsung Note 10 + 5G
-   A large amount of testing was done to ensure that the website was responsive.
-   Friends and family members were requested to review the site and documentation to point out any bugs or user experience issues, and all were content with the browsing experience.

### Known Bugs

- There can be some visual delay when navigating the product pages due to the jpg images loading in. I have used a cache method to try to combat this.

- Unable to load Heroku website in a website mockup generator to test responsiveness

- Due to Django routing, getting a validation error for HTML element (li) unable to fix without breaking padding on the navbar


### Heroku

The project was deployed to Heroku using the following steps.

1. First, we need to tell Heroku which applications and dependencies are required to run our app by creating a text file.
2. Procfile is what Heroku looks for to know which file runs the app and how to run it, so we'll use the echo command to create a Procfile.
3. Log into Heroku and "Create New App" and name the app appropriately. Select the region closest to you and create.
4. We can use Heroku CLI or, to simplify the process, set up Automatic Deployment from our GitHub repository under the deploy tab in Heroku. Search Repository name and then add.

[More info](https://devcenter.heroku.com/articles/heroku-cli)

5. Before we start Automatic deployment, create a Config variable file under "Rev Config Vars" to tell Heroku what variables are needed. Make sure "Procfiles" and all required files have been pushed to the Repository before connecting.
6. Click on connect to Github repository, and now we can click on Automatic deployment, which will push the master to Heroku.
7. Click "View" to launch your new deployed app.

### Forking the GitHub Repository

By forking the GitHub Repository, we copy the original Repository on our GitHub account to view or make changes without affecting the original Repository by using the following steps.

1. Log in to GitHub and locate the relevant Repository.
2. At the top of the Repository (not top of page), just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original Repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the relevant Repository.
2. Under the repository name, click "Clone or download".
3. To clone the Repository using HTTPS, copy the link under "Clone with HTTPS".
4. Open Git Bash
5. Change the current working directory to where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
### Heroku deployment with AWS:

- The Merge Store website was deployed to [Heroku](https://www.heroku.com/) using the following steps:

1. Install gunicorn, psycopg2-binary and DJ-database-URL using the "`PIP Install` "command.
2. Freeze all the requirements for the project into a requirements.txt file using the "`pip3 freeze > requirements.txt` "command.
3. Create a profile, with the following inside it: "`web: gunicorn merge-store.wsgi:application` ".
4. Push these changes to GitHub, using "`git add .` ", "`git commit -m'  "and "`git push` "commands.
5. Navigate to [Heroku](https://www.heroku.com/), and log in or create an account.
6. Once logged in, click on 'resources'.
7. From the add-ons search bar, add the Heroku Postgres DB, select the free account, and then submit an order form to add it to the project.
8. From the app's dashboard, click on 'settings, and then 'reveal config vars' in order to set the necessary configuration variables for the project. 
It should look like this: 

| Key                   | Value                      |
|-----------------------|----------------------------|
| AWS_ACCESS_KEY_ID     | Your AWS Access Key        |
| AWS_SECRET_ACCESS_KEY | Your AWS Secret Access Key |
| DATABASE_URL          | Your Database URL          |
| EMAIL_HOST_PASS       | Your Email Password        |
| EMAIL_HOST_USER       | Your Email Address         |
| SECRET_KEY            | Your Secret Key            |
| STRIPE_PUBLIC_KEY     | Your Stripe Public Key     |
| STRIPE_SECRET_KEY     | Your Stripe Secret Key     |
| STRIPE_WH_SECRET      | Your Stripe WH Key         |
| USE_AWS               | TRUE                       |

9. Back on the main dashboard, click on 'deploy', and then under the 'Deployment' method section, select GitHub and 'Automatic Deploys'.
10. Ensure that in settings.py, the following code is commented out:
```
Database
 https://docs.djangoproject.com/en/3.1/ref/settings/#databases
```
and the following code is added:
```
DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
```
11. Make migrations using the following command:
```
python3 manage.py makemigrations
```
and migrate the database models to the Postgres database using the following command:
```
python3 manage.py migrate
```
12. Load the fixtures from the 'product_types.json' file and then from the 'products.json' file - which is contained in the 'fixtures' folder into the database. 
This is done by using the following command:
```
python3 manage.py loaddata <file name>
```
13. Create a new superuser with the following command:
```
python3 manage.py createsuperuser
```
And then enter chosen email, username and password.

14. In settings.py, contain the previously entered database setting in an if statement, and add an else condition, so that different databases are 
used depending on the environment.
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
15. Disable 'COLLECTSTATIC' with the following code: ``` Heroku config:set DISABLE_COLLECTSTATIC=1 ``` 
so that Heroku doesn't attempt to collect the static files.
16. Add ```ALLOWED_HOSTS = ['milestone-project-04.herokuapp.com', 'localhost']``` to settings.py.
17. Add Stripe environment variables to settings.py.
18. Push to Heroku using the following command:
"`git push Heroku main` "

### Amazon Web Services:

All Static and media files for the deployed version of the site are hosted in a Amazon Web Services(AWS) S3 bucket. 
In order to create your own bucket, please follow the instructions on the AWS website. 
[Here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)

1. In the gitpod terminal, install boto3 and Django-storages using the following commands:
```pip3 install boto3 ``` and ```pip3 install django-storages```
2. Freeze the new requirements into the 'requirements.txt' file using the "`pip3 freeze > requirements.txt` "command
3. Add 'storages' to INSTALLED_APPS in settings.py.
4. Add the following code to settings.py in order to link the AWS bucket to the website:
```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'merge-store'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
5. Create a custom_storages.py file at the root level of the project. Inside it, include the locations of the Static Storage and Media Storage.
6. Delete DISABLE_COLLECTSTATIC from the Heroku Config Variables.
7. Finally, push to GitHub, and all changes should be automatically pushed to Heroku too.

### Making a Local Clone:
In order to make a local clone of the Merge store website, enter "`git clone https://github.com/MAziz-0/merge_store` "into the terminal. 


Next, create an .env.py file in the root directory of the project, and add it to the .gitignore file. 
The following code needs to be added to the .env.py file:
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"   
```

Then make sure that the required packages are installed by running the following command: 
"`pip install -r requirements.txt` "

Make migrations and then migrate in order to create a database by running the following commands:
"`python3 manage.py makemigrations` "and "`python3 manage.py migrate` ".

Load the fixtures from the migrations file and then from the 'products.json' file - which is contained in the 'fixtures' folder into the database. 
This is done by using the following command:
```
    python3 manage.py loaddata <file name> 
```

Create a superuser with the following command: "`python3 manage.py runserver` "and enter your credentials.

Run the app by entering the following command:
"`python3 manage.py runserver` "

## Credits

### Code

-   Code institute Boutique Ado lessons

### Content

-   All content was sourced from various tech websites. None of the information will be used for commercial purposes as this is an educational project.


### Media

-   The background hero image came from [Pexels](https://www.pexels.com/)
-   The images came from various tech websites, e.g. Apple, Samsung

### Acknowledgements

-   Python/Django logic learn from Code Institute Instructional videos 

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.