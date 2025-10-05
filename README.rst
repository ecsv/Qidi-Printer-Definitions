Install printer
===============

1. Basic installation (only one of them required)

   a. as AppImage:

      1. download appimage from https://github.com/SoftFever/OrcaSlicer/releases/tag/v2.3.1 and safe it as ``orca``
      2. mark the appimage as executable (``chmod +x ~/orca``)
      3. start Orcaslicer via ``~/orca``

   b. via flatpak

      1. download (`x86_64`) flatpak from https://github.com/SoftFever/OrcaSlicer/releases/tag/v2.3.1
      2. install it via `flatpak install --user OrcaSlicer-Linux-flatpak_V2.3.1_x86_64.flatpak`
      3. start it via `flatpak run io.github.softfever.OrcaSlicer` or your desktop environment runner

2. Select to use the System SSL certificates (and let it remember the choice)
3. Go through each step of the Setup Wizard and create a dummy printer (which will not be used by us)

   a. Press "Get Started"
   b. Select "Europe" and press "Next"
   c. Select under "Generic Klipper Printer" "0.4mm nozzle" and press "Next"
   d. Leave selected Filaments as is and press "Next"
   e. Don't select proprietary Plugins and just press "Finish"

4. If the "New Version" dialog appears, just select "Check for stable updates only" and then "Skip this version"

5. Download profiles from https://github.com/ecsv/Qidi-Printer-Definitions/archive/refs/heads/xmax_icarus_orca.zip
6. Go to ``File`` -> ``Import`` -> ``Import Configs`` and select the downloaded ``Qidi-Printer-Definitions-xmax_icarus_orca.zip``
7. Repeat the last step (no, I am not joking) and let it overwrite all profiles/filaments
8. Switch to the ``Prepare`` tab and switch the printer to ``Qidi X-Max Icarus 0.4 nozzle``
9. Click on the Wifi symbol next to the printer to set the ``Hostname, IP or URL`` point to the printer ``$IP``
10. Select the correct Bed type (usually, ``Cool Plate`` is wrong) - stick to ``Engineering Plate`` or ``Textured PEI`` for now
11. Select the correct Filament type (the more precise the better)
12. Select the correct process type

    ``0.20mm Engineering``
      a "consistent" slow profile which prints perimeters from Outside to inside (similar to the Cura profile)
    ``0.20mm normal``
      is basically the "fast" profile from Cura (and is not the fastest possible)
    ``0.20mm Structural``
      a slightly slower "Speed" profile with less acceleration and max speed (but usually still really fast)
    ``0.20mm Speed``
      is basically the fastest possible print speed which I've tested with good results
    ``0.16mm Structural``
      derived from ``0.20mm Structural`` with lower layer height and minor adjustments (like number of bottom/top layers)
    ``0.12mm Fast Detail``
      derived from ``0.16mm Speed`` with lower layer height but wall speed and acceleration was slightly reduced

Clear OrcaSlicer state
======================

This repository contains experimental configurations for Qidi X-Max with Icarus
2.1 (Orbiter 2.0 + Dragon Hotend). Changes will not be done in a backward or
forward compatible way. So when in doubt, please clear the Orcaslicer state::

  rm -rf ~/.cache/orca-slicer/ ~/.local/share/orca-slicer/ ~/.config/OrcaSlicer/
  rm -rf ~/.var/app/io.github.softfever.OrcaSlicer/
