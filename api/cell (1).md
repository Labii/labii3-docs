---
description: View/update cell data
---

# Cell

{% api-method method="post" host="{{ base\_url }}" path=" /tables/cell/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Cell List
{% endapi-method-summary %}

{% api-method-description %}
Create value for one or more cells
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="level" type="string" required=false %}
organization
{% endapi-method-parameter %}

{% api-method-parameter name="sid" type="string" required=false %}
organization sid
{% endapi-method-parameter %}

{% api-method-parameter name="serializer" type="string" %}
list or detail
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="token" type="string" required=true %}
Authentication token to track down who is emptying our stocks.
{% endapi-method-parameter %}
{% endapi-method-headers %}

{% api-method-query-parameters %}
{% api-method-parameter name="row\_\_sid" type="string" required=true %}
The sid of the row
{% endapi-method-parameter %}
{% endapi-method-query-parameters %}

{% api-method-form-data-parameters %}
{% api-method-parameter name="xxx" type="string" required=true %}
column\_\_sid
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=201 %}
{% api-method-response-example-description %}
Cake successfully retrieved.
{% endapi-method-response-example-description %}

```yaml
[
    {"sid": "xxx"},
    {"sid": "xxx"}
]
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=403 %}
{% api-method-response-example-description %}
No permission to edit the row
{% endapi-method-response-example-description %}

```yaml
{
    "message": "You do not have permission to perform this action."
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=406 %}
{% api-method-response-example-description %}
Errors in post parameters
{% endapi-method-response-example-description %}

```yaml
# The provided organization id is not valid
{
    "message": "Wrong id: xxx."
}

# The provided ids does not match
{
    "message": "Wrong id: organization sid (xxx) does not match to row sid (xxx)"
}

# Missing row__sid
{
    "message": "Missing row__sid in the post link."
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="patch" host="{{ base\_url }}" path=" /tables/cell/detail/{sid}/" %}
{% api-method-summary %}
Cell Detail
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="" type="string" required=false %}

{% endapi-method-parameter %}
{% endapi-method-path-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```

```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

