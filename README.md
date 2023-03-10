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
- ListAPICreateView enables:
	- Users to create their Profile
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
- ListAPICreateView enables:
	- Users to create Posts
	- Users to retrieve a list of Posts
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
- ListAPICreateView enables:
	- Users to create Recommendations
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
- ListAPICreateView enables:
	- Users to create Comments
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
- [LICEcap](https://www.cockos.com/licecap/) - to capture an area of desktop and save it directly to .GIF (for viewing in web browsers). All the testing gifs have been generated using this tool.

### Testing Technologies
### Manual Testing
This user story as an admin was tested:
"As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have full control the application using its CRUD features."

**Results are enlisted in the table**

**Test** | **Action** | **Expected Result** | **Test Result**
-------- | ------------------- | ------------------- | -----------------
User | Update and/or delete user | A user can be updated and/or deleted |**Pass**
Profile | Update and/or delete profile | A users' profile can be updated and/or deleted | **Pass**
Post | Create/ Update and/or delete post | A post can be created/ edited and/or deleted | **Pass**
Recommendation | Create/ Update and/or delete recommendation | A recommendation can be Created/ Updated and/or deleted | **Pass**
Comments | Create/ Update and/or delete comment | A comment can be Created/ Updated and/or deleted | **Pass**
Likes | Create/ Change and/or delete Likes | A Like can be Created/ Changed and/or deleted | **Pass**
Followers | Create/ Change and/or delete followers | Followers can be Created/ Changed and/or deleted | **Pass**

The tests for CRUD features were run on Django Rest Framework(DRF-UI) and on Django-Admin panel. The details are as follows:

**Django Rest Framework - User Interface**

- To access the Django Rest Framework(DRF-UI), at terminal run command `python3 manage.py runserver`. It is accessible in a preview window.

**Paths with which pages can be accessed**
Using the URLconf defined in be_inspired_dr_api.urls, one can access the pages on preview window "https://8000-roshnavakke-beinspiredd-------.gitpod.io/**extensions**"
Different pages can be accessed using following extensions:

admin/
api-auth/
dj-rest-auth/logout/
dj-rest-auth/
dj-rest-auth/registration/
profiles/
profiles/<int:pk>/
posts/
posts/<int:pk>/
recommendations/
recommendations/<int:pk>/
comments/
comments/<int:pk>/
likes/
likes/<int:pk>
likes_recommendations/
likes_recommendations/<int:pk>
followers/
followers/<int:pk>/


- To get to the preview link, follow the steps as shown in the gif below:

	![DRF UI visible to logged out user](docs/manual_testing_drf_user_interface/root_route.gif)

- All the features and links that can be accessed are shown below.

	[DRF UI visible to logged out user](docs/manual_testing_drf_user_interface/root_route_logged_out.gif)


- Manual tests for **Profile** CRUD features

	In DRF-UI, the profiles page can be accessed using extension "/profiles" for list and details "profiles/<int:pk>/". The pages can be seen as shown below in gifs:

	- [Profiles List View](docs/manual_testing_drf_user_interface/profiles_list.gif) 
	- [Profile details upon profile selection using it's "id"](docs/manual_testing_drf_user_interface/profiles_id.gif) 
	- [Profiles filters](docs/manual_testing_drf_user_interface/profiles_filters.gif) 

- Manual tests for **Post** CRUD features
	In DRF-UI, the profiles page can be accessed using extension "/posts" for list and details "posts/<int:pk>/". The pages can be seen as shown below in gifs:

	- [Posts List View](docs/manual_testing_drf_user_interface/posts_list_post_create_update_test.gif) 
	- [Post details upon post selection using it's "id"](docs/manual_testing_drf_user_interface/posts_list_post_details.gif) 
	- [Posts filters](docs/manual_testing_drf_user_interface/posts_list_filters.gif) 

- Manual tests for **Recommendation** CRUD features

	In DRF-UI, the recommendations page can be accessed using extension "/recommendations" for list and details "recommendations/<int:pk>/". The pages can be seen as shown below in gifs:

	- [Recommendations List View](docs/manual_testing_drf_user_interface/recommendations_list.gif) 
	- [Recommendation details upon recommendation selection using it's "id"](docs/manual_testing_drf_user_interface/recommendations_detail.gif) 
	- [Recommendations filters](docs/manual_testing_drf_user_interface/recommendations_filters.gif) 

- Manual tests for **Comment** CRUD features

	In DRF-UI, the comments page can be accessed using extension "/comments" for list and details "comments/<int:pk>/". The pages can be seen as shown below in gifs:

	- [Comments List View](docs/manual_testing_drf_user_interface/comments_list_create_update.gif) 
	- [Comment details upon comment selection using it's "id"](docs/manual_testing_drf_user_interface/comments_list_details.gif) 
	- [Comments filters](docs/manual_testing_drf_user_interface/comments_filter.gif) 

- Manual tests for **Like** CRUD features

	In DRF-UI, the likes page can be accessed using extension "/likes" for list and details "likes/<int:pk>/". The pages can be seen as shown below in gifs:

	- [Like list view and details upon comment selection using it's "id"](docs/manual_testing_drf_user_interface/likes_list_and_details.gif) 

	In the DRF-UI and Admin panel, as the **Like** model shares foreign key relationship with both Recommendation and Post models. And as the the post or recommendation liked once cannot be liked twice by a user, there was an issue in liking a post or a recommendation separately. This issue can be seen in the gif below. It is also explained in Issues section.

	- [Likes List Issue](docs/manual_testing_drf_user_interface/likes_list_issue.gif) 

	As a solution (as per suggestion by my mentor Elaine B. Roche), I tried separating the like model for recommendation from post. Thus, I created another App to only like recommendation individually. The tests can be found below. The issue is also noted in Issues and Fix section below.

	In DRF-UI, the likes page can be accessed using extension "/likes_recommendations" for list and details "likes_recommendations/<int:pk>/". The pages can be seen as shown below in gifs:

	- [likes_recommendations list view](docs/manual_testing_drf_user_interface/likes_recommendations_list.gif) 

	- [likes_recommendations details view](docs/manual_testing_drf_user_interface/likes_recommendations_details.gif) 

- Manual tests for **Followers** CRUD features

	In DRF-UI, the followers page can be accessed using extension "/followers" for list and details "followers/<int:pk>/". The pages can be seen as shown below in gifs:

	- [Followers List View](docs/manual_testing_drf/followers_list.gif) 
	- [Follower Detail View](docs/manual_testing_drf/follower_detail.png) 



## Django

### Project Setup
Django Rest Framework (DRF) was used to create this API. DRF project was set up and many necessary dependencies were installed following these steps:

1. Within your development environment/terminal, install Django with: `pip3 install 'django<4'` to install Django framework.
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

[Credit for the write-up- Adam Hatton's quizle-drf-api](https://github.com/adamhatton/quizle-drf-api)

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

To configure and enable JWT Tokens, the following steps were folowed:

1. Install the dj-rest-auth package for JWT tokens using `pip3 install djangorestframework-simplejwt`
2. Create a session authentication value for differentiating between Development and Production environments, this should be added to the env.py file: `os.environ['DEV'] = '1'`
3. Use the session authentication value in settings.py to determine whether to use SessionAuthentication (for in Dev) or JWT Tokens (for in Production) using the following:
~~~
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [( 
        'rest_framework.authentication.SessionAuthentication' 
        if 'DEV' in os.environ 
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )]
}
~~~
4. Add `REST_USE_JWT = True` to enable token authentication
5. Add `JWT_AUTH_SECURE = True` to ensure tokens are only sent over HTTPS
6. Give cookie names to the access and refresh tokens using:
~~~
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
~~~

[Credit for the write-up- Adam Hatton's quizle-drf-api](https://github.com/adamhatton/quizle-drf-api)

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

- Fix: To solve it, I created a separate app for Recommedation Likes called likes_recommendations and then I could select it without any clash. Similarly, I could also extend it to Posts. But with fronend I see that there is no issue. User can like a post without a need to select a Recommendation. 

- Issue 3: Category Selection
In the frontend, I added badges to enable search of posts using badges. Upon usin setCategory function, the selected badge with category must return response. 

-Fix: I added category in fiterset_fields = [categrory,] to solve this.


## Testing

## Credits and Resources
- Django REST Framework Documentation
- The codes were highly and heavily rely on CI's DRF-API walkthrough.
- Code Institute's Tutor support - Ed and Gemma
- DRF installation, project set up and deployment sections were copied from [Adam Hatton's quizle-drf-api](https://github.com/adamhatton/quizle-drf-api) and were edited as I performed in my project. 
- Other references for the project and learning resources were:
- [SnapFood API in DRF](https://github.com/aleksandracodes/snapfood-drf-api)
- [Buzz of Berlin DRF API](https://github.com/vkleer/Buzz_of_Berlin_DRF_API)
- [ci-pp5-gamer-verse-drf-api](https://github.com/Jbachtiger/ci-pp5-gamer-verse-drf-api)
- Stack Overflow





