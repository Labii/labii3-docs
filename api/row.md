# Row

{% api-method method="get" host="{{ base\_url }}" path=" /tables/row/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Row List
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
    "count": 1,
    "next": null,
    "previous": null,
    "add_permission": true,
    "results": [
        {
            "sid": "369b0a40x29f50ejotyD",
            "name": "EP107: test file table display (v8)___test file table display",
            "rowdata_set": {
                "date_start___FILO0a40x1cHMRW27bg": "2018-07-26"
            },
            "project___project__sid": "Test___ehkn0a40x1glqvAFKP",
            "owner": "Yonggan Wu",
            "is_template": false,
            "open_to_organization": false,
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

{% api-method method="post" host="{{ base\_url }}" path=" /tables/row/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Row List
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
{% api-method-parameter name="project\_\_sid" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="name" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="description" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="is\_template" type="boolean" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="open\_to\_organization" type="boolean" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="is\_archived" type="boolean" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="metadata" type="string" required=false %}

{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "sid": "369b0a40x29f50ejotyD",
    "uid": "EP107",
    "table__name_plural": "experiments",
    "name": "test file table display",
    "description": "",
    "project___project__sid": "Test___ehkn0a40x1glqvAFKP",
    "open_to_organization": false,
    "is_template": false,
    "is_archived": false,
    "metadata": [],
    "version": 8,
    "updated_by": "Yonggan Wu",
    "date_updated": "2018-07-27T03:56:42.442166Z",
    "owner": "Yonggan Wu",
    "date_created": "2018-07-27T03:56:42.066485Z",
    "identical_items": [],
    "rowdata_set": {
        "date_due___GJMP0a40x1dINSX38ch": null,
        "date_start___FILO0a40x1cHMRW27bg": "2018-07-26"
    },
    "section_set": [
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
                "description": "dd",
                "instruction": "dd",
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
                "message": "sign it well",
                "signers": []
            },
            "is_archived": false,
            "date_updated": "2018-07-27T03:56:42.747213Z",
            "date_created": "2018-07-27T03:56:42.646170Z"
        },
        ...
    ],
    "foreignkey": {},
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

{% api-method method="patch" host="{{ base\_url }}" path=" /tables/row/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Row List
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
{% api-method-parameter name="column" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="value" type="string" required=false %}

{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "sid": "369b0a40x29f50ejotyD",
    "uid": "EP107",
    "table__name_plural": "experiments",
    "name": "test file table display",
    "description": "",
    "project___project__sid": "Test___ehkn0a40x1glqvAFKP",
    "open_to_organization": false,
    "is_template": false,
    "is_archived": false,
    "metadata": [],
    "version": 8,
    "updated_by": "Yonggan Wu",
    "date_updated": "2018-07-27T03:56:42.442166Z",
    "owner": "Yonggan Wu",
    "date_created": "2018-07-27T03:56:42.066485Z",
    "identical_items": [],
    "rowdata_set": {
        "date_due___GJMP0a40x1dINSX38ch": null,
        "date_start___FILO0a40x1cHMRW27bg": "2018-07-26"
    },
    "section_set": [
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
                "description": "dd",
                "instruction": "dd",
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
                "message": "sign it well",
                "signers": []
            },
            "is_archived": false,
            "date_updated": "2018-07-27T03:56:42.747213Z",
            "date_created": "2018-07-27T03:56:42.646170Z"
        },
        ...
    ],
    "foreignkey": {},
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

{% api-method method="get" host="{{ base\_url }}" path=" /tables/row/detail/{sid}/" %}
{% api-method-summary %}
Row Detail
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
    "sid": "369b0a40x29f50ejotyD",
    "uid": "EP107",
    "table__name_plural": "experiments",
    "name": "test file table display",
    "description": "",
    "project___project__sid": "Test___ehkn0a40x1glqvAFKP",
    "open_to_organization": false,
    "is_template": false,
    "is_archived": false,
    "metadata": [],
    "version": 8,
    "updated_by": "Yonggan Wu",
    "date_updated": "2018-07-27T03:56:42.442166Z",
    "owner": "Yonggan Wu",
    "date_created": "2018-07-27T03:56:42.066485Z",
    "identical_items": [],
    "rowdata_set": {
        "date_due___GJMP0a40x1dINSX38ch": null,
        "date_start___FILO0a40x1cHMRW27bg": "2018-07-26"
    },
    "section_set": [
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
                "description": "dd",
                "instruction": "dd",
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
                "message": "sign it well",
                "signers": []
            },
            "is_archived": false,
            "date_updated": "2018-07-27T03:56:42.747213Z",
            "date_created": "2018-07-27T03:56:42.646170Z"
        },
        ...
    ],
    "foreignkey": {},
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
Row Detail
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
{% api-method-parameter name="project\_\_sid" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="name" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="description" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="is\_template" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="open\_to\_organization" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="is\_archived" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="metadata" type="string" required=false %}

{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "sid": "369b0a40x29f50ejotyD",
    "uid": "EP107",
    "table__name_plural": "experiments",
    "name": "test file table display",
    "description": "",
    "project___project__sid": "Test___ehkn0a40x1glqvAFKP",
    "open_to_organization": false,
    "is_template": false,
    "is_archived": false,
    "metadata": [],
    "version": 8,
    "updated_by": "Yonggan Wu",
    "date_updated": "2018-07-27T03:56:42.442166Z",
    "owner": "Yonggan Wu",
    "date_created": "2018-07-27T03:56:42.066485Z",
    "identical_items": [],
    "rowdata_set": {
        "date_due___GJMP0a40x1dINSX38ch": null,
        "date_start___FILO0a40x1cHMRW27bg": "2018-07-26"
    },
    "section_set": [
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
                "description": "dd",
                "instruction": "dd",
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
                "message": "sign it well",
                "signers": []
            },
            "is_archived": false,
            "date_updated": "2018-07-27T03:56:42.747213Z",
            "date_created": "2018-07-27T03:56:42.646170Z"
        },
        ...
    ],
    "foreignkey": {},
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

