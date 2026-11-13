.. rst-class:: center

`SPARTA WWW Site <index.html>`_ 

.. _sws: index.html




----------


Pictures & Movies from SPARTA Simulations
=========================================

The images and movies on this page are from SPARTA simulations.  They
have been rendered with various visualization packages.

+-------------------------------------------------------------------------------+-----------------------------------+
| :raw-html:`<A HREF = "#rti"><IMG SRC = "images/rti_thumb.jpg"></A>`           | Rayleigh-Taylor mixing            |
+-------------------------------------------------------------------------------+-----------------------------------+
| :raw-html:`<A HREF = "#rmi"><IMG SRC = "images/rmi_thumb.jpg"></A>`           | Richtmyer-Meshkov mixing          |
+-------------------------------------------------------------------------------+-----------------------------------+
| :raw-html:`<A HREF = "#adapt"><IMG SRC = "images/apollo_grid_thumb.jpg"></A>` | Grid adaptivity for reentry flows |
+-------------------------------------------------------------------------------+-----------------------------------+
| :raw-html:`<A HREF = "#mir"><IMG SRC = "images/mir_thumb.jpg"></A>`           | Flow around Mir space station     |
+-------------------------------------------------------------------------------+-----------------------------------+
| :raw-html:`<A HREF = "#paraview"><IMG SRC = "images/shuttle_thumb.jpg"></A>`  | ParaView viz of reentry flows     |
+-------------------------------------------------------------------------------+-----------------------------------+

These simple animations are from the examples sub-directory of the
SPARTA distribution and are described in `this section <doc/Section_example.html>`_ of the SPARTA documentation.  Most
are 2d models.  They are all GIF files, made from snapshots produced
by the `dump image <doc/dump_image.html>`_ command.  The movies play 3
times in a loop before stopping; click the reload icon in your browser
to play them again.

+-------------------------------------------------------------------------------+----------------------------------------------------+
| :raw-html:`<A HREF = "#chem"><IMG SRC = "images/ambi_thumb.jpg"></A>`         | ambipolar flow around circle                       |
+-------------------------------------------------------------------------------+----------------------------------------------------+
| :raw-html:`<A HREF = "#chem"><IMG SRC = "images/axi_thumb.jpg"></A>`          | axisymmetric flow around circle                    |
+-------------------------------------------------------------------------------+----------------------------------------------------+
| :raw-html:`<A HREF = "#chem"><IMG SRC = "images/chem_thumb.jpg"></A>`         | collisional flow with chemistry in a box           |
+-------------------------------------------------------------------------------+----------------------------------------------------+
| :raw-html:`<A HREF = "#circle"><IMG SRC = "images/circle_thumb.jpg"></A>`     | flow around a circle                               |
+-------------------------------------------------------------------------------+----------------------------------------------------+
| :raw-html:`<A HREF = "#collide"><IMG SRC = "images/collide_thumb.jpg"></A>`   | collisional flow in a box                          |
+-------------------------------------------------------------------------------+----------------------------------------------------+
| :raw-html:`<A HREF = "#emit"><IMG SRC = "images/emit_thumb.jpg"></A>`         | surface and face emission from and around a circle |
+-------------------------------------------------------------------------------+----------------------------------------------------+
| :raw-html:`<A HREF = "#flowfile"><IMG SRC = "images/flowfile_thumb.jpg"></A>` | flow profile defined by file                       |
+-------------------------------------------------------------------------------+----------------------------------------------------+
| :raw-html:`<A HREF = "#free"><IMG SRC = "images/free_thumb.jpg"></A>`         | free molecular flow in a box                       |
+-------------------------------------------------------------------------------+----------------------------------------------------+
| :raw-html:`<A HREF = "#sphere"><IMG SRC = "images/sphere_thumb.jpg"></A>`     | flow around a sphere                               |
+-------------------------------------------------------------------------------+----------------------------------------------------+
| :raw-html:`<A HREF = "#spiky"><IMG SRC = "images/spiky_thumb.jpg"></A>`       | flow around a spiky circle                         |
+-------------------------------------------------------------------------------+----------------------------------------------------+
| :raw-html:`<A HREF = "#step"><IMG SRC = "images/step_thumb.jpg"></A>`         | flow around a staircase step                       |
+-------------------------------------------------------------------------------+----------------------------------------------------+

