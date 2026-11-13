.. meta::
   :description: SPARTA home page
   :keywords: SPARTA, DSMC, Direct Simulation Monte Carlo
   :google-site-verification: jIe-V87O61oNvgWFgBXMeF5bFl35XjSaG0Fm8_7q5VU
   :review: 07_09_2014
   :filename: index.html
   :subject: SPARTA home page
   :sandia.approval_type: formal
   :sandia.approved: 2014-15557W
   :mssmarttagspreventparsing: TRUE
   :author: Steve Plimpton


.. rst-class:: center

SPARTA Direct Simulation Monte Carlo (DSMC) Simulator
=====================================================

.. rst-class:: center

*The generation of random numbers is too important to be left to
chance.* -- Robert Coveyou 

.. rst-class:: center

*God does not play dice.* -- Albert Einstein 

.. raw:: html

   <style>
     .logo-hover { display: inline-block; position: relative; line-height: 0; }
     .logo-hover .logo-anim { position: absolute; left: 0; top: 0;
                              width: 100%; height: 100%; }
     /* The animated file is named only in a custom property, so the
        browser does not fetch it until this rule actually uses it. */
     .logo-hover:hover .logo-anim { background-image: var(--logo-anim);
                                    background-size: contain; }
     .logo-hint { color: #555; }
   </style>
   <CENTER>
   <span class="logo-hover">
   <img src="images/logo_static.gif" width="150" height="150" alt="SPARTA logo">
   <span class="logo-anim" style="--logo-anim:url('images/logo.gif')" aria-hidden="true"></span>
   </span>
   <br>
   <small class="logo-hint">hover to animate</small>
   </CENTER>


----------


.. rst-class:: center-cells

+-----------------------------------------------+----------------------------------------------------------+--------------------------------------+-------------------------------------+
| **Documentation**\                            | **Code**\                                                | **Results**\                         | **Other**\                          |
+-----------------------------------------------+----------------------------------------------------------+--------------------------------------+-------------------------------------+
| `Features <features.html>`_                   | `Download <https://sjplimp.github.io/download.html>`_    | `Publications <papers.html>`_        | `Mail list <mail.html>`_            |
+-----------------------------------------------+----------------------------------------------------------+--------------------------------------+-------------------------------------+
| `Manual <doc/Manual.html>`_                   | `GitHub <https://github.com/sparta/sparta>`_             | `Pictures & Movies <pictures.html>`_ | `Authors <authors.html>`_           |
+-----------------------------------------------+----------------------------------------------------------+--------------------------------------+-------------------------------------+
| `Tutorials <tutorials.html>`_                 | `SourceForge <https://sourceforge.net/projects/sparta>`_ | `Benchmarks <bench.html>`_           | `Other codes & tools <other.html>`_ |
+-----------------------------------------------+----------------------------------------------------------+--------------------------------------+-------------------------------------+
| `Commands <doc/Section_commands.html#cmd_5>`_ | `Latest features & bug fixes <bug.html>`_                | `Citing SPARTA <papers.html>`_       | `Open source <open_source.html>`_   |
+-----------------------------------------------+----------------------------------------------------------+--------------------------------------+-------------------------------------+
|                                               | `Report bugs & request features <unbug.html>`_           |                                      | .                                   |
+-----------------------------------------------+----------------------------------------------------------+--------------------------------------+-------------------------------------+

.. _download: https://sjplimp.github.io/download.html



.. _pizza: https://lammps.github.io/pizza



SPARTA is an acronym for Stochastic PArallel Rarefied-gas
Time-accurate Analyzer.

SPARTA is a parallel DSMC or Direct Simulation Monte Carlo code for
performing simulations of low-density gases in 2d or 3d.  Particles
advect through a hierarchical Cartesian grid that overlays the
simulation box.  The grid is used to group particles by grid cell for
purposes of performing collisions and chemistry.  Physical objects
with triangulated surfaces can be embedded in the grid, creating cut
and split grid cells.  The grid is also used to efficiently find
particle/surface collisions.

SPARTA runs on single processors or in parallel using message-passing
techniques and a spatial-decomposition of the simulation domain.  The
code is designed to be easy to modify or extend with new
functionality.

SPARTA is distributed as an `open source code <open_source.html>`_ under
the terms of the `GPL <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>`_, or sometimes (by request) under the terms
of the `GNU Lesser General Public License (LGPL) <http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html>`_.  The current
version can be downloaded `here <https://sjplimp.github.io/download.html>`_.

SPARTA was primarily developed at `Sandia National Laboratories <https://www.sandia.gov>`_,
a US `Department of Energy <https://www.energy.gov>`_ (DOE) laboratory.  The authors and
funding are listed on `this page <authors.html>`_.

.. _gpl: http://www.gnu.org/licenses/old-licenses/gpl-2.0.html



.. _gnu2: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html



.. _snl: https://www.sandia.gov



.. _doe: https://www.energy.gov



.. _sjp: https://sjplimp.github.io




----------


.. rst-class:: center

Recent SPARTA News
------------------

* :raw-html:`<IMG SRC = "images/new.gif">` (8/26) Release of version 27 Aug 2026. It
  updates the Kokkos library to v5.0.2, which requires building the
  `KOKKOS package <doc/Section_accelerate.html>`_ with CMake, and ports many
  styles to KOKKOS. It adds a new VTK package with native `dump vtk <doc/dump_vtk.html>`_ styles, a majorant collision frequency (MCF)
  collision scheme and a transient adaptive subcell (TAS)
  collision-partner selection method via
  `collide\_modify <doc/collide_modify.html>`_, an "mflow" mass-flow inlet
  and time-averaged "subsonic" boundary condition for `fix emit/surf <doc/fix_emit_surf.html>`_, and a new `fix controller <doc/fix_controller.html>`_ PID feedback controller. It also
  allows `implicit surfaces <doc/read_isurf.html>`_ to be used in
  axisymmetric models, enhances the `global <doc/global.html>`_ "optmove"
  option, extends the library interface with embedding support, and adds
  `dump image <doc/dump_image.html>`_ rendering enhancements and
  transparency. See more details `here <bug.html>`_.
* :raw-html:`<IMG SRC = "images/new.gif">` (9/25) Release of version 24 Sep 2025. It
  fixes some issues from the 10Sep2025 release (and before).
* :raw-html:`<IMG SRC = "images/new.gif">` (9/25) Release of version 10 Sep 2025. It
  adds `dump\_modify <https://sparta.github.io/doc/dump_modify.html>`_
  "gridgroup" and "surfgroup" keywords to
  `dump\_image <https://sparta.github.io/doc/dump_image.html>`_, adds `fix emit/face <https://sparta.github.io/doc/fix_emit_face.html>`_ "modulate"
  option for insertion of time-varying flows, adds python support via a
  new `python <https://sparta.github.io/doc/python.html>`_ command and
  `python-style variables <https://sparta.github.io/doc/variable.html>`_,
  reduces particle memory by 25%, adds a new `fix custom <https://sparta.github.io/doc/fix_custom.html>`_ command along
  with new `custom <https://sparta.github.io/doc/custom.html>`_ command
  options, adds options to the
  `create\_particles <https://sparta.github.io/doc/create_particles.html>`_
  command to use `custom <https://sparta.github.io/doc/custom.html>`_
  per-grid attributes, and adds tallying for individual gas and surface
  collisions and reactions. See more details `here <bug.html>`_.
* :raw-html:`<IMG SRC = "images/new.gif">` (1/25) Release of version 20 Jan 2025. It
  improves explicit to implicit surface conversion in `create isurf <doc/create_isurf.html>`_ and adds a new multi-point decrement for
  ablation in `fix ablate <doc/fix_ablate.html>`_. It also improves the
  accuracy of the free path and adds a new mean collision time in
  `compute lambda/grid <doc/compute_lambda_grid.html>`_. The new mean
  collision time is used for variable timestepping in `compute dt/grid <doc/compute_dt_grid.html>`_. It also adds a new `compute surf <doc/compute_surf.html>`_ "torque" option, and `fix halt <doc/fix_halt.html>`_ which can be used to stop a simulation early
  based on a user-specified criteria. See more details `here <bug.html>`_.
* :raw-html:`<IMG SRC = "images/new.gif">` (9/24) Release of version 4 Sep 2024. It
  adds `create\_isurf <doc/create_isurf.html>`_ to convert explicit surfaces
  to implicit surfaces, custom per-surf options to `fix emit/surf <doc/fix_emit_surf.html>`_, a variable special function which
  allows particle-style variables to access per-grid quantities, and
  adds momentum and energy contributions of `fix emit/surf <doc/fix_emit_surf.html>`_ in the results of `compute surf <doc/compute_surf.html>`_. See more details `here <bug.html>`_.
* :raw-html:`<IMG SRC = "images/new.gif">` (3/24) Release of version 7 Mar 2024.  It
  adds support for `global variable time stepping <doc/fix_dt_reset.html>`_, enhances functionality of
  `custom attributes <doc/custom.html>`_ for particles, grid cells, and
  surface elements, adds Kokkos support for FFTs and surface reactions,
  adds an option to compute chemistry rates without performing
  reactions, and adds an option to dump the area of surface elements to
  a file with the `dump surf <doc/dump.html>`_ command. See more details
  `here <bug.html>`_.
* :raw-html:`<IMG SRC = "images/new.gif">` (4/23) Release of version 13 Apr 2023. It
  includes support for Python 3, a new `fix surf/temp <doc/fix_surf_temp.html>`_ command, support for custom
  per-grid-cell attributes, an optimized particle move algorithm when a
  model has a regular grid and no surface elements, a new option for the
  create\_particles command to add particles in grid cells cut by surface
  elements.  See more details `here <bug.html>`_.
* :raw-html:`<IMG SRC = "images/new.gif">` (7/22) Release of version 18 July 2022.
  It includes new options for the `compute surf <doc/compute_surf.html>`_
  command, a new `no-slip option <doc/surf_collide.html>`_ for specular
  surface collisiont, and a new `surface collision adiabatic model <doc/surf_collide.html>`_ with isotropic scattering.  See more
  details `here <bug.html>`_.
* :raw-html:`<IMG SRC = "images/new.gif">` (2/22) Options to add various kinds of
  external fields to influence particle advection.  They can be
  spatially or time varying and applied on a per-particle or
  per-grid-cell basis. See the doc page for the `global field <doc/global.html>`_ command.
* :raw-html:`<IMG SRC = "images/new.gif">` (10/21) Added a surf\_react adsorb command
  which has support for on-surface chemistry reactions and storage of
  surface state, i.e. per-surface-element concentrations of various
  on-surface species.  This enables modeling of both gas/surface and
  surface/surface chemical reaction networks.
* :raw-html:`<IMG SRC = "images/new.gif">` (11/20) Removed hierarchical grid parent
  cells from the internally stored data structures.  The code now only
  stores child cells.  For large problems with many levels of grid
  adaptation, this frees up a large amount of memory.
* :raw-html:`<IMG SRC = "images/new.gif">` (1/20) Added support for `transparent surfaces <doc/Section_howto.html#howto_15>`_ which tally statistics when
  particles pass throught them.
* :raw-html:`<IMG SRC = "images/new.gif">` (10/19) Added these commands for
  `ablation modeling <doc/Section_howto.html#howto_14>`_ of implicit
  surface elements: `fix ablate <doc/fix_ablate.html>`_, `compute isurf/grid <doc/compute_isurf_grid.html>`_, `compute react/isurf/grid <doc/compute_react_isurf_grid.html>`_,
  `write\_isurf <doc/write_isurf.html>`_.
* :raw-html:`<IMG SRC = "images/new.gif">` (4/19) Added support for implicit 2d and
  3d surface elements defined by a grid corner point values in a read-in
  file.  These are in contrast to explicit surface elements defined by
  line segments (2d) or triangles (3d).
* :raw-html:`<IMG SRC = "images/new.gif">` (2/19) Added support for distributed
  surface elements so that complex surfaces with huge element counts
  can be modeled, with the elements stored acrossed processors.
* :raw-html:`<IMG SRC = "images/new.gif">` (8/18) SPARTA development is now
  supported on `GitHub <https://github.com/sparta/sparta>`_ and with a
  `mail list <mail.html>`_.
* :raw-html:`<IMG SRC = "images/new.gif">` (1/18) Added new sections to the
  `Benchmark page <bench.html>`_ with performance results using the new Kokkos
  accelerator options on a variety of new machines and hardware,
  including multi-core CPUs (via threading), GPUs, and KNLs.
* :raw-html:`<IMG SRC = "images/new.gif">` (12/17) Added a KOKKOS package to the
  code to allow building with the open-source Kokkos library which
  provides support for running SPARTA on different architectures,
  including multi-core CPUs (via threading), GPUs, and KNLs.  See `this section <doc/Section_accelerate.html>`_ of the manual for details.
* :raw-html:`<IMG SRC = "images/new.gif">` (4/17) Added a subsonic pressure boundary
  condition via a `surf\_collide piston <doc/surf_collide.html>`_ command,
  as well as a 2d/3d FFT capability for grid based quantities on regular
  grids via the `compute fft/grid <doc/compute_fft_grid.html>`_
  command.
* :raw-html:`<IMG SRC = "images/new.gif">` (8/16) Added `fix ave/histo <doc/fix_ave_histo.html>`_ and `fix ave/histo/weight <doc/fix_ave_histo.html>`_ commands to enable
  histogramming of various quantities during a simulation.
* :raw-html:`<IMG SRC = "images/new.gif">` (1/16) Added `grid-style variables <doc/variable.html>`_ so that user-defined per-grid quantities
  can be calculated on-the-fly and output more easily.
* :raw-html:`<IMG SRC = "images/new.gif">` (10/15) Added a `near-neighbor collision model <doc/collide_modify.html>`_ for selecting pairs of collision
  partners.
* :raw-html:`<IMG SRC = "images/new.gif">` (9/15) Posted slides for a half-day
  tutorial short-course on SPARTA, taught at the biennial DSMC15
  conference.  See the `Tutorials <tutorials.html>`_ link above.
* :raw-html:`<IMG SRC = "images/new.gif">` (8/15) Added static and on-the-fly grid
  adaptivity via the `adapt\_grid <doc/adapt_grid.html>`_ and `fix adapt <doc/fix_adapt.html>`_ commands.  Also added commands to
  `move <doc/move_surf.html>`_ or `remove <doc/remove_surf.html>`_ surface
  elements.
* :raw-html:`<IMG SRC = "images/new.gif">` (5/15) Added a `fix emit/surf <doc/fix_emit_surf.html>`_ command to enable particle outflux
  from surface elements, including their use as a global influx
  boundary.
* :raw-html:`<IMG SRC = "images/new.gif">` (5/15) Surface reaction models have been
  added via the `surf\_react <doc/surf_react.html>`_ command. The full set
  of dissociation, ionization, exchange, and recombination reactions,
  for both gas-phase and surface chemitstry are now implemented.
* :raw-html:`<IMG SRC = "images/new.gif">` (5/15) Added an ambipolar approximation
  for modeling charged plasmas.  See `this howto discussion <doc/Section_howto.html#howto_11>`_ for an explanation of
  using the various new commands and command options that enable the
  approximation.
* :raw-html:`<IMG SRC = "images/new.gif">` (2/15) Added a `fix emit/face/file <doc/fix_emit_face_file.html>`_ command to enable
  spatially-varying particle influx through a simulation box face, as
  defined by a file of mesh points and values.
* :raw-html:`<IMG SRC = "images/new.gif">` (12/14) Added two new reaction styles to
  the `react <doc/react.html>`_ command, for the Quantum-Kinetic (QK) model
  and a hybrid Total Collision Energy / Quantum Kinetic (TCE/QK)
  model.
* :raw-html:`<IMG SRC = "images/new.gif">` (10/14) Added two `Python scripts <doc/Section_tools.html#paraview>`_ which can convert SPARTA
  output files to ParaView format for interactive 3d viz.
  `Paraview <https://www.paraview.org>`_ is a popular freely-available
  visualization tool.
* :raw-html:`<IMG SRC = "images/new.gif">` (8/14) Added a `stl2surf.py tool <doc/Section_tools.html#stl2surf>`_ to convert STL-format
  triangulation files into the SPARTA `surface file <doc/read_surf.html>`_
  format.
* :raw-html:`<IMG SRC = "images/new.gif">` (8/14) Enabled axi-symmetric 2d models.
  See `Section 4.2 <doc/Section_howto.html#howto_2>`_ of the manual for
  details.
* :raw-html:`<IMG SRC = "images/new.gif">` (7/14) Initial open-source release of
  SPARTA.


----------


.. rst-class:: center

SPARTA Highlight
----------------

.. rst-class:: center

(see the `Pictures & Movies <pictures.html>`_ page for more examples of
SPARTA calculations) 

This is work by Michael Gallis (magalli at sandia.gov) at Sandia.

This calculation was done to model Richtmyer/Meshkov mixing which
occurs when a light gas is on top of a heavier gas and a shock induces
mixing and turbulent effects.

This is a large 2d calculation of He (green) on top of Ar (red).  4.5B
particles were run with 400M grid cells for 240K timesteps.  The
simulation was run on 32K nodes (16 cores per node, 512K MPI tasks) of
the Sequoia BG/Q machine at Lawrence Livermore National Labs (LLNL).

Snapshot images of the simulation were created using SPARTA's `dump image <doc/dump_image.html>`_ command, rather than saving particle data
to disk.  The first 2 images are the initial and final state of the
simulation.  The rightmost image is a movie of the simulation.

.. image:: ../images/mix_initial_small.jpg
   :target: images/mix_initial.png

.. image:: ../images/mix_final_small.jpg
   :target: images/mix_final.png

.. image:: ../images/mix_final_small.jpg
   :target: movies/mix.mov

2 images and a 0.5 Mb QuickTime movie

This paper has further details about the mixing model:

**Direct Simulation Monte Carlo: The Quest for Speed**\ , M. A. Gallis,
J. R. Torczynski, S. J. Plimpton, D. J. Rader, and T. Koehler,
Proceedings of the 29th Rarefied Gas Dynamics (RGD) Symposium, Xi'an,
China, July 2014.  (to be published by AIP)
(`abstract <abstracts/rgd14.html>`_)

.. raw:: html

   <!-- Past SPARTA highlights:
   -->



.. toctree::
   :hidden:
   :glob:

   authors
   bench
   bug
   features
   mail
   open_source
   other
   papers
   pictures
   tutorials
   unbug
   abstracts/*
   bench/*
