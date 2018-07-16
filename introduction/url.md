---
base_url: 'https://www.labii.com'
---

# URL

Labii API is mostly interact with URLs, this section introduce the rules to constructor the URL.

## Types:

Labii API contains two types of url, list view and details view.

* **List view:** provide a list of items. 

  `{{base_url}}/api/v1/[app]/[table]/list/[level]/[sid]/[serializer]/`

* **Detail view:** provide the detail of a item.

  `{{base_url}}/api/v1/[app]/[table]/detail/[sid]/`

## A**pp:**

The applications, see [Apps and Tables](apps-and-tables.md)

## T**able:**

The table of the application, see [Apps and Tables](apps-and-tables.md)

## Level:

At which level to grab the data. It needs to work together with [sid](url.md#sid)

* **user**, get a list of objects for the provided user
* **organization**, get a list of objects for the provided organization 
* **project**, get a list of objects for the project
* **table**, get a list of objects for the table

> Note: Not all levels were allowed for all methods.

## SID:

The encrypted id of the object.

## Serializer:

The serializer controls how much data to display. Use the correct serializer can speed up queries.

* **name**, displays sid and name only. Fastest.
* **list**, displays some basic columns. 
* **detail**, displays all relevant details. Slowest.

