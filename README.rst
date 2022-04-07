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
* Oswald, Vermon Adams, SIL Open Font License
* Titillium, Accademia di Belle Arti Urbino, SIL Open Font License
* Space Mono, Colophon Foundry, SIL Open Font License
* DejaVu Sans, Bitstream Vera Fonts Copyright, Arev Fonts Copyright, Public Domain, see https://dejavu-fonts.github.io/License.html
* Baloo Bhaijaan, Ek Type (www.ektype.in), SIL Open Font License
* Tajawal, Boutros International, SIL Open Font License
* Poppins, Indian Type Foundry, SIL Open Font License
* Almarai, Boutros Fonts, SIL Open Font License
* Ubuntu, Canonical, Ubuntu Font License 1.0

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

Copyright 2021 rami.io GmbH

Released under the terms of the Apache License 2.0


.. _pretix: https://github.com/pretix/pretix
.. _pretix development setup: https://docs.pretix.eu/en/latest/development/setup.html
