# AstroData Hack Week Website

This is the source of the website found at http://astrohackweek.github.io/

## How to Contribute

Hack Week 2014 Participants: you can contribute a post by writing what you'd like to say either in markdown, restructured text, plain text, or an IPython notebook. If you're comfortable with github and the Pull Request system, that's the best way to do things. If not, then feel free to email your content to Jake, and he will post it for you!

Please feel free to email Jake or to file an Issue in this repository with any questions you have.

For those contributing via github, here are some tips:

### Contributing via markdown

For markdown, create a file in the ``posts/`` subdirectory. You can model your file off [``posts/astro-hack-week-wrapup.md``](https://raw.githubusercontent.com/AstroHackWeek/website_source/master/posts/astro-hack-week-wrapup.md). Note that the HTML at the top is optional: it just inserts the picture into the file. For a quick summary of using markdown, see [the Daring Fireball guide](http://daringfireball.net/projects/markdown/)

At the top of each markdown file is some blog metadata. You can modify that by hand with your post's title, author, date, etc. After adding your post to the directory, submit it as a pull request, and Jake will push it to the website!

### Developing markdown on the Hackpad

You can export your hackpad to markdown by clicking on your profile picture or name on teh righthand sidebar, and then selecting "download as markdown" or somesuch. This will export all of the hackpads that you own to a zip archive, which you can unpack and then check in. It's nice to leave your hackpad in good shape, so this approach has some value.

### Images for posts

If you have image files you'd like to include in your post, you can put them in the ``files/images`` subdirectory, and reference them using an HTML tag (e.g. ``<img src="/images/HackWeek.jpg" width="300px">``).

### Contributing via Notebook

This blog build system is set up to accept posts composed entirely in IPython notebook. All this requires is to put the notebook file in the ``posts/`` subdirectory, and to add a metadata file. For example, the post within [``posts/multi-output-random-forests.ipynb``](https://github.com/AstroHackWeek/website_source/blob/master/posts/multi-output-random-forests.ipynb) has metadata in [``posts/multi-output-random-forests.meta``](https://github.com/AstroHackWeek/website_source/blob/master/posts/multi-output-random-forests.meta). If you send a pull request containing your notebook plus an associated metadata file, Jake will be able to quickly publish your post to the web.

# How to Build the Site

If you wish to build a copy of the site locally and check how your post will be displayed once it is published, you will first need to install the [Nikola](http://getnikola.com) Python package and a few prerequisites. If you're using Anaconda for your Python setup, it can be done as follows:

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

And point your browser to http://localhost:8000.

If you'd like to publish the site to http://astrohackweek.github.io, then use ``nikola deploy`` (Note: you need to be one of the site maintainers in order to do this).
