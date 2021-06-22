# TECH-TiONARY 

TECH-TiONARY is dictionary dedicated to store Computer Science and tech terms.
The objective of the site is to have short definitions of common terms used in the field of computer since and technology but without giving a full explain of the term in question, for example for terms related to coding it will not provide examples of use.

The target user is those that want a quick summary of some term/words that they could have read in more in detail documentation or around the web.
Also it is possible for guest to register in the website acquiring the ability of add/edit/delete entries to the dictionary (with some limitations for the last two options).

## Features

### Existing Features

- __Navigation Bar__

    - Featured on all eight pages, the full responsive navigation bar includes links to the Home page (main search), Log In, Register, User profile, Edit User Details, Search Results, Add Entry and Edit Entry. It is identical in each page to allow for easy navigation.
    - The navigation bar allows the user to navigate through the site with different screen size devices devices without having to use the "back" and "Forward" buttons.
    - Depending if the user is a Registered one or Anonymous guest some of the options will be or not present in the menu.

- __Search Page__

    - The Search page (main page and also accessible with the "Home" option in the menu) presents a field where the user can search inside the dictionary

- __Search Results__

    - In this section the results from the search are shown as a collapsible listed
    - If not match is found in the database a warning message is presented

- __Register User page__

    - In this section of the web an anonymous user can register to gain the ability to add/edit/delete entries from dictionary
    - The user have to provide a username, e-mail and a password
    - There is a link to the Log In page in case that the user have already registered.

- __Log In page__

    - In the Log In area the user have to provide a valid (already registered) Username and Password
    - If the Log In details are incorrect a warning message is shown
    - There is a link to the Register page in case that the user wants to register.

- __User Profile__

    - In the User Profile all the entries added by the user are listed
    - In every entry there are buttons that allow to delete or edit the entry
    - There is a button that sends the user to the Edit User details section

- __Edit User__

    - The Edit User section allow the user to update its email and password

- __Add Entry__

    - In this section a registered user can add a new entry to the dictionary, with a new term and a definition associated
    - Automatically the Username is added to the entry

- __Edit Entry__

    - This section provides two fields that allow a register to edit a term and its definition
    - The current value for the entries are shown on the top of the edit field to help the user known the previous values and avoid possible mistakes
    - The user only can edit entries made by itself

- __Databases__

For this project I used a database with two collections, one for the terms of the dictionary and another one for the users:
- USER collection structure

    KEY | VALUES
    -------|-------
    user | 
    email | 
    password | 

- TERMS collection structure

    KEY | VALUES
    -------|-------
    term |
    user | 
    definition | 

### Future Features

- Add some random search results to the main search page to make it more appealing
- Add checks to avoid duplicate entries
- Night mode color Scheme
- The ability to add user as administrator that can add/edit/delete users and entries in the dictionary
- A GUI for the administrator user
- A dedicated error page with descriptives messages (For example, when an user tries to delete an entry by a different user)
- There is too much space unused at the sides of the pages, specially with big monitors. Could be a good idea try to use it for something
  or add some kind of decoration
 
## UX

A user of the website:
- Should be able to search for terms inside the dictionary (All users)
- Anonymous users can't add, delete or edit terms in the database
- Anonymous users could become registered user using the corresponding form
- Registered users should be able add new entries to the dictionary
- Registered users only will be able to edit/delete their own entries
- Register user would have the option to update the email and password used for registration


## Typography and Color Scheme

The intention under the color scheme choose for the project was to focus on the reading experience for that reason
I choose black and white for the majority of the page.

I change the color of headers for the list of terms added by the user in the user profile page to break a bit the monotony and to emphasise
the collapsible element.

For buttons I use green for submit actions and red to cancel or going back a step, since I think there are well understand globally.


## Wireframes

