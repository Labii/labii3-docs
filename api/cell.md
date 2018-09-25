---
description: Create or update the data of a cell.
---

# Cell

{% api-method method="get" host="" path=" /tables/cell/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Cell List
{% endapi-method-summary %}

{% api-method-description %}
Get the cell objects for a certain condition. Currently, the API is used to get the cost status of specific Column Widgets.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="level" type="string" required=true %}
level=organization
{% endapi-method-parameter %}

{% api-method-parameter name="sid" type="string" required=true %}
sid=organization sid
{% endapi-method-parameter %}

{% api-method-parameter name="serializer" type="string" required=true %}
choose of \[name, list, detail\]
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="token" type="string" required=true %}
the authentication token
{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "page_size": 10,
    "page_number": 1,
    "page_count": 17,
    "count": 162,
    "next": "...",
    "previous": null,
    "add_permission": false,
    "results": [
        {
            "sid": "yBEH0a40x76ffAFKPUZ50",
            "widget": "Text",
            "record": "FL154: widgets-backlink-view  1.png",
            "change_permission": true
        },
    ]
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=401 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
Authentication credentials were not provided.
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=403 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
You do not have permission to perform this action.
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="" path=" /tables/cell/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Cell List
{% endapi-method-summary %}

{% api-method-description %}
Create a new cell for a row.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="level" type="string" required=true %}
level=organization
{% endapi-method-parameter %}

{% api-method-parameter name="sid" type="string" required=true %}
sid=organization sid
{% endapi-method-parameter %}

{% api-method-parameter name="serializer" type="string" required=true %}
choose of \[name, list, detail\]
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="token" type="string" required=true %}
the authentication token
{% endapi-method-parameter %}
{% endapi-method-headers %}

{% api-method-query-parameters %}
{% api-method-parameter name="row\_\_sid" type="string" required=true %}
the sid of the row
{% endapi-method-parameter %}
{% endapi-method-query-parameters %}

{% api-method-body-parameters %}
{% api-method-parameter name="{xxx: xxx}" type="object" required=false %}
Have to be {column sid: value}
{% endapi-method-parameter %}
{% endapi-method-body-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=201 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "sid": "369b0a40x29f50ejotyD"
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=401 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
Authentication credentials were not provided.
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=403 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
You do not have permission to perform this action.
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=406 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
Wrong id - the provided sid is not correct
Wrong level - the provided level is not acceptable
Missing row__sid in the post link.
Your organization does not have enough credits, contact sales@labii.com!
Wrong id: organization sid (xxx) does not match to row sid (xxx)
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="patch" host="" path=" /tables/cell/detail/{sid}/" %}
{% api-method-summary %}
Cell Detail
{% endapi-method-summary %}

{% api-method-description %}
Update the content of a cell.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="sid" type="string" required=true %}
cell sid
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="token" type="string" required=true %}
the authentication token
{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "sid": "yBEH0a40x76ffAFKPUZ50",
    "date_updated": "2018-09-25T01:53:04.673228Z",
    "date_created": "2018-09-25T01:53:04.664391Z",
    "change_permission": true
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=401 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
Authentication credentials were not provided.
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=403 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
You do not have permission to perform this action.
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=406 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
Wrong id - the provided sid is not correct
Your organization does not have enough credits, contact sales@labii.com!
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}



