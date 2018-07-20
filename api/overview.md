# Overview

### API
Each API has a list view and detail view.

|API|Description|List view|Detail view|
|-|-|-|-|
|Organization|The organization object|`/organizations/organization/list/{level}/{sid}/{serializer}/`|`/organizations/organization/detail/{sid}`|
|Organization Member|Member of the organization|`/organizations/organizationmember/list/{level}/{sid}/{serializer}/`|`/organizations/organizationmember/detail/{sid}`|
|Team|Team of the organization|`/organizations/team/list/{level}/{sid}/{serializer}/`|`/organizations/team/detail/{sid}`|
|Organization Widget|Installed widgets|`/organizations/organizationwidget/list/{level}/{sid}/{serializer}/`|`/organizations/organizationwidget/detail/{sid}`|
|Statement|Monthly statement|`/organizations/statement/list/{level}/{sid}/{serializer}/`|`/organizations/statement/detail/{sid}`|

### Levels

Levels defines the scope of records to retrieve. It is a required parameter for `list` API. These levels are used at Labii:
* **organization**: return the results within the organization level
* **user**: return the results for a particular user

Not all levels are available for all `list` API. Error of `HTTP_406_NOT_ACCEPTABLE` will return if a wrong level is used. The table below lists all allowed levels:

|List API|level=organization|level=user|
|-|-|-|
|Organization List|Yes|Yes|
|Organization Member List|Yes|-|
|Team List|Yes|Yes|
|Organization Widget|Yes|-|
|Statement List|Yes|-|

### Methods
Labii's APIs belong to the Representational State Transfer (REST) category. They allow you to perform `RESTful` operations such as reading, modifying, adding or deleting data. Here are list of methods used:
* **GET**: Fetch one or more objects
* **POST**: Create an object
* **PUT**: Update an object
* **PATCH**: Partially update an object
* **DELETE**: Remove an object


Different roles have different permissions in using the methods. There are five roles at the organization level:
* **Admin**: The administrators
* **Member**: The members of the organization
* **Alumni**: The members who have left the organization
* **User**: Other Labii users who do not belong to the organization
* **Anonymous**: Unauthorized user

|API|GET|POST|PUT|PATCH|DELETE|
|-|-|-|-|-|-|
|Organization List|Admin, Member|Admin||||
|Organization Detail|Admin, Member|||Admin||
|Organization Member List|Admin, Member|Admin||||
|Organization Member Detail|Admin, Member|||Admin||
|Team List|Admin, Member|Admin||||
|Team Detail|Admin, Member|||Admin|Admin|
|Organization Widget List|Admin, Member|Admin||||
|Organization Widget Detail|Admin, Member||||Admin|
|Statement List|Admin|||||
|Statement Detail|Admin|||||

### Status Codes

Here is a list of status code used by Labii API:
* **HTTP_200_OK**: return when api call successful
* **HTTP_201_CREATED**: return when a object is created
* **HTTP_204_NO_CONTENT**: return when a object is successfully deleted
* **HTTP_401_UNAUTHORIZED**: return when user is not authenticated
* **HTTP_403_FORBIDDEN**: return when user do not have permission
* **HTTP_406_NOT_ACCEPTABLE**: return when parameter is not correct
* **HTTP_500_INTERNAL_SERVER_ERROR**: return on internal errors
