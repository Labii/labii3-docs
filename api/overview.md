# Overview

Labii helps scientists from biotech and pharmaceutical companies document, manage, and interpret research data with **Electronic Lab Notebook (ELN)** and **Laboratory Information Management System (LIMS)**.

Labii's APIs belong to the Representational State Transfer (REST) category. They allow you to perform `RESTful` operations such as reading, modifying, adding or deleting data.

### API
Each API has a list view and detail view.

|API|Description|List view|Detail view|
|-|-|-|-|
|Organization|The organization object|`/organizations/organization/list/{level}/{sid}/{serializer}/`|`/organizations/organization/detail/{sid}`|
|Organization Member|Member of the organization|`/organizations/organizationmember/list/{level}/{sid}/{serializer}/`|`/organizations/organizationmember/detail/{sid}`|
|Team|Team of the organization|`/organizations/team/list/{level}/{sid}/{serializer}/`|`/organizations/team/detail/{sid}`|
|Organization Widget|Installed widgets|`/organizations/organizationwidget/list/{level}/{sid}/{serializer}/`|`/organizations/organizationwidget/detail/{sid}`|
|Statement|Monthly statement|`/organizations/statement/list/{level}/{sid}/{serializer}/`|`/organizations/statement/detail/{sid}`|
|Project|The project object|`/projects/project/list/{level}/{sid}/{serializer}/`|`/projects/project/detail/{sid}`|
|Project Member|Project member or team|`/projects/projectmember/list/{level}/{sid}/{serializer}/`|`/projects/projectmember/detail/{sid}`|
|Table|The table object|`/tables/table/list/{level}/{sid}/{serializer}/`|`/tables/table/detail/{sid}`|
|Column|The columns of a table|`/tables/column/list/{level}/{sid}/{serializer}/`|`/tables/column/detail/{sid}`|
|Filter|The filters of a table|`/tables/filter/list/{level}/{sid}/{serializer}/`|`/tables/filter/detail/{sid}`|
|Row|The rows of a table|`/tables/row/list/{level}/{sid}/{serializer}/`|`/tables/row/detail/{sid}`|
|Section|The sections of a row|`/tables/section/list/{level}/{sid}/{serializer}/`|`/tables/section/detail/{sid}`|
|Version|The versions of a row|`/tables/version/list/{level}/{sid}/{serializer}/`|`/tables/version/detail/{sid}`|
|Activity|User activities|`/activities/activity/list/{level}/{sid}/{serializer}/`|`/activities/activity/detail/{sid}`|
|Widget|The widget object|`/widgets/widget/list/{level}/{sid}/{serializer}/`|`/widgets/widget/detail/{sid}`|

### Levels

Levels defines the scope of records to retrieve. It is a required parameter for `list` API. These levels are used at Labii:
* **organization**: return the results within the organization level
* **user**: return the results for a particular user
* **project**: return the results for a project

Not all levels are available for all `list` API. Error of `HTTP_406_NOT_ACCEPTABLE` will return if a wrong level is used. The table below lists all allowed levels:

|List API|level=organization|level=user|level=project|
|-|-|-|-|
|Organization List|Yes|Yes|-|
|Organization Member List|Yes|-|-|
|Team List|Yes|Yes|-|
|Organization Widget|Yes|-|-|
|Statement List|Yes|-|-|
|Project List|Yes|Yes|-|
|Project Member List|Yes|-|Yes|
|Table List|Yes|-|-|
|Column List|Yes|-|-|
|Filter List|Yes|Yes|-|
|Row List|Yes|Yes|Yes|
|Section List|Yes|-|-|
|Version List|Yes|-|-|
|Activity|Yes|Yes|-|
|Widget|*|-|-|

### Methods
Here are list of methods used:
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

And 3 roles at the project level:
* **Project Admin**: The administrator of a project
* **Project Edit**: The members has `edit` permission at the project
* **Project View**: The members has `view` permission at the project

|API|GET|POST|PUT|PATCH|DELETE|
|-|-|-|-|-|-|
|Organization List|Admin, Member|Admin|-|-|-|
|Organization Detail|Admin, Member|-|-|Admin|-|
|Organization Member List|Admin, Member|Admin|-|-|-|
|Organization Member Detail|Admin, Member|-|-|Admin|-|
|Team List|Admin, Member|Admin|-|-|-|
|Team Detail|Admin, Member|-|-|Admin|Admin|
|Organization Widget List|Admin, Member|Admin|-|-|Admin|
|Organization Widget Detail|Admin, Member|-|-|-|Admin|
|Statement List|Admin|-|-|-|-|
|Statement Detail|Admin|-|-|-|-|
|Project List|Admin, Project Admin, Project Edit, Project View|Admin|-|-|-|
|Project Detail|Admin, Project Admin, Project Edit, Project View|-|-|Admin, Project Admin|-|
|Project Member List|Admin, Project Admin, Project Edit, Project View|Admin, Project Admin|-|-|-|
|Project Member Detail|Admin, Project Admin, Project Edit, Project View|-|-|Admin, Project Admin|Admin, Project Admin|
|Table List|Admin, Member|Admin|-|-|-|
|Table Detail|Admin, Member|-|-|Admin|-|
|Column List|Admin, Member|Admin|-|-|-|
|Column Detail|Admin, Member|-|-|Admin|-|
|Filter List|Admin, Member|Admin, Member|-|-|-|
|Filter Detail|Admin, Member|-|-|Admin, Member|Admin, Member|
|Row List|Admin, Project Admin, Project Edit, Project View|Project Admin, Project Edit|-|Project Admin, Project Edit|-|
|Row Detail|Admin, Project Admin, Project Edit, Project View|-|-|Project Admin, Project Edit|-|
|Section List|Admin, Project Admin, Project Edit, Project View|Project Admin, Project Edit|-|-|-|
|Section Detail|Admin, Project Admin, Project Edit, Project View|-|-|Project Admin, Project Edit|-|
|Version List|Admin, Project Admin, Project Edit, Project View|-|-|-|-|
|Version Detail|Admin, Project Admin, Project Edit, Project View|-|-|-|-|
|Activity List|Admin, Member|-|-|-|-|
|Activity Detail|-|-|-|-|-|
|Widget List|Admin, Member|-|-|-|-|
|Widget Detail|Admin, Member|-|-|-|-|

### Status Codes

Here is a list of status code used by Labii API:
* **HTTP_200_OK**: return when api call successful
* **HTTP_201_CREATED**: return when a object is created
* **HTTP_204_NO_CONTENT**: return when a object is successfully deleted
* **HTTP_401_UNAUTHORIZED**: return when user is not authenticated
* **HTTP_403_FORBIDDEN**: return when user do not have permission
* **HTTP_406_NOT_ACCEPTABLE**: return when parameter is not correct
* **HTTP_500_INTERNAL_SERVER_ERROR**: return on internal errors
