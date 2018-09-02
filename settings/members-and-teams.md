---
description: Permission and member management.
---

# Members and Teams

## Members

Only members can view or edit the data of the organization. There are 3 different roles for members:

| Role | Description | Positions |
| :--- | :--- | :--- |
| Administrators | The account administrators, they have full permission to configure the account. | CEOIT administrators |
| Members | The active members of the organization. | ScientistsCollaborators |
| Alumni | The members who have left the organization. Set `is_archived=true` to disable a member's permission.  |  |

**To add a member:** 

Settings -&gt; Member -&gt; Click "+" in the Nav -&gt; Fill in the form and Submit.

![Add a new member](../.gitbook/assets/member-add.png)

{% hint style="info" %}
Unlimited users can be added for PPU option.

On Subscription option, set `is_archived=true` will free up seat for another user.
{% endhint %}

{% hint style="info" %}
**Date End** is used as reference only, it could not a user's permission. Use `is_archived=true` to disable a member's permission. 
{% endhint %}

## Team

A team is a collection of members. Team can be created to assign same permission to a project. A team is for those members working on the same project. 

**To add a team:** 

Settings -&gt; Team -&gt; Click "+" in the Nav -&gt; Fill in the form and Submit.

![Add a team](../.gitbook/assets/team-add.png)

