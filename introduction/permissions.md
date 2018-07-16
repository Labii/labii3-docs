# Permissions

Labii use object-based permissions, each user shall has different permission toward one same object.

## Types:

Labii use the following permissions to control the methods:

| PERMISSION | DESCRIPTION |
| :--- | :--- |
| view\_organization | Is the user has permission to view all data belong to this organization. |
| change\_organization | Is the user can: change Organization settings, add/change Organization Members, add/change Organization Teams, add/change Projects, add/change Tables, active Widgets, add/change records. |
| edit\_organization | Is the user can create the records for the Organization. Mostly it is the Table data. |
| view\_project | Is the user has permission to view all record belong to this project. |
| change\_project | Is the user can: change Project settings, add/change members/teams to the project, add/change records. |

## Allowed Methods:

Different permission is allowed for different methods and urls. Here is the summary:

| Level | URL | Get | Post | Put | Patch | Delete |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| organization | List | view\_organization | - | - | - | - |
| organization | Detail | view\_organization | - | - | change\_organization | - |
| parent=organization | List | view\_organization | change\_organization | - | - | - |
| parent=organization | Detail | view\_organization | - | - | change\_organization | - |
| project | List | view\_project | change\_organization | - | - | - |
| project | Detail | view\_project | - | - | change\_project | - |
| parent=project | List | view\_project | change\_row | - | change\_row | - |
| parent=project | Detail | view\_project | - | - | change\_row | - |

* parent=organization, refer to the table has organization as a foreign key.
* parent=project, refer to the table has project as a foreign key.

