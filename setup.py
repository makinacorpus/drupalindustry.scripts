from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='drupalindustry.scripts',
      version=version,
      description="Scripts around Drupal deployment (install, clean, ...) " \
                  "in drupalindustry environments. Uses drush.",
      long_description=open("README.rst").read() + "\n",
      classifiers=["Programming Language :: Python", ],
      keywords="drupal deployment deploy install",
      author='Benoit Bryon',
      author_email='benoit.bryon@makina-corpus.com',
      url='https://github.com/makinacorpus/drupalindustry.scripts',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'': 'src'},
      namespace_packages=['drupalindustry'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools', ],
      entry_points=""" # -*- Entry points: -*-
      [console_scripts]
      drupalindustry = drupalindustry.scripts.commands:main
      """,
      )