Wireframes for the project can be found [here](https://github.com/ED-IP/Milestone-3-project/blob/master/docs/Milestone_project_3_wireframes.pdf)

## Technologies Used

- **[HTML]**
	- **HTML** is used to create the structure of the web-page.

- **[Materialize](https://materializecss.com/)**
    - **Materialize** is used to provide css style and some JavaScript content.

- **[Font Awesome](https://fontawesome.com/)**
	- The website use several symbols from **Font Awesome** service.

## To do / Incomplete features

- There are several input fields that need to indicate that they have some restrictions in the characters they can accept and limitations in length
- ~~Add the footer~~
- Adjust the footer height
- Visually more engaging warning message (when matches aren't found in the dictionary, a user trying to edit a entry that is not their etc...)
- ~~Remove Debug from app.py~~
   
## Testing

The tests have been done for mobile / small screen devices:
 - Samsung S8, with Brave Browser 1.25.73
 - Developers tools from Brave browser Desktop and Firefox Desktop

For Desktop site the following browsers has been used:
 - Firefox 89.0.1 (Windows version)
 - Brave 1.25.72 (windows version)

### User stories testing

    - Users Should be able to search for terms inside the dictionary (Anonymous and registered):
        - Tested doing searches as a different register users and not register user.
          The behaviour is the expected one, returning entries from inside the dictionary or an error message if no match is found.
        
    - Anonymous users can't add, delete, edit terms or edit user profiles
        - If an anonymous user tries to edit a term using an URL to reach the edit entry page a warning is shown
        - If it tries to add a term using an URL to reach the add term page a warning is shown
        - If it tries to reach the profile page of a register user to be able to delete a term an error happens and the app crashes (added to the bug section)
        - Same results for mobile and desktop configurations
    
    - Anonymous users can become registered user using the corresponding form
        - Tested in mobile an desktop configurations, working as intended. The user is created without issues with the data submitted by the form
    
    - Registered users should be able add new entries to the dictionary
        - Functionality works as intended on mobile and desktop adding the terms, description and the user that create the entry to the dictionary.
    
    - Registered users only will be able to edit/delete their own entries
        - Tested that register users can only access their own profile so they can not delete terms on other users profiles
        - Anonymous users can't access any profile and therefore they can not access to the delete option (returns a 500 error, added to bug section)        

    - Register user would have the option to update the email and password used for registration
        - Tested the functionality on mobile and desktop, the entry in the database is updated but there is a bug with the success messages (noted in the bug section)

### Other scenarios:
    - If an entry that has been deleted is tried to be updated an error appears

- [W3C Validation tools](https://validator.w3.org/)
   - All the HTML files were tested with the W3C validator, some html errors were found and fixed.
   - Still there are errors that I think are related to the Jinja templates

- [CSS Validator](https://jigsaw.w3.org/css-validator/)
   - Style.css was tested with the css validator, no error was found

- [JSHint]https://jshint.com/
   - script.js was tested with JSHint no warnings were given

### Lighthouse tests:

Desktop:

Section | Performance | Accessibility | Best Practices | Seo
------------|------|------|------|------
Main Search | 99 | 92 | 100 | 89
Register user | 100 | 92 | 100 | 89
Log In user | 100 | 92 | 100 | 78
User Profile | 100 | 84 | 100 | 89
Edit term | 100 | 92 | 100 | 91
Add term | 99 | 92 | 100 | 89
Edit User | 99 | 92 | 100 | 89

Mobile:

Section | Performance | Accessibility | Best Practices | Seo
------------|------|------|------|------
Main Search | 96 | 92 | 100 | 91
Register user | 97 | 92 | 100 | 91
Log In user | 97 | 92 | 100 | 82
User Profile | 96 | 84 | 100 | 91
Edit term | 96 | 92 | 100 | 91
Add term | 96 | 92 | 100 | 91
Edit User | 96 | 92 | 100 | 91

The test didn't work for the Search Result page.

### Browser's Developer tools

The developers tools were used to tes the reponsive design of the site.

- In general it works correctly but there is a constant issue with the text (in buttons specially) that overflow the button.
- Ipad and Iphone settings show a white line at the right side that runs from the top to the bottom of the screen in severeal models.
- Using the Navbar menu covers all the screen when Galaxy fold setting was tested. Once an option is selected the menu closes correctly

### Bugs

- When an update in the user profile successfully happens two alerts messages appears, one for success and another for failure
- On mobile (Samsung S8, Brave Browser 1.25.73, and developer tools mobile view):
     - The text for the title bar, the buttons edit/delete in the user_profile appears outside of their place.
- If an anonymous user tries to reach the profile page of a register user an error happens and the app crashes (on Firefox returns a 500 error)
    application should not crash and show a message instead

## Deployment

### GitHub Deployment

To deploy the project on GitHub Pages:
 1. Go to the address of the repository https://github.com/ED-IP/Milestone-3-project
 2. Click on the settings tab.
 3. Go to the "Pages" section.
 4. On the Sources section, click on the "None" button and select the Master branch.
 5. Click Save
 
 The project should be deployed now

### Heroku Deployment

These are the steps followed to deploy the proyect on Heroku

1. Create a requierements.txt, in Gitpod terminal:
    - pip3 freeze --local > requirements.txt
    
2. Create a Procfile, in Gitpod terminal:
    - echo web: python app.py > Procfile
    - open the Procfile and check that there is no trailing lines after the text

3. Add and push the files to GitHub:
    - git add requirements.txt
    - git add Procfile
    - git commit -m ""
    - git push

4. On the Heroku Dashboard click in the New button and choose "New App"

5. Choose a name and a region (for the project I use Europe) and click create

6. Once the app is created click on the settings tab, and then click on "Reveal config Vars" button.
    - Add the following key, values pairs
        
        KEY | VALUES
        --------------|--------------
        IP | 0.0.0.0
        MONGO_DBNAME| name of the database
        MONGO_URI| mongodb+srv://user:passworduser@namecluster.8pkrb.mongodb.net/collection?retryWrites=true&w=majority
        PORT| 5000
        SECRET_KEY    |
    
    - Note: The values used in the project are not present here as they include passwords and user

7. Go to the Deployment tab and in the Deployment Method section choose GitHub
    - In the connect to GitHub choose the correct repository and click connect
        
8. In the section Automatic Deploys choose the branch to deploy (in my case was the master one) and click in Enable Automatic Deploys

9. After building the project it should be deployed. You can open the app by clicking in the Open App button at the top of the page

10. The project is deployed at this address https://dictionary-cs.herokuapp.com/

## Credits

The following terms and part of the descriptions were taken from [Wikipedia](https://www.wikipedia.com) and added to the dictionary

[Computer Science](https://en.wikipedia.org/wiki/Computer_science)
[Solid State Drive](https://en.wikipedia.org/wiki/Solid-state_drive)
[Central Processing Unit](https://en.wikipedia.org/wiki/Central_processing_unit)
[Graphic Processing Unit](https://en.wikipedia.org/wiki/Graphics_processing_unit)
[Hard disk drive](https://en.wikipedia.org/wiki/Hard_disk_drive)
[Compiler](https://en.wikipedia.org/wiki/Compiler)
[Source code](https://en.wikipedia.org/wiki/Source_code)
[Binary code](https://en.wikipedia.org/wiki/Binary_code)
[Internet](https://en.wikipedia.org/wiki/Internet)


The use of a second @app.route was inspired for the following post [stackoverflow](https://stackoverflow.com/questions/17873820/flask-url-for-with-multiple-parameters)

The following links were consulted to solve issues during the development

https://www.w3schools.com/python/python_mongodb_update.asp

https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find_one