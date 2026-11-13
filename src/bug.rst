.. rst-class:: center

`SPARTA WWW Site <index.html>`_ 

.. _sws: index.html




----------


Latest Features and Bug Fixes in SPARTA
=======================================

This page is a continuous listing of new features and bug fixes for
the SPARTA simulator.

In some cases, new features change the syntax or operation of an
existing input script command, which can cause SPARTA output to
change, or even "break" an earlier working script.  These cases are
highlighted below with a "BACKWARD COMPATIBILITY" note.

To stay up-to-date with the current SPARTA, you can download the
current tarball from the `download page <https://sjplimp.github.io/download.html>`_ at any time, and
re-build the code.  It will include all the features/fixes listed
below.

.. _download: https://sjplimp.github.io/download.html




----------


.. raw:: html

   <span id="version"></span>

What version of SPARTA do you have?
---------------------------------------------------------------------------------

A SPARTA "version" is the date when it was released, such as 10 Aug
2014.  SPARTA is updated continuously.  Every time we fix a bug or add
a feature, we release it immediately, as listed below.  Each dated
copy of SPARTA contains all the features and bug-fixes up to and
including that version date.  The version date is printed to the
screen and logfile every time you run SPARTA.  It is also in the file
src/version.h and in the SPARTA directory name created when you unpack
a tarball.

* If you browse the HTML or PDF doc pages on the SPARTA WWW site, they
  always describe the most current version of SPARTA.
* If you browse the HTML or PDF doc pages included in your tarball, they
  describe the version you have.

Note that you can download tarballs of previous SPARTA releases, going
back several years, from the `SPARTA GitHub website <https://github.com/sparta/sparta>`_.  See the "Releases" box on
the rightside of the page and open the "Assets" tab of any release
entry.  Likewise if you have a git clone of the SPARTA repository, you
can type "git tag" to see the list of releases and and do a "git
checkout" of any of them.





**27 Aug 2026**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/27Aug2026>`_

Details for all releases are
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Update the Kokkos library in SPARTA to v5.0.2, which requires building
  the `KOKKOS package <https://sparta.github.io/doc/Section_accelerate.html>`_
  with CMake, by Stan Moore (SNL) and the Kokkos developers in `PR #596 <https://github.com/sparta/sparta/pull/596>`_
* Port many styles to the `KOKKOS package <https://sparta.github.io/doc/Section_accelerate.html>`_,
  including `fix emit/surf <https://sparta.github.io/doc/fix_emit_surf.html>`_,
  `regions <https://sparta.github.io/doc/region.html>`_, surface collide and
  surface reaction models, and many computes, by Stan Moore (SNL) in
  `PR #632 <https://github.com/sparta/sparta/pull/632>`_
* Close remaining feature gaps in the `KOKKOS package <https://sparta.github.io/doc/Section_accelerate.html>`_, lift
  hard-coded limits on the number of fix, compute, surface collide, and
  surface reaction instances, and fix host/device coherence bugs, by Stan
  Moore (SNL) in `PR #676 <https://github.com/sparta/sparta/pull/676>`_
* Add a new VTK package with native
  `dump vtk <https://sparta.github.io/doc/dump_vtk.html>`_ styles for
  particles, grid cells, and surfaces by Stan Moore (SNL) in `PR #655 <https://github.com/sparta/sparta/pull/655>`_
* Add a majorant collision frequency (MCF) collision scheme via the
  `collide\_modify <https://sparta.github.io/doc/collide_modify.html>`_
  "scheme" keyword by Stan Moore (SNL) in `PR #646 <https://github.com/sparta/sparta/pull/646>`_
* Add a transient adaptive subcell (TAS) collision-partner selection
  method via the
  `collide\_modify <https://sparta.github.io/doc/collide_modify.html>`_
  "partners" keyword by James Almgren-Bell (UT Austin) and Stan Moore
  (SNL) in `PR #647 <https://github.com/sparta/sparta/pull/647>`_
* Add `fix emit/surf <https://sparta.github.io/doc/fix_emit_surf.html>`_
  "mflow" option for mass-flow inlets and a time-averaged "subsonic"
  boundary condition by Stan Moore (SNL) in `PR #644 <https://github.com/sparta/sparta/pull/644>`_, based on the original
  implementation in `PR #430 <https://github.com/sparta/sparta/pull/430>`_
  by Cosimo89, hieu325, vimalrajv, and syamalpraneeth (ASML
  Netherlands)
* Add a new `fix controller <https://sparta.github.io/doc/fix_controller.html>`_ command, a
  PID feedback controller, by Stan Moore (SNL) in `PR #631 <https://github.com/sparta/sparta/pull/631>`_
* Allow `implicit surfaces <https://sparta.github.io/doc/read_isurf.html>`_
  to be used in axisymmetric models by Stan Moore (SNL) in `PR #664 <https://github.com/sparta/sparta/pull/664>`_
* Add boundary condition, dense cell index, and axisymmetric support to
  the `global <https://sparta.github.io/doc/global.html>`_ "optmove" option
  by Stan Moore (SNL) in `PR #672 <https://github.com/sparta/sparta/pull/672>`_
* Extend the `library interface <https://sparta.github.io/doc/Section_howto.html>`_ with
  embedding support, and add `dump image <https://sparta.github.io/doc/dump_image.html>`_ rendering
  enhancements and transparency, by Stan Moore (SNL) in `PR #656 <https://github.com/sparta/sparta/pull/656>`_ and `PR #673 <https://github.com/sparta/sparta/pull/673>`_
* Allow ambipolar ions to act as third bodies in dissociation and
  recombination `reactions <https://sparta.github.io/doc/react.html>`_ by
  Stan Moore (SNL) in `PR #642 <https://github.com/sparta/sparta/pull/642>`_
* Support vibrational mode degeneracy in the
  `species <https://sparta.github.io/doc/species.html>`_ vibration file by
  Stan Moore (SNL) in `PR #643 <https://github.com/sparta/sparta/pull/643>`_
* Fix the vibrational and rotational energy sampling cutoff for species
  with many degrees of freedom by Stan Moore (SNL) in `PR #638 <https://github.com/sparta/sparta/pull/638>`_
* Fix two energy-redistribution bugs in reacting electronic energy
  exchange by Arnaud Borner (NASA Ames) in `PR #654 <https://github.com/sparta/sparta/pull/654>`_
* Add a performance summary printed at the end of a run by Stan Moore
  (SNL) in `PR #609 <https://github.com/sparta/sparta/pull/609>`_
* Flag invalid use of the wildcard character in compute/fix args used as
  inputs by other commands by Steve Plimpton (SNL retired) in `PR #653 <https://github.com/sparta/sparta/pull/653>`_

Note: this release is particularly large due to enhanced productivity
from the use of AI-assisted coding agents including Claude Code and
Github Copilot (see co-authored commits).

BACKWARD COMPATIBILITY: The `KOKKOS package <https://sparta.github.io/doc/Section_accelerate.html>`_ must now
be built with CMake, since Kokkos v5.0.2 no longer supports Makefile
builds, and requires a compiler which supports C++20.  The
src/MAKE/Makefile.\*kokkos\* files have been removed.  Building SPARTA
without the KOKKOS package still only requires C++11.

BACKWARD COMPATIBILITY: The
`collide\_modify <https://sparta.github.io/doc/collide_modify.html>`_
"nearcp" keyword is deprecated and superseded by the "partners"
keyword; the old syntax is still accepted.  The "persp" keyword of
`dump image <https://sparta.github.io/doc/dump_image.html>`_ has been
removed (it never worked).  The global vector output by `fix ablate <https://sparta.github.io/doc/fix_ablate.html>`_ is now length 3
instead of 2, and "fix ablate" now uses the surface collision and
reaction models assigned by
`surf\_modify <https://sparta.github.io/doc/surf_modify.html>`_ for ablated
surfaces instead of always using the first model.  Invalid use of the
wildcard character in compute/fix args used as inputs by other
commands is now flagged as an error instead of being silently
accepted.


----------


**24 Sep 2025**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/24Sep2025>`_

Details for all releases are
 `here <https://github.com/sparta/sparta/releases>`_

This release fixes some issues from the 10Sep2025 release (and
before).


----------


**10 Sep 2025**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/10Sep2025>`_

Details for all releases are
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Add `dump\_modify <https://sparta.github.io/doc/dump_modify.html>`_
  "gridgroup" and "surfgroup" keywords to
  `dump\_image <https://sparta.github.io/doc/dump_image.html>`_ by Steve
  Plimpton (SNL retired) in `PR #547 <https://github.com/sparta/sparta/pull/547>`_
* Add `fix emit/face <https://sparta.github.io/doc/fix_emit_face.html>`_
  "modulate" option for insertion of time-varying flows by Steve
  Plimpton (SNL retired) in `PR #551 <https://github.com/sparta/sparta/pull/551>`_
* Add "is\_file()" special function for
  `variables <https://sparta.github.io/doc/variable.html>`_ by Stan Moore
  (SNL) in `PR #558 <https://github.com/sparta/sparta/pull/558>`_
* Add python support via a new
  `python <https://sparta.github.io/doc/python.html>`_ command and
  `python-style variables <https://sparta.github.io/doc/variable.html>`_ by
  Steve Plimpton (SNL retired) in `PR #564 <https://github.com/sparta/sparta/pull/564>`_
* Reduce particle memory use by 25% by Matt Bettencourt (NVIDIA) in `PR #567 <https://github.com/sparta/sparta/pull/567>`_
* Add new `fix custom <https://sparta.github.io/doc/fix_custom.html>`_
  command along with new
  `custom <https://sparta.github.io/doc/custom.html>`_ command options by
  Steve Plimpton (SNL retired) in `PR #550 <https://github.com/sparta/sparta/pull/550>`_
* Add options to the
  `create\_particles <https://sparta.github.io/doc/create_particles.html>`_
  command to use `custom <https://sparta.github.io/doc/custom.html>`_
  per-grid attributes for created particles by Steve Plimpton (SNL
  retired) in `PR #554 <https://github.com/sparta/sparta/pull/554>`_
* Add tallying for individual gas and surface collisions and reactions
  by Steve Plimpton (SNL retired) in `PR #405 <https://github.com/sparta/sparta/pull/405>`_


----------


**20 Jan 2025**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/20Jan2025>`_

Details for all releases are
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Improved explicit to implicit surface conversion in `create isurf <doc/create_isurf.html>`_ command and added a new multi-point decrement for
  DSMC ablation in `fix ablate <doc/fix_ablate.html>`_ by Andrew Hong (SNL) in `PR #495 <https://github.com/sparta/sparta/pull/495>`_
* More accurate mean free path and new mean collision time in `compute lambda/grid <doc/compute_lambda_grid.html>`_ by Arnaud Borner (NASA Ames) in `PR #282 <https://github.com/sparta/sparta/pull/282>`_
* New `compute surf <doc/compute_surf.html>`_ torque option by Steve Plimpton (SNL
  retired) and Darrell Robertson (NASA Ames) in `PR #517 <https://github.com/sparta/sparta/pull/517>`_
