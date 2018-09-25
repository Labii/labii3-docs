# Overview

## URL

Object has two type of url represent two different views:

* List

  ```text
  {{base_url}}/{app}/{model}/list/{level}/{sid}/{serializer}/
  ```

* View

  ```text
  {{base_url}}/{app}/{model}/detail/{sid}/
  ```

Wheres,

* **base\_url**=[https://api.labii.com/v1/](https://api.labii.com/v1/), the link will change as version changes. 
* **app**, the name of application. See [Link](overview.md#link) for more details.
* **model**, the name of model. See [Link](overview.md#link) for more details.
* **level**, the scope of records to retrieve. See [Levels](overview.md#levels) for more details.
* **sid**, Static and encrypted labii object id. It have to match with level. Of `level=organization`, the `sid` have to be the `sid` of a `organization`.
* **serializer**, scope of fields of the return data
  * **name**, return only `sid` and `name`
  * **list**, return selected fields of the objects
  * **detail**, return all fields of the objects

## Link

Each API has a list `view` and `detail` view.

| API | Description | List view | Detail view |
| :--- | :--- | :--- | :--- |
| Organization | The organization object | `/organizations/organization/list/{level}/{sid}/{serializer}/` | `/organizations/organization/detail/{sid}` |
| Organization Member | Member of the organization | `/organizations/organizationmember/list/{level}/{sid}/{serializer}/` | `/organizations/organizationmember/detail/{sid}` |
| Team | Team of the organization | `/organizations/team/list/{level}/{sid}/{serializer}/` | `/organizations/team/detail/{sid}` |
| Organization Widget | Installed widgets | `/organizations/organizationwidget/list/{level}/{sid}/{serializer}/` | `/organizations/organizationwidget/detail/{sid}` |
| Statement | Monthly statement | `/organizations/statement/list/{level}/{sid}/{serializer}/` | `/organizations/statement/detail/{sid}` |
| Backup | Backup data | `/organizations/backup/list/{level}/{sid}/{serializer}/` | `/organizations/backup/detail/{sid}` |
| Project | The project object | `/projects/project/list/{level}/{sid}/{serializer}/` | `/projects/project/detail/{sid}` |
| Project Member | Project member or team | `/projects/projectmember/list/{level}/{sid}/{serializer}/` | `/projects/projectmember/detail/{sid}` |
| Table | The table object | `/tables/table/list/{level}/{sid}/{serializer}/` | `/tables/table/detail/{sid}` |
| Column | The columns of a table | `/tables/column/list/{level}/{sid}/{serializer}/` | `/tables/column/detail/{sid}` |
| Filter | The filters of a table | `/tables/filter/list/{level}/{sid}/{serializer}/` | `/tables/filter/detail/{sid}` |
| Row | The rows of a table | `/tables/row/list/{level}/{sid}/{serializer}/` | `/tables/row/detail/{sid}` |
| Cell | The cells of a row | `/tables/cell/list/{level}/{sid}/{serializer}/` | `/tables/cell/detail/{sid}` |
| Section | The sections of a row | `/tables/section/list/{level}/{sid}/{serializer}/` | `/tables/section/detail/{sid}` |
| Version | The versions of a row | `/tables/version/list/{level}/{sid}/{serializer}/` | `/tables/version/detail/{sid}` |
| Activity | User activities | `/activities/activity/list/{level}/{sid}/{serializer}/` | `/activities/activity/detail/{sid}` |
| Widget | The widget object | `/widgets/widget/list/{level}/{sid}/{serializer}/` | `/widgets/widget/detail/{sid}` |

## Levels

Levels defines the scope of records to retrieve. It is a required parameter for `list` API. These levels are used at Labii:

* **organization**: return the results within the organization level
* **user**: return the results for a particular user
* **project**: return the results for a project

Not all levels are available for all `list` API. Error of `HTTP_406_NOT_ACCEPTABLE` will return if a wrong level is used. The table below lists all allowed levels:

| List API | level=organization | level=user | level=project |
| :--- | :--- | :--- | :--- |
| Organization List | Yes | Yes | - |
| Organization Member List | Yes | - | - |
| Team List | Yes | Yes | - |
| Organization Widget | Yes | - | - |
| Statement List | Yes | - | - |
| Backup List | Yes | - | - |
| Project List | Yes | Yes | - |
| Project Member List | Yes | - | Yes |
| Table List | Yes | - | - |
| Column List | Yes | - | - |
| Filter List | Yes | Yes | - |
| Row List | Yes | Yes | Yes |
| Cell List | Yes | - | - |
| Section List | Yes | - | - |
| Version List | Yes | - | - |
| Activity | Yes | Yes | - |
| Widget | \* | - | - |

## Methods

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

| API | GET | POST | PUT | PATCH | DELETE |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Organization List | Admin, Member | Admin | - | - | - |
| Organization Detail | Admin, Member | - | - | Admin | - |
| Organization Member List | Admin, Member | Admin | - | - | - |
| Organization Member Detail | Admin, Member | - | - | Admin | - |
| Team List | Admin, Member | Admin | - | - | - |
| Team Detail | Admin, Member | - | - | Admin | Admin |
| Organization Widget List | Admin, Member | Admin | - | - | Admin |
| Organization Widget Detail | Admin, Member | - | - | - | Admin |
| Statement List | Admin | - | - | - | - |
| Statement Detail | Admin | - | - | - | - |
| Backup List | Admin | Admin | - | - | - |
| Backup Detail | Admin | - | - | - | - |
| Project List | Admin, Project Admin, Project Edit, Project View | Admin | - | - | - |
| Project Detail | Admin, Project Admin, Project Edit, Project View | - | - | Admin, Project Admin | - |
| Project Member List | Admin, Project Admin, Project Edit, Project View | Admin, Project Admin | - | - | - |
| Project Member Detail | Admin, Project Admin, Project Edit, Project View | - | - | Admin, Project Admin | Admin, Project Admin |
| Table List | Admin, Member | Admin | - | - | - |
| Table Detail | Admin, Member | - | - | Admin | - |
| Column List | Admin, Member | Admin | - | - | - |
| Column Detail | Admin, Member | - | - | Admin | - |
| Filter List | Admin, Member | Admin, Member | - | - | - |
| Filter Detail | Admin, Member | - | - | Admin, Member | Admin, Member |
| Row List | Admin, Project Admin, Project Edit, Project View | Project Admin, Project Edit | - | Project Admin, Project Edit | - |
| Row Detail | Admin, Project Admin, Project Edit, Project View | - | - | Project Admin, Project Edit | - |
| Cell List | Admin, Project Admin, Project Edit, Project View | Project Admin, Project Edit | - | - | - |
| Cell Detail | - | - | - | Project Admin, Project Edit | - |
| Section List | Admin, Project Admin, Project Edit, Project View | Project Admin, Project Edit | - | - | - |
| Section Detail | Admin, Project Admin, Project Edit, Project View | - | - | Project Admin, Project Edit | - |
| Version List | Admin, Project Admin, Project Edit, Project View | - | - | - | - |
| Version Detail | Admin, Project Admin, Project Edit, Project View | - | - | - | - |
| Activity List | Admin, Member | - | - | - | - |
| Activity Detail | - | - | - | - | - |
| Widget List | Admin, Member | - | - | - | - |
| Widget Detail | Admin, Member | - | - | - | - |

## Status Codes

Here is a list of status code used by Labii API:

* **HTTP\_200\_OK**: return when api call successful
* **HTTP\_201\_CREATED**: return when a object is created
* **HTTP\_204\_NO\_CONTENT**: return when a object is successfully deleted
* **HTTP\_401\_UNAUTHORIZED**: return when user is not authenticated
* **HTTP\_403\_FORBIDDEN**: return when user do not have permission
* **HTTP\_406\_NOT\_ACCEPTABLE**: return when parameter is not correct
* **HTTP\_500\_INTERNAL\_SERVER\_ERROR**: return on internal errors