All the images below are shown in small size.  Click on the image to
view a larger version.  For movies, click on the small image to
trigger the animation or a download of the movie file.





.. raw:: html

   <span id="rti"></span>

Rayleigh-Taylor mixing
----------------------------------------------------------------

This is work by Michael Gallis (magalli at sandia.gov) at Sandia.

This calculation was done to model Rayleigh/Taylor mixing which occurs
when a heavy gas is on top of a light gas and gravity induces mixing
and turbulent effects.

This is a large 3d calculation of He (red) on top of Ar (blue).  4.5B
particles were run with 400M grid cells for 240K timesteps.  The
simulation was run on 32K nodes (16 cores per node, 512K MPI tasks) of
the Sequoia BG/Q machine at Lawrence Livermore National Labs (LLNL).

Snapshot images of the simulation were created using SPARTA's `dump image <doc/dump_image.html>`_ command, rather than saving particle data
to disk.  The first image is the final state of the simulation.  The
second image is a movie of the simulation.

.. image:: ../images/rti_longtime_small.jpg
   :target: images/rti_longtime.png

.. image:: ../images/rti_longtime_small.jpg
   :target: movies/rti_longtime.mov

Second image is for a 165 MB QuickTime movie.

This paper has further details about the simulations:

**Direct simulation Monte Carlo investigation of the Rayleigh-Taylor
instability**\ , M. A. Gallis, T. P. Koehler, J. R. Torczynski,
S. J. Plimpton, Phys Rev Fluids, 1, 043403 (2016).
(`abstract <abstracts/prf16.html>`_)


----------


.. raw:: html

   <span id="rmi"></span>

Richtmyer-Meshkov mixing
------------------------------------------------------------------

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
simulation.  The thrid image is a movie of the simulation.  The fourth
image is a comparison of the DSMC results to experiment and a
continuum Navier-Stokes simulation.

.. image:: ../images/mix_initial_small.jpg
   :target: images/mix_initial.png

.. image:: ../images/mix_final_small.jpg
   :target: images/mix_final.png

.. image:: ../images/mix_final_small.jpg
   :target: movies/mix.mov

.. image:: ../images/rmi_dsmc_expt_ns_small.jpg
   :target: images/rmi_dsmc_expt_ns.jpg

This paper has further details about the simulations:

**Direct simulation Monte Carlo investigation of the Richtmyer-Meshkov
instability**\ , M. A. Gallis, T. P. Koehler, J. R. Torczynski,
S. J. Plimpton, Physics of Fluids, 27, 084105 (2015).
(`abstract <abstracts/pof15.html>`_)
(`http://dx.doi.org/10.1063/1.4928338 <http://dx.doi.org/10.1063/1.4928338>`_)


----------


.. raw:: html

   <span id="mir"></span>

Flow around Mir space station
-----------------------------------------------------------------------

This is work by Michael Gallis (magalli at sandia.gov) at Sandia,
using a surface mesh for the Mir space station provided by Jay LeBeau
(NASA).

This calculation was done to model flow around Mir at an altitude of
300K feet.  1.6B particles were used (at steady state) with a
computational grid of 10M cells.  The Mir surface mesh has 53K
triangles.  The simulation ran for 0.5M timesteps on 128 nodes (2048
cores) of a large Intel Xeon cluster at Sandia.  The final
time-averaged steady-state grid and surface element data was written
to a file and visualized by `TecPlot <https://www.tecplot.com>`_.  The
grid cell coloring is for gas temperature; the surface element
coloring is for heatflux onto the surface.

