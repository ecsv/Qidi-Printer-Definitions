Install printer
===============

1. download appimage from https://github.com/Ultimaker/Cura/releases (we assume
   here that it is cura 5.1) and save it as ~/cura
2. mark the appimage as executable (chmod +x ~/cura)
3. start cura once via ~/cura and just close it again
4.  Install printer definitions in ~/.local/share/cura/5.1::

      curl -L https://github.com/ecsv/Qidi-Printer-Definitions/archive/refs/heads/xmax_icarus.tar.gz |tar -C ~/.local/share/cura/5.1/ -xzv --strip-components=1

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


Qidi X-Max configuration
========================

These profiles are made for the Qidi X-Max running firmware 2.27 and having
Icarus 2.0 with Dragon Hotend (Standard Flow) + Orbiter 2.0 installed.
It assumes that the flow is not configured to any specific material die
swelling and is instead trying to modify the material specific flow parameter.

The configuration gcode was::

  ; Motor adjustments
  
  M8002 I1; X motor direction
  M8005 I1; Stepper motor direction
  
  ; Set XY distance (commented, normally not required. Set to match your printer X and Y values)
  M8024 I300; X
  M8025 I255; Y
  
  ; E-step adjustments
  M8011 S0.0014492753623188406; E-steps, recommended 0.001570796 but that would be only 637 steps and not 690 as recommended by the Orbiter 2 manufacturer
  
  ; Set Bed height
  M8026 I296.850006; Z height (commented, normally not required. Set to match your printer build height)
  
  ; Set max temp
  ; M8022 I400; (use at own risk, increase print temp)
  
  ; Acceleration and Jerk
  M8007 I6; Jerk, recommended 15
  M8008 I500; Acceleration X/Y, recommended 1000
  
  ; Save
  M8500; Save changes

Unloading filament
==================

It is not really related to these Cura profile but it is recommended
not to use Qidis unloading procedure because it tried to push heavily
with filament against the nozzle. This will sooner or later affect the
extruder (gears).

Instead, heat up the hotend to the filament temperature and run::

  ; To wait for temperature:
  ;M109 S220
  
  M83
  G0 E-15 F2000        ;extract filament to cold end area 
  G4 P5000            ;wait for three seconds
  G0 E15 F2000         ;push back the filament to smash any stringing 
  G0 E-15 F2000      ;Extract back fast in the cold zone 
  G0 E-70 F300        ;Continue extraction slowly, allow the filament time to cool solid before it reaches the gears
