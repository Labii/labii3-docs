# Statement

{% api-method method="get" host="{{ base\_url }}" path=" /organizations/statement/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Statement List
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
    "page_count": 2,
    "count": 1,
    "next": null,
    "previous": null,
    "add_permission": true,
    "results": [
        {
            "sid": "xxx",
            "date_start": "2018-07-27",
            "date_end": "2018-08-26",
            "subscription_cost": "$200.0",
            "ppu_cost": "$0",
            "widget_usage_cost": "$0.00",
            "record_storage_cost": "$0",
            "file_storage_cost": "$0",
            "total": "$200.0",
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

{% api-method method="get" host="{{ base\_url }}" path=" /organizations/statement/detail/{sid}/" %}
{% api-method-summary %}
Statement Detail
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
    "organization": 1,
    "date_start": "2018-07-27",
    "date_end": "2018-08-26",
    "subscription_price": "$100/seat/month",
    "seats": 2,
    "subscription_cost": "$200.0",
    "ppu_price": "$0/record",
    "record_count": 1,
    "ppu_cost": "$0",
    "widget_usage_cost": "$0.00",
    "version_count": 1829,
    "record_storage_price": "$0/version",
    "record_storage_cost": "$0",
    "file_storage_price": "$10/100G/Month",
    "file_size": "188.7 MB",
    "file_storage_cost": "$0",
    "total": "$200.0",
    "is_current": true,
    "is_subscription": true
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

