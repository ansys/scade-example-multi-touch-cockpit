.. _contribute_SCADE_MULTI_TOUCH_COCKPIT:

Contribute
##########

Overall guidance on contributing to a PyAnsys library appears in
`Contributing <https://dev.docs.pyansys.com/how-to/contributing.html>`_
in the *PyAnsys developer's guide*. Ensure that you are thoroughly familiar
with this guide before attempting to contribute to the Ansys SCADE multi-touch
cockpit example.

The following contribution information is specific to the Ansys SCADE multi-touch
cockpit interface.

Install in developer mode
-------------------------

Installing the Ansys SCADE multi-touch cockpit interface in developer mode allows you to modify the
source and enhance it.

#. Clone the ``ansys-scade-example-multi-touch-cockpit`` repository:

   .. code:: bash

      git clone https://github.com/ansys/scade-example-multi-touch-cockpit.git

#. Access the ``scade-example-multi-touch-cockpit`` directory where the repository has been cloned:

   .. code:: bash

      cd scade-example-multi-touch-cockpit

#. Create a clean Python 3.10 environment and activate it:

   You should use the interpreter delivered with Ansys SCADE. For example,
   ``C:\Program Files\ANSYS Inc\v232\SCADE\contrib\Python310\python.exe``.

   .. code:: bash

      # Create a virtual environment
      python -m venv .venv

      # Activate it in Windows CMD environment
      .venv\Scripts\activate.bat

      # Activate it in Windows Powershell
      .venv\Scripts\Activate.ps1

#. Make sure that you have the latest required build system, documentation, testing,
   and CI tools:

   .. code:: bash

      python -m pip install -U pip     # Upgrading pip
      python -m pip install -r requirements/requirements_doc.txt     # for building the documentation

Use ``pre-commit``
^^^^^^^^^^^^^^^^^^
The example for the Ansys SCADE boiler plate interface follows the PEP8 standard as outlined in
`PEP 8 <https://dev.docs.pyansys.com/coding-style/pep8.html>`_ in
the *PyAnsys developer's guide* and implements style checking using
`pre-commit <https://pre-commit.com/>`_.

To ensure your code meets minimum code styling standards, run these commands::

  pip install pre-commit
  pre-commit run --all-files

You can also install this as a pre-commit hook by running this command::

  pre-commit install

This way, it's not possible for you to push code that fails the style checks::

  $ pre-commit install
  $ git commit -am "added my cool feature"
  Add License Headers......................................................Passed
  check for merge conflicts................................................Passed
  debug statements (python)................................................Passed
  trim trailing whitespace.................................................Passed
  check yaml...............................................................Passed
  fix requirements.txt.....................................................Passed
  Check GitHub workflows...................................................Passed

Build documentation
-------------------
To build documentation, you can run these commands:

.. code:: bash

    # build and view the doc from a Windows environment
    .\doc\make.bat clean
    .\doc\make.bat html
    start .\doc\_build\html\index.html

Post issues
-----------
Use the `Issues <https://github.com/ansys/scade-example-multi-touch-cockpit/issues>`_
page for this repository to report bugs and request new features. When possible,
use the issue templates provided. If your issue does not fit into one of these templates,
click the link for opening a blank issue.

If you have general questions about the PyAnsys ecosystem, email
`pyansys.core@ansys.com <pyansys.core@ansys.com>`_. If your
question is specific to the Ansys SCADE multi-touch
cockpit interface, ask your question in an issue as described
in the previous paragraph.

.. LINKS AND REFERENCES


.. _pip: https://pypi.org/project/pip/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
