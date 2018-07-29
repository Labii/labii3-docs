---
description: >-
  All APIs at Labii need token to authenticate. This page introduces the methods
  of login, logout, sign in, forget password, and reset password.
---

# Authentication

{% api-method method="post" host="{{base\_url}}/accounts/" path="auth/" %}
{% api-method-summary %}
Auth
{% endapi-method-summary %}

{% api-method-description %}
Provide username and password to exchange a valid token. 
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-form-data-parameters %}
{% api-method-parameter name="password" type="string" required=true %}
login password
{% endapi-method-parameter %}

{% api-method-parameter name="username" type="string" required=true %}
email of the account
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Login successful
{% endapi-method-response-example-description %}

```yaml
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
    "user": {
        "sid":"xxx",
        "first_name":"xxx",
        "last_name":"xxx",
        "email":"xxx@labii.com"
    }
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=406 %}
{% api-method-response-example-description %}
Wrong username or password
{% endapi-method-response-example-description %}

```
["Unable to log in with provided credentials."]
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="{{ base\_url }}/accounts" path="/forgetpassword/" %}
{% api-method-summary %}
Forget Password
{% endapi-method-summary %}

{% api-method-description %}
Receive a email to reset the password.   
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-form-data-parameters %}
{% api-method-parameter name="email" type="string" required=true %}
email of the account
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{tag: xxxxx}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="{{ base\_url }}/accounts/" path="resetpassword/?tag={tag}" %}
{% api-method-summary %}
Reset Password
{% endapi-method-summary %}

{% api-method-description %}
Change user password. 
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-query-parameters %}
{% api-method-parameter name="tag" type="string" required=true %}
The tag returned from forget password method
{% endapi-method-parameter %}
{% endapi-method-query-parameters %}

{% api-method-form-data-parameters %}
{% api-method-parameter name="password" type="string" required=true %}
The new password
{% endapi-method-parameter %}
{% endapi-method-form-data-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
{}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=406 %}
{% api-method-response-example-description %}
Wrong parameters
{% endapi-method-response-example-description %}

```
Error: Missing Tag in GET! - Tag is missing in the url
Error: Wrong Tag! - Tag is not valid
Unknown request! - User not exists
The link has expired - Tag is valid for only 30 min
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="{{base\_url}}/accounts" path="/logout/" %}
{% api-method-summary %}
Logout
{% endapi-method-summary %}

{% api-method-description %}
Logout your account, invalid the token.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="token" type="string" required=true %}
user token
{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
{}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=401 %}
{% api-method-response-example-description %}
Wrong token
{% endapi-method-response-example-description %}

```

```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}



