# Statement

Show the monthly statement of your organization.

## List URL

```text
{{base_url}}/organizations/statement/list/[level]/[sid]/[serializer]/
```

**Wheres,**

* level = organization
* sid = organization encrypted id
* serializer = \[list/detail\]

**Methods allowed:**

* GET

## Detail URL

```text
{{base_url}}/organizations/statement/detail/[sid]/
```

**Wheres,**

* sid = statement encrypted id

**Methods allowed:**

* GET

\#\# Install {\#install}

The first thing is to get the GitBook API client.

{% tabs %}
{% tab title="JavaScript" %}
\`\`\`bash

$ npm install gitbook-api

\`\`\`
{% endtab %}

{% tab title="Go" %}
\`\`\`bash

$ go get github.com/GitbookIO/go-gitbook-api

\`\`\`
{% endtab %}
{% endtabs %}

