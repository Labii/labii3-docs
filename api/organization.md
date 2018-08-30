# Organization

{% api-method method="get" host="{{ base\_url }}" path="/organizations/organization/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Organization List
{% endapi-method-summary %}

{% api-method-description %}
Get a list of organizations
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="level" type="string" required=true %}
organization or user
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
    "days_available": 182,
    "add_permission": false,
    "change_permission": true,
    "results": [
        {
            "sid": "xxx",
            "name": "xxx",
            "username": "xxx",
            "description": "xxx",
            "logo_icon": "xxx",
            "logo_wordmark": "xxx",
            "is_academic": false,
            "is_subscription": true,
            "available_till": "2019-01-01",
            "payment": {
                "payment_option": "Subscription",
                "seats": 5,
                "available_till": "2019-01-01",
                "days_available": 180,
                "is_academic": "False",
                "credits": "$499.25"
            },
            "table_set": [
                {
                    "sid": "xxx",
                    "icon": "assignment",
                    "name_singular": "experiment",
                    "name_plural": "experiments",
                    "name_system": null,
                    "description": "An experiment is the lab note to document procedures carried out to support, refute, or validate a hypothesis.",
                    "unique_code": "EP",
                    "table_type": "Document",
                    "order": 1
                },
                ...
            ],
            "project_set": [
                {
                    "name": "xxx",
                    "sid": "xxx"
                },
                ...
            ],
            "widget_set": [
                {
                    "sid": "xxx",
                    "icon": "format_color_text",
                    "name": "Rich Text",
                    "subscription_price": "Free",
                    "PPU_price": "Free",
                    "notes": "Add Text with WYSIWYG Text Editor",
                    "component___status___WidgetActive": true,
                    "description": "Use this widget to add text from a WYSIWYG Text Editor. Other records can also be inserted via Mention(@).",
                    "instruction": "* To insert a link of other item, use <b>mention (@[Search Term])</b>. <br />- Type \"@\" to trigger suggestions. Click a list or press Enter to insert. Use \"__\" in search term to separate multiple keywords. For example, to find a experiment did by John, the mention term is <i>@ep__john</i><br />\r\n* To insert a consumption, use <b>mention (@[Amount]__[Unit]__of__[Search Term])</b>. For example, to insert the consumption of 10 ug of sample DNA: <i>@10__ug__of__sample__dna</i> <br />\r\n- The mentioned item can be a <i>Location</i>, consumption for all <i>Substance</i> in the location will be created. For example, to insert the consumption of 50 ul of all 96 miRNAs in a 96-well plate: <i>@50__ul__of__mirna__96__well__plate</i>",
                    "usecase": "",
                    "related_to": "",
                    "apply_to": "Substance,Document,File",
                    "allow_multiple": true,
                    "is_readonly": false,
                    "is_archived": false,
                    "is_public": true,
                    "date_updated": "2018-07-22T20:25:22.214763Z",
                    "date_created": "2018-01-03T05:31:33.477489Z"
                },
                ...
            ],
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

{% api-method method="post" host="{{ base\_url }}" path="/organizations/organization/list/{level}/{sid}/{serializer}/" %}
{% api-method-summary %}
Organization List
{% endapi-method-summary %}

{% api-method-description %}
Add a new organization.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="level" type="string" required=true %}
user
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
{% api-method-parameter name="name" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="username" type="string" required=true %}
Username of organization.
{% endapi-method-parameter %}

{% api-method-parameter name="description" type="string" required=false %}

{% endapi-method-parameter %}

{% api-method-parameter name="seats" type="string" required=false %}

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
    "name": "xxx",
    "username": "xxx",
    "description": "xxx",
    "logo_icon": "xxx",
    "logo_wordmark": "xxx",
    "is_academic": false,
    "is_subscription": true,
    "available_till": "2019-01-01",
    "payment": {
        "payment_option": "Subscription",
        "seats": 5,
        "available_till": "2019-01-01",
        "days_available": 180,
        "is_academic": "False",
        "credits": "$499.25"
    },
    "table_set": [
        {
            "sid": "xxx",
            "icon": "assignment",
            "name_singular": "experiment",
            "name_plural": "experiments",
            "name_system": null,
            "description": "An experiment is the lab note to document procedures carried out to support, refute, or validate a hypothesis.",
            "unique_code": "EP",
            "table_type": "Document",
            "order": 1
        },
        ...
    ],
    "project_set": [
        {
            "name": "xxx",
            "sid": "xxx"
        },
        ...
    ],
    "widget_set": [
        {
            "sid": "xxx",
            "icon": "format_color_text",
            "name": "Rich Text",
            "subscription_price": "Free",
            "PPU_price": "Free",
            "notes": "Add Text with WYSIWYG Text Editor",
            "component___status___WidgetActive": true,
            "description": "Use this widget to add text from a WYSIWYG Text Editor. Other records can also be inserted via Mention(@).",
            "instruction": "* To insert a link of other item, use <b>mention (@[Search Term])</b>. <br />- Type \"@\" to trigger suggestions. Click a list or press Enter to insert. Use \"__\" in search term to separate multiple keywords. For example, to find a experiment did by John, the mention term is <i>@ep__john</i><br />\r\n* To insert a consumption, use <b>mention (@[Amount]__[Unit]__of__[Search Term])</b>. For example, to insert the consumption of 10 ug of sample DNA: <i>@10__ug__of__sample__dna</i> <br />\r\n- The mentioned item can be a <i>Location</i>, consumption for all <i>Substance</i> in the location will be created. For example, to insert the consumption of 50 ul of all 96 miRNAs in a 96-well plate: <i>@50__ul__of__mirna__96__well__plate</i>",
            "usecase": "",
            "related_to": "",
            "apply_to": "Substance,Document,File",
            "allow_multiple": true,
            "is_readonly": false,
            "is_archived": false,
            "is_public": true,
            "date_updated": "2018-07-22T20:25:22.214763Z",
            "date_created": "2018-01-03T05:31:33.477489Z"
        },
        ...
    ],
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

{% api-method-response-example httpCode=406 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
Wrong id - The provided sid is not correct
Wrong id: xxx. The sid does not match to user! - The sid does not match to token information
Wrong level: xxx. Acceptable levels is user. - Wrong level provided
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="{{ base\_url }}" path="/organization/detail/{sid}/" %}
{% api-method-summary %}
Organization Detail
{% endapi-method-summary %}

{% api-method-description %}
Get the organization object
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="sid" type="string" required=true %}
organization sid
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
    "name": "xxx",
    "username": "xxx",
    "description": "xxx",
    "logo_icon": "xxx",
    "logo_wordmark": "xxx",
    "is_academic": false,
    "is_subscription": true,
    "available_till": "2019-01-01",
    "payment": {
        "payment_option": "Subscription",
        "seats": 5,
        "available_till": "2019-01-01",
        "days_available": 180,
        "is_academic": "False",
        "credits": "$499.25"
    },
    "table_set": [
        {
            "sid": "xxx",
            "icon": "assignment",
            "name_singular": "experiment",
            "name_plural": "experiments",
            "name_system": null,
            "description": "An experiment is the lab note to document procedures carried out to support, refute, or validate a hypothesis.",
            "unique_code": "EP",
            "table_type": "Document",
            "order": 1
        },
        ...
    ],
    "project_set": [
        {
            "name": "xxx",
            "sid": "xxx"
        },
        ...
    ],
    "widget_set": [
        {
            "sid": "xxx",
            "icon": "format_color_text",
            "name": "Rich Text",
            "subscription_price": "Free",
            "PPU_price": "Free",
            "notes": "Add Text with WYSIWYG Text Editor",
            "component___status___WidgetActive": true,
            "description": "Use this widget to add text from a WYSIWYG Text Editor. Other records can also be inserted via Mention(@).",
            "instruction": "* To insert a link of other item, use <b>mention (@[Search Term])</b>. <br />- Type \"@\" to trigger suggestions. Click a list or press Enter to insert. Use \"__\" in search term to separate multiple keywords. For example, to find a experiment did by John, the mention term is <i>@ep__john</i><br />\r\n* To insert a consumption, use <b>mention (@[Amount]__[Unit]__of__[Search Term])</b>. For example, to insert the consumption of 10 ug of sample DNA: <i>@10__ug__of__sample__dna</i> <br />\r\n- The mentioned item can be a <i>Location</i>, consumption for all <i>Substance</i> in the location will be created. For example, to insert the consumption of 50 ul of all 96 miRNAs in a 96-well plate: <i>@50__ul__of__mirna__96__well__plate</i>",
            "usecase": "",
            "related_to": "",
            "apply_to": "Substance,Document,File",
            "allow_multiple": true,
            "is_readonly": false,
            "is_archived": false,
            "is_public": true,
            "date_updated": "2018-07-22T20:25:22.214763Z",
            "date_created": "2018-01-03T05:31:33.477489Z"
        },
        ...
    ],
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
Wrong id - The provided sid is not correct
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="patch" host="{{ base\_url }}" path="/organization/detail/{sid}/" %}
{% api-method-summary %}
Organization Detail
{% endapi-method-summary %}

