# Build an instant messaging app with Django (and realtime database events) 🌮
realtime database event (in the lightest way, without Django channels) 

I wrote this tutorial to show the simplest way to add fully async Django, including: 

- reading from the Django database in real-time using the new async Django query features 
- a very lightweight setup for async (one pip command to install Daphne). Daphne is fully-integrated into Django. You run 'python manage.py runserver' as usual and it runs Daphne. (Daphne is also very easy to deploy: 2 lines)
- mo extra dependencies. No redis. No extra Django channels installation.
- Fast to do ⏰ I always want to learn things and get going as fast as possible.

Whenever I've looked online in the past for a nice example about adding real-time asynchronous events with Django, the content out there showed length exxamples involving loads of heavy dependencies like Redis. 
Lots of steps. 
Not any more. This is the simplest way to add real-time events to Django 🌮


## 1. Initial Setup and Daphne Integration

### Install Django and Daphne

```bash
pip install django daphne
django-admin startproject core .
python manage.py startapp sim
```

### Add 'daphne' and your app to `INSTALLED_APPS` in `core/settings.py`

```python
# core/settings.py

INSTALLED_APPS = [
    'daphne',
    # ...
    'sim',
    # ...
]

```

### Set `ASGI_APPLICATION` in `core/settings.py`

```python
# core/settings.py

ASGI_APPLICATION = 'core.asgi.application'

```

## 2. Developing Views

### Implement views in `sim/views.py`

```python
[]
```

### Add another view with an asynchronous function for server-sent events (SSE)

```python
```



## 3. URL Configuration

### Add URL patterns in `sim/urls.py` for your views
- Create `sim/urls.py` and add the following::

```python
# sim/urls.py


```

### Update `core/urls.py` to include the app's URLs

```python


```

## 4. Frontend Templates

### Create a `templates` directory in your app

- Create a directory named `templates` in the `sim` directory.

### Develop an HTML template with JavaScript to handle server-sent events

- Create a file named `chat.html` in the `templates` directory.
```html
```

### Add a template lobby to let users choose a name
- Create a file named `lobby.html` in the `templates` directory.
```html
```


## 6. Building the Chat Feature

### Implement chat message models and database setup

```python
# sim/models.py

```

- Run migrations to create the database table for the new model.

```bash
python manage.py makemigrations
python manage.py migrate

```



## Running the Application

### Run the Django app using the Daphne server

```bash
python manage.py runserver
```

You should see something similar to the examples given below. Note that the Daphne server is working:
```bash
Django version 4.2.7, using settings 'core.settings'
Starting ASGI/Daphne version 4.0.0 development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Access the application in a web browser to test SSE functionality

- Visit `http://127.0.0.1:8000/` in your web browser.
- You should see the chat interface, and the page should automatically update with new messages.

### Develop a chat view to handle message sending and receiving

```python
# sim/views.py
@login_required
def chat(request):
    return render(request, 'chat.html')

```

### Update the frontend to include chat interface elements

- Update the `sse.html` template to include the chat interface.
- Add a form to send chat messages and a script to handle form submission and message sending.

```html
[chat.html]
```



## 9. Styling and Interface Design

### Design and style the chat interface for a user-friendly experience

- Update the `chat.html` template to include the chat interface and styling.

```html
```


+ Part 2: Deploy the Django app with server-sent events (realtime chat app, Daphne)