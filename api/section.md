---
description: >-
  Sections are the module of document. Use section to insert different type of
  data. A section holds the data for a widget for one particular record.
---

# Section

{% api-method method="get" host="{{ base\_url }}" path=" /tables/section/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Section List
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
    "page_count": 5,
    "count": 1,
    "next": null,
    "previous": null,
    "add_permission": true,
    "results": [
        {
            "sid": "xxx",
            "name": "Double Signature",
            "widget___widget__sid": "xxx",
            "description": "",
            "is_archived": false,
            "order": 1,
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

{% api-method method="post" host="{{ base\_url }}" path=" /tables/section/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Section List
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

{% api-method-query-parameters %}
{% api-method-parameter name="row\_\_sid" type="string" required=false %}

{% endapi-method-parameter %}
{% endapi-method-query-parameters %}

{% api-method-form-data-parameters %}
{% api-method-parameter name="widget\_\_sid" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="name" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="description" type="string" required=false %}

{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=201 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "sid": "xxx",
    "table__name_plural": "experiments",
    "row__sid": "xxx",
    "widget__sid": "xxx",
    "name": "Double Signature",
    "description": "",
    "order": 1,
    "widget_set": {
        "sid": "xxx",
        "icon": "gesture",
        "name": "Double Signatures",
        "subscription_price": "Free",
        "PPU_price": "$0.2",
        "notes": "dd",
        "component___status___WidgetActive": false,
        "description": "xxx",
        "instruction": "xxx",
        "usecase": "",
        "related_to": "",
        "apply_to": "Substance,Document,File",
        "allow_multiple": false,
        "is_readonly": false,
        "is_archived": false,
        "is_public": true,
        "date_updated": "2018-07-22T20:27:40.367371Z",
        "date_created": "2018-02-24T02:55:10.448466Z"
    },
    "data": null,
    "section_data": {
        ...
    },
    "is_archived": false,
    "date_updated": "2018-07-27T03:56:42.747213Z",
    "date_created": "2018-07-27T03:56:42.646170Z"
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

{% api-method method="get" host="{{ base\_url }}" path=" /tables/section/detail/{sid}/" %}
{% api-method-summary %}
Section Detail
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
    "sid": "xxx",
    "table__name_plural": "experiments",
    "row__sid": "xxx",
    "widget__sid": "xxx",
    "name": "Double Signature",
    "description": "",
    "order": 1,
    "widget_set": {
        "sid": "xxx",
        "icon": "gesture",
        "name": "Double Signatures",
        "subscription_price": "Free",
        "PPU_price": "$0.2",
        "notes": "dd",
        "component___status___WidgetActive": false,
        "description": "xxx",
        "instruction": "xxx",
        "usecase": "",
        "related_to": "",
        "apply_to": "Substance,Document,File",
        "allow_multiple": false,
        "is_readonly": false,
        "is_archived": false,
        "is_public": true,
        "date_updated": "2018-07-22T20:27:40.367371Z",
        "date_created": "2018-02-24T02:55:10.448466Z"
    },
    "data": null,
    "section_data": {
        ...
    },
    "is_archived": false,
    "date_updated": "2018-07-27T03:56:42.747213Z",
    "date_created": "2018-07-27T03:56:42.646170Z"
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

{% api-method method="patch" host="{{ base\_url }}" path=" /tables/section/detail/{sid}/" %}
{% api-method-summary %}
Section Patch
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
{% api-method-parameter name="name" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="description" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="order" type="number" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="data" type="object" required=false %}

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
    "sid": "xxx",
    "table__name_plural": "experiments",
    "row__sid": "xxx",
    "widget__sid": "xxx",
    "name": "Double Signature",
    "description": "",
    "order": 1,
    "widget_set": {
        "sid": "xxx",
        "icon": "gesture",
        "name": "Double Signatures",
        "subscription_price": "Free",
        "PPU_price": "$0.2",
        "notes": "dd",
        "component___status___WidgetActive": false,
        "description": "xxx",
        "instruction": "xxx",
        "usecase": "",
        "related_to": "",
        "apply_to": "Substance,Document,File",
        "allow_multiple": false,
        "is_readonly": false,
        "is_archived": false,
        "is_public": true,
        "date_updated": "2018-07-22T20:27:40.367371Z",
        "date_created": "2018-02-24T02:55:10.448466Z"
    },
    "data": null,
    "section_data": {
        ...
    },
    "is_archived": false,
    "date_updated": "2018-07-27T03:56:42.747213Z",
    "date_created": "2018-07-27T03:56:42.646170Z"
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



