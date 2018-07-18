# Authentication

This page introduces the methods of login, logout, sign in, forget password, and reset password.

## Auth

Provide username and password to exchange a valid token. The token will be invalid after 30 minutes of idle.

```text
POST: {{base_url}}/accounts/login/
```

{% tabs %}
{% tab title="Bash" %}
```text
$ curl -d "username=test@labii.com&password=1234567" -X POST {{base_url}}/accounts/login/
```

**Data Fields:**

* email
* password

**Return Json**

```text
{token: xxxxxxx}
```
{% endtab %}

{% tab title="JavaScript" %}
```text
{token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9}
```

**Error message**

* 405, Method not allowed.
  * GET
  * PUT
  * PATCH
  * DELETE
* 406, Unable to log in with provided credentials.
  * Wrong username or password
  * User not activate or email not validate.
* 429, Request was throttled.
  * Anonymous: 5/hour
  * Login user: 1000/hour

## Forget Password

Reset password from an email. The email will receive a link to reset the password.
{% endtab %}
{% endtabs %}

