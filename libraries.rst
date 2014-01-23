.. _libraries:
.. highlight:: bash 

******************************
Libraries
******************************

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

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

