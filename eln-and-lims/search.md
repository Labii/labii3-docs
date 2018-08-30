---
description: >-
  Labii provides sophisticated search function to help you address your
  scientific problems.
---

# Search

## In-Page Search

Use this function to narrow down the number of items to display in one page. On the list view of projects, there is a search icon on the top, where you can click and start typing. The results are only from that table category, and will appear as you type. 

![In-Page Search](../.gitbook/assets/search-in-page.png)

## Global Search

If want to search any records match to one or two phases, use global search. 

On the sidebar, click on **Search** to search. 

![Global Search](../.gitbook/assets/search-global.png)

## Filter

Filter function is table specific. To filter records, first click a table in the side bar, and then choose **Filter xxx** \(the name will update as the table name changes\) from the filter dropdown. 

![Filter Menu](../.gitbook/assets/filter-menu.png)

Once selected, a filter form will be opened. 

![Filter Form](../.gitbook/assets/filter-form.png)

**To build a query:**

1. Click **ADD QUERY**
2. Select a Field, Lookup Expression and provide a lookup value.
3. Click **ADD QUERY** again to add more queries.
4. Click **Delete** button to remove the query; Use Up/Down Button to change query order.

{% hint style="info" %}
The **Name** and **Description** fields are optional. If the **Name** is provided, the filter will be saved and can be accessed from the filter dropdown menu.
{% endhint %}

{% hint style="info" %}
When a filter is saved, the **Users** filed can be customized to define who can use the filter. The owner will be added to the users list automatically. 
{% endhint %}

**Fields:**

Fields are the column title of the table. The list of fields will updated as the table changes. Before using the filter function, you have to have clear idea which field is the data come from. If you are not quite sure, use the [global search](search.md#global-search). 

**Lookup Expression:**

* **Is equal to**, find records that have exactly match to the provided value, case insensitive.
* **Not equal to**, find records that do not match to the provided value.
* **Contains**, find records that contains the provided value, case insensitive.
* **Not contains**, find records that does not contains the string of provided value.
* **Greater than or equal to**, find the records greater than or equal to the provided value, for **Date** and **Number** type of columns only.
* **Less than or equal to**, find the records less than or equal to the provided value, for **Date** and **Number** type of columns only.

**Value:**

The value to lookup.

* Use `true` or `false` for boolean. 
* Use `YYYY-MM-DD` for date.

## Examples

**Signatures:**

* Find all signed/unsigned documents `is_locked=true/false`
* Find all signed/unsigned documents by a specific role \(role=Author\) `is_locked=true/false&signature__role__iexact=Author`
* Find all signed/unsigned documents by a user `is_locked=true/false&signature__signer__sid=xxx is_locked=true/false&signature__signer__first_name=xxx is_locked=true/false&signature__signer__last_name=xxx is_locked=true/false&signature__signer__first_name=xxx&signature__signer__last_name=xxx`

