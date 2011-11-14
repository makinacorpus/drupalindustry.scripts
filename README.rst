########################
drupalindustry.templates
########################

Scripts around Drupal deployment (install, clean, ...) in drupalindustry
environments. Uses drush and Python.

************
Installation
************

From source
===========

* Install Python. This software was developed with Python 2.6.
* Get the source:
  ::

    git clone https://github.com/makinacorpus/drupalindustry.scripts.git
    cd drupalindustry.scripts

* Build package, i.e. install dependencies and configure environment:
  ::

    python bootstrap.py -d
    bin/buildout

* You got a local bin/drupalindustry command.

*****
Usage
*****

::

  bin/drupalindustry COMMAND

Where COMMAND is one of:

* clean-all
* clean-db
* clean-files
* clean-settings
* create-db
* delete-db
* get-drush
* install
* make
* reinstall
