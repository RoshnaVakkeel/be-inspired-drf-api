# BE INSPIRED - DRF API

## Table of Contents

- [Design](<#design>)
	- [User Stories](<#user-stories>)
	- [Database Schema](<#database-schema>)
	- [Details](<#details>)
        - [User](<#user>)
	    - [Profile](<#profile>)
	    - [Post](<#post>)
        - [Recommendation](<#recommendation>)
		- [Comment](<#comment>)
	    - [Like](<#like>)
		- [Followers](<#followers>)
- [Technologies](<#technologies>)
	- [Development Technologies](<#development-technologies>)
	- [Testing Technologies](<#testing-technologies>)
- [Django](<#django>)
	- [Project Setup](<#project-setup>)
	- [Custom API with DRF](<#custom-api-with-drf>)
	- [JWT Tokens](<#jwt-tokens>)
- [Deployment](<#deployment>)
    - [Heroku](<#heroku>)
- [Issues and Fixes](<#issues-and-fixes>)
- [Testing](<#testing>)
	- [Manual Testing](<#manual-testing>)
	- [Validation](<#validation>)
- [Credits and Resources](<#credits-and-resources>)
	- [Code](<#code>)

## Design

### User Stories
The API was designed using the back end to achieve the user stories mentioned in the front end of 'Be Inspired' project. The back-end focuses on its administration side and can be described as one user story:

As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have full control the application using its CRUD features.

### Database Schema
The database was built using the Django Rest Framework. It makes use of Django models, serializers, and views. The Data Schema was designed as shown below:

![Database Schema](docs/images/database_schema_be_inspired.png)

### Details

#### User 

##### Model
- The User model consists of information about the user and is a part of Django allauth library. 
- Relationships of User entity with other entities
	- One-to-one relation with the Profile entity owner field
	- One-to-many ForeignKey relation with the Follower entity owner and followed fields
	- One-to-many ForeignKey relation with the Post entity owner field
	- One-to-many ForeignKey relation with the Recommendation entity owner field
	- One-to-many ForeignKey relation with the Comment entity owner field
	- One-to-many ForeignKey relation with the Like entity owner field

#### Profile 

##### Profile Model
- The Profile entity contains the following keys: owner, name, age_group, brief_bio, created_on, updated_on and image
- One-to-one relation between the owner field and the user entity id field

##### Profile Serializer
The Profile model serializer adds additional fields when a model instance that is returned by the API:
- is_owner: To know if the user making the request is the owner
- following_id: To know who the user is following
- posts_count: To know how many posts have been created by the user
- recommendations_count: To know how many recommendations have been created by the user

##### Profile Views
Django generics API views were used for Profile model:
- ListAPIView enables:
	- Users to retrieve a list of Profiles
- RetrieveUpdateAPIView enables:
	- Users to obtain a single Profile instance
	- Users to update a single Profile instance (if it is theirs)

#### Post 

##### Post Model
- The Post entity contains the fields: owner, title, category, description, created_on, updated_on and image
- Relationships of Post entity with other entities
	- One-to-many ForeignKey relation with the Comment entity owner field
	- One-to-many ForeignKey relation with the Like entity owner field

##### Post Serializer
The Post model serializer adds additional fields for when a model instance that is returned by the API:
- is_owner: Whether the user making the request is the owner
- profile_id: The profile id of the user that created the post
- profile_image: The profile image of the user that made the post
- comments_count: To know how many comments did the post recieve
- likes_count: To know how many likes did the post recieve
- like_id: checks if the logged in user has liked any posts

##### Post Views
Django generics API views were used for Post model:
- ListAPIView enables:
	- Users to retrieve a list of posts
- RetrieveUpdateDestroyAPIView enables:
	- Users to obtain a single Post instance
	- Users to update a single Post instance (if they own it)

#### Recommedation

##### Recommedation Model
- The Recommedation entity contains the fields: owner, title, category, description, created_on, updated_on and image
- Relationships of Recommedation entity with other entities
	- One-to-many ForeignKey relation with the Comment entity owner field
	- One-to-many ForeignKey relation with the Like entity owner field

##### Recommendation Serializer
The Recommendation model serializer adds additional fields for when a model instance that is returned by the API:
- is_owner: Whether the user making the request is the owner
- profile_id: The profile id of the user that created the Recommendation
- profile_image: The profile image of the user that made the Recommendation
- comments_count: To know how many comments did the Recommendation recieve
- likes_count: To know how many likes did the Recommendation recieve
- like_id: checks if the logged in user has liked any Recommendations

##### Recommendation Views
Django generics API views were used for Recommendation model:
- ListAPIView enables:
	- Users to retrieve a list of Recommendations
- RetrieveUpdateDestroyAPIView enables:
	- Users to obtain a single Recommendation instance
	- Users to update a single Recommendation instance (if they own it)

#### Comments

##### Comments Model
- The Comment entity contains the fields: owner, content, post, recommendation, created_on, updated_on
- Relationships of Comment entity with other entities
	- ForeignKey relation with the Post entity owner field
	- ForeignKey relation with the Recommendation entity owner field

##### Comment Serializer
The Comment model serializer adds additional fields for when a model instance that is returned by the API:
- is_owner: Whether the user making the request is the owner
- profile_id: The profile id of the user that created the Comment
- profile_image: The profile image of the user that made the Comment
- created_on: To calculate how long ago the comment was created
- updated_on: To calculate how long ago the comment was updated

##### Comment Views
Django generics API views were used for Comment model:
- ListAPIView enables:
	- Users to retrieve a list of Comments
- RetrieveUpdateDestroyAPIView enables:
	- Users to obtain a single Comment instance
	- Users to update a single Comment instance (if they own it)

#### Likes

##### Like Model
- The Like entity contains the fields: owner, post, recommendation, created_on
- Relationships of Like entity with other entities
	- ForeignKey relation with the Post entity owner field
	- ForeignKey relation with the Recommendation entity owner field

##### Like Serializer
The Like model serializer adds additional fields for when a model instance that is returned by the API:
- owner: To display username of the user

##### Like Views
Django generics API views were used for Like model:
- ListAPIView enables:
	- Users to retrieve a list of Likes and create a Like
- RetrieveUpdateAPIView enables the users:
	- to get a single Like instance
	- to delete a single Like instance (if they own it)

#### Follower 

##### Follower Model
- The Follower entity contains the fields: owner, followed and created_on
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the followed field and the User model id field

##### Follower Serializer
The Follower model serializer adds additional fields for when a model instance that is returned by the API:
- owner: To display username of the user
- followed_name: To display the name of the user who is following the user

##### Follower Views
Django generics API views were used for Follower model:
- ListAPIView enables:
	- Users to retrieve a list of Followers and create a Follower
- RetrieveUpdateAPIView enables the users:
	- to get a single Follower instance
	- to delete a single Follower instance (if they own it)

### Development Technologies

**Languages**
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

**Frameworks & Libraries**

- [Django](https://www.djangoproject.com/) - to build the database
- [Cloudinary](https://cloudinary.com/) - to store and serve files
- [Pillow](https://python-pillow.org/) - imaging library used to enable image fields in the Profile, Post and Recommendation models
- [Django rest auth](https://django-rest-auth.readthedocs.io/en/latest/) - to implement account authorisation
- [Django Rest Framework](https://www.django-rest-framework.org/) -  to develop the API that works in conjunction with the database
-- [django-filter](https://django-filter.readthedocs.io/en/stable/) - used to enable filtering of resources

**Tools**

- [Lucidchart](https://lucid.app/lucidchart/) - to create a diagram of the Database Schema
- [Gitpod](https://www.gitpod.io/) - to code and develop the website
- [Git](https://git-scm.com/) – for version control (Gitpod terminal to commit to Git, and pushing to GitHub)
- [GitHub](https://github.com/) – to store the source code 
- [Heroku](https://www.heroku.com/) - to host and deploy the live website
- [Random Key Generator](https://randomkeygen.com/) - to generate secret key for Django 

### Testing Technologies


## Django

### Project Setup
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
At the terminal
~~~
git add .
git commit -m "initial commit"
git push
~~~

- App Creation
After creation of new App using `python3 manage.py startapp <app>`, it must be added to installed apps in settings.py.

- Once the database models are created in 'models.py' file, they must be registered in 'admin.py' file of the respective app directory. Later the migrations must be made to the database.

### Custom API with DRF
To create APIs using Django Rest Framework. These steps are to be followed 

**Installation**
Within the development environment, these dependencies also need to be installed with :
- `pip3 install djangorestframework`- installs the Django Rest Framework
- `pip3 install django-filter`- allows filtering, searching and sorting of API data

In `settings.py` file go to INSTALLED_APPS variable and add:
~~~
'rest_framework',
'django_filters',
~~~
After installation, generate a requirements.txt document. 

**Serializers**

"Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types." -- [source](https://www.django-rest-framework.org/api-guide/serializers/#serializers). These work similarly to Django's Form and ModelForm classes.

- Serializers are declared to serialize and deserialize data that corresponds to Model objects.
- In order to return complete object instances based on the validated data .create() and .update() methods are used.
- 

**Views**

Throughout in the DRF views.py file, GenericAPIView was used.
"Using the APIView class is similar to a regular View class, as usual, the incoming request is dispatched to an appropriate handler method such as .get() or .post(). Additionally, a number of attributes may be set on the class that control various aspects of the API policy." - [source](
https://www.django-rest-framework.org/api-guide/views/)

To control the basic view behavior these attributes were used [(source)](https://www.django-rest-framework.org/api-guide/generic-views/): 
- serializer_class - The serializer class used for validating and deserializing input, and for serializing output.
- permission_class - To allow only user to be able to access the view
- queryset - The queryset is used for returning objects from this view.
- filter_backends - A list of filter backend classes are used for filtering the queryset. Defaults to the same value as the DEFAULT_FILTER_BACKENDS setting. 

Install Django Filters: `pip3 install django-filter`
In settings.py, in templates add: 'django-filters'
Then update dependencies using `pip3 freeze > requirements.txt`

Additionally generate a view to render in 'views.py' file and create and wire up 'urls.py' in the respective directory. Then in 'urls.py' of project directory, for Class-based views
- Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

### JWT Tokens

## Deployment

### Heroku

## Issues and Fix

- Issue 1:
In Django Admin, Home › Comments › Comments › Add comment section, while saving a Comment error appears. It says that all the fields are cumpulsory. Comments Entity has foreign key relationship with Post and Recommedation entities. So, in the Comment model, both post and recommedation fields were defined. The field class type for both was provided as null=True considering the empty value to be accepted.
~~~
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        default=None,
        null=True
        )
    recommendation = models.ForeignKey(
        Recommendation,
        on_delete=models.CASCADE,
        default=None,
        null=True
        )
~~~

But Django admin would only save the comment if both fields were selected. I wanted them to be independent i.e. 

Fix:

The field class type was changed from null=True to blank=True and the issue was solved. It was a validation error. In the field options, null is purely database-related, whereas blank is validation-related.
Reference: https://docs.djangoproject.com/en/4.1/topics/db/models/


- Issue 2: Multiple migration error into database
My Like model has foreign key relationship with both Post and Recommendation entities. I can only add a like if I select both Post and Recommendation, but I wanted them to be independent. So, I added blank=True in field class types. But then I could not migrate the changes to database. Like issue 1, I added field class type as blank=True and skipped null=True. But in the terminal then new error appeared upon running 'python3 manage.py migrate' command. Error at terminal: 
django.db.utils.IntegrityError: NOT NULL constraint failed: new__comments_comment.post_id

Fix: 
With the help of Tutor support (special thanks to Ed, CI), as suggested, I deleted the latest migration instances and manually and migrated freshly and the issue solved. 

- Issue 3: Integrity Error
My issue 2 persisted. My Like model has foreign key relationship with both Post and Recommendation entities. I can only add a like if I select both Post and Recommendation, but I wanted them to be independent. So, I added blank=True and null=True in field class types. 

Then when post is selected and not recommendation, the error reads:
django.db.utils.IntegrityError: NOT NULL constraint failed: likes_like.recommendation_id

Then when a recommendation is selected and not a post, the error reads:
django.db.utils.IntegrityError: NOT NULL constraint failed: likes_like.post_id

Then I removed blank=True field class types for both posts and recommendations fields. The issue now is that when both options are not selected in Home › Likes › Likes › Add like in Django admin page, validation error is raised that both the fields are required. 
[Screenshots of the error 3](docs/issues/issue_3_integrity_error.pdf)

## Testing

## Credits and Resources

### Code


