# Learning Web Development Through Django

Web servers communicate by sending HTTP requests (client -> server) and responses (server -> client).

[**Static sites**](https://mdn.mozillademos.org/files/13841/Basic%20Static%20App%20Server.png) use a GET request to get hard coded / static data from the server.

[**Dynamic sites**](https://mdn.mozillademos.org/files/13839/Web%20Application%20with%20HTML%20and%20Steps.png) have static components as well as dynamically created data through applications.

Web frameworks are collections of functions, objects, rules and other code constructs designed to solve common problems, speed up development, and simplify the different types of tasks faced in a particular domain.

A view is a function that receives a request, does computation/modeling, and then returns a response.

### Handling the request with views.py

```
def my_function(request):
    #get HttpRequest
    #do cool things
    return HttpResponse('things!')
  ```

### Defining data models with models.py

Models define the structure of stored data, including the field types and possibly also their maximum size, default values, selection list options, help text for documentation, label text for forms, etc. The definition of the model is independent of the underlying database — you can choose one of several as part of your project settings.

### virtualenv commands

* deactivate — Exit out of the current Python virtual environment
* workon — List available virtual environments
* workon name_of_environment — Activate the specified Python virtual environment
* rmvirtualenv name_of_environment — Remove the specified environment.

### Creating the Framework
1. Use the django-admin tool to create the project folder, basic file templates, and project management script (manage.py).
2. Use manage.py to create one or more applications.
3. Register the new applications to include them in the project.
4. Hook up the url/path mapper for each application.

### Inside the project folder (not the container)
* *settings.py* contains all the website settings. This is where we register any applications we create, the location of our static files, database configuration details, etc.  

* *urls.py* defines the site url-to-view mappings. While this could contain all the url mapping code, it is more common to delegate some of the mapping to particular applications.

* *wsgi.py* is used to help your Django application communicate with the web server. You can treat this as boilerplate.

### applications
`python3 manage.py startapp <app name>`
* A migrations folder, used to store "migrations" — files that allow you to automatically update your database as you modify your models.

* \__init__.py — an empty file created here so that Django/Python will recognise the folder as a Python Package and allow you to use its objects within other parts of the project.

# Running database migrations
### Using Object Relational Mapper

A django model is the structure of a record in an ORM.

Django is "somewhat opinionated" - its decoupled architecture means that you can usually pick and choose from a number of different options, or add support for completely new ones if desired.

[Django Framework](https://mdn.mozillademos.org/files/13931/basic-django.png)

**EVERY time you update the structure of your underlying data - run the following code:**

```
python3 manage.py makemigrations
python3 manage.py migrate
```
