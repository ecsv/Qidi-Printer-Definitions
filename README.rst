Install printer
===============

1. Basic installation (only one of them required)

   a. as AppImage:

      1. download appimage from https://github.com/Ultimaker/Cura/releases (we assume
         here that it is cura 5.8) and save it as ~/cura
      2. mark the appimage as executable (chmod +x ~/cura)
      3. start cura once via ~/cura and just close it again
      4.  Install printer definitions in ~/.local/share/cura/5.8::

            curl -L https://github.com/ecsv/Qidi-Printer-Definitions/archive/refs/heads/xmax_icarus.tar.gz |tar -C ~/.local/share/cura/5.8/ -xzv --strip-components=1
             curl -L https://raw.githubusercontent.com/pedrolamas/klipper-preprocessor/master/KlipperPreprocessor.py -o ~/.local/share/cura/5.8/scripts/KlipperPreprocessor.py


   b. via flatpak

      1. Install from flathub::

             flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
             flatpak install com.ultimaker.cura

      2. start cura once via `flatpak run com.ultimaker.cura`
      3. Install printer definitions::

             curl -L https://github.com/ecsv/Qidi-Printer-Definitions/archive/refs/heads/xmax_icarus.tar.gz |tar -C ~/.var/app/com.ultimaker.cura/data/cura/5.8/ -xzv --strip-components=1
             curl -L https://raw.githubusercontent.com/pedrolamas/klipper-preprocessor/master/KlipperPreprocessor.py -o ~/.var/app/com.ultimaker.cura/data/cura/5.8/scripts/KlipperPreprocessor.py

2. start cura again

   a. agree to user license agreement
   b. ignore changelog
   c. skip creation of "Ultimaker Account"
   d. "Add a non-networked printer" -> Qidi -> X-Max
   e. Accept machine settings

3. Go to Marketplace to install "OctoPrint Connection" (Green Octo symbol on top of a blue connector)
4. Restart Cura
5. Go to Preferences -> Printers -> Connect OctoPrint

   a. Select the octopi instance from the list
   b. Request (API Key) -> Login in browser and grant the access to the application
   c. enable "Connect to printer before sending printjob"
   d. Press connect
   e. Close dialogs

6. Go to "Monitor" tab to check if the cam is visible and the connection is working

Clear Cura state
================

This repository contains experimental configurations for Qidi X-Max with Icarus
2.1 (Orbiter 2.0 + Dragon Hotend). Changes will not be done in a backward or
forward compatible way. So when in doubt, please clear the cura state::

  rm -rf ~/.cache/Ultimaker\ B.V. ~/.cache/cura/ ~/.config/cura ~/.local/share/cura
  
  
Klipper Estimator
=================

In your post-processing scripts, there should be a Klipper Preprocessor.
Please create a config file::

  {
    "max_velocity": 450.0,
    "max_acceleration": 6750.0,
    "minimum_cruise_ratio": 0.5,
    "square_corner_velocity": 5.0,
    "instant_corner_velocity": 1.0,
    "move_checkers": [
      {
        "axis_limiter": {
          "axis": [
            0.0,
            0.0,
            1.0
          ],
          "max_velocity": 10.0,
          "max_accel": 15.0
        }
      },
      {
        "extruder_limiter": {
          "max_velocity": 120.0,
          "max_accel": 1796.047292491724
        }
      }
    ]
  }

And download https://github.com/Annex-Engineering/klipper_estimator/releases

In your post-processing configuration, please disable "Add TIMELAPSE_TAKE_FRAME"
and enable "Use klipper estimator". Specify the **full path** to your config
file and to klipper estimator
