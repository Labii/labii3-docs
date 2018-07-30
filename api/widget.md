---
description: >-
  Widget provide powerful add-ons to your records. Widgets are created and
  maintained by Labii Inc. and therefore, you do not have permission to change.
---

# Widget

{% api-method method="get" host="{{ base\_url }}" path=" /widgets/widget/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Widget List
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
    "page_count": 3,
    "count": 22,
    "next": null,
    "previous": null,
    "add_permission": false,
    "results": [
        {
            "sid": "xxx",
            "icon": "text_fields",
            "name": "Plain Text",
            "subscription_price": "Free",
            "PPU_price": "Free",
            "notes": "Add plain text, with markdown support",
            "usecase": "xxx",
            "related_to": "rich text",
            "allow_multiple": true,
            "is_readonly": false,
            "is_public": true,
            "component___status___WidgetActive": true,
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

{% api-method method="get" host="{{ base\_url }}" path=" /widgets/widget/detail/{sid}/" %}
{% api-method-summary %}
Widget Detail
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
    "icon": "text_fields",
    "name": "Plain Text",
    "subscription_price": "Free",
    "PPU_price": "Free",
    "notes": "Add plain text, with markdown support",
    "component___status___WidgetActive": false,
    "description": "Use this widget to add text with a simple editor. The typical application is Results, Steps, Overview, Description, et.al. The editor also supports Markdown.",
    "instruction": "Markdown is optional, to use Markdown, read more about markdown at https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet. <br>\r\n## - Heading<br>\r\n* Unordered list<br>\r\n1. Ordered list<br>\r\nEmphasis, aka italics, with *asterisks* or _underscores_.<br>\r\nStrong emphasis, aka bold, with **asterisks** or __underscores__.<br>\r\nCombined emphasis with **asterisks and _underscores_**.<br>\r\nStrikethrough uses two tildes. ~~Scratch this.~~<br>",
    "usecase": "soem application",
    "related_to": "rich text",
    "apply_to": "Substance,Document,File",
    "allow_multiple": true,
    "is_readonly": false,
    "is_archived": false,
    "is_public": true,
    "screenshot_1": ""
    "screenshot_1": ""
    "date_updated": "2018-07-22T20:25:12.008598Z",
    "date_created": "2018-01-06T19:13:20.282546Z"
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



