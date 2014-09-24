AstroData Website
=================
Website build with [Nikola](http://getnikola.com)

To build this site, first install the prerequisites:

```
[~]$ conda install ipython-notebook markdown jinja2 pip
[~]$ pip install nikola
```

Then you can build the site using

```
[~]$ nikola build
```

and preview using

```
[~]$ nikola serve
```

And point your browser to http://localhost:8000

How to Contribute
-----------------
Hack Week Participants: you can contribute a post by writing what you'd like to say either in markdown, restructured text, plain text, or an IPython notebook.
Check out the ``posts/`` subdirectory of this repository for some examples.
Any images or figures you'd like to include (other than those embedded in IPython notebooks) can be put in the ``files/images/`` directory.
If you have something you'd like to post, you can email it to Jake (or better, submit it via a pull request), and Jake will take care of adding it to the blog and pushing the content to the web.

For examples of posts in markdown and notebook format, see the [posts subdirectory](https://github.com/AstroHackWeek/website_source/tree/master/posts) of this repository. Note that markdown posts contain some metadata at the top of the file, while notebook posts have metadata in a separate file.


Feel free to open issues with any questions you have or any problems with the site. Thanks!
