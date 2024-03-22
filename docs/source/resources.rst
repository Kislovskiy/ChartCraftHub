Resources and Tools We Use
==========================

.. _resources:



Matplotlib
----------

* `Matplotlib cheatsheets <https://matplotlib.org/cheatsheets/>`_

* `Matplotlib making a helper function <https://matplotlib.org/stable/users/explain/quick_start.html#making-a-helper-functions>`_

* `Nicolas P. Rougier. Scientific Visualization: Python + Matplotlib <https://github.com/rougier/scientific-visualization-book>`_
    This book is one of Artem's favorite resources.
    It covers many advanced topics with great detail.
    Rougier's book is almost impossible to read quickly as each page makes you think.
    The chapter on Figure design is among Artem's favorites.
    The book is available for free on GitHub.

* `Orland, Paul. Math for Programmers <https://www.manning.com/books/math-for-programmers>`_
    The idea of using mathematics in this workshop came from Paul Orland's book.
    The book is a great resource, and since many mathematical concepts reuse the same ideas, it became an excellent resource for writing a workshop on code reusability.

* `Matthes, Eric. Python crash course: A hands-on, project-based introduction to programming <https://nostarch.com/python-crash-course-3rd-edition>`_
    It takes a lot of work to explain complex topics to beginners.
    Eric writes his books so that even experienced programmers can find something they didn't know before.
    A Python crash course book has a chapter on data visualization and maptlotlib worth checking out.
    He also maintains several helpful cheat sheets, including one for Matplotlib, on his `website <https://ehmatthes.github.io/pcc_3e/cheat_sheets/>`_.

* `Golden Ratio SymPy <https://github.com/sympy/sympy/blob/master/sympy/core/numbers.py#L3794-L3854>`_

* `Golden Ratio Wiki <https://en.wikipedia.org/wiki/Golden_ratio>`_

Libraries build on top of Matplotlib
------------------------------------

* `seaborn <https://github.com/mwaskom/seaborn>`_
* `aquarel <https://github.com/lgienapp/aquarel>`_

Advice on project organization
------------------------------
* `Matplotlib has a cookiecutter template <https://github.com/matplotlib/matplotlib-extension-cookiecutter>`_

* `Best Practices for Data Science Project Workflows and File Organization <https://github.com/moldach/project-directory>`_


Workshop Writing Resources
--------------------------

Artem wrote this section to remind himself of the resources he used to write a workshop.
He was inspired to start writing the tutorial after of Daniele Procida the autor of `Diátaxis <https://diataxis.fr/>`_.

Quotes from books
-----------------
* `Matthes, Eric. Python crash course: A hands-on, project-based introduction to programming <https://nostarch.com/python-crash-course-3rd-edition>`_
    * "One of the most popular tools is Matplotlib, a mathematical plotting library. In this chapter, we'll use Matplotlib to make simple plots, such as line graphs and scatter plots."
    * "A colormap is a sequence of colors in a gradient that moves from a starting to an ending color."
    * "Matplotlib assumes your screen resolution is 100 pixels per inch; if this code doesn't give you an accurate plot size, adjust the numbers as necessary. Or, if you know your system's resolution, you can pass subplots() the resolution using the dpi parameter:"

* Dale, Kyran. Data Visualization with Python and JavaScript. " O'Reilly Media, Inc.", 2022.
    "Often the best chart for the job is a static chart where full editorial control lies with the creator."

    "In essence, with OO Matplotlib we are dealing with a figure, which you can think of as a drawing canvas with one or more axes (or plots) embedded in it. Both figures and axes have properties that can be independently specified."



