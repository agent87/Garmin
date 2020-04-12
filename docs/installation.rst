============
Installation
============

The bare minimum required to install Alabaster is as follows:

* If you're on **Sphinx 1.2 or older**:

    * ``pip install alabaster`` or equivalent.
    * Add the following to your ``conf.py`` so Alabaster's theme location &
      mini-extension are located & loaded:

       .. code-block:: python

            import alabaster

            html_theme_path = [alabaster.get_path()]
            extensions = ['alabaster']
            html_theme = 'alabaster'

    * If you've installed Alabaster by hand (without using ``pip``) and/or are
      doing funky things to your PYTHONPATH, you may need to replace the
      ``alabaster.get_path()`` call with your own explicit string, as per `the
      Sphinx config docs
      <http://sphinx-doc.org/config.html#confval-html_theme_path>`_.

* If you have **Sphinx 1.3 or above**: