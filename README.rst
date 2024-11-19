Install printer
===============

1. Basic installation (only one of them required)

   a. as AppImage:

      1. download appimage from https://github.com/Ultimaker/Cura/releases (we assume
         here that it is cura 5.9) and save it as ~/cura
      2. mark the appimage as executable (chmod +x ~/cura)
      3. start cura once via ~/cura and just close it again
      4.  Install printer definitions in ~/.local/share/cura/5.9::

            curl -L https://github.com/ecsv/Qidi-Printer-Definitions/archive/refs/heads/xmax_icarus.tar.gz |tar -C ~/.local/share/cura/5.9/ -xzv --strip-components=1
            rm -rf ~/.cache/cura/


   b. via flatpak

      1. Install from flathub::

             flatpak --user remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
             flatpak --user config --set languages ""
             flatpak --user install com.ultimaker.cura

      2. start cura once via `flatpak run com.ultimaker.cura`
      3. Install printer definitions::

             curl -L https://github.com/ecsv/Qidi-Printer-Definitions/archive/refs/heads/xmax_icarus.tar.gz |tar -C ~/.var/app/com.ultimaker.cura/data/cura/5.9/ -xzv --strip-components=1
             rm -rf ~/.var/app/com.ultimaker.cura/cache

2. start cura again

   a. agree to user license agreement
   b. ignore changelog
   c. skip creation of "Ultimaker Account"
   d. "Add a non-networked printer" -> Qidi -> X-Max
   e. Accept machine settings

3. Go to Marketplace to install "OctoPrint Connection" (Green Octo symbol on top of a blue connector)
4. Restart Cura
5. Go to Preferences -> Printers -> Connect Moonraker

   a. Address http://$IP/
   b. Format "UFP with Thumbnail"
   c. Press Save
   e. Close dialogs

Clear Cura state
================

This repository contains experimental configurations for Qidi X-Max with Icarus
2.1 (Orbiter 2.0 + Dragon Hotend). Changes will not be done in a backward or
forward compatible way. So when in doubt, please clear the cura state::

  rm -rf ~/.cache/Ultimaker\ B.V. ~/.cache/cura/ ~/.config/cura ~/.local/share/cura
