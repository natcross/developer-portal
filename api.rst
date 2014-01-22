.. _api:
.. highlight:: bash 

*****************************
API Documentation
*****************************
.. split-pane::

  .. container::

  .. code-box::
    .. code-block:: bash

       Some js code.
       document.write("this is something");
       function() {
        return true;
       }

    .. code-block:: js

       Some js code.
       document.write("this is something");
       function() {
        return true;
       }

    .. code-block:: php

       Some js code.
       document.write("this is something");
       function() {
        return true;
       }

    .. code-block:: ruby

       Some js code.
       document.write("this is something");
       function() {
        return true;
       }       

=============================
Overview
=============================

.. split-pane::
  
  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

  .. code-box::

    .. code-block:: bash

=============================
Authentication
=============================

.. split-pane::

  .. compound::
    Authentication with the Data Import API is done with a single API key and your RJMetrics client id. To request an API key, please contact RJMetrics support at support@rjmetrics.com.

    You can authenticate to the API by providing your API key as a GET parameter on your request.

    .. code-box::

      .. code-block:: bash

        curl -v https://connect.rjmetrics.com/:endpoint?apikey=<apikey>

    Important: This key has write access to your RJMetrics data warehouse. Do not distribute this key to untrusted third parties.

  .. code-box::
    .. code-block:: bash

       Some bash code.
       curl -h http://www.google.com?q=hello+world

    .. code-block:: js

       Some js code.
       document.write("hello world");

    .. code-block:: php

       Some PHP code.
       echo "hello world";

    .. code-block:: ruby

       Some ruby code.
       "hello world"

=============================
Return Codes
=============================

.. split-pane::

  .. compound::

    The Data Import API uses standard HTTP return codes to indicate the status of a request. Your app should handle each of the following return statuses gracefully.

  .. code-box::
    .. code-block:: bash

       Some bash code.
       curl -h http://www.google.com?q=hello+world+2

    .. code-block:: js

       Some js code.
       document.write("hello world 2");

    .. code-block:: php

       Some PHP code.
       echo "hello world 2";

    .. code-block:: ruby

       Some ruby code.
       "hello world 2"

=============================
Sandbox
=============================

.. split-pane::

  .. compound::

    The Data Import API has a full sandbox environment at

    .. code-box::

      .. code-block:: bash
      
        https://sandbox-connect.rjmetrics.com

    The sandbox uses the same keys and return codes as the production API

  .. code-box::
    .. code-block:: bash

       Some bash code.
       curl -h http://www.google.com?q=hello+world+3

    .. code-block:: js

       Some js code.
       document.write("hello world 3");

    .. code-block:: php

       Some PHP code.
       echo "hello world 3";

    .. code-block:: ruby

       Some ruby code.
       "hello world 3"