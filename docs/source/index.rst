.. ChartCraftHub documentation master file, created by
   sphinx-quickstart on Tue Feb 20 22:07:32 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: images/logo.svg
   :alt: Code, debug, reuse this chart logo
   :align: center

.. note::
   The project is under active development. The documentation is not complete yet.

A home for "Code, debug, reuse this chart" workshop docs. The code is available on [`GitHub <https://github.com/Kislovskiy/ChartCraftHub/>`_].

.. image:: images/amld_code_debug_reuse_this_chart.png
   :alt: Code, debug, reuse this chart
   :align: center

What is Matplotlib?
-------------------

`Matplotlib <https://github.com/matplotlib/matplotlib>`_ is a huge plotting library. In March 2024, the project has ``256024`` lines of code.

.. code-block:: bash

   ~/d/matplotlib ❯❯❯ find . -name "*.py" -exec cat {} + | wc -l
   256024

With approximately ``1114`` classes.

.. code-block:: bash

   ~/d/matplotlib ❯❯❯ find . -name "*.py" -exec grep -h '^\s*class\s\+' {} + | wc -l
   1114

It's a big and very flexible codebase to create any plots.
And with a great power comes a bigger challenge to understand how to use it effectively.
But before we dive into the code, let's ask ourselves a question:

Why do we need a workshop about matplotlib in the era of Large Language Models and ChatGPT?
-------------------------------------------------------------------------------------------

In the `keynote <https://youtu.be/yWhp2v9_UFc?si=h3LNdyIpQE9Vde2w>`_ titled "Training the most important model" at PyConTH 2023, Naomi Ceder made a point, that our mental models of how code and applications work are vital to understanding the capabilities of our tools and fixing their problems when things go wrong.

At "Code, debug, reuse this chart" workshop Artem and Teresa will help you to build the mental model of matplotlib.
This workshop aims to provide insights and skills that LLMs cannot offer: understanding how to utilize matplotlib and organize  Python visualization project for re-usability.

After several attempts on making use of LLM for creating code for this tutorial, with an opinionated view, we could say that ChatGPT is very good in extrapolating words for matplotlib code generation.
This often leads to a "spaghetti code".
The task of condensing the generated content by summarizing and optimizing was almost always failed causing the divergent results and change in the visual output.
This makes us to believe that there are still numerous opportunities for chart craftsmanship and this tutorial should help you to get the necessary skills.

Setup
-----

Check out the :doc:`setup` section for further information, including how to
:ref:`install <installation>` the project.

Contents
--------

.. toctree::

   intro
   setup
   section_1
   section_2
   section_3
   resources
   terminology
