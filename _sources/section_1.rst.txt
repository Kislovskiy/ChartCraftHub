1. Exploring Matplotlib Internals: Figures, Axes, and More
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. section_1:

In this section
~~~~~~~~~~~~~~~


Figure
~~~~~~

According to the Oxford English Dictionary, the word "figure" has several meanings.

**Figure**

- **n**
  1. a number or numerical symbol.
  2. a geometric or decorative shape defined by one or more lines.
  3. a diagram or illustrative drawing.

- **v**
  1. play an important part.
  2. calculate arithmetically.
  3. (*figure someone/thing out*) understand someone or something.
  4. think; consider.

In many cases, figures do not exist in isolation, they appear in the text, presentation, or webpage.

Have you ever noticed that in many places, figures look alien?
They are very different than the rest of the environment they are placed in.

Here is an example of such a figure:

.. figure:: images/default_figure.png
   :alt: Default Figure
   :align: center
   :width: 640

   **Figure 1.** A figure created with Matplotlib default settings.

The content is pixelated and hard to read. The figure below looks better.

.. figure:: images/figure_sized.png
   :alt: Default Figure with adjusted size and font properties
   :align: center
   :width: 500

   **Figure 2.** A figure with adjusted shape size and font size.

There is still a tiny misalignment regarding fonts with the rest of the webpage.
But this is quite a complex problem to align.
Matplotlib excels in generating high-quality figures.

In the context of this workshop, a Figure is an object with physical properties like width and height.
It also contains axes, lines, fonts, and legends.

You don't need to be a designer to create pretty figures; start with the right Figure size and font properties.
This should improve the overall integrity of the documents because the plots will look like they belong to the rest of the document.

For example, here is a screenshot of a simple HTML page we'll create in the first part of the workshop.
Looks like LaTeX, right?
But it is not; it is just an HTML page with an appropriately configured Matplotlib figure.

.. figure:: images/cmf10_html_example.png
   :alt: example of html page with uniform font properties
   :align: center
   :width: 398

   **Figure 3**. Plain HTML provides full control over the document's look, making it easy to match the font properties of the figure and the webpage.

Part 1: Working with Figures in Matplotlib
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The figure is the central object of this workshop.
In Matplotlib, the figure is the top-level object for all the plot elements.
Mastering the figure object is crucial to creating high-quality visualizations that look nice in the context of the document.

The goal of Part 1 is to create a document with a figure using the same font properties as the rest of the content.

TODO: link to the jupyter notebook.

**Matplotlib Documentation Pointers:**

* https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_size_units.html#sphx-glr-gallery-subplots-axes-and-figures-figure-size-units-py

* https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo.html#sphx-glr-gallery-text-labels-and-annotations-fonts-demo-py

* https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_file.html#sphx-glr-gallery-text-labels-and-annotations-font-file-py

* https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_family_rc.html#sphx-glr-gallery-text-labels-and-annotations-font-family-rc-py

* https://matplotlib.org/stable/gallery/text_labels_and_annotations/usetex_fonteffects.html#sphx-glr-gallery-text-labels-and-annotations-usetex-fonteffects-py

Anatomy of a Figure
~~~~~~~~~~~~~~~~~~~

.. figure:: images/anatomy.png
   :alt: Anatomy of a Figure by N. Rougier
   :align: center
   :width: 480

   **Figure 3**. Anatomy of a Figure by N. Rougier (`source <https://github.com/rougier/scientific-visualization-book/blob/master/code/anatomy/anatomy.py>`_).


Axes
~~~~

* https://matplotlib.org/stable/gallery/axisartist/axis_direction.html#sphx-glr-gallery-axisartist-axis-direction-py

* https://matplotlib.org/stable/gallery/axisartist/demo_axisline_style.html#sphx-glr-gallery-axisartist-demo-axisline-style-py

Summary
~~~~~~~