* Added `fix halt <doc/fix_halt.html>`_ which can be used to stop a
  simulation early based on a user-specified criteria, copied and
  adapted from LAMMPS by Stan Moore (SNL) in `PR #524 <https://github.com/sparta/sparta/pull/524>`_
* Use mean collision time in `compute lambda/grid <doc/compute_lambda_grid.html>`_
  for variable timestepping in `compute dt/grid <doc/compute_dt_grid.html>`_ by Alan
  Stagg (SNL) in `PR #540 <https://github.com/sparta/sparta/pull/540>`_

BACKWARD COMPATIBILITY: The syntax for `compute lambda/grid <doc/compute_lambda_grid.html>`_ changed slightly.


----------


**4 Sep 2024**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/4Sep2024>`_

Details for all releases are 
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Added `create\_isurf <doc/create_isurf.html>`_ command to convert explicit
  surfaces to implicit surfaces by Andrew Hong (SNL) in `PR #447 <https://github.com/sparta/sparta/pull/447>`_
* Added custom per-surf options to `fix emit/surf <doc/fix_emit_surf.html>`_ command by Steve Plimpton (SNL
  retired) in `PR #491 <https://github.com/sparta/sparta/pull/491>`_
* Modified small corner value removal in
  `fix\_ablate <doc/fix_ablate.html>`_ command by Andrew Hong (SNL) in `PR #463 <https://github.com/sparta/sparta/pull/463>`_
* Added a `variable special function <doc/variable.html>`_ which allows
  particle-style variables to access per-grid quantities by Steve
  Plimpton (SNL retired) in `PR #511 <https://github.com/sparta/sparta/pull/511>`_
* Added momentum and energy contributions tallied by `fix emit/surf <doc/fix_emit_surf.html>`_ in the results of "compute surf" by
  Zak Echo (SNL) in `PR #502 <https://github.com/sparta/sparta/pull/502>`_

BACKWARD COMPATIBILITY: SPARTA now requires a C++11 compatible compiler
(KOKKOS package requires C++17).


----------


**7 Mar 2024**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/7Mar2024>`_

Details for all releases are 
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Add `global variable time stepping <doc/fix_dt_reset.html>`_ capability
  by Alan Stagg (SNL) in `PR #385 <https://github.com/sparta/sparta/pull/385>`_
* Enhance functionality of `custom attributes <doc/custom.html>`_ for
  particles, grid cells, and surface elements by Steve Plimpton (SNL
  retired) in `PR #428 <https://github.com/sparta/sparta/pull/428>`_
* Add Kokkos support for `FFTs <doc/compute_fft_grid.html>`_ by James
  Almgren-Bell (UT Austin), Sam Mish (UC Davis), and Stan Moore (SNL) in
  `PR #451 <https://github.com/sparta/sparta/pull/451>`_
* Port global and prob `surface reactions <doc/surf_react.html>`_ to Kokkos
  by Stan Moore (SNL) in `PR #396 <https://github.com/sparta/sparta/pull/396>`_
* Add an option to `compute surf <doc/compute_surf.html>`_ to compute the
  chemical energy due to catalytic surface reactions by Arnaud Borner
  (NASA Ames) in `PR #278 <https://github.com/sparta/sparta/pull/278>`_
* TCE chemistry enhancement (new option) + option to compute chemistry
  rates without performing reaction by Arnaud Borner (NASA Ames) and
  Mitchell Gosma (UIUC) in `PR #279 <https://github.com/sparta/sparta/pull/279>`_
* Extend the `dump surf <doc/dump.html>`_ command with the option to dump
  the area of surface elements to file by Tim Teichmann (KIT) in `PR #438 <https://github.com/sparta/sparta/pull/438>`_
* Introduce "nflux\_incident" and "mflux\_incident" to the
  `compute\_surf <doc/compute_surf.html>`_ command by Tim Teichmann (KIT,
  ITEP): in `PR #416 <https://github.com/sparta/sparta/pull/416>`_
* Add variable Np support to the `fix emit/surf <doc/fix_emit_surf.html>`_
  command by Steve Plimpton (SNL retired) in `PR #409 <https://github.com/sparta/sparta/pull/409>`_
* Do not emit particles in cells that are outside of the flow volume by
  Tim Teichmann (KIT) in `PR #431 <https://github.com/sparta/sparta/pull/431>`_

BACKWARD COMPATIBILITY: The format of stored info in restart files
changed with the enhancement of custom attributes. Thus this version
of the code cannot read older restart files, and vice versa.


----------


**13 Apr 2023**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/13Apr2023>`_

Details for all releases are 
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Added optimized particle move algorithm with `global optmove <doc/global.html>`_ setting, Alan Stagg (SNL), `PR #156 <https://github.com/sparta/sparta/pull/156>`_
* Implemented a variable surface temperature model based on the
  re-radiative equilibrium law, as `fix surf/temp <doc/fix_surf_temp.html>`_ command, Arnaud Borner (NASA Ames),
  `PR #277 <https://github.com/sparta/sparta/pull/277>`_
* Moved ParaView unit and integration tests under SPARTA CI using CMake,
  Tom Otahal (SNL), `PR #347 <https://github.com/sparta/sparta/pull/347>`_
* Added support for Python3, Stefan Fechter (DLR), `PR #355 <https://github.com/sparta/sparta/pull/355>`_, `PR #392 <https://github.com/sparta/sparta/pull/392>`_
* Optimized Kokkos package, Stan Moore (SNL), `PR #357 <https://github.com/sparta/sparta/pull/357>`_, `PR #401 <https://github.com/sparta/sparta/pull/401>`_
* Added support for custom per-grid data in the form of integer/double
  vectors/arrays, Steve Plimpton, `PR #358 <https://github.com/sparta/sparta/pull/358>`_
* Updated Kokkos library version bundled with SPARTA, Stan Moore (SNL),
  `PR #367 <https://github.com/sparta/sparta/pull/367>`_, `PR #394 <https://github.com/sparta/sparta/pull/394>`_
* Refactored and improved `Paraview documentation <doc/Section_howto.html#howto_16>`_, Thomas Otahal (SNL),
  `PR #369 <https://github.com/sparta/sparta/pull/369>`_
* Added argon shock tube example, Jenny Horing and Marisa Petrusky (CU
  Boulder), `PR #376 <https://github.com/sparta/sparta/pull/376>`_
* Enabled the `create\_particles <doc/create_particles.html>`_ command to
  insert particles in cut and split cells which are overlapped by
  surface elements, Steve Plimpton, `PR #381 <https://github.com/sparta/sparta/pull/381>`_
* Enabled particle/reorder without collisions, Stan Moore (SNL), `PR #389 <https://github.com/sparta/sparta/pull/389>`_


----------


**18 Jul 2022**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/18Jul2022>`_

Details for all releases are 
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Update of Kokkos library version bundled with SPARTA, Stan Moore
  (SNL), `PR #353 <https://github.com/sparta/sparta/pull/353>`_, `PR #345 <https://github.com/sparta/sparta/pull/345>`_
* New compute surf options, Steve Plimpton (SNL), `PR #344 <https://github.com/sparta/sparta/pull/344>`_
* New averaging option for fix temp/rescale, Steve Plimpton (SNL), `PR #334 <https://github.com/sparta/sparta/pull/334>`_
* Surf\_collide specular no-slip option, Michael Gallis (SNL), `PR #324 <https://github.com/sparta/sparta/pull/324>`_
* Surf\_collide adiabatic model with isotropic scattering, Tim Teichmann
  (KIT) `PR #329 <https://github.com/sparta/sparta/pull/329>`_


----------


**7 Jan 2022**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/7Jan2022>`_

Details for all releases are 
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Update restart file to store all global options (`PR #316 <https://github.com/sparta/sparta/pull/316>`_), Stan Moore (SNL)
* Add fix temp/global/rescale command to use as a global thermostat on
  the temperature of the entire system (`PR #314 <https://github.com/sparta/sparta/pull/314>`_), Steve Plimpton (SNL)
* Generalize surf collide rotation check to axisymmetric (`PR #311 <https://github.com/sparta/sparta/pull/311>`_), Steve Plimpton (SNL)
* Allow Kokkos surf\_collide\_diffuse to use fixes with custom data (`PR #310 <https://github.com/sparta/sparta/pull/310>`_), Stan Moore (SNL)
* Allow the maximum number or discrete vibrational modes to be extended
  (`PR #307 <https://github.com/sparta/sparta/pull/307>`_), Steve Plimpton
  (SNL)
* Add Kokkos version of fix ambipolar (`PR #304 <https://github.com/sparta/sparta/pull/304>`_), Stan Moore (SNL)
* Add more general external fields (`PR #303 <https://github.com/sparta/sparta/pull/303>`_), Steve Plimpton (SNL)
* Allow continuous rotational DOFs = 3 for complex molecular species
  (`PR #301 <https://github.com/sparta/sparta/pull/301>`_), Steve Plimpton
  (SNL)
* Update Kokkos library in SPARTA to v3.5.0 (`PR #300 <https://github.com/sparta/sparta/pull/300>`_), Stan Moore (SNL)
* Enhancements to the Sparta ParaView tools to allow processing of very
  large refined grids in parallel (`PR #299 <https://github.com/sparta/sparta/pull/299>`_), Thomas Otahal (SNL)
* Add subset option to compute reduce (`PR #297 <https://github.com/sparta/sparta/pull/297>`_), Steve Plimpton (SNL)
* Add fix temp/rescale command for thermostatting (`PR #296 <https://github.com/sparta/sparta/pull/296>`_), Steve Plimpton (SNL)
* Add Exodus 2 format output to surf2paraview.py (`PR #295 <https://github.com/sparta/sparta/pull/295>`_), Thomas Otahal (SNL)
* Enable reaction tallying in computes for on-surface reactions (`PR #294 <https://github.com/sparta/sparta/pull/294>`_), Steve Plimpton (SNL)
* Add nflux to compute\_boundary and compute\_surf commands (`PR #293 <https://github.com/sparta/sparta/pull/293>`_), Tim Teichmann (ITEP,
  KIT)

BACKWARD COMPATIBILITY: The format of stored info in restart files
changed with the addition of global options. Thus this version of the
code cannot read older restart files, and vice versa.


----------


**20 Oct 2021**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/20Oct2021>`_

Details for all releases are 
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Improve scalability of surf2grid algorithm for the persurf case (`PR #241 <https://github.com/sparta/sparta/pull/241>`_), Steve Plimpton (SNL)
* Insure cut/split cell calculations work robustly when round-off issues
  arise (`PR #244 <https://github.com/sparta/sparta/pull/244>`_), Steve
  Plimpton (SNL)
* Add Kokkos support for tvib and custom per-particle attributes (fix
  vibmode, compute tvib/grid) (`PR #251 <https://github.com/sparta/sparta/pull/251>`_), Stan Moore (SNL)
* Allow Kokkos SPARTA to compile with the AMD HIP backend (`PR #255 <https://github.com/sparta/sparta/pull/255>`_), Stan Moore (SNL)
* Update Kokkos library in SPARTA to v3.4.1 (`PR #256 <https://github.com/sparta/sparta/pull/256>`_), Stan Moore (SNL)
* Change RNG in SPARTA from Park to Knuth algorithm (aka ran3 in
  Numerical Recipes book) (`PR #266 <https://github.com/sparta/sparta/pull/266>`_), Michael Gallis
  (SNL), Arnaud Borner (NASA), Stan Moore (SNL)
