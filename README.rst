Install printer
===============

1. download appimage from https://github.com/prusa3d/PrusaSlicer
   and save it as ~/prusa
2. mark the appimage as executable (`chmod +x ~/prusa`)
3. start prusa once via ~/prusa and just close it again
4.  Install printer definitions in ~/.config/PrusaSlicer/::

      curl -L https://github.com/ecsv/Qidi-Printer-Definitions/archive/refs/heads/xmax_icarus_prusa.tar.gz |tar -C ~/.config/PrusaSlicer/ -xzv --strip-components=1
