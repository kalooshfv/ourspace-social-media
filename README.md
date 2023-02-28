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
   Generally, this involves: django, django-all-auth, dj-rest-auth, Pillow, whitenoise.

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


## Known Issues

These are a few known bugs and/or missing features to the website that could not
be fixed or executed on time.

1. No friend request feature
2. Not deployed
3. Image stretching at several intervals in the homepage and register preview if not uploaded in 1x1 format
4. Still using Session Authentication instead of Token Authentication
5. Empty footer on posts not belonging to the user (meant for friend request feature)
6. No TDD
7. Possible double clicking on jQuery-activated buttons, causing error messages to show up
8. Not responsive (apart from innate responsiveness from Bootstrap)
9. When testing with other devices, some modules weren't caught by 'pip install -r requirements.txt'. Examples: django, django-allauth, dj-rest-auth, django-all-auth, Pillow, whitenoise.
10. and many more...

## Thank You

Thanks for looking at the application. I hope you can give me constructive criticism so I can use it to better my work next time.
