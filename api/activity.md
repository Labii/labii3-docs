# Activity

{% api-method method="get" host="{{ base\_url }}" path=" /activities/activity/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Activity List
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
    "page_count": 232,
    "count": 2311,
    "next": null,
    "previous": null,
    "add_permission": true,
    "results": [
        {
            "icon": "edit",
            "user": {
                "sid": "xxx",
                "first_name": "xxx",
                "last_name": "xxx",
                "email": "xxx@labii.com"
            },
            "action": "Updated",
            "field": "data of Section (Files (No Preview))",
            "new_data": "{\"files\": [{\"sid\": \"xxx\", \"name\": \" FL143: xxx.xlsx (v3)\"}, {\"sid\": \"xxx\", \"name\": \" FL141: xxx.xlsx (v3)\"}, {\"sid\": \"xxx\", \"name\": \" FL8: xxx.xlsx (v3)\"}]}",
            "target": "Files (No Preview)",
            "model": "section",
            "object_sid": "xxx",
            "date_created": "2018-07-27T07:10:57.133353Z"
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