* Fix issue with temperature varying rotational relaxation not
  maintaining equilibrium at steady state (`PR #268 <https://github.com/sparta/sparta/pull/268>`_), Zakari Eckert (SNL)
* Add nsplit to dump\_grid command (`PR #272 <https://github.com/sparta/sparta/pull/272>`_), Tim Teichmann (KIT)
* Add a surf\_react adsorb model which allows for species to adsorb on
  the surface and surface elements (or box faces) to store state about
  what is adsorbed, which affects future reactions (`PR #128 <https://github.com/sparta/sparta/pull/128>`_ and `PR #291 <https://github.com/sparta/sparta/pull/291>`_), Krishnan Gopalan
  (NASA Ames) and Steve Plimpton (SNL)
* Add grid-style variable option to fix ablate (`PR #292 <https://github.com/sparta/sparta/pull/292>`_), Steve Plimpton

BACKWARD COMPATIBILITY: The global surfpush command was removed.
Because the random number generator changed, simulations with this
versions will not exactly reproduce old simulations.

This is the `list of changed files <patches/files.20Oct21>`_ versus the
26Feb21 version.


----------


**26 Feb 2021**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/26Feb2021>`_

Details for all releases are 
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Added new radius/only cell weighting mode for axisymmetric
  simulations.  See the `global weight <doc/global.html>`_ command. `PR #211 <https://github.com/sparta/sparta/pull/211>`_ and `PR #236 <https://github.com/sparta/sparta/pull/236>`_
* Extended the `global mem/limit <doc/global.html>`_ command to also work for
  acquiring ghost cells. `PR #220 <https://github.com/sparta/sparta/pull/220>`_
* Updated the Kokkos library bundled with SPARTA. `PR #230 <https://github.com/sparta/sparta/pull/230>`_
* Updated the grid2paraview.py tool to read new grid file format that
  does not have parent information (Tom Otahal, SNL), `PR #212 <https://github.com/sparta/sparta/pull/212>`_
* Various other small bugfixes since the last patch

This is the `list of changed files <patches/files.26Feb21>`_ versus the
20Nov20 version.


----------


**20 Nov 2020**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/20Nov2020>`_

Details for all releases are 
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Removed parent cells from the data structures used to store the
  logical structure of the hierarchical grid used in SPARTA.  Each
  processor now stores only the child cells it owns (plus ghost child
  cells).  For large grids with many levels of adaptation this reduces
  the memory cost significantly, since previously each processor stored
  a copy of all the parent cells. `PR #192 <https://github.com/sparta/sparta/pull/192>`_
* Distributed explicit surfaces can now be used with grid adaptation,
  via the `adapt\_grid <doc/adapt_grid.html>`_ and `fix adapt <doc/fix_adapt.html>`_ commands. `PR #192 <https://github.com/sparta/sparta/pull/192>`_
* The `global cellmax <doc/global.html>`_ command was removed, since it is
  no longer needed.  The algorithm that used it for mapping surface
  elements to grid cells was reformulated since it previously relied on
  parent cells. `PR #192 <https://github.com/sparta/sparta/pull/192>`_
* Added interspecies collision parameters (Ed Piekos, SNL), `PR #28 <https://github.com/sparta/sparta/pull/28>`_
* Added CTest and CDash support (Evan Harvery, SNL), `PR #177 <https://github.com/sparta/sparta/pull/177>`_

BACKWARD COMPATIBILITY: The format of stored info in restart files
changed with the removal of parent cells.  Thus this version of the
code cannot read older restart files, and vice versa.

This is the `list of changed files <patches/files.20Nov20>`_ versus the
6Jul20 version.


----------


**6 Jul 2020**

Details on what changed in this release are
  `here <https://github.com/sparta/sparta/releases/tag/6Jul2020>`_

Details for all releases are 
 `here <https://github.com/sparta/sparta/releases>`_

Only new features or notable changes are highlighted here:

* Enabled use of the ambipolar model with recombination reactions.
  Includes a refactoring of group-based collisions, with or without the
  ambiopolar model.  See `PR #159 <https://github.com/sparta/sparta/pull/159>`_
* Option to build SPARTA via CMake.  See `PR #155 <https://github.com/sparta/sparta/pull/155>`_
* Fixed some issues with reading/writing of restart files in low-memory
  mode. See `PR #161 <https://github.com/sparta/sparta/pull/161>`_
* Fixed a bug with the compute tvib/grid command.  See `PR #165 <https://github.com/sparta/sparta/pull/165>`_

This is the `list of changed files <patches/files.6Jul20>`_ versus the
7May20 version.


----------


**7 May 2020**

These are the updates in this release:

* Allow use of restart files larger than 2 GB.
* Kokkos versions of the `compute property/grid <doc/compute_property_grid.html>`_ and `compute distsurf/grid <doc/compute_distsurf_grid.html>`_ comands.
* Updated ParaView visualization scripts.
* Various small bug fixes, mostly with recently added features.

NOTE: This release breaks restart file backwards compatibility, so an
old restart file created by a previous version of the code cannot be
used by the current code version.

This is the `list of changed files <patches/files.7May20>`_ versus the
24Jan20 version.


----------


**24 Jan 2020**

Fixed a bug with grid adaptation introduced by recent code changes.
Also fixed a few other small bugs.

This is the `list of changed files <patches/files.24Jan20>`_ versus the
9Jan20 version.


----------


**9 Jan 2020**

Fixed a small code issue in yesterday's release that broke
compilation with the -DSPARTA\_BIGBIG flag, for running huge
simulations.

This is the `list of changed files <patches/files.9Jan20>`_ versus the
8Jan20 version.


----------


**8 Jan 2020**

This patch release contains 3 new features:

* 3 new computes which tally counts of reactions at surfaces
* Options for transparent surfaces, useful for talling statistics
* 3 new surface collision models - work by Krishnan Gopalan (NASA)

More details:

\a) The new computes which tally surface reactions are `compute react/surf <doc/compute_react_surf.html>`_, `compute react/isurf/grid <doc/compute_react_isurf_grid.html>`_, and `compute react/boundary <doc/compute_react_boundary.html>`_.  `Compute react/isurf/grid <doc/compute_react_isurf_grid.html>`_ can be used with
the `fix ablate <doc/fix_ablate.html>`_ comand to drive surface ablation,
either by itself or in conjunction with the `fix ave/grid <doc/fix_ave_grid.html>`_ command.

In addition, when gas reactions are defined by the
`react <doc/react.html>`_ command, or surface reactions are defined by
the `surf\_react <doc/surf_react.html>`_ command, the counts of each
reaction that occurred during a run are now printed to the screen and
logfile at the end of the run.  This is discussed
`here <doc/Section_start.html#start_7>`_.  The surface reaction
quantities are likewise stored by the `surf\_react <doc/surf_react.html>`_
command, so that they can be accessed by `variables <doc/variable.html>`_
or `stats <doc/stats_style.html>`_ output.

\b) See the `Section Howto 6.15 <doc/Section_howto.html#howto_15>`_ doc page
for a description of how to define and use transparent surfaces.

\c) These are the new surface collision models:

* cll = Cercignani, Lampis, and Lord collision model
* td = thermal desorption collision model from Krishnan Gopalan
* impulsive = collision model for high translational and low internal energies, e.g. a beam of particles, also from Krishnan Gopalan

Details are described on the `surf collide <doc/surf_collide.html>`_ doc
page.

This is the `list of changed files <patches/files.8Jan20>`_ versus the
15Oct19 version.


----------


**15 Oct 2019**

Added the following commands to enable ablation modeling of implicit
surfaces:

* `fix ablate <doc/fix_ablate.html>`_
* `compute isurf/grid <doc/compute_isurf_grid.html>`_
* `write\_isurf <doc/write_isurf.html>`_

These files may also be useful.  The former contains example input
scripts and log files.  The latter gives an overview of ablation
modeling with SPARTA and the relevant commands to use.

* examples/ablation
* `doc/Section\_howto.html#howto\_14 <doc/Section_howto.html#howto_14>`_

Also enabled use of a variable temperature in the `surf\_collide diffuse <doc/surf_collide.html>`_ command, to model time-dependent
surface temperatures.

This is the `list of changed files <patches/files.15Oct19>`_ versus the
9Sep19 version.


----------


**9 Sep 2019**

Extended the `read\_surf <doc/read_surf.html>`_,
`write\_surf <doc/write_surf.html>`_, and `read\_isurf <doc/read_isurf.html>`_
commands to work with explicit, distributed, and implicit surfaces.
For simulations with large counts of explicit surfaces, multiple files
can be used so that the reading and writing can be done in parallel
from many processors.  The explicit surface data file now has 2
formats, with and without a Points section. If the section is not
included, individual point coords are listed with the line and surface
elements. Lines and Triangles now have a unique ID. The lines and
triangles do not need to be listed in order in the file(s), which will
typically be the case in a file written when surface elements are
distributed.

See the `write\_surf <doc/write_surf.html>`_ and
`read\_surf <doc/read_surf.html>`_ commands for details.  Also added
support for the clip operation in the `read\_surf <doc/read_surf.html>`_
command for distributed surfaces.

Fixed a bug with the `dump image ssao <doc/dump_image.html>`_ command
which was reading the dfactor parameter incorrectly.

This is the `list of changed files <patches/files.9Sep19>`_ versus the
16Apr19 version.


----------


**16 Apr 2019**

Arnaud Borner (NASA Ames) added a marching cubes algorithm to enable
3d implicit surfaces (triangles) to be used in a simualation model.

See these doc pages and example scripts for more info
on using 3d implicit surfaces in a simulation:

* `Section howto 6.13 <doc/Section_howto.html#howto_13>`_
* `read\_isurf <doc/read_isurf.html>`_ command
* `tools/implicit\_grid.py <doc/Section_tools.html#implicit>`_
* examples/implicit/in.implicit.3d.\*

This is the `list of changed files <patches/files.16Apr19>`_ versus the
15Apr19 version.


----------


**15 Apr 2019**

Some bug fixes in the collision model (non hard-sphere case) and for
recombination reactions and the TCE reaction model.  These were either
corner cases or small effects.  Thanks to Israel Sebastiao (Purdue U),
Arnaud Borner (NASA Ames Research Center), and @j-d-fuhr (GitHub).

Added rendezvous method for summing surface tallies for output.
Should be much faster for large surface element counts or large
processor counts.

Various Kokkos optimizations.

Low-memory version of reading/writing restart files via the `global mem/limit <doc/global.html>`_ command.

Added some more statistics (mean, min, max, variance) to timing output
at the end of runs.

This is the `list of changed files <patches/files.15Apr19>`_ versus the
15Feb19 version.


----------


**15 Feb 2019**

Added support for distributed surface elements and for implicit 2d
surfaces defined by grid cell corner point values.  This means there
are 3 flavors of surfaces now supported: non-distributed explicit (as
before, the default), distributed explicit (new), and implict (new,
which are also distributed).  The explicit distributed surfaces are
useful to save memory when huge numbers of surface elements are
defined.  Implicit surfaces are useful for modeling porous materials
where the structure of the material may be determined by experimental
images.

