<!--
.. title: Hack the textbook figures
.. slug: Hack-the-textbook-figures
.. date: 2014-10-05 11:00:00 UTC-07:00
.. tags: hacking, visualization, statistics, machine learning, IPython Notebook
.. author: Michael Gully-Santiago
.. link:
.. description: Hacking on the Statistics, Data Mining, and Machine Learning in Astronomy Textbook figures
.. type: text
-->

Every single figure in the [text book](http://press.princeton.edu/titles/10159.html) *Statistics, Data Mining, and Machine Learning in Astronomy* is [downloadable and fully reproducible online](http://www.astroml.org/book_figures/).  Jake VanderPlas accomplished this heroic feat as a graduate student at the University of Washington.  Jake recalled the origin story to some of us at the hack week.  He explained that he would usually have the figure done the same week it was conceived, and was really pretty happy with the whole experience of being a part of making the textbook and ultimately becoming a coauthor.  His figures are now indispensable. Because of Jake's investment, generations of astronomers to come can now benefit from reproducing the explanatory material in the Textbook.  The figures are complementary to the textbook prose.  The textbook prose explains the theoretical framework underlying the concepts.  Equations are derived.  But by digging into the textbook figure Python code, the reader can see how the method is *implemented*, and try it out by tweaking the input.  "What happens if I double the noise? Or decimate the number of data points?  Or change this-or-that parameter?  How long does it take to run?"  

These and other questions motivated my hack idea, which was to dig into the source code of textbook figures and do some hacking.  

<div id="test_figure"></div>
<script type="text/javascript" src="/js/hack-book-figs.js"></script>
<script>
  draw_figure("test_figure");
</script>

So on Wednesday of the Hack Week a table of about 8 of us all hacked the book figures.  The figure above is one of those figures, 
<!-- TEASER_END -->
hacked by Beth Reid (BIDS) and Phil Marshall (SLAC).  Beth and Phil *pair-coded* on Figure 8.10 (*c.f.* [the original figure](http://www.astroml.org/book_figures/chapter8/fig_gp_example.html)).  This choice of figure and its redesign were both inspired by Hack Week breakout sessions!  Specifically, Dan Foreman-Mackey's Gaussian Process breakout on Monday, and Jake's breakout on [D3.js](http://d3js.org/) and his matplotlib wrapper for it, [MPLD3](http://mpld3.github.io/).  As you can see, Beth and Phil's figure shows a special hover-over effect for different realizations of the Gaussian Process curves consistent with the data points.  See the textbook, the figure caption, and/or [Dan's Gaussian Process Tutorial](https://speakerdeck.com/dfm/an-astronomers-introduction-to-gaussian-processes-v2) for further discussion.

Hack Week participants Wilma Trick and Michael Walther (MPIA Heidelberg, Germany) hacked on Figure 9.14, [available here](http://gully.github.io/astroMLfigs/html/fig09_14.html).  Ruth Angus (Oxford, currently a pre-doctoral visitor at CfA) made an interactive version of Figure 9.2 using IPython Notebooks.
Specifically, she changed the mean center positions of the two clusters of points in the figures to address the question-  "What happens if the classification boundary is not so obvious?  How does the classifier grapple with uncertainty?"  It was fascinating to see the classification boundary update in real-time as Ruth dragged the `interact()` slider left and right.

You can find all of the submitted hacked book figures on the project page: [http://gully.github.io/astroMLfigs/](http://gully.github.io/astroMLfigs/).  I welcome hack submissions from the community!  If you have hacked on one of Jake's book figures, please submit it via GitHub pull request to the GitHub repository.

Meanwhile, I worked on a visualization of my ongoing observational research project on discovery and characterization of young brown dwarfs in nearby star forming regions.
Specifically, my hack was aimed at visualizing the spatial distributions of sources in my custom multi-band photometric catalog compared to existing catalogs.  I used hover-over tooltips to gain instantaneous, detailed information on each source.  This hack was not merely of academic interest- I wanted a quick way to spot-check cross matched catalogs to see how well the matching performed on individual regions.  In the past I have detected astrometric solution errors in this way, for example.  The scroll wheel offered smooth dynamic range zooming from degree to arcsecond field-of-view.  The key challenge/innovation here was that my catalog contained 54,000 sources, which is too many for MPLD3, even on modern machines.  So I used the [Bokeh Plot Library](http://bokeh.pydata.org/), which I had learned about a week earlier from Bryan Van de Ven (Continuum Analytics) at the Austin Python Users Group [meetup](http://www.meetup.com/austinpython/).  Bokeh is similar to MPLD3, but it has some distinct advantages for displaying massive datasets.  Specifically their Abstract Rendering implementation has been shown to handle over 4 GB of census data.  Since Bokeh (and MPLD3) are effectively converting the figures into javascript, the figures look great in the browser, notably IPython Notebooks.  I'm planning to release my hack alongside a future publication describing the custom photometric catalog.