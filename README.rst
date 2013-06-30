AppFlower - Rapid Business Application Framework
================================================

`AppFlower`_ is a rapid application builder framework that provides a
visual designer studio for building web applications without prior
knowledge of programming, using drag and drop and no coding.  Create web
applications in minutes and say goodbye to expensive custom development.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- AppFlower configurations:
   
   - Installed from upstream source code to /var/www/appflower

- SSL support out of the box.
- `PHPMyAdmin`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, phpMyAdmin: username **root**
-  AppFlower: username **admin**


.. _AppFlower: http://www.appflower.com/
.. _TurnKey Core: http://www.turnkeylinux.org/core
.. _PHPMyAdmin: http://www.phpmyadmin.net
