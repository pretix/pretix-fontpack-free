Fontpack: Free fonts
====================

This is a plugin for `pretix`_ that adds fonts to the PDF editor.

Font list
---------

* Roboto, Christian Robertson, Apache License 2.0
* Lato, Lukasz Dziedzic, SIL Open Font License
* Montserrat, The Montserrat Project Authors, SIL Open Font SLicense
* Fira Sans, Mozilla, SIL Open Font License
* Noto Sans, Google, SIL Open Font License
* Droid Serif, Google, Apache License 2.0
* Vollkorn, FRiTZe, SIL Open Font License

Development setup
-----------------

1. Make sure that you have a working `pretix development setup`_.

2. Clone this repository, eg to ``local/pretix-fontpack-free``.

3. Activate the virtual environment you use for pretix development.

4. Execute ``python setup.py develop`` within this directory to register this application with pretix's plugin registry.

5. Execute ``make`` within this directory to compile translations.

6. Restart your local pretix server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.


License
-------

Copyright 2017 Raphael Michel

Released under the terms of the Apache License 2.0


.. _pretix: https://github.com/pretix/pretix
.. _pretix development setup: https://docs.pretix.eu/en/latest/development/setup.html
