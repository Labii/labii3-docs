---
description: Enhance your ELN & LIMS with goal management
---

# Goal management

## Overview

It is the end of year and it is that time of the year to review what you did in last year and what you are planning to do for the coming new year. 

With Labii ELN & LIMS, you are able to management your research goals, and more, categorize each experiment note based on your research goal.

## Before start

Before getting started, the below widgets are required and please make sure they have been activated. [Click here to learn how to activate or deactivate a widget. ](../settings/widgets.md)

* [Rich Text](../widgets/text.md)
* [Table](../widgets/table.md)
* [Backlink](../widgets/foreign-key-relationships.md)

{% hint style="info" %}
Note: only the administrators can perform the actions.
{% endhint %}

## Configuration

### 1\) [Create a table](../settings/tables.md#add-a-table) named **goals**:

> Table Name \(Singular\) = goal  
> Table Name \(Plural\) = goals  
> Description = Research goals  
> Unique Code = GL  
> Icon = adjust  
> Type = Substance

### 2\) [Create the following **columns**](../settings/tables.md#customize-column) for the table **goals:**

1. **year**, the year of the goal
2. **date\_start**, the start date of the goal
3. **date\_end**, the end date of the goal
4. **status**, the status of the goal
5. **parent**, what goal is the goal subsequent to, use this field to create a big goal and many more detailed small goals
6. **assignee**, who should be responsible to the goal

![Column settings for Goals](../.gitbook/assets/goal-columns-labii-eln-lims.png)

Default value for the year \(the value can be updated later, please keep one value at one line\):

* 2018
* 2019
* 2020
* 2021
* 2022

Default value for the status \(the value can be updated later, please keep one value at one line\):

* Under Discussion
* Backlist
* In Progress
* Failed
* Canceled
* Completed

### 3\) [Create the following **sections**](../settings/tables.md#customize-default-sections):

1. **Overview**, brief description of the goal
2. **What to expect**, what's the outcome of the goal
3. **Cost estimation**, how much would it cost to accomplish the goal
4. **Sub Goals**, other goals that related to this goal
5. **Jobs**, the jobs related to this goal. This section can be changed to `experiments`, `protocols`, et.al.
6. **Detail**, the column value of the goal
7. **Review**, the year-end review of the goal. What has been done, how much it cost.

![Default sections of goal](../.gitbook/assets/goal-sections-labii-eln-lims.png)

### 4\) Add ForeignKey relationship to the goal:

To link experiment notes with goals, you need to first add a ForeignKey column in the table of **experiments**. And then select a goal you created each time when creating an experiment note.

### 5\) Year-end Review:

Don't forget to review your goals at the end of year. Specifically described what has been done, what need to be improved, what is the actually cost of the goal.

Also, do not forget to update the status of the goal. 

Hope you all getting successfully completed goals!

