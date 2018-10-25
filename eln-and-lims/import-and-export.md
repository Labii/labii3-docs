---
description: Use Import and Export to connect Labii with external data.
---

# Import and Export

## Import

External data can be imported into Labii. Labii supports \*.tsv. Please convert your excel or \*.csv files to \*.tsv file before Import.

Labii do not have any request on the number of columns. You will have option to match the headers with fields in Labii. Please use the first row as headers.

To import,

1. Select a table category from the sidebar.
2. Click the **Menu** button on the top bar and click **Import**.
3. Choose which project to import from the drop-down list. 
4. Upload your \*.tsv file.
5. Choose the columns to match with each header for your records. 
6. Click **Submit**.

![Import Experiments](../.gitbook/assets/screen-shot-2018-08-28-at-11.42.36-pm.png)

The title of the model shows the number of records to import. 

* Each field of form represent a column in your \*.tsv file. 
* The dropdown options are the table fields in Labii. 
* The value of first row is displayed as the field description. 

![Match headers with Labii columns](../.gitbook/assets/screen-shot-2018-08-29-at-12.02.25-am.png)

{% hint style="info" %}
On default, Labii will create new records for all imported records. If you want to update an existing record, please include a "UID" column. If unique ID is provided, the import function will update for that record.
{% endhint %}

{% hint style="info" %}
Each field can only be matched for once, except the **metadata**. If metadata is selected, the title will be treat as metadata label and value will be treat as metadata value.
{% endhint %}

### Prepare Import Table

Although Labii provides flexibilities in number of columns. Certain data type have to be prepared in a proper way to imported correctly.

We recommend you to prepare the data in a excel sheet or google sheets and then save the data as \*.tsv.

Here are some important notes to pay attention to:

* First row as title. Please always include title at the first row.
* Use `#` at the beginning of a row to ignore. The whole row with **\#** at the beginning will be excluded from importing.
* The number of column does not matter. You can ignore a column via not selecting a matched column.
* The order of column does not matter.
* Use **Unique ID \(UID\)** to match and update existing records. The UIDs that do not match to records in database will be ignored and a new UID will be assigned. **UID is mostly used to update an existing records.**
* For **Select** Use the exact value of your choose. use **`,`** to separate multiple values for **MultiSelect**. 
* For **ForeignKey** columns, use **UID** or **name** to match. use **`,`** to separate multiple **UIDs** or **names** for **ForeignKeys**.
* For **Boolean** columns, Use **true** for true and **false** for false.
* For **Date** columns, use **YYYY-MMMM-DD** 

## Export

Click the **Menu** drop-down list and click **Export as TSV**. The files will download on your computer. 

![](../.gitbook/assets/screen-shot-2018-08-28-at-11.44.42-pm.png)

{% hint style="info" %}
The AdBlock might block the downloading. Please disable your AdBlock if the download does not happen.
{% endhint %}