* Knaflic, Cole Nussbaumer. Storytelling with data: A data visualization guide for business professionals. John Wiley & Sons, 2015.
    * "Understanding and employing concepts like the 3-minute story, the Big Idea, and storyboarding will enable you to clearly and succinctly tell your story and identify the desired flow."

    * "The 3-minute story is exactly that: if you had only three minutes to tell your audience what they need to know, what would you say? This is a great way to ensure you are clear on and can articulate the story you want to tell."

    * "If you need to communicate multiple different units of measure, this is also typically easier with a table than a graph."

    * "If I had to pick a single go-to graph for categorical data, it would be the horizontal bar chart, which flips the vertical version on its side. Why? Because it is extremely easy to read."

    * "Kurt Vonnegut (author of novels such as Slaughterhouse-Five and Breakfast of Champions) outlined the following tips, which I've excerpted from his short article, “How to Write with Style” (a great quick read):

        1. Find a subject you care about. It is this genuine caring, and not your games with language, which will be the most compelling and seductive element in your style.
        2. Do not ramble, though.
        3. Keep it simple. Great masters wrote sentences which were almost childlike when their subjects were most profound. “To be or not to be?” asks Shakespeare’s Hamlet. The longest word is three letters.
        4. Have the guts to cut. If a sentence, no matter how excellent, does not illuminate your subject in some new and useful way, scratch it out.
        5. Sound like yourself. I myself find that I trust my own writing most, and others seem to trust it most, too, when I sound most like a person from Indianapolis, which is what I am.
        6. Say what you meant to say. If I broke all the rules of punctuation, had words mean whatever I wanted them to mean, and strung them together higgledy-piggledy, I would simply not be understood.
        7. Pity the readers. Our audience requires us to be sympathetic and patient teachers, ever willing to simplify and clarify.

    * "Strategies for avoiding the spaghetti graph"
    * "When presenting content in a live setting, you want to be able to walk your audience through the story, focusing on just the relevant part of the visual. However, the version that gets circulated to your audience—as a pre-read or takeaway, or for those who weren't able to attend the meeting—needs to be able to stand on its own without you, the presenter, there to walk the audience through it."
    * "For example, I could start with a blank graph. This forces the audience to look at the graph details with you, rather than jump straight to the data and start trying to interpret it. You can use this approach to build anticipation within your audience that will help you to retain their attention. From there, I subsequently show or highlight only the data that is relevant to the specific point I am making, forcing the audience's attention to be exactly where I want it as I am speaking."

* VanderPlas, Jake. Python data science handbook: Essential tools for working with data. " O'Reilly Media, Inc.", 2016.
    * "Newer tools like ggplot and ggvis in the R language, along with web visualization toolkits based on D3js and HTML5 canvas, often make Matplotlib feel clunky and old-fashioned. Still, I'm of the opinion that we cannot ignore Matplotlib's strength as a well-tested, cross-platform graphics engine."

* McKinney, Wes. Python for data analysis. " O'Reilly Media, Inc.", 2022.
    * "matplotlib is a desktop plotting package designed for creating plots and figures suitable for publication. The project was started by John Hunter in 2002 to enable a MATLAB-like plotting interface in Python."
    * "Rather than use multiple visualization tools in this book, I decided to stick with matplotlib for teaching the fundamentals, in particular since pandas has good integration with matplotlib. You can adapt the principles from this chapter to learn how to use other visualization libraries as well."
    * "These plot axis objects have various methods that create different types of plots, and it is preferred to use the axis methods over the top-level plotting functions like plt.plot. For example, we could make a line plot with the plot method (see Figure 9-3):"
    * "The axes class has a set method that allows batch setting of plot properties."
    * "To exclude one or more elements from the legend, pass no label or label="_nolegend_"."
    * "that are geared primarily toward preparing figures for publication."
    * "As we'll see in the next section, the seaborn package has several built-in plot themes or styles that use matplotlib's configuration system internally."
    * "For creating static graphics for print or web, I recommend using matplotlib and libraries that build on matplotlib, like pandas and seaborn, for your needs. For other data visualization requirements, it may be useful to learn how to use one of the other available tools. I encourage you to explore the ecosystem as it continues to evolve and innovate into the future."


* Johansson, R. Numerical Python: Scientific Computing and Data Science Applications with Numpy, SciPy and Matplotlib, Apress, Berkeley, CA, 2019.
    The idea of showing multiple subplots next to each other to easily compare the different representation of the data.

