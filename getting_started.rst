.. _getting_started:
.. highlight:: bash 

******************************
Getting Started
******************************

Before you begin, you should checkout the "Libraries" section to install your chosen client library.

Here are some quick examples that can get you started with the Import API:

.. _installing-docdir:

Create a Users Table
====================

In your app, you probably have a ``user`` object with some data like ``id``, ``email``, and ``acquisition_source``.

Let's walk through how you would push this data to the Import API.

First, let's lay out a template for pushing the data:

.. code-box::

  .. code-block:: js
  
    var rjmetrics = require("rjmetrics");
    client = new rjmetrics.Client(your-client-id, "your-api-key");

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

  .. code-block:: php

    require 'vendor/autoload.php';
    $client = new RJMetrics\Client($your-client-id, "your-api-key");

    // make sure the client is authenticated before we do anything
    if($client->authenticate()) {
      // this is where we'll push the data
    }

  .. code-block:: clojure

    (ns examples.acquisition-source
      (:require [rjmetrics.core :as rjmetrics]))

    (defn run
      []
      (let [config {:client-id your-client-id :api-key "your-api-key"}]
        (when (rjmetrics/authenticated? config)
          ;; this is where we'll push data
          )))

Next, we want to actually push the data. Let's create a new function to do the dirty work of syncing the new data:

.. code-box::

  .. code-block:: js

    function syncUser(client, user) {
      return client.pushData(
        // table named "users"
        "users",
        {
          // user_id is the unique key here, since each user should only
          // have one record in this table
          "keys": ["id"],
          "id": user.id,
          "email": user.email,
          "acquisition_source": user.acquisition_source
        });
    }

  .. code-block:: php

    function syncUser($client, $user) {
      $dataToPush = new stdClass();
      $dataToPush->id = $user->id;
      $dataToPush->email = $user->email;
      $dataToPush->acquisition_source = $user->acquisitionSource;
      // user_id is the unique key here, since each user should only
      // have one record in this table
      $dataToPush->keys = array("id");

      // table named "users"
      return $client->pushData("users", $dataToPush);
    }

  .. code-block:: clojure

    (defn- sync-user
      [config user]
      (let [result (rjmetrics/push-data config
                                        ;; table named "users"
                                        "users"
                                        ;; user_id is the unique key here, since each user
                                        ;; should only have one record in the table
                                        (assoc user :keys ["id"]))]
        (if (= (-> result first :status) 201)
            (print "Synced user with id" (:id user) "\n")
            (print "Failed to sync user with id" (:id user) "\n"))))

Now we can incorporate this new function into our original script:

.. code-box::

  .. code-block:: js

    var rjmetrics = require("rjmetrics");
    var client = new rjmetrics.Client(your-client-id, "your-api-key");

    function syncUser(client, user) {
      return client.pushData(
        // table named "users"
        "users",
        {
          // user_id is the unique key here, since each user should only
          // have one record in this table
          "keys": ["id"],
          "id": user.id,
          "email": user.email,
          "acquisition_source": user.acquisition_source
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
          syncUser(client, user).then( function(data) {
            console.log("Synced user with id " + user.id);
          }, function(error) {
            console.error("Failed to sync user with id " + user.id);
          })
        });
      }
    }, console.error)

  .. code-block:: php

    require 'vendor/autoload.php';
    $client = new RJMetrics\Client($your-client-id, "your-api-key");

    function syncUser($client, $user) {
      $dataToPush = new stdClass();
      $dataToPush->id = $user->id;
      $dataToPush->email = $user->email;
      $dataToPush->acquisition_source = $user->acquisitionSource;
      // user_id is the unique key here, since each user should only
      // have one record in this table
      $dataToPush->keys = array("id");

      // table named "users"
      return $client->pushData("users", $dataToPush);
    }

    // let's define some fake users
    function fakeUserGenerator($id, $email, $acquisitionSource) {
      $toReturn = new stdClass();

      $toReturn->id = $id;
      $toReturn->email = $email;
      $toReturn->acquisitionSource = $acquisitionSource;

      return $toReturn;
    }

    $users = array(
      fakeUserGenerator(1, "joe@schmo.com", "PPC"),
      fakeUserGenerator(2, "mike@smith.com", "PPC"),
      fakeUserGenerator(3, "lorem@ipsum.com", "Referral"),
      fakeUserGenerator(4, "george@vandelay.com", "Organic"),
      fakeUserGenerator(5, "larry@google.com", "Organic"),
    );

    // make sure the client is authenticated before we do anything
    if($client->authenticate()) {
      // iterate through users and push data
      foreach($users as $user) {
        $responses = syncUser($client, $user);

        // api calls always return an array of responses
        foreach($responses as $response) {
          if($response->code == 201)
            print("Synced user with id {$user->id}\n");
          else
            print("Failed to sync user with id {$user->id}\n");
        }
      }
    }

  .. code-block:: clojure

    (ns examples.acquisition-source
      (:require [rjmetrics.core :as rjmetrics]))

    (defn- sync-user
      [config user]
      (let [result (rjmetrics/push-data config
                                        ;; table named "users"
                                        "users"
                                        ;; user_id is the unique key here, since each user
                                        ;; should only have one record in the table
                                        (assoc user :keys ["id"]))]
        (if (= (-> result first :status) 201)
            (print "Synced user with id" (:id user) "\n")
            (print "Failed to sync user with id" (:id user) "\n"))))

    (defn run
      []
      (let [config {:client-id your-client-id :api-key "your-api-key"}
            ;; let's define some fake users
            users [{:id 1, :email "joe@schmo.com", :acquisition_source "PPC"}
                   {:id 2, :email "mike@smith.com", :acquisition_source "PPC"}
                   {:id 3, :email "lorem@ipsum.com", :acquisition_source "Referral"}
                   {:id 4, :email "george@vandelay.com", :acquisition_source "Organic"}
                   {:id 5, :email "larry@google.com", :acquisition_source "Organic"}]]
        ;; make sure the client is authenticated before we do anything
        (when (rjmetrics/authenticated? config)
          ;; iterate through users and push data
          (dorun (map (partial sync-user config) users)))))

You can run this example with the following command:

.. code-box::

  .. code-block:: js

    npm install
    node users-table.js

  .. code-block:: php

    composer install
    php users-table.php

  .. code-block:: clojure

    lein repl

    > (ns examples.users-table)
    > (require :reload 'examples.users-table)
    > (run)