These are the doc pages, new or altered commands, tools, and examples
that were added to support these new features:

* `Section howto 6.13 <doc/Section_howto.html#howto_13>`_
* `global surfs <doc/global.html>`_ command
* `read\_isurf <doc/read_isurf.html>`_ command
* `tools/jagged2d.py <doc/Section_tools.html#jagged>`_
* `tools/jagged3d.py <doc/Section_tools.html#jagged>`_
* `tools/implicit\_grid.py <doc/Section_tools.html#implicit>`_
* examples/jagged
* examples/implicit
* examples/circle/in.circle.distributed
* examples/sphere/in.sphere.distributed

Note that not all commands related to surface processing are supported
by the new explcit or implicit surface options.  However tests are
made and error messages should be printed when a not-yet-supported
commmand is used.  See the discussion in `Section howto 6.13 <doc/Section_howto.html#howto_13>`_ for more details.

This is the `list of changed files <patches/files.15Feb19>`_ versus the
4Jan19 version.


----------


**4 Jan 2019**

Added a new algorithm for mapping surface elements to grid cells.  The
original algorithm can still be selected via the `global surfgrid <doc/global.html>`_ command.  The `global cellmax <doc/global.html>`_ and `global splitmax <doc/global.html>`_
settings were also added.

The new algorithm is the default for systems with large surface
element counts.  It should be faster and more scalable than the
previous algorithm when the count of surface elements or processors is
large.

An overflow bug when using extremely large grids was fixed.

A new version of the KOKKOS is included in this patch release.

This is the `list of changed files <patches/files.4Jan19>`_ versus the
13Nov18 version.


----------


**13 Nov 2018**

Made some internal changes to the surface element data structures.
Should not change the behavior of the code for users, but
it touches a lot of files.

This is the `list of changed files <patches/files.13Nov18>`_ versus the
29Oct18 version.


----------


**29 Oct 2018**

Stan Moore and Alan Stagg (Sandia): Added a `global mem/limit <doc/global.html>`_ option to limit the memory allocated and
used when load-balancing or reordering particles.  For very large
simulations which are memory bound this can enable the simulation to
run when one of these operations would otherwise run out of available
memory and generate an error.  See `PR #12 <https://github.com/sparta/sparta/pull/12>`_.

This is the `list of changed files <patches/files.29Oct18>`_ versus the
24Oct18 version.


----------


**24 Oct 2018**

Fixed a bug in the `compute tvib/grid <doc/compute_tvib_grid.html>`_
command when calculating vibrational temperatures of groups with
multiple species.  See `PR #15 <https://github.com/sparta/sparta/pull/15>`_.

This is the `list of changed files <patches/files.24Oct18>`_ versus the
5Sep18 version.


----------


**5 Sep 2018**

Stan Moore, Alan Stagg, and Tim Fuller (Sandia): Additions to KOKKOS
package to support TCE reactions, histogramming fixes, and several
computes.  See `PR #11 <https://github.com/sparta/sparta/pull/11>`_.

Zhi-Hui Wang (University of Chinese Academy of Sciences (UCAS)) and
Israel Borges Sebastiao (Purdue University): Enhanced collision models
to use of omega averaged over the 2 species involved in a collision.
See `PR #10 <https://github.com/sparta/sparta/pull/10>`_.

Small bug fix for ambipolar reactions.

This is the `list of changed files <patches/files.5Sep18>`_ versus the
22Jun18 version.


----------


**22 Jun 2018**

Added discrete vibrational energy modes to the collision and reaction
models.  An optional species files with vibrational mode info on
polyatomic molecular species with 4,6,8 vibrational degrees of freedom
can be input.  An overview of how to use this feature is give in
`Section 6.12 <doc/Section_howto.html#howto_12>`_ of the manual.

See these commands for more details:

* `collide\_modify vibrate no/smooth/discrete <doc/collide_modify.html>`_
* `species file ID1 ID2 ... vibfile vfile <doc/species.html>`_
* `fix vibmode <doc/fix_vibmode.html>`_

There is an examples/vibrate directory with an example input
script that uses these options.

This is the `list of changed files <patches/files.22Jun18>`_ versus the
4Apr17 version.


----------


**4 Apr 2018**

Stan Moore (Sandia) added an option to use per-processor CPU time as a
balancing metric to the `balance\_grid <doc/balance_grid.html>`_ and
`fix\_balance <doc/fix_balance.html>`_ commands.

He also enabled the `compute boundary <doc/compute_boundary.html>`_ and
`surf\_collide <doc/surf_collide.html>`_ commands to work with Kokkos.

This version also includes a new version of the Kokkos library
included with SPARTA.

This is the `list of changed files <patches/files.4Apr18>`_ versus the
23Dec17 version.


----------


**23 Dec 2017**

One more time ... must have drunk too much Christmas eggnog.

This is the `list of changed files <patches/files.23Dec17>`_ versus the
22Dec17 version.


----------


**22 Dec 2017**

We forgot to include the Kokkos library itself in the SPARTA
disribution in the the 21 Dec 2017 version!  This version has it.
See lib/README and lib/kokkos once you unpack the tarball.

This is the `list of changed files <patches/files.22Dec17>`_ versus the
21Dec17 version.


----------


**21 Dec 2017**

Stan Moore, Dan Ibanez, and Tim Fuller (Sandia) have done heroic work
to enable SPARTA to work with the open-source `Kokkos library <https://github.com/kokkos/kokkos>`_.  This is implemented as a
new KOKKOS package in the code.  For an application code like SPARTA,
Kokkos is designed to enable one set of source-code modifications to
run reasonably efficient on a variety of hardware, e.g. multi-core
CPU, GPU, and KNL nodes.  See these sections of the manual for more
details:

* `Section packages <doc/Section_packages.html>`_
* `Section accelerate <doc/Section_accelerate.html>`_
* `KOKKOS package <doc/Section_accelerate.html#acc_3>`_
* `suffix <doc/suffix.html>`_ command
* `package <doc/package.html>`_ command

Note that only some styles and options within the code are
Kokkos-enabled at this point.  This includes the basic move and
collide operations, including for geometries with hierarchical grids
and embedded surfaces.  This `Section 3.5 <doc/Section_commands.html#cmd_5>`_ has (k) flags listed for fixes
and computes that have been adapated for Kokkos.

We also plan to soon post some benchmark numbers on the SPARTA web
page to indicate what kind of performance is possible on different
node architectures (CPU, GPU, KNL) via Kokkos.

The timing output produced at the end of a run was enhanced to include
info about fixes that operate during the timestepping.  Depending on
the input script, some of these can invoke expensive operations
including compute commmands.  This category of operation is now listed
as a "Modify" timing in the breakdown of the timestep.

This is the `list of changed files <patches/files.21Dec17>`_ versus the
27Jul17 version.


----------


**27 Jul 2017**

Eric Emdee (PPPL) called attention to an incorrect use of uniform
versus Gaussian random numbers in the particle emission models from
the simulation box face or surfaces.  This makes a small (~3%)
difference in the distribution of emitted particle velocities.  The
following commands are affected:

* `fix emit/face <doc/fix_emit_face.html>`_
* `fix emit/face/file <doc/fix_emit_face_file.html>`_
* `fix emit/surf <doc/fix_emit_surf.html>`_
* `surf\_collide diffuse <doc/surf_collide.html>`_

This is the `list of changed files <patches/files.27Jul17>`_ versus the
4 May 2017 version.


----------


**4 May 2017**

Fixed a bug with the new `surf\_collide piston <doc/surf_collide.html>`_
command which was not tallying properties correctly on the simulation
box boundary when particles were deleted.  Also added a couple new
keywords to the `compute boundary <doc/compute_boundary.html>`_ command
and made it's tallying similar to the `compute surf <doc/compute_surf.html>`_ command, by using weighted particle counts
for many of the keywords.

Added grid groups via the `group grid <doc/group.html>`_ command, similar
to surface element groups.  This allows grid cells to be assigned to
one or more groups.  The groups are now used as required or optional
arguments to several compute and fix commands as well as other
commands in this list, to optionally limit which grid cells
computations are performed for:

* `compute grid <doc/compute_grid.html>`_
* `compute distsurf/grid <doc/compute_distsurf_grid.html>`_
* `compute eflux/grid <doc/compute_eflux_grid.html>`_
* `compute pflux/grid <doc/compute_pflux_grid.html>`_
* `compute property/grid <doc/compute_property_grid.html>`_
* `compute sonine/grid <doc/compute_sonine_grid.html>`_
* `compute thermal/grid <doc/compute_thermal_grid.html>`_
* `compute tvib/grid <doc/compute_tvib_grid.html>`_
* `dump grid <doc/dump.html>`_
* `fix ave/grid <doc/fix_ave_grid.html>`_
* `fix ave/histo <doc/fix_ave_histo.html>`_
* `fix ave/histo/weight <doc/fix_ave_histo.html>`_
* `fix adapt/grid <doc/fix_adapt.html>`_
* `adapt\_grid <doc/adapt_grid.html>`_

A new grid *group-ID* argument is required for the computes in the
list, is now implemented by the `dump grid <doc/dump.html>`_ command (was
already an argument), and is required by the `fix ave/grid <doc/fix_ave_grid.html>`_, `fix adapt/grid <doc/fix_adapt.html>`_, and
`adapt\_grid <doc/adapt_grid.html>`_ commands.  A *group-ID* setting is a
new optional keyword for the `fix ave/histo <doc/fix_ave_histo.html>`_
and `fix ave/histo/weight <doc/fix_ave_histo.html>`_ commands for grid
cell selection in the histogramming, as are new optional keywords
*region* and *mixture* for particle selection in the histogramming.

BACKWARD COMPATIBILITY: This means the syntax for all of the commands
in the above list have changed (except dump grid and the fix ave/histo
commands) because they now require an additional grid group-ID
argument.  The format of restart files also changes with this release,
because the grid group and surface element group information is now
stored differently.

The grid cell group assignments persist when doing grid adaptation,
via the `adapt\_grid <doc/adapt_grid.html>`_ or `fix adapt/grid <doc/fix_adapt.html>`_ commands, which means new refined
or coarsened grid cells inherit the same group assignment from their
predecessor cells.

Fixed a bug when using `adaptive gridding <doc/adapt_grid.html>`_
with cell weighting via the `global weight <doc/global.html>`_ command,
where the weights were not reset correctly for adapated grid cells.

Added a *temperature* option to the
`create\_particles <doc/create_particles.html>`_ command to allow creation
of particles with a thermal temperature gradient.

This is the `list of changed files <patches/files.4May17>`_ versus the
4 Apr 2017 version.


----------


**4 Apr 2017**

Added a new `surf\_collide piston <doc/surf_collide.html>`_ which can be
used on a simulation box boundary or a set of surface elements that
act like a boundary, as a subsonic pressure boundary condition.

Added a new `compute fft/grid <doc/compute_fft_grid.html>`_ command to
calculated 2d or 3d FFTs of per-grid quantities, so long as the
simulation grid is regular (not hierarchical).  This can be used for
computing energy spectra in turbulent flows.

