.. _getting_started:
.. highlight:: bash 

******************************
Getting Started
******************************

Before you begin, you should checkout the :doc:`libraries` section to install your chosen client library.

Here are some quick examples that can get you started with the Import API

.. _installing-docdir:

Create a Users Table
====================

Your most important table in RJMetrics is your Users table. In your app, you probably have a ``user`` object with some data like ``id``, ``email``, and ``acquisition_source``.

Let's walk through how you would push this data to the Import API.

First, let's lay out a template for pushing the data. We'll make sure the client is :ref:`authenticated <api-authentication>` and prepare to push the data to the Import API.

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

Next, we want to actually push the data. Let's create a new function to do the dirty work of syncing the new data. Check out the :ref:`upsert documentation <api-upsert>` to learn about the specifics on data that can be pushed to the API.

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

Putting it all together, we incorporate the `syncUser` function into our original script.

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

This example is included with the :doc:`client libraries <libraries>` or can be `downloaded from github <http://www.github.com/rjmetrics>`_.

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


Create an Orders Table
======================

Now, let's create an orders table with the following fields: ``id``, ``user_id``, ``value`` and ``sku``.

We'll need a new function to push the order object:

.. code-box::

  .. code-block:: js

    function syncOrder(client, order) {
      return client.pushData(
        "orders",
        {
          "keys": ["id"],
          "id": order.id,
          "user_id": order.user_id,
          "value": order.value,
          "sku": order.sku
        });
    }

  .. code-block:: php

    function syncOrder($client, $order) {
      $dataToPush = new stdClass();
      $dataToPush->id = $order->id;
      $dataToPush->user_id = $order->user_id;
      $dataToPush->value = $order->value;
      $dataToPush->sku = $order->sku;
      $dataToPush->keys = array("id");

      return $client->pushData("orders", $dataToPush);
    }

  .. code-block:: clojure

    (defn- sync-order
      [config order]
      (let [result (rjmetrics/push-data config
                                        "orders"
                                        (assoc order :keys ["id"]))]
        (if (= (-> result first :status) 201)
            (print "Synced order with id" (:id order) "\n")
            (print "Failed to sync orfer with id" (:id order) "\n"))))

Now, we can plug this into the same template from the users table:

.. code-box::

  .. code-block:: js

    var rjmetrics = require("rjmetrics");
    var client = new rjmetrics.Client(your-client-id, "your-api-key");

    function syncOrder(client, order) {
      return client.pushData(
        "orders",
        {
          "keys": ["id"],
          "id": order.id,
          "user_id": order.user_id,
          "value": order.value,
          "sku": order.sku
        });
    }

    var orders = [
      {"id": 1, "user_id": 1, "value": 58.40,  "sku": "milky-white-suede-shoes"},
      {"id": 2, "user_id": 1, "value": 23.99,  "sku": "red-button-down-fleece"},
      {"id": 3, "user_id": 2, "value": 5.00,   "sku": "bottle-o-bubbles"},
      {"id": 4, "user_id": 3, "value": 120.01, "sku": "zebra-striped-game-boy"},
      {"id": 5, "user_id": 5, "value": 9.90  , "sku": "kitten-mittons"}
    ];

    client.authenticate().then( function(data) {
      var hasErrors = false;

      data.forEach( function(el) {
        if(el.code != 201) {
          hasErrors = true;
          console.error("Failed to authenticate: " + el.body.reasons);
        }
      });

      if(!hasErrors) {
        orders.forEach( function(order) {
          syncOrder(client, order).then( function(data) {
            console.log("Synced order with id " + order.id);
          }, function(error) {
            console.error("Failed to sync order with id " + order.id);
          })
        });
      }
    }, console.error)

  .. code-block:: php

    require 'vendor/autoload.php';
    $client = new RJMetrics\Client($your-client-id, "your-api-key");

    function syncOrder($client, $order) {
      $dataToPush = new stdClass();
      $dataToPush->id = $order->id;
      $dataToPush->user_id = $order->user_id;
      $dataToPush->value = $order->value;
      $dataToPush->sku = $order->sku;
      $dataToPush->keys = array("id");

      return $client->pushData("orders", $dataToPush);
    }

    function fakeOrderGenerator($id, $userId, $value, $sku) {
      $toReturn = new stdClass();

      $toReturn->id = $id;
      $toReturn->user_id = $userId;
      $toReturn->value = $value;
      $toReturn->sku = $sku;

      return $toReturn;
    }

    $orders = array(
      fakeOrderGenerator(1, 1, 58.40, "milky-white-suede-shoes"),
      fakeOrderGenerator(2, 1, 23.99, "red-buttons-down-fleece"),
      fakeOrderGenerator(3, 2, 5.00, "bottle-o-bubbles"),
      fakeOrderGenerator(4, 3, 120.01, "zebra-striped-game-boy"),
      fakeOrderGenerator(5, 5, 9.90, "kitten-mittons")
    );

    if($client->authenticate()) {
      foreach($orders as $order) {
        $responses = syncOrder($client, $order);

        foreach($responses as $response) {
          if($response->code == 201)
            print("Synced order with id {$order->id}\n");
          else
            print("Failed to sync order with id {$order->id}\n");
        }
      }
    }

  .. code-block:: clojure

    (ns examples.orders-table
      (:require [rjmetrics.core :as rjmetrics]))

    (defn- sync-order
      [config order]
      (let [result (rjmetrics/push-data config
                                        "orders"
                                        (assoc order :keys ["id"]))]
        (if (= (-> result first :status) 201)
            (print "Synced order with id" (:id order) "\n")
            (print "Failed to sync orfer with id" (:id order) "\n"))))

    (defn run
      []
      (let [config {:client-id your-client-id :api-key "your-api-key"}
            orders [{:id 1, :user_id 1 :value 58.40  :sku "milky-white-suede-shoes"}
                    {:id 2, :user_id 1 :value 23.99  :sku "red-button-down-fleece"}
                    {:id 3, :user_id 2 :value 5.00   :sku "bottle-o-bubbles"}
                    {:id 4, :user_id 3 :value 120.01 :sku "zebra-striped-game-boy"}
                    {:id 5, :user_id 5 :value 9.90   :sku "kitten-mittons"}]]
        (when (rjmetrics/authenticated? config)
          (dorun (map (partial sync-order config) users)))))
