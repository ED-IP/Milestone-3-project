# Tech-Tionary 

TECH-TiONARY is dictionay dedicated to store Computer Science and tech terms.
The objective of the site is to have short definitions of common terms used in the field of computer since and technology but without giving a full explain of the term in question, for example for terms related to coding it will not provide examples of use.

The target user is those that want a quick summary of some term/words that they could have read in more in detail documentation or around the web.
Also it is possible for guest to register in the website adquiring the ability of add/edit/delete entrys to the dictionary (with some limitations for the last two options).

## Features

### Existing Features

- __Navigation Bar__

    - Featured on all eight pages, the full responsive navigation bar includes links to the Home page (main search), Log In, Register, User profile, Edit User Details, Search Results, Add Entry and Edit Entry. It is identical in each page to allow for easy navigation.
    - The navigation bar allows the user to navigate through the site with different screen size devices devices without having to use the "back" and "Forward" buttons.
    - Depending if the user is a Registered one or Anonimous guest some of the options will be or not present in the menu.

- __Search Page__

    - The Search page (main page and also accesible with the "Home" option in the menu) presents a field where the user can search inside the dictionary

- __Search Results__

    - In this section the results from the search are shown as a collapsible listed
    - If not match is found in the database a warning message is presented

- __Register User page__

    - In this section of the web an anonimous user can register to gain the ability to add/edit/delete entrys from dictionary
    - The user have to provide a username, e-mail and a password
    - There is a link to the Log In page in case that the user have already registered.

- __Log In page__

    - In the Log In area the user have to provide a valid (already registered) Username and Password
    - If the Log In details are incorrect a warning message is shown
    - There is a link to the Register page in case that the user wants to register.

- __User Profile__

    - In the User Profile all the entrys added by the user are listed
    - In every entry there are buttons that allow to delete or edit the entry
    - There is a button that sends the user to the Edit User details section

- __Edit User__

    - The Edit User section allow the user to update its email and password

- __Add Entry__

    - In this section a registered user can add a new entry to the dictionary, with a new term and a definition associated
    - Automatically the Username is added to the entry

- __Edit Entry__

    - This section provides two fields that allow a register to edit a term and its definition
    - The current value for the entrys are shown on the top of the edit field to help the user known the previous values and avoid possible mistakes
    - The user only can edit entrys made by itself


### Future Features

- Add some random search results to the main search page to make it more appealing
- Add checks to avoid duplicate entrys
- Night mode color Scheme
- The ability to add user as administrator that can add/edit/delete users and entrys in the dictionary
- A GUI for the administrator user
- A dedicated error page with descriptives messages (E.G: when an user tries to delete an entry by a different user)
 
## UX

A user of the website:
- Should be able to search for terms inside the dictionary (All users)
- Anonimous users can't add, delete or edit terms in the database
- Anonimous users could become registered user using the corresponding form
- Registered users should be able add new entrys to the dictionary
- Registered users only will be able to edit/delete their own entrys
- Register user would have the option to update the email and password used for registration


## Typography and Color Scheme

1. Typography:

## Wireframes

Wireframes for the project can be found [here](https://github.com/ED-IP/Milestone-3-project/blob/master/docs/Milestone_project_3_wireframes.pdf)

## Technologies Used

- **[HTML]**
	- **HTML** is used to create the structure of the web-page.

- **[Materialize](https://materializecss.com/)**
    - **Materialize** is used to provide css style for the web-page

- **[Font Awesome](https://fontawesome.com/)**
	- The website use several simbols from **Font Awesome** service.

## To do / Incomplete features

- There are several input fields that need to indicate that they have some restrictions in the characters they can accept and limitations in length
- Add the footer
- Visually more engaging warning message (when matches aren't found in the dictionary, a user trying to edit a entry that is not their etc...)
- Remove Debug from app.py
   
## Testing

The tests have been done on mobile using a Samsung S8, with Brave Browser 1.25.73
On Desktop the following browsers has been used for testing:

- User stories testing

    - Users Should be able to search for terms inside the dictionary (Anonimous and registered):
        - Tested doing search as a diferent register users and not register user. The behaviour is the expected one, returning entrys from inside the dictionary.

    - Anonimous users can't add, delete or edit terms in the database
        - If an anonimous user tries to edit a term using an URL to reach the edit entry page a warning is shown
        - If it tries to add a term using an URL to reach the add term page a warning is shown
        - If it tries to reach the profile page of a register user to be able to delete a term an error happens and the app crashes
        - Same results happens in mobile and desktop configurations
    
    - Anonimous users could become registered user using the corresponding form
        - Tested in mobile an desktop configurations, working as intended. The user is created without issues with the data submited by the form
    
    - Registered users should be able add new entrys to the dictionary
        - Functionality wors as intended on mobile and desktop
    
    - Registered users only will be able to edit/delete their own entrys
        - 
        
        

    - Register user would have the option to update the email and password used for registration

- Other scenarios:
    - If an entry that has been deleted is tried to be updated an error appears


### Bugs

- When an update in the user profile happens two alerts messages appears, one for success and another for failure
- On mobile view (Samsung S8, Brave Browser 1.25.73), the text for the buttons edit/delete in the user_profile appears outside of the button
- On mobile view (Samsung S8, Brave Browser 1.25.73), the Title on the Navbar doesn't render completelly


## Deployment

### Heroku Deployment

- These are the steps followed to deploy the proyect on Heroku

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

    5. Choose a name and a region (for the proyect I use Europe) and click create

    6. Once the app is created click on the settings tab, and then click on "Reveal config Vars" button.
        - Add the following key, values pairs
        
        KEY | VALUES
        --------------|--------------
        IP | 0.0.0.0
        MONGO_DBNAME|
        MONGO_URI| mongodb+srv://user:passworduser@namecluster.8pkrb.mongodb.net/collection?retryWrites=true&w=majority
        PORT| 5000
        SECRET_KEY    |

    7. Go to the Deployment tab and in the Deployment Method section choose GitHub
        - In the connect to GitHub choose the correct repository and click connect
        
    8. In the section Automatic Deploys  choose the branch to deploy (in mycase was the master one) and click in Enable Automtic Deploys

    9. After building the proyect it should be deployed. You can open the app by clicking in the Open App button at the top of the page

    10. The address for the deployed proyect: https://dictionary-cs.herokuapp.com/


## Credits

https://stackoverflow.com/questions/17873820/flask-url-for-with-multiple-parameters

https://www.w3schools.com/python/python_mongodb_update.asp

https://stackoverflow.com/questions/60547442/pymongo-update-one-not-updating-based-on-id

https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find_one

### HTML

 

### Javascript

 

### Content


### Media

- Images links :
	- [owner](https://www.google.com)(placeholder)
	
