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
   :height: 480

   **Figure 1.** A figure created with Matplotlib default settings.

The content is pixelated and hard to read. The figure below looks better.

.. figure:: images/figure_sized.png
   :alt: Default Figure with adjusted size and font properties
   :align: center
   :width: 500
   :height: 200

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

   **Figure 3**. Plain HTML provides full control over the document's look, making it easy to match the font properties of the figure and the webpage.

Part 1: Working with Figures in Matplotlib
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The figure is the central object of this workshop.
In Matplotlib, the figure is the top-level object for all the plot elements.
Mastering the figure object is crucial to creating high-quality visualizations that look nice in the context of the document.

The goal of Part 1 is to create a document with a figure using the same font properties as the rest of the content.

TODO: link to the jupyter notebook.

Axes
~~~~