Added *nwt* and *mflux* keywords to the `compute surf <doc/compute_surf.html>`_ command, for tallying of weighted particle
collisions with surface elements, and also the mass flux onto each
surface element.

This is the `list of changed files <patches/files.4Apr17>`_ versus the
16 Mar 2017 version.


----------


**16 Mar 2017**

Fixed two bugs.  The first was with grid adaptation sometimes creating
a new grid whose grid cells and corner points could not be succesfully
marked as inside versus outside a surface.

The second was with surface reactions sometimes creating a new
particle that was not in the correct grid cell, which could lead to
the particle moving inside the surface, or other errors.

This is the `list of changed files <patches/files.16Mar17>`_ versus the
10 Mar 2017 version.


----------


**10 Mar 2017**

Fixed a bug with the `fix ave/surf <doc/fix_ave_surf.html>`_ command when
used with a single input value.

Thanks to Dan Barnes (Coronado Consulting) for flagging this issue.

This is the `list of changed files <patches/files.10Mar17>`_ versus the 8
Sep 2016 version.


----------


**8 Sep 2016**

Fixed a couple of logic bugs for multi-group recombination reactions.

This is the `list of changed files <patches/files.8Sep16>`_ versus the 23
Aug 2016 version.


----------


**23 Aug 2016**

Fixed a couple of bookkeeping bugs with recombination reactions, one
for single group collisions, one for multi-group collisions.

This is the `list of changed files <patches/files.23Aug16>`_ versus the 8
Aug 2016 version.


----------


**8 Aug 2016**

Enhanced the syntax for many commands to allow multiple selected
values from a compute or fix vector, or multiple columns from a
compute or fix array, to be specified with a single argument, using a
wildcard syntax.  E.g. specifiying c\_ID[\*] as a single argument gets
expanded into multiple arguments c\_ID[1], c\_ID[2], ..., using
these wildcard rules:

* \* = 1 to N
* \*n = 1 to n
* m\* = m to N
* m\*n = m to n

where N is the length of the vector or number of columns in the array.

These commands now have the enhanced syntax:

* `stats\_style <doc/stats_style.html>`_
* `dump particles or dump grid or dump surf <doc/dump.html>`_
* `compute reduce <doc/compute_reduce.html>`_
* `fix ave/grid <doc/fix_ave_grid.html>`_
* `fix ave/histo <doc/fix_ave_histo.html>`_
* `fix ave/surf <doc/fix_ave_grid.html>`_
* `fix ave/time <doc/fix_ave_time.html>`_

Also removed a restriction on the header line printed before stats
output during a run.  The per-column fields were limited to 8
characters each which could mean long IDs for computes, fixes, or
variable names were truncated.  Now the full column name, as specified
in the `stats\_style <doc/stats_style.html>`_ command, is output.  This
includes the "c\_", "f\_", or "v\_" prefix for compute, fix, variable
quantities, so there will be no ambiguity if a compute and fix have
the same ID.

Added options to the `stats\_modify format <doc/stats_modify.html>`_ and
`dump\_modify format <doc/dump_modify.html>`_ commands, and made their
syntax consistent with each other.

Each now takes a *line* option to specify the format of an entire line
of output, *int* and *float* options to specify the format of each
integer or floating point value output, an *M string* option to change
the format of a single value in column M of the output, or a *none*
option to restore the default format for all output values.

BACKWARD COMPATIBILITY: Several of the commands listed above
previously allowed an entire array of input values (from a compute or
fix) to be specified using just the ID of the compute or fix.  You now
have to use the wildcard syntax above to have the same effect.

BACKWARD COMPATIBILITY: This patch can change the format of one line
in the screen or logfile output, namely the header line that describes
the columns of stats output.  If your output includes quantities from
a compute or fix or variable, then that line will have a slightly
different syntax, as described above.  If you have a post-processing
parser that reads that line or uses it to identify columns of data,
you may to need to adjust your parse semantics.

BACKWARD COMPATIBILITY: The `dump\_modify format <doc/dump_modify.html>`_
command previously only allowed the format for an entire line to be
specified.  Using that option now requires the "line" setting be used
after "format", to distinguish it from the other options that were
added.

This is the `list of changed files <patches/files.8Aug16>`_ versus the 5
Aug 2016 version.


----------


**5 Aug 2016**

Added `fix ave/histo <doc/fix_ave_histo.html>`_ and `fix ave/histo/weight <doc/fix_ave_histo.html>`_ commands, to enable
histogramming of global, per-particle, and per-grid cell quantities.
The histograms can also be time averaged if desired.

Also added an internal-style variable to the "variable" command for
use as input to other SPARTA commands which use a variable they can
reset.  The `create\_particles <doc/create_particles.html>`_ command is an
example.  This is more efficient way to enable variable values
to be reset internally by the code.

BACKWARD COMPATIBILITY: The
`create\_particles <doc/create_particles.html>`_ command now requires an
internal-style variable, not an equal-style variable as input for some
its species, density, and velocity options.

This is the `list of changed files <patches/files.5Aug16>`_ versus the 11
Jul 2016 version.


----------


**11 Jul 2016**

Fixed a normalization error with the `compute thermal/grid press <doc/compute_thermal_grid.html>`_ command which was not including a
cell weighting factor.  This typically gave incorrect answers for
axisymmetric problems where radially dependent cell weighting is often
enabled.

This is the `list of changed files <patches/files.11Jun16>`_ versus the 6
Jun 2016 version.

Thanks to Dmitrii Ivchencko (University of Limoges, France) for
pointing out the problem.


----------


**6 Jun 2016**

Tried to make the cutting and splitting of grid cells by surfaces a
more robust operation and give users less to worry about.

* The numerical round-off fix where surface points are shifted slightly
  when they are within an epsilon distance of grid cell surfaces has
  been automated, so there should no longer be a need to use the `global surfpush <doc/global.html>`_ command.  It is still there for debugging
  purposes, but "global surfpush yes" is now the default.
* The code is now more agressive about marking the corner points as
  inside versus outside for grid cells that overlap with surfaces.  This
  makes the marking of non-overlapping grid cells as inside versus
  outside less likely to get stuck with an error that not all cells
  could be marked.

This is the `list of changed files <patches/files.6Jun16>`_ from the 2
Jun 2016 version.


----------


**2 Jun 2016**

Disallow Tsurf = 0.0 for the `surf\_collide diffuse <doc/surf_collide.html>`_ model.  This can cause problems with
particles effectively sticking to surfaces w/out bouncing off.

This is the `list of changed files <patches/files.2Jun16>`_ from the 1
Jun 2016 version.


----------


**1 Jun 2016**

Fixed a bug with the `read\_restart <doc/read_restart.html>`_ command not
resetting the `global surfmax <doc/global.html>`_ setting correctly, if
it had been set to a large value in the input script that wrote the
restart file.

This is the `list of changed files <patches/files.1Jun16>`_ from the 31
May 2016 version.


----------


**31 May 2016**

Added *fx*\ , *fy*\ , *fz* options to the `compute surf <doc/compute_surf.html>`_ command to allow drag and lift on a body
in a flow to be more easily computed.

This is the `list of changed files <patches/files.31May16>`_ from the 24
May 2016 version.


----------


**24 May 2016**

Fixed a bug with the `write grid parent <doc/write_grid.html>`_ command,
when dumping grids with 64-bit IDs (and parent cells that actually
exceeded 32 bits).

This is the `list of changed files <patches/files.24May16>`_ from the 10
May 2016 version.


----------


**10 May 2016**

Added 2 new compute commands, `compute eflux/grid <doc/compute_eflux_grid.html>`_ and `compute pflux/grid <doc/compute_pflux_grid.html>`_, for tallying the per-grid
cell energy and momentum flux densities.  These were implemented with
help from Alejandro Garcia (San Jose State University).

Also fixed a bug in the `read\_restart <doc/read_restart.html>`_ command
when reading very large restart files (with > 2B grid cells), when the
code is compiled with the -DSPARTA\_BIGBIG option.

This is the `list of changed files <patches/files.10May16>`_ from the 31
Mar 2016 version.


----------


**31 Mar 2016**

Fixed a bug with how the `compute surf <doc/compute_surf.html>`_ command
was interacting with the `fix ave/surf <doc/fix_ave_surf.html>`_ and
`dump surf <doc/dump.html>`_ commands.  It had to do with when the
normalization factors were applied to surface tallying, which caused
problems if the results of the compute were used multiple times (on
the same timestep) by different commands.

Thanks to Flavia Bonelli (Karlsruhe, Germany) for sending a script
that triggered the issue.

This is the `list of changed files <patches/files.31Mar16>`_ from the 21
Mar 2016 version.


----------


**21 Mar 2016**

Alan Stagg (ORNL) flagged an occasional bug with the
`species <doc/species.html>`_ command reading species files with long
lists of species.

This is the `list of changed files <patches/files.21Mar16>`_ from the 14
Mar 2016 version.


----------


**14 Mar 2016**

Fixed a typo bug with the `group surf <doc/group.html>`_ *union* and
*intersect* options.

Thanks to Alan Stagg (ORNL) for pointing out the problem.

This is the `list of changed files <patches/files.14Mar16>`_ from the 13
Mar 2016 version.


----------


**13 Mar 2016**

Fixed some bugs in `grid adaptation <doc/adapt_grid.html>`_, `surface groups <doc/group.html>`_, and the `compute distsurf <doc/compute_distsurf_grid.html>`_ command.

Thanks to Ram Prakash (UNSW-ADFA, Canberra) for sending a script that
triggered these problems.

This is the `list of changed files <patches/files.13Mar16>`_ from the 12
Mar 2016 version.


----------


**12 Mar 2016**

Changed the formula used for the `compute grid massrho <doc/compute_grid.html>`_ value to be for all particles in the
grid cell (i.e. total mass), not the per-particle average.

BACKWARD COMPATIBILITY: This will change the value output by this
compute, or `fix ave/grid <doc/fix_ave_grid.html>`_ or `dump grid <doc/dump.html>`_, for the *massrho* value.

Thanks to Israel Sebastiao (Purdue) for pointing this out.

This is the `list of changed files <patches/files.12Mar16>`_ from the 11
Mar 2016 version.


----------


**11 Mar 2016**

A couple of files were mistakenly not checked into the repository
for the 9/10 Mar versions.

This is the `list of changed files <patches/files.11Mar16>`_ from the 10
Mar 2016 version.


----------


**10 Mar 2016**

Added a *velocity* option to the
`create\_particles <doc/create_particles.html>`_ command.  It allows the
streaming velocity of created particles to be set by
spatially-dependent variables which depend on the position of the
created particle.  The formulas for both are defined by `equal-style variables <doc/variable.html>`_.  Example input script commands and a
small animation of a movie with an initial velocity distribution that
causes particles to collapse to a point is included in the
`create\_particles <doc/create_particles.html>`_ command doc page.

This is the `list of changed files <patches/files.10Mar16>`_ from the 9
Mar 2016 version.


----------


**9 Mar 2016**

Fixed a bug in the `group surf <doc/group.html>`_ command with how it was
using surface IDs vs surface types.

