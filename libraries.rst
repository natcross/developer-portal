.. _libraries:
.. highlight:: bash 

******************************
Libraries
******************************

Introduction
=============================

To make integrating with the Import API as easy as possible, we've created some client libraries for you to use. Have your own library? Want to contribute to ours? `Reach out to us! <mailto:support@rjmetrics.com>`_


PHP
=============================

Installation
-----------------------------

The RJMetrics PHP client library can be installed using Composer_.

Add the following to your project's ``composer.json``:

.. _Composer: https://getcomposer.org

  .. code-block:: js

    {
      "require": {
        ...
        "rjmetrics/rjmetrics-client": "0.1.1"
      }
    }

Now, you can use the library in your script, like this:

  .. code-block:: php

    <?php

    require 'vendor/autoload.php';
    $client = new RJMetrics\Client($myClientId, $myApiKey);

    /* do stuff with $client */

    ?>

Usage
-----------------------------

The PHP client has three methods: ``__construct``, ``authenticate``, and ``pushData``.

  .. php:method:: __construct($clientId, $apiKey, $timeoutInSeconds = 10)

      Takes a `clientId` and `apiKey`. If either are invalid, this function will immediately throw an `InvalidArgumentException`. It will then hit the live API to test the given credentials. If that authentication fails, it will throw a `RJMetrics\UnableToConnectException`.

      :param int $clientId: The client ID
      :param string $apiKey: The API Key
      :param int $timeoutInSeconds: The timeout in seconds. Defaults to 10 seconds
      :returns: object

  .. php:method:: authenticate()

      This function will run authentication against the live API. Will return true if authentication succeeds, false if it fails.

      :returns: true if authentication succeeds, false if it fails

  .. php:method:: pushData($tableName, $data, $url = self::API_BASE)

      Given a table name and a valid php object or array, this function will push it to the Import API. If `tableName` or `data` are invalid, this function will throw an `InvalidArgumentException`.

      Per the Import API spec, it breaks `data` down into chunks of 100 records per request.

      :param string $table:
      :param array/object $data:
      :param string $url: optional
      :returns: an array of Httpful response objects.

For more information, you can see the `documentation for Httpful <http://phphttpclient.com/>`_ or `view the source on Github <https://github.com/RJMetrics/RJMetrics-php>`_.



Ruby
=============================

Installation
-----------------------------

The RJMetrics Ruby client library is available as a gem:

  .. code-block:: bash

    gem install rjmetrics-client

You can also install it via bundler by adding the following line:

  .. code-block:: ruby

    gem 'rjmetrics-client'

Now, you can use the library like this:

  .. code-block:: ruby

    require "rjmetrics-client/client"
    client = Client.new(client_id, api_key)

    # do stuff with client

Usage
----------------------------

The Ruby client has three methods: ``initialize``, ``authenticated?``, and ``pushData``.
    
  .. rb:method:: initialize(client_id, api_key, timeout_in_seconds = 10)

      Constructs a Client instance if it receives valid arguments or will raise an ArgumentError.

      :client_id: [Integer] your RJMetrics Client ID
      :api_key: [String] your RJMetrics API Key
      :timeout_in_seconds: [Integer] seconds to wait for API responses or nil

  .. rb:method:: pushData(table_name, data, url = API_BASE)

      Sends data to RJMetrics Data Import API.

      :table_name: [String] the table name you wish to store the data
      :data: [Hashamp] or Array of Hashmaps of data points that will get sent
      :url: [String] Import API url or nil
      :returns: [Array] results of each request to RJMetrics Data Import API     

For more information, check out the `source code on Github <https://github.com/RJMetrics/RJMetrics-ruby>`_.

Javascript
=============================

Installation
-----------------------------

The RJMetrics Javascript client library is available as a gem:

  .. code-block:: bash

    npm install rjmetrics

You can also install it via npm by adding the following line to the dependencies field in your ``package.json`` file:

  .. code-block:: js

    "rjmetrics": "0.1.1"

Now, you can use the library like this:

  .. code-block:: js

    var rjmetrics = require("rjmetrics");
    client = rjmetrics.Client(api_key, client_id);

    # do stuff with client

For more information, check out the `source code on Github <https://github.com/RJMetrics/RJMetrics-ruby>`_.

Clojure
=============================

Installation
-----------------------------

You can install the RJMetrics Clojure client library by adding the following dependency to your ``project.clj``.

  .. code-block:: clojure

    [rjmetrics "0.1.0"]

Now, you can use the library like this:

  .. code-block:: clojure

    (ns example
      (:require [rjmetrics.core :as rjmetrics]))

    (def config-map {:client-id 1
                      :api-key "your-api-key"})

    (when (rjmetrics/authenticated? config-map)
      ;; do stuff with client
      )

