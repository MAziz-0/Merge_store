<h1 align="center">Merge Store</h1>

[View the live project here.](https://merge-store.herokuapp.com/)

I have created a web application that showcases an e-commerce store that sells a curated collection of highly-rated tech. Tech websites inspire Merge Store. Its clean interface and easy to navigate store has an urban and modern feeling aesthetic to it. I created a clean and approachable website that is a centrepiece for potential shoppers to interact with. The website consists of easily readable information pertaining to the products it provides with necessary images and product information. The key features of the website include a working shopping bag and checkout system.

<h2 align="center"><img src="https://user-images.githubusercontent.com/41737293/139531565-69c11160-6ce9-4d58-88ba-f919da33d474.png"></h2>


### Project Specifications

| CRITERIA | MEETS SPECIFICATIONS
|---|:---
| Home page | The User is greeted with a home page which is the website's foundation that introduces the store with a shopping banner to entice potential shoppers to view the new collection available.
| Products | The Website has separate pages with information on products the firm provides.
| User Authentication | The User can register an account that allows them to log in and log out, add delivery information, and products added to the bag or ordered are assigned to the logged-in User.
| Shopping | Users can add items to the bag, increase and decrease the number of items through the easy to use shopping bag page.
| Checkout | Once registered and logged in, users can add items to bag and checkout using the Stripe checkout system.


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
        8. As a First Time Visitor, I want to easily select the quantity of a product, add to checkout, and process an order.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to view my shopping bag to see what I have added to the bag.
        2. As a Returning Visitor, I want to view my profile to check my order history once I have made an order.

    -   #### Frequent User Goals
        1. As a Frequent User, I want to check to see if I can log into my account without issue.
        2. As a Frequent User, I want to check to see if there are new products added to the website.
        3. As a Frequent User, I want to navigate the website and find things where they are supposed to be.

-   ### Design
    -   #### Colour Scheme
        The two main colours represent the dark, chic aesthetic as intended. I have used a contrast of dark colours and white to make the website visually appealing.
    -   #### Typography
        -   The Helvetica font is the main font used throughout the whole website. Helvetica is standardised and used to achieve readability and professionalism; it is both attractive and appropriate for tech-related websites.
    -   #### Imagery
        -   Imagery is vital. The background hero images on the home page are designed to create an urban, modern feel to capture potential shoppers interests. All images for products show professional markups of the products, which are clear to the User.

*   ### Wireframes

    -  Wireframe - [View](https://user-images.githubusercontent.com/41737293/139533448-122d080b-a4ef-4440-af74-cb5a4fa73ddf.JPG)

   
## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Bootstrap](https://getbootstrap.com/)
    -  Bootstrap was used to create for majority of the website.
1. [Django](https://www.djangoproject.com/)
    -  Django was used to create all the features apps such as the shopping bag and checkout system.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
1. [Heroku:](https://en.wikipedia.org/wiki/Heroku)
    - Heroku is used to store the project's code after being pushed from Git and allows us to deploy the project live.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://user-images.githubusercontent.com/41737293/126455811-def56c72-13dd-4e5a-8e68-b0bd971de246.JPG) during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every project page to ensure no syntax errors.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - Unable to validate a Django routed page due to a child element being missing.
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://user-images.githubusercontent.com/41737293/139533492-0a5815c8-8464-43d8-bd86-79d373990202.JPG)


### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to be pulled in by the presentation of the website.

        1. Upon entering the site, users are automatically greeted with a clean and inviting home page introducing the products. There is a Hero Image that has a modern urban look with the intention of captivating the shopper.
        2. There is a delivery banner informing the User of a deal, and the homepage indicates a new curated collection of items.
        
        - [View](https://user-images.githubusercontent.com/41737293/139528510-9fa06baf-e881-4119-82c8-c9c56ea1fabd.JPG)

    2. As a First Time Visitor, I want to view a list of products.

        1. A navigation bar is available for the User categorising the product line into easy sections for the User to access what they wish to see.
       
          - [View](https://user-images.githubusercontent.com/41737293/139528561-10cf0cac-da19-48be-b37d-8b7072465c30.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/139528538-42be1b78-70f8-4c00-a4ed-ec0435a03fcc.JPG)


    3. As a First Time Visitor, I want to view individual products in detail.

        1. I can select a product that takes me to the product page, which gives me more information on the item.
        
          - [View](https://user-images.githubusercontent.com/41737293/139528567-feca0514-9092-4642-b10c-c77b95e406a0.JPG)

    4. As a First Time Visitor, I want to view the total of my purchases at any time

        1. I can see the total of my orders on the shopping bag icon, or I can see the full detail of the bag by clicking the shopping bag icon on the top right corner of the website.
        
          - [View](https://user-images.githubusercontent.com/41737293/139528614-9c8849cb-61ea-4f8d-be65-c8c97cd3097b.JPG)
    
    5. As a First Time Visitor, I want to easily register for an account, be able to log in and log out and recover my password and view my profile.

        1. User authentication options are all available via the My Account tab on the navigation bar.
        
          - [View](https://user-images.githubusercontent.com/41737293/139528701-36d7abb3-5b42-4007-b1c4-d83c5ab0166d.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/139528729-c5526223-eec9-4a7a-a76e-e0afe5313367.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/139528747-6032930b-ecad-4a36-84b3-ef8a96f898fc.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/139528760-85362e5b-4b16-4966-9668-4766355c570f.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/139528783-b96944a9-dee4-4841-88d0-01260e5c57e7.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/139528798-51809a7f-166f-4cdd-9018-afd01606f26f.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/139528846-2f48e7b1-85f0-4039-9efe-f5e972e92268.JPG)

    6. As a First Time Visitor, I want to be able to filter and sort products by category, price and rating.

        1. Sort dropdown is provided on the products page to filter by standard sorting parameters.
        
          - [View](https://user-images.githubusercontent.com/41737293/139528887-49d7004e-0565-49ac-b3d2-e13cd406c605.JPG)

    7. As a First Time Visitor, I want to be able to search for a product by name or description and see results.

        1. Search functions are available on the navigation bar, allowing users to search by product name or description.
        
          - [View](https://user-images.githubusercontent.com/41737293/139528967-99511e92-85b0-4e95-be01-6e1cfa7cdea2.JPG)

    8. As a First Time Visitor, I want to easily select the quantity of a product, add to checkout, and process an order.

        1. Users can select the quantity of an item, add it to the shopping bag and finish checking out using the Stripe checkout system. 
        
          - [View](https://user-images.githubusercontent.com/41737293/139529047-12b067f6-b1a7-4ee2-8438-1221168d9e1f.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/139529028-328ba6ff-deb9-40fe-bda5-f1b8a7da01e1.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/139529054-86f1d1c5-06fe-4cf6-8731-780cc964b115.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/139529065-83791d55-bd3e-48d8-adc8-938fa59a962a.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/139529076-34254108-2b09-427a-af73-5db3bc873ab1.JPG)
   

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to view my shopping bag to see what I have added to the bag.
        
          - [View](https://user-images.githubusercontent.com/41737293/139529117-9b183b7a-76e3-4264-a245-ba98a2737894.JPG)

    2. As a Returning Visitor, I want to view my profile to check my order history once I have made an order.

          - [View](https://user-images.githubusercontent.com/41737293/139529138-f94af269-0d08-4f8a-b918-9d80fadc79fd.JPG)


-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if I can log into my account without issue.

        1. The User can log in without issue as long as the username and password are correct. Password can be reset, and confirmation emails are received upon creating an account and verifying the account.

    2. As a Frequent User, I want to check to see if there are new products added to the website.

        1. Admin users can update product pages to add items to the product line so normal users can frequent the website to look for new products.

        - [View](https://user-images.githubusercontent.com/41737293/139529232-88e801c4-4294-41e5-925b-c9823d742175.JPG)

    3. As a Frequent User, I want to navigate the website and find things where they are supposed to be.

        1. Navigation bar is simple and straightforward. 
        2. Finding what you need is not difficult as everything is placed visibly and makes sense.
    

### Further Testing

-   The live project has been tested  on a variety of devices such as Desktop and Samsung Note 10 + 5G
-   A large amount of testing was done to ensure that the website was responsive.
-   Friends and family members were requested to review the site and documentation to point out any bugs or user experience issues, and all were content with the browsing experience.

### Known Bugs

- There can be some visual delay when navigating the product pages due to the jpg images loading in. I have used a cache method to try to combat this.

- Unable to load Heroku website in a website mockup generator to test responsiveness

- Due to Django routing, getting a validation error for HTML element (li) unable to fix without breaking padding on navbar


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