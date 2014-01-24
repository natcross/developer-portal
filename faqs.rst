.. _faqs:
.. highlight:: bash 

******************************
FAQs
******************************

.. _installing-docdir:

General
=============================


What is the Data Import API?
-----------------------------

The Data Import API (or just Import API) provides a simple way for RJMetrics customers to get data from various sources into RJMetrics. Once the data enters the Import API, it will become accessible through the RJMetrics data warehouse, just like a database connection.


What type of data can I send?
-----------------------------

We use it for systems monitoring, CRM analytics, syncing data from Google Drive, and plenty of other purposes.

Our customers use it to report on their helpdesks, shopping carts, ad platforms and more.

If it's not in a database, the Import API is your best bet.


Who *should* use the Import API? Who *shouldn't*?
-------------------------------------------------

Using the Import API requires a certain level of technical expertise. Someone comfortable writing and maintaining a small Ruby or PHP script will be more than qualified.

If the data in question is a medium to large data set (>10M rows), and in a database, it is likely better to set up a direct database connection.


Security
=============================


How secure is the API?
-----------------------------

The API uses SSL which is terminated at the server. From there your data is encrypted using public/private keypairs all the way through to our data warehouse.

Given that, it is best not to send extremely sensitive data, like credit card numbers.


What happens if my API key is compromised?
------------------------------------------

Luckily, nobody can *access* data with your API key, they can only *send* it.

You can always request to disable an API key by `contacting our support team <mailto:support@rjmetrics.com>`_.

PCI
-----------------------------

RJMetrics is PCI level 3 compliant.
