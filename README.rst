proof of concept for breaky breaky
==================================

Based on `this ticket`_, here's a minimal Django project to show the output I'm
(perhaps wrongly) expecting, vs the output I get.

Try it out
----------

- clone this project.
- pip install -r requirements.txt
- python manage.py migrate
- export ALLOWED_HOSTS=... if necessary
- python manage.py runserver

URLs
----

Going to ``/`` will give you two options:

- going to ``/include/`` will render a standard recursive include, and shows
  the output I've been trying to re-create with ``{% reuse %}``
- going to ``/sniplate/`` attempts to do the equivalent thing, but using
  ``{% load_widgets %}`` and ``{% reuse %}``

.. _this ticket: https://github.com/funkybob/django-sniplates/issues/54
