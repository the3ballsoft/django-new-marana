django-new-marana
=======================


A Cookiecutter_ template for Django for new marañas. Made for creating landing page and REST apis for mobile and web applications.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Features
---------

* For Python 2.7.x, 3.4.x, 3.5.x 
* For Django 1.8
* Complete Django-Rest-Framework_ integration
* Token_ authentication
* Twitter Bootstrap_ v4.0.0 - alpha_
* Comes with custom user model ready to go.
* Django admin flat-theme_ 
* Simple export_ tables in django admin (xls, json. html).
* Optimized development and production settings
* Easy integration with Webfaction 

.. _alpha: http://blog.getbootstrap.com/2015/08/19/bootstrap-4-alpha/
.. _Django-Rest-Framework: http://www.django-rest-framework.org/
.. _Token: http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
.. _flat_theme: https://pypi.python.org/pypi/django-flat-theme
.. _export: https://github.com/burke-software/django-admin-export
.. _Bootstrap: https://github.com/twbs/bootstrap
.. _django-avatar: https://github.com/jezdez/django-avatar/


Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get cookiecutter. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/the3ballsoft/django-new-marana.git

You'll be prompted for some questions, answer them, then it will create a Django project for you.


**Warning**: After this point, change 'Genesis Guerrero', 'the3ballsoft@gmail.com', etc to your own information.

It prompts you for questions. Answer them::

    Cloning into 'django-new-marana'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    github_repository_name [project_name]: reddit_clone
    app_name [repo_name]: reddit
    author_name [Your Name]: Antinogeno Martinez
    email [Your email]: antinogeno@yahoo.es
    description [A short description of the project.]: A reddit clone.
    github_username  The owner of the repository. Either your github username or organization name.]: antinogeno12


Enter the project and take a look around::

    $ cd reddit/
    $ ls

Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:the3ballsoft/redditclone.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?


For Readers of Two Scoops of Django 1.8
--------------------------------------------

You may notice that some elements of this project do not exactly match what we describe in chapter 3. The reason for that is this project, amongst other things, serves as a test bed for trying out new ideas and concepts. Sometimes they work, sometimes they don't, but the end result is that it won't necessarily match precisely what is described in the book I co-authored.


Contributing
--------------------------------------------

Want a new feature or find a bug? Submit a Pull Request!