Thanks to Ram Prakash (UNSW-ADFA, Canberra) for sending a script that
triggered this problem.

This is the `list of changed files <patches/files.9Mar16>`_ from the 8
Mar 2016 version.


----------


**8 Mar 2016**

Added two options to the `create\_particles <doc/create_particles.html>`_
command, with keywords *species* and *density*\ .  The first allows the
species of created particles to be set by a spatially-dependent
variable which depends on the position of the created particle.  The
second allows the density of particles created in each grid cell to be
set by a spatially-dependent variable which depends on the center
point of the grid cell.  The formulas for both are defined by
`equal-style variables <doc/variable.html>`_.  Example input script
commands and snapshots of the initial particle distributions are
included in the `create\_particles <doc/create_particles.html>`_ command
doc page.

This is the `list of changed files <patches/files.8Mar16>`_ from the 29
Feb 2016 version.


----------


**29 Feb 2016**

Fixed some bookkeeping issues for grid cells volumes when cells are
adjacent to a surface but wholly inside or wholly outside, i.e. the
surface elements just touch the face, edge, or corner point of a grid
cells.

This is the `list of changed files <patches/files.29Feb16>`_ from the 22
Feb 2016 version.


----------


**22 Feb 2016**

Implemented a near-neighbor algorithm for choosing collision partners.
The new option is enabled by the `collide\_modify nearcp <doc/collide_modify.html>`_ command.  This is a means of choosing
a collision partner J for a particle I that is geometrically closer
(within its grid cell) than the standard algorithm which simply
chooses any random particle J within the grid cell.  It is more
expensive than the standard algorithm but can enable the use of larger
grid cells due to the sub-grid-cell resolution if offers.

This is the `list of changed files <patches/files.22Feb16>`_ from the 17
Feb 2016 version.


----------


**17 Feb 2016**

Fixed a logic bug with the `fix emit/surf <doc/fix_emit_surf.html>`_
command when running a problem geometry where surfaces split grid
cells into sub-cells.

Thanks to Alan Stagg (ORNL) for sending a script that triggered
this problem.

This is the `list of changed files <patches/files.17Feb16>`_ from the 16
Feb 2016 version.


----------


**16 Feb 2016**

Changed the inner workings of the `global surfpush yes <doc/global.html>`_ command, which is used when there are round-off
issues when mapping surface elements to grid cells which in rare cases
can generate an error.  The command now allows setting of 3 values
(slo,shi,svalue) which determine the range of surface point positions
that are altered, and the new value they are set to.  Using the *yes*
option sets these 3 settings to generically good values which seem to
work for most of the round-off issues we have seen.

Added some error checking and warning messages to the various `fix emit <doc/fix_emit_face.html>`_ command variants when using the *subsonic*
keyword to invoke subsonic boundary conditions.  There are unusual
cases (empty grid cells, small temperatures) which can lead to extreme
flow conditions that we try to protect against more carefully.

This is the `list of changed files <patches/files.16Feb16>`_ from the 5
Jan 2016 version.


----------


**5 Jan 2016**

Added grid-style variables to SPARTA as explained on the
`variable <doc/variable.html>`_ doc page.  Similar to equal-style and
particle-style variables, grid-style variables define a formula that
is calculated for each grid cell in the simulation.  The formulas can
contain a variety of scalar quantities and math operations as well as
per-grid quantities calculated by a per-grid compute (e.g. the
`compute grid <doc/compute_grid.html>`_ command), a per-grid fix
(e.g. the `fix ave/grid <doc/fix_ave_grid.html>`_ command), or another
grid-style variable.  Grid-style variables can be used as input to the
`dump grid <doc/dump.html>`_, `compute reduce <doc/compute_reduce.html>`_,
and `fix ave/grid <doc/fix_ave_grid.html>`_ commands.

This is the `list of changed files <patches/files.5Jan16>`_ from the 8
Dec 2015 version.


----------


**8 Dec 2015**

Added a pressure option to the VALUES listing in the input data file
read by the `fix emit/face/file <doc/fix_emit_surf.html>`_ command.  This
allow a subsonic boundary condition to be set on a face of the
simulation box where the pressure and temperature or just a pressure
are spatially varying.  This allows for consistent boundary conditions
when the flow is subsonic.

Also fixed some addtitional issues with using the subsonic boundary
condition with all 3 of the fix emit commands, when starting with an
empty simulation box, i.e. no particles initially exist in the cells
where particles are to be inserted.

This is the `list of changed files <patches/files.8Dec15>`_ from the 25
Nov 2015 version.


----------


**25 Nov 2015**

Added a *subsonic* option to the `fix emit/surf <doc/fix_emit_surf.html>`_ command to allow a subsonic boundary
condition to be set for surfaces in the simulation box by specifying a
pressure and temperature or just a pressure.  This allows for
consistent boundary conditions when the flow is subsonic.

Also fixed some issues we discovered with the recently released `fix emit/face <doc/fix_emit_face.html>`_ command.

This is the `list of changed files <patches/files.25Nov15>`_ from the 6
Nov 2015 version.


----------


**6 Nov 2015**

Added a *subsonic* option to the `fix emit/face <doc/fix_emit_face.html>`_ command to allow a subsonic boundary
condition to be set for one or more faces of the simulation box by
specifying a pressure and temperature or just a pressure.  This allows
for consistent boundary conditions when the flow is subsonic.  At some
point, we plan to add a similar capability to the `fix emit/face/file <doc/fix_emit_face_file.html>`_ and `fix emit/surf <doc/fix_emit_surf.html>`_ commands.

Added *temp* and *press* values to the `compute thermal/grid <doc/compute_thermal_grid.html>`_ command, so that either or
both a temperature and pressure can be calculated for each grid cell
based on the thermal (non-streaming) kinetic energy of particles in
the cell.

BACKWARD COMPATIBILITY: Previously, the "compute
thermal/grid"-doc/compute\_thermal\_grid.html command did not take any
values, because it only computed a thermal temperature.  It now
requires at least one value to be specified.

This is the `list of changed files <patches/files.6Nov15>`_ from the 3
Nov 2015 version.


----------


**3 Nov 2015**

Added *pxrho*\ , *pyrho*\ , *pzrho*\ , and *kerho* values to the
`compute grid <doc/compute_grid.html>`_ command to tally momentum and
kinetic energy density on a per-grid cell basis.

This is the `list of changed files <patches/files.3Nov15>`_ from the 23
Oct 2015 version.


----------


**23 Oct 2015**

Added two `mixture <doc/mixture.html>`_ keywords for rotational and
vibrational temperature, in addition to thermal temperature, which can
be used to set the initial rotational and vibrational energy of
created particles, e.g. via the
`create\_particles <doc/create_particles.html>`_ command or the various
fixes that emit particles from simulation box faces and surfaces.

Added a *nearcp* keyword to the
`collide\_modify <doc/collide_modify.html>`_ command to enable selection
of collision partners via a near neighbor algorithm, as opposed to
randomly selecting collision partners from all the particles in a grid
cell.  The details of the algorithm and a paper citation are given on
the `collide\_modify <doc/collide_modify.html>`_ doc page.

BACKWARD COMPATIBILITY: The internal syntax of `restart files <doc/read_restart.html>`_ changed to add the two new temperature
options to mixtures.  This means the current version of the code
cannot read old restart files and vice versa.

This is the `list of changed files <patches/files.23Oct15>`_ from the 4
Oct 2015 version.


----------


**4 Oct 2015**

Added a `read\_particles <doc/read_particles.html>`_ command which reads a
snapshot of particles into the current simulation from a file, in the
same format the `dump particle <doc/dump.html>`_ command creates.  This
allows a simulation to start with a previous simulation's set of
particles, or to use particles output from another simulation code as
input to SPARTA, assuming they have been massaged into the needed
format.

This is the `list of changed files <patches/files.4Oct15>`_ from the 3
Oct 2015 version.


----------


**3 Oct 2015**

Fixed a couple issues with how restart files are used to re-initialize
a system.  It should now be easier to read a restart file
early in an input script and not have to re-define other simulation
properties at different points of the restart script as compared
to the original input script.

Also, if the restart file is read on a different number of processors,
it may be necessary to re-balance the partitioning of grid cells to
processors so that the simulation can be setup with needed ghost
cells.  There are new additional *gridcut* and *balance* options on
the `read\_restart <doc/read_restart.html>`_ command to enable this.

This is the `list of changed files <patches/files.3Oct15>`_ from the 2
Oct 2015 version.


----------


**2 Oct 2015**

Added *nfrac* and *massfrac* keywords to the `compute grid <doc/compute_grid.html>`_ command.  Added *nparent*\ , *nchild*\ , and
*nsplit* keywords to the `stats\_style <doc/stats_style.html>`_ command.

Added a `compute thermal/grid <doc/compute_thermal_grid.html>`_ command
that does time averaging for thermal temperature calculation over all
timesteps, when it is used as input to the `fix ave/grid <doc/fix_ave_grid.html>`_ command.  The *thermal* keyword of the
`compute sonine/grid <doc/compute_sonine_grid.html>`_ command has been
removed, since the new command replaces its functionality.

Previously, computing a thermal temperature via the `compute sonine/grid thermal <doc/compute_sonine_grid.html>`_ command used
center-of-mass (COM) velocities that were only calculated for the
current timestep.  In the new command, when doing time averaging via
the `fix ave/grid <doc/fix_ave_grid.html>`_ command, the COM velocity is
calculated for all particles across multiple timesteps.  We think this
is a more accurate and less noisy way to do it.

This is the `list of changed files <patches/files.2Oct15>`_ from the 22
Sep 2015 version.


----------


**22 Sep 2015**

Added a *massrho* keyword to the `compute grid <doc/compute_grid.html>`_
command.

Added a *vanish* style model to the
`surf\_collide <doc/surf_collide.html>`_ commmand, which simply deletes
particles when they hit surface elements assigned to that model.  This
is a way to have a group of surface elements act as an outflow
boundary for particles, as well as an inflow boundary via the `fix emit/surf <doc/fix_emit_surf.html>`_ command.

Surface collision and surface reaction models also now tally the
number of particles that hit and react on the surface elements they
are assigned to.  Both for the current timestep and cummulative counts
during a run.  These values can be accessed by the
`stats\_style <doc/stats_style.html>`_ command for output with statistics,
and by `variables <doc/variable.html>`_ that define formulas.  The latter
means they can be used by any command that uses a variable as input,
e.g. "the `fix ave/time <doc/fix_ave_time.html>`_ command.

This is the `list of changed files <patches/files.22Sep15>`_ from the 12
Sep 2015 version.


----------


**12 Sep 2015**

Fixed some compiler warnings that were showing up on a Mac compile.

This is the `list of changed files <patches/files.12Sep15>`_ from the 11
Sep 2015 version.


----------


**11 Sep 2015**

Edited/added some src/MAKE/Makefile.machine files to make
building SPARTA more straightforward.  Also changed some
of the example input scripts.

This is the `list of changed files <patches/files.11Sep15>`_ from the 21
Aug 2015 version.


----------


**21 Aug 2015**

