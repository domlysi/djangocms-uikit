# DjangoCMS UiKit

This package implements the UiKit Elements as reusable Plugins for the DjangoCMS. 

### Prerequisites

You need a Django CMS Project. 
If you wanna know how to start a Django CMS Project check the the Docs.

[Django-CMS.org](http://docs.django-cms.org/en/release-3.4.x/introduction/install.html) - Installing Django CMS

### Quick Start
Install DjangoCMS-UiKit:

    python3 -m pip install djangocms-uikit
   
Then add ``djangocms-uikit`` to ``INSTALLED_APPS``

Don't forget:

    python3 manage.py makemigrations
    python3 manage.py migrate
    

Next download the UiKit Files or add the CDNs to your project main template.

Before the ``</head>`` tag:
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/uikit/3.1.7/css/uikit.min.css">
```

Before the ``</body>`` tag:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/uikit/3.1.7/js/uikit.min.js" type="text/javascript"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/uikit/3.1.7/js/uikit-icons.min.js" type="text/javascript"></script>
```

## Built With

* [DjangoCms](https://github.com/divio/django-cms) - The easy-to-use and developer-friendly CMS

## Authors

* **Dominik Lysiak** - *Main Contributor* - [Personal Website](https://dominiklysiak.de)

See also the list of [contributors](https://github.com/domlysi/djangocms-uikit/graphs/contributors) who participated in this project.

## License

This project is licensed - see the [LICENSE.md](LICENSE.md) file for details

## Todo

* Nearly everything for now