The first image is a single snapshot of a cut plane through the data
set.  The second image is a "movie" of scanning the cut plane through
the data set.  The third and fourth images are of similar data sets
rendered by the `ParaView visualization toolkit <https://www.paraview.org>`_.

.. image:: ../images/mir_small.jpg
   :target: images/mir.png

.. image:: ../images/mir_small.jpg
   :target: movies/mir.mov

.. image:: ../images/mir2_small.jpg
   :target: images/mir2.jpg

.. image:: ../images/mir3_small.jpg
   :target: images/mir3_crop.jpg


----------


.. raw:: html

   <span id="adapt"></span>

Grid adaptivity for reentry flows
-----------------------------------------------------------------------------

These are snapshots of the adapted grid used to model
flow around spacecraft.

The first image is of the Apollo capsule, with flow coming from the
lower left.  The grid is adapted through 5 levels.  The second image
is of the Mir space station with a few levels of adaptation around the
leading edge of the surfaces directly impacted by the flow.

.. image:: ../images/apollo_grid_small.jpg
   :target: images/apollo_grid.jpg

.. image:: ../images/mir5_small.jpg
   :target: images/mir5_half.jpg


----------


.. raw:: html

   <span id="paraview"></span>

ParaView viz of reentry flows
----------------------------------------------------------------------------

These are snapshots from simulations done by Michael Gallis (magalli
at sandia.gov) to illlustrate use of the open-source `ParaView visualization package <https://www.paraview.org>`_ with SPARTA output.  Each is a simple
demonstration of flow around a spacecraft in the upper atomosphere,
e.g. as it undergoes re-entry.

.. _paraview: https://www.paraview.org



The workflow for running the simulations was as follows.

\a) Convert an STL file representing the object to a SPARTA surface
data file, readable by the `read\_surf <doc/read_surf.html>`_ command.
This conversion was done with the `stl2surf tool <doc/Section_tools.html#stl2surf>`_.  The STL and sdata surface files
are in the data directory of the distribution.

\b) Run a SPARTA simulation which produces grid and surface element
output via the `dump grid <doc/dump.html>`_ and `dump surf <doc/dump.html>`_
commands.

\c) Convert the output to ParaView format via the `paraview tools <doc/Section_tools.html#paraview>`_ Python scripts.

\d) Run `ParaView <https://www.paraview.org>`_ to produce images like these or
animations.

Thsee are images of the Orion, Gemini, and Apollo capsules, and the
space shuttle.

.. image:: ../images/orion_small.jpg
   :target: images/orion.jpg

.. image:: ../images/gemini_small.jpg
   :target: images/gemini.jpg

.. image:: ../images/apollo_small.jpg
   :target: images/apollo.jpg

.. image:: ../images/shuttle_small.jpg
   :target: images/shuttle.jpg





.. raw:: html

   <span id="chem"></span>

Ambipolar
----------------------------------------------------

Flow of ambipolar plasma around a circle.

`Input script <inputs/in.ambi.txt>`_ for this problem from the
example/ambi directory.  The ambipolar ions, induced by the flow
colliding with with the surface, are shown larger in the movie.

.. image:: ../images/ambi_small.jpg
   :target: movies/ambi.gif


----------


.. raw:: html

   <span id="chem"></span>

Axisymmetry
------------------------------------------------------

Axisymmetric flow around a circle (sphere).

`Input script <inputs/in.axi.txt>`_ for this problem from the
example/axi directory.

.. image:: ../images/axi_small.jpg
   :target: movies/axi.gif


----------


.. raw:: html

   <span id="chem"></span>

Chemistry
----------------------------------------------------

Collisional flow with chemistry in a box.

`Input script <inputs/in.chem.txt>`_ for this problem from the
example/chem directory.

.. image:: ../images/chem_small.jpg
   :target: movies/chem.gif