Options for adapting the hierarchical grid used by SPARTA have been
added.  This can either be done before or between `run <doc/run.html>`_
commands via the `adapt\_grid <doc/adapt_grid.html>`_.  Or adaptation can
be performed on-the-fly during a run, via the `fix adapt <doc/fix_adapt.html>`_ command.  Adapation can involve refinement
and/or coarsening of grid cells, based on a variety of criteria,
including values calculated by `computes <doc/compute.html>`_ or
`fixes <doc/fix.html>`_.  The `compute distsurf/grid <doc/compute_distsurf_grid.html>`_ command was added to
calculate one such criterion: distance of a grid cell from any surface
element.

Commands to modify surfaces have also been added.  The
`move\_surf <doc/move_surf.html>`_ and `fix move/surf <doc/fix_move_surf.html>`_ commands allow a group of surface
elements to be moved in various manners either between runs or during
a run.  The `write\_surf <doc/write_surf.html>`_ command write surface
elements to a file, which can be useful after clipping has taken
place, surface elements have been moved or removed.  The
`remove\_surf <doc/remove_surf.html>`_ command can remove a subset of
surface elements from the simulation.

The list of new commands is here:

* `adapt\_grid <doc/adapt_grid.html>`_
* `fix adapt <doc/fix_adapt.html>`_
* `move\_surf <doc/move_surf.html>`_
* `fix move/surf <doc/fix_move_surf.html>`_
* `write\_surf <doc/write_surf.html>`_
* `remove\_surf <doc/remove_surf.html>`_
* `compute distsurf/grid <doc/compute_distsurf_grid.html>`_

See new example problems that exercise these commmands in the
examples/adapt and surf directories, and on the Pictures/Movies page
of the web site (soon).

The `ParaView tools <doc/Section_tools.html#paraview>`_ have also been
upgraded to work with grid files that adapt over time, for
visualization using `ParaView <https://www.paraview.org>`_.

This is the `list of changed files <patches/files.21Aug15>`_ from the 17
Jun 2015 version.


----------


**17 Jun 2015**

One more forgotten file!

This is the `list of changed files <patches/files.17Jun15>`_ from the 16
Jun 2015 version.


----------


**16 Jun 2015**

Forgot a new file needed in yesterday's update.

This is the `list of changed files <patches/files.16Jun15>`_ from the 15
Jun 2015 version.


----------


**15 Jun 2015**

Fixed a bug when one of the `fix emit <doc/fix_emit_face.html>`_ face commands
emitted particles on multiple faces of the simulation box and the `fix balance <doc/fix_balance.html>`_ command was also enabled.

This is the `list of changed files <patches/files.15Jun15>`_ from the 15
May 2015 version.


----------


**15 May 2015**

Small bug in yesterday's post.  This should fix it.

This is the `list of changed files <patches/files.15May15>`_ from the 14
May 2015 version.


----------


**14 May 2015**

Added a *region* keyword to the `create\_grid <doc/create_grid.html>`_
command which be used in place of the *level* keyword at any level of
a hierarchical grid definition.  This allows the grid to be refined
based on whether a grid cell is inside a geometric region defined by
the `region <doc/region.html>`_ command.  Regions can be simple geometric
objects or unions or intersections of simple objects or other unions
or intersections.  This is thus a more flexible way of defining a
hierarchical grid.

This is the `list of changed files <patches/files.14May15>`_ from the 13
May 2015 version.


----------


**13 May 2015**

Fixed a bug with surface clipping in the read\_surf command, when
multiple surfaces are read in, and the later ones are clipped.

This is the `list of changed files <patches/files.13May15>`_ from the 12
May 2015 version.


----------


**12 May 2015**

Several new features are added to the code in this version.

The ambipolar approximation for plasmas (charged particles) is now
supported.  See `Section howto 4.11 <doc/Section_howto.html#howto_11>`_
for details of how the ambipolar approximation is implemented in
SPARTA and how to use it from an input script.  Relevant commands
inlcude:

* `fix ambipolar <doc/fix_ambipolar.html>`_
* `collide\_modify ambipolar yes <doc/collide_modify.html>`_
* `react <doc/react.html>`_ command with ambipolar reactions
* `compute count <doc/compute_count.html>`_

Gas reaction models for ionization were added to the dissociation and
exchange options, all of which can now be specified via the
`react <doc/react.html>`_ command.  These can now include ambipolar
reactions involvoing ambipolar ions and their electrons.

Surface reaction models for dissociation, exchange, and recombination
can now be specified via the `surf\_react <doc/surf_react.html>`_ command.
These can include ambipolar reactions, e.g. recombination of ions and
their electrons.

Surface groups were added so that properties like collision and
reaction models can be assigned to subsets of surface elements.  This
is implemented via a new `group <doc/group.html>`_ commmand.  Several
commands now take surface group IDs as arguments, changing their
syntax.  The following commands are affected.

* `read\_surf <doc/read_surf.html>`_
* `compute surf <doc/compute_surf.html>`_
* `fix ave/surf <doc/fix_ave_surf.html>`_
* `surf\_modify <doc/surf_modify.html>`_

Also the `bound\_modify <doc/bound_modify.html>`_ command syntax is
changed, since surface reaction models can be assigned to simulation
box boundaries as well.

The fix inflow and fix inflow/file commands were renamed to `fix emit/face <doc/fix_emit_face.html>`_ and `fix emit/face/file <doc/fix_emit_face_file.html>`_.

A new `fix emit/surf <doc/fix_emit_surf.html>`_ command was added to
enable outflux of particles from surface elements.

A *region* option was added to the
`create\_particles <doc/create_particles.html>`_, `fix emit/face <doc/fix_emit_face.html>`_, and `fix emit/face/file <doc/fix_emit_face_file.html>`_ commands.  This allows
creation of particles within limited geometric regions of the
simualation domain.

All the dump commmands now take a "group" argument, changing their
syntax, to select which particles, grid cells, or surface elements are
output.  I.e. the dump particle and dump image commands take a
mixture-ID as an argument, the dump grid command takes a grid group ID
as an argument (only "all" is currently an option), and the dump
surface command takes a surface group ID as an argument.  See the
`dump <doc/dump.html>`_ command doc page for details.

A bug was fixed for the `fix emit/face/file <doc/fix_emit_face_file.html>`_ cmomand when using it for
2d axisymmetric models.  The appropriate axisummetric volume
weightings were not being applied to grid cells to adjust their number
of created particles.

BACKWARD COMPATIBILITY: The internal syntax of `restart files <doc/read_restart.html>`_ changed to add group information.  This
means the current version of the code cannot read old restart files
and vice versa.  The syntax of these commands changed:
`read\_surf <doc/read_surf.html>`_, `compute surf <doc/compute_surf.html>`_,
`fix ave/surf <doc/fix_ave_surf.html>`_,
`surf\_modify <doc/surf_modify.html>`_,
`bound\_modify <doc/bound_modify.html>`_.  Likewise the `dump particle <doc/dump.html>`_, `dump grid <doc/dump.html>`_, and `dump surface <doc/dump.html>`_ command syntax changed to take an extra
argument.  The fix inflow and fix inflow/face commands were renamed to
`fix emit/face <doc/fix_emit_face.html>`_ and `fix emit/face/file <doc/fix_emit_face_file.html>`_.

This is the `list of changed files <patches/files.12May15>`_ from the 13
Mar 2015 version.


----------


**13 Mar 2015**

Added some visualization examples using `ParaView <https://www.paraview.org>`_ and the
`paraview tools <doc/Section_tools.html#paraview>`_ provided with SPARTA
to convert SPARTA output to ParaView input.  The example pics are on
the `Pictures & Movies page <pictures.html#paraview>`_ of the web site.
The surface data and STL files used for several of these space craft
were added to the data directory of the distribution.

.. _paraview: https://www.paraview.org



This is the `list of changed files <patches/files.13Mar15>`_ from the 6
Mar 2015 version.


----------


**6 Mar 2015**

Tom Otahal (Sandia) has enhanced his `Python scripts <doc/Section_tools.html#paraview>`_ which can convert SPARTA grid
data (input and output) to ParaView format.  It can now read a SPARTA
parent grid which defines a hierarchical grid with multiple levels of
refinement.  It also now allows for specification of 2d slice planes,
each of which will output ParaView files with grid values on the 2d
plane.

This is the `list of changed files <patches/files.6Mar15>`_ from the 5
Mar 2015 version.


----------


**5 Mar 2015**

Fixed a memory issue when performing reactions on a problem where
collisions are performed for multiple species groups within each grid
cell.

Also fixed a logic bug with clipping multiple sucessive surfaces,
read in by the `read\_surf <doc/read_surf.html>`_ command.

This is the `list of changed files <patches/files.5Mar15>`_ from the 4
Mar 2015 version.

Thanks to Arnaud Borner (NASA Ames) and Aggelos Klothakis for
sending test problem that triggered the issues.


----------


**4 Mar 2015**

Fixed a small issue with a couple of Makefiles that were
causing issues on Macs.

This is the `list of changed files <patches/files.4Mar15>`_ from the 26
Feb 2015 version.

Thanks to David Wolfe (NPS) for calling attention to these issues.


----------


**26 Feb 2015**

Added a `fix inflow/file <doc/fix_emit_face_file.html>`_ command which
allows input of particles on a simulation box face, with properties of
the input specified in a file.  The file contains a mesh of points
that overlay part or all of the box face.  Quantities can be defined
at the mesh points that affect the created particles, e.g. a streaming
velocity, thermal temperature, number fractions of species in the
mixture, overall density, etc.  The quantities can vary spatially on
the mesh, so that the input flux of particles is also spatially
varying.

There is an examples/flowfile directory with an example input script,
as well as a movie on the `SPARTA movies web page <https://sparta.github.io/pictures.html>`_ that illustrates use of
the command.

This is the `list of changed files <patches/files.26Feb15>`_ from the 21
Feb 2015 version.


----------


**21 Feb 2015**

One more change that was mistakenly introduced by the 17Feb15 patch.

This is the `list of changed files <patches/files.21Feb15>`_ from the 17
Feb 2015 version.


----------


**17 Feb 2015**

Fixed bug in `restart files <doc/read_restart.html>`_ not including the
`global weight cell <doc/global.html>`_ command setting if it was
enabled, which was added for axisymmetric geometries.

This is the `list of changed files <patches/files.17Feb15>`_ from the 16
Feb 2015 version.

Thanks to Angelos Klothakis for sending a script that triggered
this issue.


----------


**16 Feb 2015**

Two small bug fixes in the `VSS collision model <doc/collide.html>`_.
One could generate unrealistic temperatures as the outcome of certain
reactions.  The second was a bookkeeping error for the code vs the
format of the input data file of reactions, with regard to
dissociation reactions producing only monoatomic products (molecule +
atom -> 3 atoms).

Also some changes to a few coefficients in the input data file
for TCE reactions in air.

This is the `list of changed files <patches/files.16Feb15>`_ from the 21
Jan 2015 version.

Thanks to Arnaud Borner (NASA Ames) for calling attention
to these issues and flagging the specific TCE reactions.


----------


**21 Jan 2015**

Fixed an rare bug with particle moves hitting exactly on the
edge or corner point of a surface element that is in common with
multiple surfaces.

