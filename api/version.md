# Version

{% api-method method="get" host="{{ base\_url }}" path=" /tables/version/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Version List
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
    "page_count": 183,
    "count": 1829,
    "next": "http://127.0.0.1:8000/v1/tables/version/list/organization/ehkn0a40x1glqvAFKP/list/?page=2",
    "previous": null,
    "add_permission": false,
    "results": [
        {
            "sid": "xxx",
            "hash": "VGd4bzZhZmVhMzBkOWZlMmViNTdmZDE3YzBhOWVlMTUwYmMzSEZMcQ__",
            "previousHash": "WFFWbGRlMzViMmM1MzViZmM0MTdmYjU2N2FmZWFkYmFjOGJkWHFRSw__",
            "version": 8,
            "activity_message": "Updated data of Section (Files (No Preview)) from None to {\"files\": [{\"sid\": \"orux0a40x239qvAFKPUZ\", \"name\": \" FL143: FL154_ Small Workbook.xlsx (v3)\"}, {\"sid\": \"mpsv0a40x237otyDINSX\", \"name\": \" FL141: 2015-5-5 lib pool.xlsx (v3)\"}, {\"sid\": \"ehkn0a40x7dglqvAFKP\", \"name\": \" FL8: linkers and templates for subset-2.xlsx (v3)\"}]}",
            "is_valid": true,
            "updated_by": {
                "sid": "xxx",
                "first_name": "xxx",
                "last_name": "xxx",
                "email": "xxx@labii.com"
            },
            "date_created": "2018-07-27T07:10:57.279388Z",
            "change_permission": false
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

{% api-method method="get" host="{{ base\_url }}" path=" /tables/version/detail/{sid}/" %}
{% api-method-summary %}
Version Detail
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
    "hash": "VGd4bzZhZmVhMzBkOWZlMmViNTdmZDE3YzBhOWVlMTUwYmMzSEZMcQ__",
    "previousHash": "WFFWbGRlMzViMmM1MzViZmM0MTdmYjU2N2FmZWFkYmFjOGJkWHFRSw__",
    "version": 8,
    "data": {
        ...
    }
    "activity_message": "Updated data of Section (Files (No Preview)) from None to {\"files\": [{\"sid\": \"orux0a40x239qvAFKPUZ\", \"name\": \" FL143: FL154_ Small Workbook.xlsx (v3)\"}, {\"sid\": \"mpsv0a40x237otyDINSX\", \"name\": \" FL141: 2015-5-5 lib pool.xlsx (v3)\"}, {\"sid\": \"ehkn0a40x7dglqvAFKP\", \"name\": \" FL8: linkers and templates for subset-2.xlsx (v3)\"}]}",
    "updated_by": {
        "sid": "xxx",
        "first_name": "xxx",
        "last_name": "xxx",
        "email": "xxx@labii.com"
    },
    "date_updated": "2018-07-27T07:10:57.293464Z",
    "date_created": "2018-07-27T07:10:57.279388Z",
    "change_permission": false
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

