---
description: 101 of Labii widgets
---

# Summary

## Add Widget





## Edit Widget



## Metadata Labels

The specific variables can be provided via adding metadata to your **organization**, **project**, or **record**. The metadata labels is defined in the `metadata_labels` field of widget. If these field is empty, no metadata need to set up.

The metadata is specific in order:

* **organization**, add the metadata to organization level if you want the metadata available to all users in  the organization. See [here](../settings/organization-detail.md#metadata) for more details. 
* **project**, add the metadata to project level if you want the metadata available to the users in the project. Other users from other project could not use the metadata. The metadata at the project level will overwrite the metadata at the organization level. 
* **record/row**, add the metadata to record level. This metadata can only been used for this record. The metadata at record level will overwrite the same metadata at the project or organization level.

{% hint style="info" %}
The priority of metadata: record &gt; project &gt; organization
{% endhint %}



