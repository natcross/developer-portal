.. _api:
.. highlight:: bash 

*****************************
API Documentation
*****************************
.. split-pane::

  .. container::

  .. code-box::

    .. code-block:: bash

    .. code-block:: php

    .. code-block:: ruby

=============================
Overview
=============================

.. split-pane::
  
  .. compound::
    The RJMetrics Data Import API allows you to push arbitrary data into your RJMetrics data warehouse. We built it using REST principles for simplicity.

    This API accepts and returns valid JSON for all its methods. Each method uses a standard HTTP verb (GET/POST/PUT) and uses standard HTTP response codes for returning statuses.

  .. code-box::

    .. code-block:: bash

      curl -v https://connect.rjmetrics.com/

=============================
Authentication
=============================

.. split-pane::

  .. compound::
    Authentication with the Data Import API is done with a single API key and your RJMetrics client id. To request an API key, please contact RJMetrics support at support@rjmetrics.com.

    You can authenticate to the API by providing your API key as a GET parameter on your request.

    **Important**: This key has write access to your RJMetrics data warehouse. Do not distribute this key to untrusted third parties.

  .. code-box::

    .. code-block:: bash

      curl -v https://connect.rjmetrics.com/v2/client/:cid/:endpoint?apikey=:apikey

    .. code-block:: php

      <?php
      $client = new \RJMetrics\Client($clientId, $apiKey);
      if($client->authenticate())
        // connected successfully
      ?>

    .. code-block:: ruby

      client = Client.new(client_id, api_key)
      if client.authenticated?
        # connected successfully

=============================
Return Codes
=============================

.. split-pane::

  .. compound::

    The Data Import API uses standard HTTP return codes to indicate the status of a request. Your app should handle each of the following return statuses gracefully.

    Generally speaking, codes in the 2xx range indicate a successful transaction, codes in the 4xx range indicate a bad request, and codes in the 5xx range indicate an error on our end. If errors in the 5xx range persist, please contact RJMetrics support at support@rjmetrics.com.

  .. code-box::

    .. code-block:: bash

      200 OK - request was successful.
      201 Created - new data was added as a result of the request.
      400 Bad request - Your request was missing a required parameter.
      401 Unauthorized - Authorization failed. Double check your API key.
      404 Not Found - The resource you are looking for does not exist.
      500 Server Error - Something went wrong on RJMetrics' end.

    .. code-block:: php

      200 OK - request was successful.
      201 Created - new data was added as a result of the request.
      400 Bad request - Your request was missing a required parameter.
      401 Unauthorized - Authorization failed. Double check your API key.
      404 Not Found - The resource you are looking for does not exist.
      500 Server Error - Something went wrong on RJMetrics' end.

    .. code-block:: ruby

      200 OK - request was successful.
      201 Created - new data was added as a result of the request.
      400 Bad request - Your request was missing a required parameter.
      401 Unauthorized - Authorization failed. Double check your API key.
      404 Not Found - The resource you are looking for does not exist.
      500 Server Error - Something went wrong on RJMetrics' end.

=============================
Versioning
=============================

.. split-pane::

  .. compound::

    The current version of the Import API is v2.

    v1 is still available, but will be deprecated in the future.

  .. code-block::

    .. code-box:: bash

=============================
Test Environment
=============================

.. split-pane::

  .. compound::

    The Data Import API has a full test (sandbox) environment.

    The sandbox environment uses the same keys and return codes as the production API, but does not persist incoming data. You can use this environment to test your integration.

  .. code-box::

    .. code-block:: bash

      curl -v https://sandbox-connect.rjmetrics.com/v2/client/:cid/:endpoint?apikey=:apikey

    .. code-block:: php

      <?php
      $client->pushData(
        "table_name",
        $test_data,
        \RJMetrics\Client::SANDBOX_BASE
      );
      ?>

    .. code-block:: ruby

      client.pushData(
        "table_name",
        test_data,
        Client::SANDBOX_BASE
      )

=============================
Methods
=============================

Status
-----------------------------

