.. _libraries:
.. highlight:: bash 

.. rst-class:: col-md-12
******************************
Libraries
******************************

To make integrating with the Import API as easy as possible, we've created some client libraries for you to use. Have your own library? Want to contribute to ours? `Reach out to us! <mailto:support@rjmetrics.com>`_

------------

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

For more information, you can see the `documentation for Httpful <http://phphttpclient.com/>`_ or `view the source on Github <https://github.com/RJMetrics/RJMetrics-php>`_.

------------

Ruby
=============================

Installation
-----------------------------

The RJMetrics Ruby client library is available as a gem:

  .. code-block:: bash

    gem install rjmetrics-client

You can also install it via bundler by adding the following line in your `Gemfile`:

  .. code-block:: ruby

    gem 'rjmetrics-client'

Now, you can use the library like this:

  .. code-block:: ruby

    require "rjmetrics-client"
    client = RJMetricsClient.new(client_id, api_key)

    # do stuff with client

For more information, check out the `source code on Github <https://github.com/RJMetrics/RJMetrics-ruby>`_.

------------

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

For more information, check out the `source code on Github <https://github.com/RJMetrics/RJMetrics-js>`_.

------------

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

For more information, check out the `source code on Github <https://github.com/RJMetrics/RJMetrics-clj>`_.

