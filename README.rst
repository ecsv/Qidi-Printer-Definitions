Install printer
===============

1. download appimage from https://github.com/Ultimaker/Cura/releases (we assume
   here that it is cura 5.4) and save it as ~/cura
2. mark the appimage as executable (chmod +x ~/cura)
3. start cura once via ~/cura and just close it again
4.  Install printer definitions in ~/.local/share/cura/5.4::

      curl -L https://github.com/ecsv/Qidi-Printer-Definitions/archive/refs/heads/xmax_icarus.tar.gz |tar -C ~/.local/share/cura/5.4/ -xzv --strip-components=1

5. start cura again

   a. agree to user license agreement
   b. ignore changelog
   c. skip creation of "Ultimaker Account"
   d. "Add a non-networked printer" -> Qidi -> X-Max
   e. Accept machine settings

6. Go to Marketplace to install "OctoPrint Connection" (Green Octo symbol on top of a blue connector)
7. Restart Cura
8. Go to Preferences -> Printers -> Connect OctoPrint

   a. Select the octopi instance from the list
   b. Request (API Key) -> Login in browser and grant the access to the application
   c. enable "Connect to printer before sending printjob"
   d. Press connect
   e. Close dialogs

9. Go to "Monitor" tab to check if the cam is visible and the connection is working

Clear Cura state
================

This repository contains experimental configurations for Qidi X-Max with Icarus
2.1 (Orbiter 2.0 + Dragon Hotend). Changes will not be done in a backward or
forward compatible way. So when in doubt, please clear the cura state::

  rm -rf ~/.cache/Ultimaker\ B.V. ~/.cache/cura/ ~/.config/cura ~/.local/share/cura
