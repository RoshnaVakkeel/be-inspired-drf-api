# BE INSPIRED - DRF API

## Table of Contents

- [Design](<#design>)
	- [User Stories](<#user-stories>)
	- [Database Schema](<#database-schema>)
        - [User](<#user>)
	    - [Profile](<#profile>)
        - [Followers](<#followers>)
	    - [Post](<#post>)
        - [Recommendation](<#recommendation>)
	    - [Like](<#like>)
	    - [Comment](<#comment>)
- [Testing](<#testing>)
	- [Manual Testing](<#manual-testing>)
	- [Validation](<#validation>)
- [Technologies](<#technologies>)
	- [Development Technologies](<#development-technologies>)
	- [Testing Technologies](<#testing-technologies>)
- [Deployment](<#deployment>)
	- [Django](<#django>)
	    - [Project Setup](<#project-setup>)
	    - [JWT Tokens](<#jwt-tokens>)
        - [Heroku Deployment](<#heroku-deployment>)
	- [Heroku](<#heroku>)
- [Credits and Resources](<#credits-and-resources>)
	- [Code](<#code>)

## Design
### User Stories
The API was designed using the back end to achieve the user stories mentioned in the front end of 'Be Inspired' project. The back-end focuses on its administration side and can be described as one user story:

As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have full control the application using its CRUD features.

### Database Schema
The database was built using the Django Rest Framework. It makes use of Django models, serializers, and views. The Data Schema was designed as shown below:

![Database Schema](docs/images/database_schema_be_inspired.png)

#### User Model

- The User model consists of information about the user and is a part of Django allauth library. 
- Relationships of User entity with other entities
	- One-to-one relation with the Profile entity owner field
	- One-to-many ForeignKey relation with the Follower entity owner and followed fields
	- One-to-many ForeignKey relation with the Post entity owner field
	- One-to-many ForeignKey relation with the Recommendation entity owner field
	- One-to-many ForeignKey relation with the Comment entity owner field
	- One-to-many ForeignKey relation with the Like entity owner field

#### Profile Model

- The Profile entity contains the following keys: owner, name, age_group, brief_bio, created_on, updated_on and image
- One-to-one relation between the owner field and the user entity id field

## Project Setup
Django Rest Framework (DRF) was used to create this API. DRF project was set up and many necessary dependencies were installed following these steps:

1. Within your development environment/terminal, install Django with: `pip3 install django>4` to install Django framework.
2. The code at terminal `pip3 install <package>` was used to install different dependencies:
- `pip3 install django-cloudinary-storage`- for Cloudinary to store uploaded image files
- `pip3 install Pillow` - To allow ImageFields to be used in the database models
- `pip3 install djangorestframework`- To install Django Rest Framework

3. Once these dependencies are installed, requirements.txt is updated using: `pip3 freeze > requirements.txt`. 
4. New Django project using the command `django-admin startproject <your-project-name> .` (dot at the end is necessary create it in root directory).
5. Add your installed apps to the `settings.py` file INSTALLED_APPS variable. The required lines are:
~~~
'cloudinary_storage',
'cloudinary',
'rest_framework',

~~~
6. To configure cloudinary, the following variables need to be set in settings.py: 
- `CLOUDINARY_STORAGE`: this should be set to your own cloudinary URL. Create env.py file in root directory and create a`CLOUDINARY_URL` environment variable in an env.py file like this
~~~
import os

os.environ['CLOUDINARY_URL'] = 'cloudinary:<url from personal cloudinary account>
~~~

and import this into the settings.py file using:
~~~
import os
if os.path.exists('env'):
    import env
~~~
 
`CLOUDINARY_STORAGE` is to be set to: `{'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')}` which retrieves the env.py variable in a development environment, but also allows a Config Var to be set in Heroku for later deployment to Heroku.

- `MEDIA_URL`: this is set to '/media/' in this project
- `DEFAULT_FILE_STORAGE`: is to be set to 'cloudinary_storage.storage.MediaCloudinaryStorage'

7. . Whilst in the `env.py` file, create a `SECRET_KEY` variable which will be used later for Heroku deployment. To generate a new Django secret key, do a google search for a random key generator and use one of the results to create a key. The variable can be created using: 
~~~
os.environ ["SECRET_KEY"] = "<copy and paste the secret key>"
~~~
Back in settings.py, find the `SECRET_KEY` variable and replace the assignment as follows:
~~~
SECRET_KEY = os.environ.get('SECRET_KEY')
~~~


~~~
git add .
git commit -m "initial commit"
git push
~~~
