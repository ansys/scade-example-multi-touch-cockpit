.. role:: raw-html-m2r(raw)
   :format: html

Getting started
===============

Install
-------
To install the multi-touch cockpit interface, run this command to clone the
`repository <https://github.com/ansys/scade-example-multi-touch-cockpit>`_
to your local machine

.. code-block:: bash

    git clone https://github.com/ansys/scade-example-multi-touch-cockpit.git


Generate, build, and execute standalone interface
-------------------------------------------------

#. Launch SCADE Display.

#. Select **File > Open** and then the ``model/scade-display/DisplayPanel.etp``
   project.

   .. raw:: html

      <p align="center">
        <img src="_static/fileOpenP.png" alt="file open"/>
      </p>

#. Select the ``Windows`` configuration to enable the generation of a standalone application
   running on Windows.

   .. raw:: html

      <p align="center">
        <img src="_static/selectConf.png" alt="select conf"/>
      </p>

#. Click **Execute**.

   .. raw:: html

      <p align="center">
        <img src="_static/execute.png" alt="execute"/>
      </p>


Test execution on host
----------------------

#. Launch SCADE Test.

#. Select **File > Open** and then the ``model/scade-test/SmartBoilerControl_Test.etp``
   SCADE test projet.

   .. raw:: html

      <p align="center">
        <img src="_static/fileOpenSCADE.png" alt="file open scade"/>
      </p>

#. Select **Project > Test tool > Execute tests**.

   .. raw:: html

      <p align="center">
        <img src="_static/executeTests.png" alt="execute tests"/>
      </p>