{% api-method-description %}
Partial update the organization information
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="sid" type="string" required=true %}
organization sid
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

{% api-method-parameter name="logo\_icon" type="string" required=false %}
Icon logo picture data
{% endapi-method-parameter %}

{% api-method-parameter name="logo\_wordmark" type="string" required=false %}
Wordmark logo picture data
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
    "name": "xxx",
    "username": "xxx",
    "description": "xxx",
    "logo_icon": "xxx",
    "logo_wordmark": "xxx",
    "is_academic": false,
    "is_subscription": true,
    "available_till": "2019-01-01",
    "payment": {
        "payment_option": "Subscription",
        "seats": 5,
        "available_till": "2019-01-01",
        "days_available": 180,
        "is_academic": "False",
        "credits": "$499.25"
    },
    "table_set": [
        {
            "sid": "xxx",
            "icon": "assignment",
            "name_singular": "experiment",
            "name_plural": "experiments",
            "name_system": null,
            "description": "An experiment is the lab note to document procedures carried out to support, refute, or validate a hypothesis.",
            "unique_code": "EP",
            "table_type": "Document",
            "order": 1
        },
        ...
    ],
    "project_set": [
        {
            "name": "xxx",
            "sid": "xxx"
        },
        ...
    ],
    "widget_set": [
        {
            "sid": "xxx",
            "icon": "format_color_text",
            "name": "Rich Text",
            "subscription_price": "Free",
            "PPU_price": "Free",
            "notes": "Add Text with WYSIWYG Text Editor",
            "component___status___WidgetActive": true,
            "description": "Use this widget to add text from a WYSIWYG Text Editor. Other records can also be inserted via Mention(@).",
            "instruction": "* To insert a link of other item, use <b>mention (@[Search Term])</b>. <br />- Type \"@\" to trigger suggestions. Click a list or press Enter to insert. Use \"__\" in search term to separate multiple keywords. For example, to find a experiment did by John, the mention term is <i>@ep__john</i><br />\r\n* To insert a consumption, use <b>mention (@[Amount]__[Unit]__of__[Search Term])</b>. For example, to insert the consumption of 10 ug of sample DNA: <i>@10__ug__of__sample__dna</i> <br />\r\n- The mentioned item can be a <i>Location</i>, consumption for all <i>Substance</i> in the location will be created. For example, to insert the consumption of 50 ul of all 96 miRNAs in a 96-well plate: <i>@50__ul__of__mirna__96__well__plate</i>",
            "usecase": "",
            "related_to": "",
            "apply_to": "Substance,Document,File",
            "allow_multiple": true,
            "is_readonly": false,
            "is_archived": false,
            "is_public": true,
            "date_updated": "2018-07-22T20:25:22.214763Z",
            "date_created": "2018-01-03T05:31:33.477489Z"
        },
        ...
    ],
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
Wrong id - The provided sid is not correct
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}