----------


.. raw:: html

   <span id="circle"></span>

Circle
---------------------------------------------------

Flow around a circle.

`Input script <inputs/in.circle.txt>`_ for this problem from the
example/circle directory.

.. image:: ../images/circle_small.jpg
   :target: movies/circle.gif


----------


.. raw:: html

   <span id="collide"></span>

Collisions
--------------------------------------------------------

Collisional flow in a box.

`Input script <inputs/in.collide.txt>`_ for this problem from the
example/collide directory.

.. image:: ../images/collide_small.jpg
   :target: movies/collide.gif


----------


.. raw:: html

   <span id="emit"></span>

Surface and face emission
--------------------------------------------------------------------

Surface emission and box face from and around a circle
and from a second circle used as a boundary.

Input scripts for 7 cases, from the examples/emit directory.

* `emission from box face <inputs/in.emit.face.txt>`_
* `emission from box face within region, <inputs/in.emit.face.region.txt>`_
* `emission from circle in flow direction <inputs/in.emit.surf.flow.txt>`_
* `emission from circle in flow direction within region <inputs/in.emit.surf.flow.region.txt>`_
* `emission from circle in normal direction <inputs/in.emit.surf.normal.txt>`_
* `emission from circle in normal direction within region <inputs/in.emit.surf.normal.region.txt>`_
* `emission from circle arc used as boundary <inputs/in.emit.surf.boundary.txt>`_

.. image:: ../images/emit.face.small.jpg
   :target: movies/emit.face.gif

.. image:: ../images/emit.face.region.small.jpg
   :target: movies/emit.face.region.gif

.. image:: ../images/emit.surf.flow.small.jpg
   :target: movies/emit.surf.flow.gif

.. image:: ../images/emit.surf.flow.region.small.jpg
   :target: movies/emit.surf.flow.region.gif

.. image:: ../images/emit.surf.normal.small.jpg
   :target: movies/emit.surf.normal.gif

.. image:: ../images/emit.surf.normal.region.small.jpg
   :target: movies/emit.surf.normal.region.gif

.. image:: ../images/emit.surf.boundary.small.jpg
   :target: movies/emit.surf.boundary.gif


----------


.. raw:: html

   <span id="flowfile"></span>

Flow profile defined by file
---------------------------------------------------------------------------

Particle influx through box face defined by mesh values in a file via
the `fix emit/face/file <doc/fix_emit_face_file.html>`_ command.

`Input script <inputs/in.flowfile.txt>`_ and `flow profile definition <inputs/flow.face.txt>`_ for this problem from the
example/flowfile directory.

.. image:: ../images/flowfile_small.jpg
   :target: movies/flowfile.gif


----------


.. raw:: html

   <span id="free"></span>

Free molecular flow
--------------------------------------------------------------

Free molecular flow in a box.

`Input script <inputs/in.free.txt>`_ for this problem from the
example/free directory.

.. image:: ../images/free_small.jpg
   :target: movies/free.gif


----------


.. raw:: html

   <span id="sphere"></span>

Sphere
---------------------------------------------------

Flow around a sphere.

`Input script <inputs/in.sphere.txt>`_ for this problem from the
example/sphere directory.

.. image:: ../images/sphere_small.jpg
   :target: movies/sphere.gif


----------


.. raw:: html

   <span id="spiky"></span>

Spiky circle
--------------------------------------------------------

Flow around a spiky circly, illustrating cut and split cells.

`Input script <inputs/in.spiky.txt>`_ for this problem from the
example/spiky directory.

.. image:: ../images/spiky_small.jpg
   :target: movies/spiky.gif


----------


.. raw:: html

   <span id="step"></span>

Step
-----------------------------------------------

Flow around a staircase step.

`Input script <inputs/in.step.txt>`_ for this problem from the
example/step directory.

.. image:: ../images/step_small.jpg
   :target: movies/step.gif

