.. _extending:

Extending Social
================

Social has a pretty modular design.  Each type of social network account is
represented by a subclass of the ``social.accounts.Account`` class.  The main
loop is an implementation of a breadth first search: the nodes are Accounts, and
the edges are returned by these accounts.

Essentially, each ``Account`` implements three functions which directly
contribute to the search.

- First, a static method ``match()``, which takes something I refer to as
  breadcrumbs.  The breadcrumbs are essentially things that may lead to a new
  social networking account - URL, email, and username.  More on that later.
  Essentially, this function should return a truthy value if the breadcrumbs
  match an account in this social network.
- Second, a constructor that accepts the same breadcrumbs as ``match()``.
  This creates an ``Account`` instance that corresponds to whatever social
  network account matched in ``match()``.
- Finally, an ``expand()`` instance method, which takes an info object and
  returns an iterable of breadcrumbs.  This function visits the social
  networking account and returns all possible hints to other social networking
  accounts.  It also updates the info object with more info about the person.

So, with this functionality, you can see how the basic algorithm works:

.. code::

   while queue is not empty:
       get an Account from the queue
       expand it
       for each resulting breadcrumb:
           if any account type matches:
               create an instance of it and add it to the queue

Breadcrumbs objects
-------------------

The ``match()`` and ``__init__()`` functions of ``Accounts`` both take something
I refer to as breadcrumbs.  These are just standard keyword arguments that
should be used whenever breadcrumbs are expected.  More commonly, they are just
splatted dictionaries.  Here are the current keyword arguments expected whenever
"breadcrumbs" are expected:

- ``url``: This is usually what's expected and returned.  Essentially, a URL may
  be to another social network profile, or a personal website.
- ``email``: Maybe you can search for a profile using an email address.
- ``username``: This one is a bit less reliable, so it should *not* be matched
  against, only used in the constructor.

Info objects
------------

In addition, the ``expand()`` function is passed a parameter named ``info``.
This is a dictionary-like object that should be consulted if any additional
information (like a person's name) is needed.  It's not quite like an ordinary
dictionary though.

.. code:: python

          info['emails'] = 'example@example.com'

The above sample code will add the email to a set containing all emails found so
far (instead of overwriting an existing email).  When you access a property and
it exists, it will always return back a set of values instead of just a single
value.

- ``usernames``: should map to the set of usernames we've seen this person use
  thus far in the search.
- ``emails``: self explanatory
- ``fullname``: should map to the person's full name, or None.
- ``city``: the person's city
- ``state``: the person's state or province
- ``country``: the person's country
- ``phones``: a set of phone numbers (as strings)

Your code should not assume that any of these keys exist.  Create them if they
do not exist, but make sure they are as documented here.  Any key you would like
to set, but already exists, you may want to instead add your value to a list in
``key-others``.  For example, if you have a fullname that differs from the one
already there, add it to a list in the key ``fullname-others``.

I'll probably make a class to abstract away all these details soon.

Full ``Account`` Class Documentation
------------------------------------

.. autoclass:: social.accounts.Account
   :members:
   :special-members:
   :exclude-members: __weakref__
