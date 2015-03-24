<!--
.. title: Bayesian Evidence Calculation
.. slug: bayesian-evidence
.. date: 2014-10-03 08:00:00 UTC-07:00
.. tags: hacking, bayesian evidence
.. author: Kyle Barbary
.. link:
.. description: Methods for calculating Bayesian evidence
.. type: text
-->

In a Bayesian framework, object classification or model comparison can
be done naturally by comparing the Bayesian _evidence_ between two or
more models, given the data. The evidence is the integral of the
likelihood of the data over the entire prior volume for all the model
parameters, weighted by the prior. (The ratio of evidence for two
different models is known as the [Bayes
Factor](http://en.wikipedia.org/wiki/Bayes_factor).) This
multi-dimensional integral gets increasingly computationally intensive
as the number of parameters increases. As a result, several clever
algorithms have been developed to efficiently approximate the answer.

In this hack, I looked at a couple specific implementations of such
algorithms in Python.

<!-- TEASER_END -->

Thermodynamic integration in Emcee
==================================

Parallel tempering is one way to calculate evidence. Dan F-M's
excellent Python package [Emcee](http://dan.iel.fm/emcee/current/)
includes a `PTSampler` (PT = parallel tempering) that has a method
`PTSampler.thermodynamic_integration_log_evidence()` for performing
the evidence integral after the sampler is run. Phil Marshall ran the
sampler on the test problem from the docs, wherein the likelihood
function is simply a mixture of two 2-d gaussians and the prior is
uniform. For this simple function, the evidence can be calculated
analytically, so the result from `PTSampler` can be checked.

As detailed in an [Emcee pull
request](http://github.com/dfm/emcee/pull/131) it turned out that the
`PTSampler` result didn't match the analytic solution. This appears to
be a bug in `PTSampler`! It's now handed off to one of the Emcee
developers.

Nested sampling in Nestle
=========================

[Nested
sampling](http://en.wikipedia.org/wiki/Nested_sampling_algorithm) is
another algorithm for calculating evidence. There are a number of
variants on the method. Without going into it in detail, the nested
sampling algorithm employs a population of "active" points sampling
the parameter space. The variants are chiefly concerned with
efficiently choosing a new active point from the region of parameter
space occupied by the current active point, *without* being biased by
the existing points.

[MultiNest](http://ccpforge.cse.rl.ac.uk/gf/project/multinest/) is a
popular implementation of one variant, and there is even a [Python
wrapper](http://johannesbuchner.github.io/PyMultiNest/index.html) for
it. While MultiNest is free for academic use, it doesn't have a truly
open-source license, making widespread distribution and installation
more complicated.

Single-ellipsoidal variant
--------------------------

<div style="float:right">
<img src="/images/nested_sampling_single.png">
</div>

I was motivated by the MultiNest licensing issue to make available my
own simple pure-Python implementation of nested sampling in a package
called [Nestle](https://github.com/kbarbary/nestle) (rhymes with
"wrestle"), tuning up the docs and implementing an automated
test. Nestle currently implements a "single-ellipsoidal" variant of
nested sampling, where a single ellipsoid is drawn around active
points, and a new active point is picked uniformly from within the
ellipse. This works well when the likelihood is unimodal: the single
ellipse is a good approximation to the region occupied by the
points. Unfortunately, the method suffers when the likelihood is
multimodal. When this happens, the active points form multiple
clusters in parameter space. Shown at left is what happens when you
draw a single ellipsoid around such points. When you then chose a new
point uniformly from within this ellipse, you're most likely to pick a
point nowhere near the active points (and probably with lower
likelihood than all the active points). You then have to keep picking
new points from within the ellipse until you happen to get a good one.

Multi-ellipsoidal
-----------------

<div style="float:right">
<img src="/images/nested_sampling_multi.png">
</div>

The solution implemented in MultiNest is to try to detect clusters of
points and draw multiple ellipsoids around the clusters (see right
figure).  Picking a point from within these *two* ellipses is much
more likely to yield a point near the existing active points. However,
finding clusters robustly is non-trivial.

Future
======

I plan to keep working on Nestle, for use in my own projects and to make
it available to others. Here's a rough to-do list:

* Make the original "MCMC" sampling variant available as an option.
* Make the multi-ellipsoidal sampling available as an option, possibly
  using the [X-means](http://www.cs.cmu.edu/~dpelleg/kmeans.html)
  clustering algorithm.
* Speed ups if necessary, using Cython.
* I'd like to have a Julia implementation as well.
