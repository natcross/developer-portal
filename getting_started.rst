.. _getting_started:
.. highlight:: bash 

******************************
Getting Started
******************************

Before you begin, you should checkout the "Libraries" section to install your chosen client library.

Here are some quick examples that can get you started with the Import API:

.. _installing-docdir:

Add acquisition source to your users table
==========================================

Let's start with a common use case: you have a ``users`` table with some standard information, like ``user_id``, ``email``, and ``created_date``.

Now you have some extra data, and you want to add an extra field to your ``users`` table: ``acquisition_source``.

First, let's lay out a template for pushing the extra data:

.. code-box::

  .. code-block:: js
  
    var rjmetrics = require("rjmetrics");
    client = new rjmetrics.Client("your-client-id", "your-api-key");

    // make sure the client is authenticated before we do anything
    client.authenticate().then( function(data) {
      // check the response for errors
      var hasErrors = false;

      // `authenticate` and `pushData` always return an array of results
      data.forEach( function(el) {
        // 201 is a successful push or authenticate. anything else is an error.
        if(el.code != 201) {
          hasErrors = true;
          console.error("Failed to authenticate: " + el.body.reasons);
        }
      });

      if(!hasErrors) {
        // this is where we'll push the data
      }
    }, console.error)

Next, we want to actually push the data. Since we'll want to correlate this data with our ``users`` table in the RJMetrics data warehouse, we'll need a foreign key: ``user_id``. We'll also push a new field, ``acquisition_source``. We'll push these to a table called ``users_acquisition_source``.

Let's create a new function to do the dirty work of syncing the new data:

.. code-box::

  .. code-block:: js

    function syncAcquisitionSources(client, user_id, acquisition_source) {
      return client.pushData(
        // table named "users_acquisition_source"
        "users_acquisition_source",
        {
          // user_id is the unique key here. there should only be one
          // record per client id.
          "keys": ["user_id"],
          "user_id": user_id,
          "acquisition_source": acquisition_source
        });
    }

Now we can incorporate this new function into our original script:

.. code-box::

  .. code-block:: js

    var rjmetrics = require("rjmetrics");
    var client = new rjmetrics.Client("your-client-id", "your-api-key");

    function syncAcquisitionSources(client, user_id, acquisition_source) {
      return client.pushData(
        // table named "users_acquisition_source"
        "users_acquisition_source",
        {
          // user_id is the unique key here, since each user should only
          // have one record in this table
          "keys": ["user_id"],
          "user_id": user_id,
          "acquisition_source": acquisition_source
        });
    }

    // let's define some fake users
    var users = [
      {id: 1, email: "joe@schmo.com", acquisition_source: "PPC"},
      {id: 2, email: "mike@smith.com", acquisition_source: "PPC"},
      {id: 3, email: "lorem@ipsum.com", acquisition_source: "Referral"},
      {id: 4, email: "george@vandelay.com", acquisition_source: "Organic"},
      {id: 5, email: "larry@google.com", acquisition_source: "Organic"},
    ];

    // make sure the client is authenticated before we do anything
    client.authenticate().then( function(data) {
      // check the response for errors
      var hasErrors = false;

      // `authenticate` and `pushData` always return an array of results
      data.forEach( function(el) {
        // 201 is a successful push or authenticate. anything else is an error.
        if(el.code != 201) {
          hasErrors = true;
          console.error("Failed to authenticate: " + el.body.reasons);
        }
      });

      if(!hasErrors) {
        // iterate through users and push data
        users.forEach( function(user) {
          syncAcquisitionSources(client, user.id, user.acquisition_source).then( function(data) {
            console.log("Synced user with id " + user.id);
          }, function(error) {
            console.error("Failed to sync user with id " + user.id);
          })
        });
      }
    }, console.error)

2. Step 2 Title
=============================

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum 


.. code-box::

  .. code-block:: bash
  
    curl -v https://connect.rjmetrics.com/:endpoint?apikey=<apikey>

  .. code-block:: js

     document.write("hello world!");
     function(input) {
      return input;
     }

  .. code-block:: php

    <?php
     echo "Hello World!";
     function($input) {
      return $input;
     }
    ?>

  .. code-block:: ruby

     Some Ruby code.

