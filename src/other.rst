.. rst-class:: center

`SPARTA WWW Site <index.html>`_ 

.. _sws: index.html



.. _pizza: https://lammps.github.io/pizza




----------


Other Codes and Tools
=====================

This page gives pointers to other DSMC codes, as well as various
software tools which can be useful in conjunction with SPARTA.

We are happy to "advertise" other codes and tools here.  Send the
`authors <authors.html>`_ an email if you want to add your software to
the list.


----------


Other DSMC codes
----------------

These are other general-purpose DSMC codes we are aware of, which may
be well-suited to the problems you want to model.  Most of them are
not available for direct download, but you can contact the authors for
more information.  This `Wikipedia DSMC page <https://en.wikipedia.org/wiki/Direct_simulation_Monte_Carlo>`_ has some additional
information on these codes and the groups who sponsor them.

.. _wiki: https://en.wikipedia.org/wiki/Direct_simulation_Monte_Carlo



+----------------+----------------------------------------------------------------------------------+
| DS1V,DS2V,DS3V | original DSMC codes by Graeme Bird                                               |
+----------------+----------------------------------------------------------------------------------+
| DAC            | from Jay LeBeau's group at NASA                                                  |
+----------------+----------------------------------------------------------------------------------+
| MGDS           | from Tom Schwartzentruber's group at U Minnesota                                 |
+----------------+----------------------------------------------------------------------------------+
| dsmcFoam       | an implementation of DSMC within the OpenFoam CFD package                        |
+----------------+----------------------------------------------------------------------------------+
| Monaco         | from Iain Boyd's group at U Michigan                                             |
+----------------+----------------------------------------------------------------------------------+
| SMILE          | from the Khristianovich Institute of Theoretical and Applied Mechanics in Russia |
+----------------+----------------------------------------------------------------------------------+
| PI-DSMC        | parallel version of DS2V and DS3V by Martin Rose of the PI-DSMC company          |
+----------------+----------------------------------------------------------------------------------+

Of these codes, SPARTA is most similar to DAC and MGDS in the way it
uses hierarchical Cartesian grids and embeds triangulated surfaces
into the grid, resulting in cut and split grid cells.


----------


These are high-quality visualization packages we have used for
particle simulations and can recommend.

* `TecPlot <https://www.tecplot.com>`_
* `VMD <http://www.ks.uiuc.edu/Research/vmd>`_
* `AtomEye <http://li.mit.edu/Archive/Graphics/A/>`_

TecPlot can work with grid and surface element data based on SPARTA
output.  VMD and AtomEye are particle visualizers widely used for
molecular dynamics data.  SPARTA writes out its `particle dump files <doc/dump.html>`_ in formats compatible with these programs, or
which can be converted via `auxiliary tools <doc/Section_tools.html>`_ to
the needed format.

We are also currently working on enabling SPARTA output of particles,
grid, and surface element data to be visualized by
`ParaView <https://www.paraview.org>`_.

Our group has also written and released a toolkit called
`Pizza.py <https://lammps.github.io/pizza>`_ which provides some tools for doing SPARTA pre- and
post-processing, and which includes a simple OpenGL-based
visualization tool called `gl <https://lammps.github.io/pizza/doc/gl.html>`_.
Pizza.py is written in `Python <https://www.python.org>`_, and is
available for download from `this page <https://sjplimp.github.io/download.html>`_.  It also
includes tools that convert SPARTA particle dumps into input formats
readable by VMD and AtomEye.

