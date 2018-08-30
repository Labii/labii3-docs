# Table

{% api-method method="get" host="{{ base\_url }}" path=" /tables/table/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Table List
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="level" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="sid" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="serializer" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="token" type="string" required=true %}

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
    "page_count": 1,
    "count": 9,
    "next": null,
    "previous": null,
    "add_permission": true,
    "results": [
        {
            "sid": "xxx",
            "icon": "xxx",
            "name_singular": "experiment",
            "name_plural": "experiments",
            "unique_code": "EP",
            "table_type": "Document",
            "order": 1,
            "is_archived": false,
            "change_permission": true
        },
        ...
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

{% api-method-response-example httpCode=406 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
Wrong id - the provided sid is not correct
Wrong level - the provided level is not acceptable
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="{{ base\_url }}" path=" /tables/table/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Table List
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="level" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="sid" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="serializer" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="token" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-headers %}

{% api-method-form-data-parameters %}
{% api-method-parameter name="name\_singular" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="name\_plural" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="description" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="unique\_code" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="icon" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="table\_type" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="is\_archived" type="boolean" required=false %}

{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=201 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "sid": "ilor0a40x5kpuzEJOT",
    "organization": 1,
    "icon": "assignment",
    "name_singular": "experiment",
    "name_plural": "experiments",
    "name_system": null,
    "description": "An experiment is the lab note to document procedures carried out to support, refute, or validate a hypothesis.",
    "unique_code": "EP",
    "table_type": "Document",
    "order": 1,
    "is_archived": false,
    "updated_by": 1,
    "date_updated": "2018-02-06T03:22:28.120102Z",
    "date_created": "2017-09-24T00:04:56.455176Z",
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
Wrong level - the provided level is not acceptable
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="{{ base\_url }}" path=" /tables/table/detail/{sid}/" %}
{% api-method-summary %}
Table Detail
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="sid" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="token" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "sid": "ilor0a40x5kpuzEJOT",
    "organization": 1,
    "icon": "assignment",
    "name_singular": "experiment",
    "name_plural": "experiments",
    "name_system": null,
    "description": "An experiment is the lab note to document procedures carried out to support, refute, or validate a hypothesis.",
    "unique_code": "EP",
    "table_type": "Document",
    "order": 1,
    "is_archived": false,
    "updated_by": 1,
    "date_updated": "2018-02-06T03:22:28.120102Z",
    "date_created": "2017-09-24T00:04:56.455176Z",
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
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="patch" host="{{ base\_url }}" path=" /tables/table/detail/{sid}/" %}
{% api-method-summary %}
Table Detail
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="sid" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="token" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-headers %}

{% api-method-form-data-parameters %}
{% api-method-parameter name="name\_singular" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="name\_plural" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="description" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="unique\_code" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="icon" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="order" type="number" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="table\_type" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="is\_archived" type="boolean" required=false %}

{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "sid": "ilor0a40x5kpuzEJOT",
    "organization": 1,
    "icon": "assignment",
    "name_singular": "experiment",
    "name_plural": "experiments",
    "name_system": null,
    "description": "An experiment is the lab note to document procedures carried out to support, refute, or validate a hypothesis.",
    "unique_code": "EP",
    "table_type": "Document",
    "order": 1,
    "is_archived": false,
    "updated_by": 1,
    "date_updated": "2018-02-06T03:22:28.120102Z",
    "date_created": "2017-09-24T00:04:56.455176Z",
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
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}



