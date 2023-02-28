# OurSpace Social Media Platform

OurSpace is an application to a university organization named "RISTEK" in the form of a social media website made using Django and the Django REST framework.

## Installation

Follow these steps for installation on a local machine:


1. Clone the new Django template repository from your GitHub account to a
   location in the filesystem of your local development environment by using
   Git:

   ```shell
   git clone <URL of this repository> <path in local development environment>
   ```

2. Go to the location where the cloned repository is located in the local
   development environment:

   ```shell
   cd <path to the cloned repository>
   ```

3. (Optional) Activate the virtual environment:

   ```shell
   python -m venv env
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```

4. Install the dependencies needed to build, test, and run the application:

   ```shell
   pip install -r requirements.txt
   ```

5. If there are dependencies not caught by the previous command:

   ```shell
   pip install <module name>
   ```
   Generally, this involves: django, django-allauth, dj-rest-auth, Pillow, whitenoise.

6. Run the migrations.:

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Load the initial data to the application (P.S. fixtures use UTF-8 encoding, and make sure this command is executed in the repository directory):

    ```shell
    python manage.py loaddata initial_custom_user.json
    python manage.py loaddata initial_posts.json
    ```

8. Run the Django Web application using local development server:

   ```shell
   python manage.py runserver
   ```

9. Open http://localhost:8000 in your favourite Web browser to see if the Web
   application is running.

## Features

These are the features included in the website.

1. Register and Login: Standard register and login functions, with an additional profile picture field.
2. Post a Post: Enter text into the text area and click the button "POST" to post a post into the post window.
3. Edit a Post: Click on the edit button on one of your posts to edit your post; click "Finish Editing" to finish editing one of your posts.
4. Delete a Post: Click on the delete button on of your posts to delete said post.
5. Filter Posts: Filter between all posts and only your posts to show up in the post window.
6. Edit Profile: Edit your profile username, password, and profile image.

## Known Issues

These are a few known bugs and/or missing features to the website that could not
be fixed or executed on time.

1. No friend request feature
2. Not deployed
3. Image stretching at several intervals in the homepage and register preview if not uploaded in 1x1 format
4. Still using Session Authentication instead of Token Authentication
5. No User bio (design choice, won't fit on left window)
6. No TDD
7. Possible double clicking on jQuery-activated buttons, causing error messages to show up
8. Not responsive (apart from innate responsiveness from Bootstrap)
9. When testing with other devices, some modules weren't caught by 'pip install -r requirements.txt'. Examples: django, django-allauth, dj-rest-auth, Pillow, whitenoise. Caused by not using a virtual environment when developing.
10. and many more...

## Thank You

Thanks for looking at the application. I hope you can give me constructive criticism so I can use it to better my work next time.
