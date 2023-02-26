# OurSpace Social Media Platform

OurSpace is an application to a university organization named "RISTEK" in the form of a social media website made using Django and the Django REST framework.

## Installation

If you want to use the code template in this repository as a starter code for
developing a Django Web application:


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

3. Create a Python virtual environment named `env` inside the cloned repository
   by using Python's `venv` module:

   ```shell
   python -m venv env
   ```

4. Activate the virtual environment:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```

5. Verify the virtual environment has been activated by looking at the prompt
   of your shell. Make sure there is a `env` prefix in your shell. For example:

   ```shell
   # Windows using `pwsh` shell
   (env) PS C:\Users\KalooshVerrell\my-django-app
   # Linux/Unix, e.g. Ubuntu using `bash` shell
   (env) kalooshverrell@ubuntu:~/my-django-app
   ```

6. Install the dependencies needed to build, test, and run the application:

   ```shell
   pip install -r requirements.txt
   ```

7. Load the initial data to the application:
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
3. Image stretching at several intervals in the homepage and register preview
4. Still using Session Authentication instead of Token Authentication
5. Empty footer on posts not belonging to the user (meant for friend request feature)
6. No TDD
7. Possible double clicking on jQuery-activated buttons, causing error messages to show up
8. and many more...

## Thank You

Thanks for looking at the application. I hope you can give me constructive criticism so I can use it to better my work next time.