Also found a case where the `global surfpush yes <doc/global.html>`_
command needs to move surface points that are slightly outside a grid
cell to be on the surface, not just from inside to the surface (just
for the intersection operation).  So the *surfpush* option now does
both.

This is the `list of changed files <patches/files.21Jan15>`_ from the 13
Jan 2015 version.


----------


**13 Jan 2015**

Fixed an occasional bug with axisymmetic moves that could cause a
particle to end up in the wrong grid cell when being communicated to a
new processor.  This is with the `global gridcut <doc/global.html>`_
command set to a positive finite value.

This is the `list of changed files <patches/files.13Jan15>`_ from the 7
Jan 2015 version.

Thanks to Angelos Klothakis for sending a test geometry that had the
problem.


----------


**7 Jan 2015**

Added a *relax variable* option to the `collide <doc/collide.html>`_
command to allow for per-collision computation of rotational and
vibrational relaxation, instead of just the *constant* parameters used
previously.  The additional 4 parameters per species needed for the
rotational and vibrational relaxation equations can be specified in
the VSS or VHS collision data file.  See data/vss.air for examples.

This is the `list of changed files <patches/files.7Jan15>`_ from the 19
Dec 2014 version.


----------


**19 Dec 2014**

Added two new reaction styles, acessible via the
`react <doc/react.html>`_ command.  A Quantum-Kinetic (QK) model due to
Bird, and a hybrid Total Collision Energy / Quantum Kinetic (TCE/QK)
model (both parts due to Bird).  The same input file of reactions and
reaction coefficients can be used for either.  To use the hybrid
style, flags in the reaction file can be set to "A" or "Q" for each
reaction to specify whether it is performed using the TCE (Arrhenius)
or QK model.

This is the `list of changed files <patches/files.19Dec14>`_ from the 10
Dec 2014 version.


----------


**10 Dec 2014**

Fixed a bug with reading restart files via the
`read\_restart <doc/read_restart.html>`_ command when a hierarchical
multi-level grid is defined.

Also added some logic to support STL unordered maps used by the
Clang++ compiler, via the compile-time switch -DSPARTA\_UNORDERED\_MAP,
as discussed in `Section 2.2 <doc/Section_start.html#start_2>`_ of the
manual.

This is the `list of changed files <patches/files.10Dec14>`_ from the 19
Nov 2014 version.

Thanks to Arnaud Borner (NASA Ames) for sending an input
script that triggered the problem.


----------


**19 Nov 2014**

Some testing and debug lines were left in the recent update of
the `fix inflow <doc/fix_emit_face.html>`_ command, which cause incorrect
input fluxes.  This patch removes the lines.

This is the `list of changed files <patches/files.19Nov14>`_ from the 15
Nov 2014 version.


----------


**15 Nov 2014**

The `tools/grid\_refine.py <doc/Section_tools.html#gridrefine>`_ tool had
some incorrect logic for refining 3d grids.

Also added an axisymmetric example problem in examples/axi.

This is the `list of changed files <patches/files.15Nov14>`_ from the 13
Nov 2014 version.

Thanks to Baofeng Ma for pointing out the problem with the
grid\_refine tool.


----------


**13 Nov 2014**

Fixed another bug with particle moves and surface bounces in
axisymmetric models to allow for the rare case when a particle bounces
multiple times off the same surface in a single timestep, due to its
curvature.

Also, three bug fixes for  the `fix inflow <doc/fix_emit_face.html>`_ and
`surf\_collide diffuse <doc/surf_collide.html>`_ commands.

* A needed normalization factor for the inward normal vector was
  added.
* Components of inflow velocities parallel to the influx surface were
  not fully correct.
* The surface-reflected distribution of molecules was modified so that
  when the surface has a velocity component perpendicular to the surface
  the molecules will be introduced with the correct speed.

This is the `list of changed files <patches/files.13Nov14>`_ from the 3
Nov 2014 version.


----------


**3 Nov 2014**

Fixed another bug with particle moves and surface bounces in
axisymmetric models due to how to interpret the solutions to a
quadratic equation.

This is the `list of changed files <patches/files.3Nov14>`_ from the 31
Oct 2014 version.


----------


**31 Oct 2014**

Fixed a numerical round-off issue with the intersection of surface
elements and grid cells.  This could cause an error when the
`read\_surf <doc/read_surf.html>`_ command was used if the surface had
points that were "nearly" on grid cell boundaries.  The work-around is
to shift any such points from slightly inside a grid cell to the cell
boundary (just for the intersection operation).  This operation can
now be invoked by the `global surfpush yes <doc/global.html>`_ command.
At some point we will likely automatically invoke it if the error
occurs consistently.

This is the `list of changed files <patches/files.31Oct14>`_ from the 28
Oct 2014 version.

Thanks to Tim Deschenes for sending a test case with a simple geometry
that triggered the problem.


----------


**28 Oct 2014**

Roman Maltsev fixed some energy conservation bugs in the VSS collision
model for the `collide vss <doc/collide.html>`_ command.

This is the `list of changed files <patches/files.28Oct14>`_ from the 27
Oct 2014 version.


----------


**27 Oct 2014**

Particle tracking across cell boundaries and for particle/surface
collisions was too simplistic for some models, leading to lost
particles or incorrect surface bounces.  This version should fix the
problems.

This is the `list of changed files <patches/files.27Oct14>`_ from the 25
Oct 2014 version.


----------


**25 Oct 2014**

Added an option to the `read\_surf clip <doc/read_surf.html>`_ command to
allow surface points very close to the simulation box boundaries to be
pushed to the boundary before a clipping operation is performed.
This can help prevent very small line or triangles from being created
due to the clip.

This is the `list of changed files <patches/files.25Oct14>`_ from the 24
Oct 2014 version.


----------


**24 Oct 2014**

The `surf\_collide diffuse translate and rotate <doc/surf_collide.html>`_
options were missing a check to subtract out any component of surface
velocity that was normal to the surface, so that only the proper
post-bounce tangential velocity was added to colliding particles.

This is the `list of changed files <patches/files.24Oct14>`_ from the 20
Oct 2014 version.


----------


**20 Oct 2014**

The tools/stl2surf.py file was inadvertantly left out of the 12Aug14
patch.

Tom Otahal (Sandia) has written `2 Python scripts <doc/Section_tools.html#paraview>`_ which can convert SPARTA grid
and surface data (input and output) to ParaView format.
`ParaView <https://www.paraview.org>`_ is a popular, powerful,
freely-available visualization package.  You must have ParaView
installed to use the Python scripts.  See tools/paraview/README for
more details.

Fixed a memory bug with the `dump grid <doc/dump.html>`_ command
that could cause problems when there are grid cells split by surfaces
into two or more sub-cells.

Fixed a logic error when using a `global gridcut <doc/global.html>`_
value > 0.0 that showed up in flow regimes with long timesteps where
particle moves across processor boundaries were not correctly
completed.

This is the `list of changed files <patches/files.20Oct14>`_ from the 9
Oct 2014 version.


----------


**9 Oct 2014**

Added a *tvib* option to the `compute grid <doc/compute_grid.html>`_
command to enable vibrational temperature to be calculated within
the classical approximation.

The tallying of surface properties that depend on surface element
area was incorrect for axisymmetric models.

Added an error check to insure grid cell neighbors and ghost cells
have been created by the time any surfaces are read in via the
`read\_surf <doc/read_surf.html>`_ command.

NOTE: We realized particle/surface collisions in axisymmetric models
are missing some axisymmetric corrections that can cause problems for
big timesteps and collisions near the axisymmetry axis (y = 0).  An
upcoming patch should include some updated code for this.

This is the `list of changed files <patches/files.9Oct14>`_ from the 19
Aug 2014 version.


----------


**19 Aug 2014**

Added a `grid\_refine.py tool <doc/Section_tools.html#gridrefine>`_ to the
tools directory to create a grid file, readable by the
`read\_grid <doc/read_grid.html>`_ command, which has been adapted to a
surface file, readable by the `read\_surf <doc/read_surf.html>`_ command.

The tool has several options for how the adaptation is done.  At this
point, the adaptivity is strictly based on geometric considerations.
At some point we will add flow characteristics to the options, so the
new computational grid can reflect attributes of a previously computed
flow field.

This is the `list of changed files <patches/files.19Aug14>`_ from the 15
Aug 2014 version.


----------


**15 Aug 2014**

One change for applying cell weights to collisions was missing from
the 11Aug14 patch for enabling axi-symmetry.

This is the `list of changed files <patches/files.15Aug14>`_ from the 14
Aug 2014 version.


----------


**14 Aug 2014**

New `compute lambda/grid <doc/compute_lambda_grid.html>`_ command, which
can calcluate the mean free path and Knudsen number for each grid
cell.  This can be dumped to a file via the dump command and used to
adapt the computational grid, e.g. between two runs.

Soon we will also release an external script in the tools directory
to perform this adpativity operation.

This is the `list of changed files <patches/files.14Aug14>`_ from the 13
Aug 2014 version.


----------


**13 Aug 2014**

Added a `scale\_particles <doc/scale_particles.html>`_ command to allow
the total number of particles in the simulation to be scaled up or
down via particle cloning or deletion.  This is useful for changing
the resolution of a model between runs.

This is the `list of changed files <patches/files.13Aug14>`_ from the 12
Aug 2014 version.


----------


**12 Aug 2014**

Added a `stl2surf.py tool <doc/Section_tools.html#stl2surf>`_ to the tools
directory to convert stereolithography (STL) files to SPARTA-format
surface files, which can be read by the `read\_surf <doc/read_surf.html>`_
command.

The STL files must be in ASCII (text) format, which can be produced by
various meshing programs.  Note that surface object(s) in the STL file
must be "watertight" in order to be used by SPARTA (unless they are
being clipped to the simulation box), as described on the
`read\_surf <doc/read_surf.html>`_ doc page.

This is the `list of changed files <patches/files.12Aug14>`_ from the 11
Aug 2014 version.


----------


**11 Aug 2014**

Added an axi-symmetry capability to allow 2d simulations with a y=0
axis of symmetry to be run.  See the `boundary <doc/boundary.html>`_ and
`global weight <doc/global.html>`_ commands for details, and also
`Section 4.2 <doc/Section_howto.html#howto_2>`_ for an overview
discussion.

This is the `list of changed files <patches/files.11Aug14>`_ from the 29
Jul 2014 version.


----------


**29 Jul 2014**

Typo bug in the `create\_grid <doc/create_grid.html>`_ command that
affected how it processed some input script options.

This is the `list of changed files <patches/files.29Jul14>`_ from the 23
Jul 2014 version.


----------


**23 Jul 2014**

Removed a couple auxiliary files that slipped into tarball distribution
accidentally.

This is the `list of changed files <patches/files.23Jul14>`_ from the 21
Jul 2014 version.


----------


**21 Jul 2014**

Added some output of chemical reaction statistics to the screen and
log file.

This is the `list of changed files <patches/files.21Jul14>`_ from the 7
Jul 2014 version.


----------


**7 Jul 2014**

Initial public release of SPARTA.  This version supercedes earlier
distributed beta versions.