.. split-pane::

  .. compound::

    You can always check the status of the Data Import API.

    This is called when you instantiate the client.

    This will return a ``200 OK`` response if the API is operational.

  .. code-box::

    .. code-block:: bash

      curl -v https://connect.rjmetrics.com

    .. code-block:: php

    .. code-block:: ruby

Upsert
-----------------------------

.. split-pane::

  .. compound::

    The upsert method allows you to push data into your RJMetrics data warehouse. You can push entire arrays of data or single data points. This endpoint will only accept data that have the following properties:

    - The data must be valid JSON;
    - Each data point must contain a ``keys`` field. The ``keys`` field should specify which fields in the records represent the primary key(s);
    - An array of data must contain no more than 100 individual data points.

    **Important**: Each data point in your data warehouse will be uniquely indexed by the fields specified in ``keys``. If a new data point has keys that conflict with a pre-existing data point, the old data point will be replaced.

    **Tables**

    Table in the Data Import API are schemaless. There is no command to create or destroy a table - you can push data to any table name and it will be dynamically generated.

    Here are some guidelines for managing tables:

    - Create one table for each type of data point you are pushing.
    - Generally speaking, each data point pushed into a table should have the same schema.
    - Typically, one type of 'thing' will correspond to one table. For example, a typical eCommerce company might have a 'customer', 'order', 'order_item', and 'product' table.
    - Table names must be alphanumeric (plus underscores). Bad table names will result in a ``400 Bad Request`` return code.

  .. code-box::

    .. code-block:: bash

      curl -X POST -d @filename https://connect.rjmetrics.com/v2/client/:cid/table/:table/data?apikey=:apikey --header "Content-type: application/json"

      :cid - your client id
      :table - table name
      :apikey - your API key

      Example 1: Single data point

      {
        "keys": ["id"],
        "id": 1,
        "email": "joe@schmo.com",
        "status": "pending",
        "created_at": "2012-08-01 14:22:32"
      }

      Example 2: Array of data points

      [{
        "keys": ["id"],
        "id": 1,
        "email": "joe@schmo.com",
        "status": "pending",
        "created_at": "2012-08-01 14:22:32"
      },{
        "keys": ["id"],
        "id": 2,
        "email": "anne@schmo.com",
        "status": "pending",
        "created_at": "2012-08-03 23:12:30"
      },{
        "keys": ["id"],
        "id": 1,
        "email": "joe@schmo.com",
        "status": "complete",
        "created_at": "2012-08-05 04:51:02"
      }]

    .. code-block:: php

      <?php
      $client->pushData(
        "table_name",
        $test_data
      );
      ?>

      Example 1: Single data point

      {
        "keys": ["id"],
        "id": 1,
        "email": "joe@schmo.com",
        "status": "pending",
        "created_at": "2012-08-01 14:22:32"
      }

      Example 2: Array of data points

      [{
        "keys": ["id"],
        "id": 1,
        "email": "joe@schmo.com",
        "status": "pending",
        "created_at": "2012-08-01 14:22:32"
      },{
        "keys": ["id"],
        "id": 2,
        "email": "anne@schmo.com",
        "status": "pending",
        "created_at": "2012-08-03 23:12:30"
      },{
        "keys": ["id"],
        "id": 1,
        "email": "joe@schmo.com",
        "status": "complete",
        "created_at": "2012-08-05 04:51:02"
      }]

    .. code-block:: ruby

      client.pushData(
        "table_name",
        test_data
      )

      Example 1: Single data point

      {
        "keys": ["id"],
        "id": 1,
        "email": "joe@schmo.com",
        "status": "pending",
        "created_at": "2012-08-01 14:22:32"
      }

      Example 2: Array of data points

      [{
        "keys": ["id"],
        "id": 1,
        "email": "joe@schmo.com",
        "status": "pending",
        "created_at": "2012-08-01 14:22:32"
      },{
        "keys": ["id"],
        "id": 2,
        "email": "anne@schmo.com",
        "status": "pending",
        "created_at": "2012-08-03 23:12:30"
      },{
        "keys": ["id"],
        "id": 1,
        "email": "joe@schmo.com",
        "status": "complete",
        "created_at": "2012-08-05 04:51:02"
      }]
