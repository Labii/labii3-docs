# Authentication

All APIs at Labii need token to authenticate. This page introduces the methods of login, logout, sign in, forget password, and reset password.

## Auth

Provide username and password to exchange a valid token. For the security reasons:
* The token will be invalid after 30 minutes of idle.
* After 5 invalid or failed attempts your account will be locked for 24 hours to prevent unauthorized access.
* Notification will be sent out for every failed login.

Use the following command and examples to receive an token.


{% tabs %}
    {% tab title="command-line" %}
        ```text
        POST: {{base_url}}/accounts/login/
        ```

        DATA:
        * username: your email address
        * password: your password
    {% endtab %}


    {% tab title="Example" %}
        ```text
        $ curl -d "username=test@labii.com&password=1234567" -X POST {{ base_url }}/accounts/login/
        ```
    {% endtab %}

    {% tab title="Respond" %}
        ```text
        {token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9}
        ```
    {% endtab %}

    {% tab title="Errors" %}
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
    {% endtab %}


{% endtabs %}

## Forget Password

Reset password from an email. The email will receive a link to reset the password.
