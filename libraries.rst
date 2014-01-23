.. _libraries:
.. highlight:: bash 

******************************
Libraries
******************************

Introduction
=============================

To make integrating with the Import API as easy as possible, we've created some client libraries for you to use. Have your own library? Want to contribute to ours? `Reach out to us! <mailto:support@rjmetrics.com>`_

.. _installing-docdir:

PHP
=============================

Installation
-----------------------------

The RJMetrics PHP client library can be installed using Composer_.

Add the following to your project's ``composer.json``:

.. _Composer: https://getcomposer.org

.. code-box::

  .. code-block:: js
  
    {
      ...
      "repositories": [
        ...
        {"type": "vcs", "url": "https://github.com/RJMetrics/RJMetrics-php"}
      ],
      "require": {
        ...
        "rjmetrics/client": "dev-master"
      }
    }

Now, you can use the library in your script, like this:

.. code-box::

  .. code-block:: php

    <?php

    require 'vendor/autoload.php';

    $client = new \RJMetrics\Client($myClientId, $myApiKey);

    /* do stuff with $client */

    ?>

Usage
-----------------------------

The PHP client has three methods: ``__construct``, ``authenticate``, and ``pushData``.

.. code-box::

  .. code-block:: php

    /**
     * Client::__construct
     *
     * Takes a `clientId` and `apiKey`. If either are invalid, this function will
     * immediately throw an `InvalidArgumentException`. It will then hit the live API to test the
     * given credentials. If that authentication fails, it will throw a `RJMetrics\UnableToConnectException`.
     *
     * Returns itself to enable chaining.
     *
     * @param int $clientId
     * @param string $apiKey
     * @param :optional int $timeoutInSeconds
     * @return object
     */
    public function __construct($clientId, $apiKey, $timeoutInSeconds = 10) { ... }

    /**
     * Client::authenticate
     *
     * This function will run authentication against the live API. Will return true if authentication
     * succeeds, false if it fails.
     *
     * @return boolean
     */
    public function authenticate() { ... }

    /**
     * Client::pushData
     *
     * Given a table name and a valid php object or array, this function will push it to the Import
     * API. If `tableName` or `data` are invalid, this function will throw an `InvalidArgumentException`.
     *
     * Per the Import API spec, it breaks `data` down into chunks of 100 records per request.
     *
     * Returns an array of Httpful response objects.
     *
     * @param string $table
     * @param array/object $data
     * @param :optional string $url
     * @return array
     */
    public function pushData($tableName, $data, $url = self::API_BASE) { ... }

For more information, you can see the `documentation for Httpful <http://phphttpclient.com/>`_ or `view the library source on Github <https://github.com/RJMetrics/RJMetrics-php>`_.



Ruby
=============================

Installation
-----------------------------

The RJMetrics Ruby client library is available as a gem:

.. code-box::

  .. code-block:: bash

    gem install rjmetrics-client

You can also install it via bundler by adding the following line:

.. code-box::

  .. code-block:: ruby

    gem 'rjmetrics-client'

Now, you can use the library like this:

.. code-box::

  .. code-block:: ruby

    require "rjmetrics-client"
    client = RJMetricsClient.new(api_key, client_id);

    # do stuff with client

Usage
----------------------------

The Ruby client has three methods: ``initialize``, ``authenticated?``, and ``pushData``.

.. code-box::

  .. code-block:: ruby
    # Constructs a Client instance if it receives valid arguments or will raise an ArgumentError.
    #
    # @param client_id [Integer] your RJMetrics Client ID
    # @param api_key [String] your RJMetrics API Key
    # @param timeout_in_seconds [Integer] seconds to wait for API responses or nil
    def initialize(client_id, api_key, timeout_in_seconds = 10)

    # Checks if the provided Client ID and API Key are valid credentials by requestin from the RJMetrics API Sandbox.
    def authenticated?


    # Sends data to RJMetrics Data Import API.
    #
    # @param table_name [String] the table name you wish to store the data
    # @param data [Hashamp] or Array of Hashmaps of data points that will get sent
    # @param url [String] Import API url or nil
    # @return [Array] results of each request to RJMetrics Data Import API
    def pushData(table_name, data, url = API_BASE)

For more information, check out the `source code on Github <https://github.com/RJMetrics/RJMetrics-ruby>`_.

