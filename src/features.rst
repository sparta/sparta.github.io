.. rst-class:: center

`SPARTA WWW Site <index.html>`_ 

.. _sws: index.html




----------


SPARTA Features
===============

SPARTA is a Direct Simulation Monte Carlo (DSMC) code, suitable for
modeling low-density gases.  It has these general classes of
functionality:

* `General features <#general>`_
* `Models <#models>`_
* `Geometry <#geometry>`_
* `Gas-phase collisions and chemistry <#collisions>`_
* `Surface collisions <#surface>`_
* `Performance <#perf>`_
* `Diagnostics <#diag>`_
* `Output <#output>`_
* `Pre- and post-processing <#prepost>`_

A general overview of SPARTA is given in the `intro section <doc/Section_intro.html>`_ of the `SPARTA documentation <doc/Manual.html>`_.  To learn details of a feature, find
the input script command(s) that implement it, and read `their doc pages <doc/Section_commands.html#cmd_5>`_.


----------


.. raw:: html

   <span id="general"></span>

General features
--------------------------------------------------------------

* runs on a single processor or in parallel
* distributed-memory message-passing parallelism (MPI)
* spatial-decomposition of simulation domain for parallelism
* open-source distribution
* highly portable C++
* optional libraries used: MPI
* `easy to extend <doc/Section_modify.html>`_ with new features and functionality
* runs from an `input script <doc/Section_commands.html>`_
* syntax for defining and using `variables and formulas <doc/variable.html>`_
* syntax for `looping over runs <doc/jump.html>`_ and breaking out of loops
* run one or `multiple simulations simultaneously <doc/Section_howto.html#howto_3>`_ (in parallel) from one script
* `build as library <doc/Section_start.html#start_3>`_, invoke SPARTA thru `library interface <doc/Section_howto.html#howto_6>`_ or provided `Python wrapper <doc/Section_python.html>`_
* `couple with other codes <doc/Section_howto.html#howto_7>`_: SPARTA calls other code, other code calls SPARTA, umbrella code calls both

.. raw:: html

   <span id="models"></span>

Models
---------------------------------------------------

* `3d or 2d <doc/dimension.html>`_ or `2d-axisymmetric <doc/Section_howto.html#howto_2>`_ domains
* variety of `global boundary conditions <doc/boundary.html>`_
* `create particles <doc/create_particles.html>`_ within flow volume or at `inlet boundaries <doc/fix_emit_face.html>`_
* emit particles from simulation box faces due to `flow properties <doc/fix_emit_face.html>`_
* emit particles from simulation box faces due to `profile defined in file <doc/fix_emit_face_file.html>`_
* emit particles from surface elements due to `normal and flow properties <doc/fix_emit_surf.html>`_
* `ambipolar <doc/Section_howto.html#howto_11>`_ approximation for ionized plasmas

.. raw:: html

   <span id="geometry"></span>

Geometry
-------------------------------------------------------

* `Cartesian, heirarchical grids <doc/Section_intro.html#intro_3>`_ with multiple levels of local refinement
* `create grid from input script <doc/create_grid.html>`_ or `read from file <doc/read_grid.html>`_
* embed `triangulated (3d) or line-segmented (2d) surfaces <doc/Section_intro.html#intro_3>`_ in grid, `read in from file <doc/read_surf.html>`_

.. raw:: html

   <span id="collisions"></span>

Gas-phase collisions and chemistry
-----------------------------------------------------------------------------------

* collisions between all particles or pairs of species groups within grid cells
* `collision models: <doc/collide.html>`_ VSS (variable soft sphere), VHS (variable hard sphere), HS (hard sphere)
* `chemistry models: <doc/react.html>`_ TCE, QK

.. raw:: html

   <span id="surface"></span>

Surface collisions and chemistry
------------------------------------------------------------------------------

* for surface elements or global simulation box `boundaries <doc/bound_modify.html>`_
* `collisions: <doc/surf_collide.html>`_ specular or diffuse
* `reactions <doc/surf_react.html>`_

.. raw:: html

   <span id="perf"></span>

Performance
------------------------------------------------------

* `grid cell weighting <doc/global.html>`_ of particles
* `adaptation <doc/adapt_grid.html>`_ of the grid cells between runs
* `on-the-fly adaptation <doc/fix_adapt.html>`_ of the grid cells
* `static <doc/balance_grid.html>`_ load-balancing of grid cells or particles
* `dynamic <doc/fix_balance.html>`_ load-balancing of grid cells or particles

.. raw:: html

   <span id="diag"></span>

Diagnostics
------------------------------------------------------

* `global boundary statistics <doc/compute_boundary.html>`_
* `per grid cell statistics <doc/compute_grid.html>`_
* `per surface element statistics <doc/compute_surf.html>`_
* time-averaging of `global <doc/fix_ave_time.html>`_, `grid <doc/fix_ave_grid.html>`_, `surface <doc/fix_ave_surf.html>`_ statistics

.. raw:: html

   <span id="output"></span>

Output
---------------------------------------------------

* `log file of statistical info <doc/stats_style.html>`_
* `dump files <doc/dump.html>`_ (text or binary) of per particle, per grid cell, per surface element values
* binary `restart files <doc/restart.html>`_
* on-the-fly `rendered images and movies <doc/dump_image.html>`_ of particles, grid cells, surface elements

.. raw:: html

   <span id="prepost"></span>

Pre- and post-processing
----------------------------------------------------------------------

* Various pre- and post-processing serial tools are packaged with
  SPARTA; see `Section 7 <doc/Section_tools.html>`_ of the manual.
* Our group has also written and released a separate toolkit called
  `Pizza.py <https://lammps.github.io/pizza>`_ which provides tools for doing setup, analysis,
  plotting, and visualization for SPARTA simulations.  Pizza.py is
  written in `Python <https://www.python.org>`_ and is available for download from `the Pizza.py WWW site <https://lammps.github.io/pizza>`_.

.. _pizza: https://lammps.github.io/pizza



.. _python: https://www.python.org



