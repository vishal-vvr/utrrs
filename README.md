# [UTRRS](http://fuelproject.org/utrrs)

![logo](https://raw.githubusercontent.com/tenstormavi/utrrs/master/utrrsApp/static/images/logo.png)

# UNICODE TEXT RENDERING REFERENCE SYSTEM
The Unicode Text Rendering Reference System (UTRRS) is a open source web-based application which compares a rendered text character with a reference image of a text character, for comparison of differences between the two.

Comparing the results of a text rendering engine to actual text can be done without the ability to read or comprehend the language in question. This ability is available for Codepoints (Unicode Character Set), GSUB (Glyph Substitution), and GPOS (Glyph Positioning).

[know more..](http://fuelproject.org/utrrs)

# Setup
```sh
$ python3 setup.py install
$ python3 src/manage.py migrate
$ python3 src/manage.py createsuperuser
$ python3 src/manage.py runserver
```
NOTE: 
- In production env just update 
    ```
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'utrrs.settings.development') to
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'utrrs.settings.production') in src/manage.py file 
    ```
    and production env releated settings(db details and etc) in 
    ```
    utrrs/settings/production.py file
    ```
    

# License
This application is licensed under the MIT License.
Please read file [LICENSE](LICENSE) for details.

# Credits
Please read file [CONTRIBUTORS](CONTRIBUTORS.md) for list of contributors.
