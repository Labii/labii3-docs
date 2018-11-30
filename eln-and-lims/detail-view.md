---
description: Edit/View the content of a record
---

# Detail View

## Overview

The detail view of a record display the content of the record. This function is mostly used in Electronic Lab Notebook \(ELN\) to define the detail of a processing experiment. It can also used in the Laboratory Information Management System \(LIMS\) to record the detail of a record.

In [Labii ELN & LIMS](https://www.labii.com), the detail view is build up with a collection of sections. Each section holds certain data of the record, and use a specific widget to display and edit the content. For example, a summary section might holds the basic summary of an experiment, and the summary can be updated with a [Rich Text](../widgets/text.md#rich-text) widget.

![Detail View of an experiment at Labii ELN &amp; LIMS](../.gitbook/assets/detail-view-labii-eln-lims.png)

## Open detail view

The detail view can be open via clicking the name of a record. 

To get full page view of the detail:

* Click the "**Title**" of the record at the split view.
* **More -&gt; View in new page** at the split view.

## Add section

To add a section:

1. Click the **Add** menu
2. In the dropdown, select a widget
3. If the widget is not in the link, click **More Widgets** to browse more widgets
4. If a widget is not allowed to use, click **Widget Store** to active the widget. \(Note: Only administrator can perform\)
5. Once added, click edit icon to update the value of the section.

![Widget dropdown list](../.gitbook/assets/widgets-add-menu-labii-eln-lims.png)

## Edit section

### Edit section name

Click more icon and select Change Section to edit the section. The name and description of the section can be updated.

![Drop down menu of section more button](../.gitbook/assets/edit-section-labii-eln-lims.png)

### Edit section content

Click the edit icon or "**Edit Content**" in the dropdown menu to update the content of the section. Based on what widget the section is using, the interface will various a lot. The usage of each widget can be found in the [Widget](../settings/widgets.md). 

### Refresh section

If, for some reason, the content of the section is not up-to-date. Click **Refresh Section** to reload the data.

### Archive section

To discard or hide the section, click Archive Section to hide the section.

### Collapse content

The content of the section can be collapse and expand via clicking section header.

### Change order

The order of section can be change via dragging the section header.

### Save default section value

Use this function to save default section value for easy configuration. Once the default section value is saved, the value will be loaded automatically when save section is created.

The default section value is specific to:

* section name
* section widget
* table

The default section value can only been applied when above 3 parameters matches. It is saved as a metadata with the label of `SECTIONVALUE_[TABLE]_[WIDGET]_[SECTION NAME]`

The default section value can be set at 3 levels, the metadata can be saved in all or any of these levels:

1. organization
2. project
3. member

Wheres, member &gt; project &gt; organization. Labii will always use the metadata at the member level if exists, then project and organization.

## Print

The detail of the record can be print out. More -&gt; Print.

![Print view](../.gitbook/assets/print-view-labii-eln-lims.png)

{% hint style="info" %}
Section can be hidden from printing via click the **HIDE** button.
{% endhint %}

## Duplicate

Check [here](add-record.md#duplicate-from-existing-record) for more detail.

## Sign the record

All records can be signed via [Signature](../widgets/signature.md) widget. Once signed, the document is locked from editing. However, the read-only widget can still been added to display the data of the records.

