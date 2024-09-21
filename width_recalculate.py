#! /usr/bin/env python3

from math import pi

WIDTH = 0.45
HEIGHT = 0.2
NOZZLE = 0.4
FILAMENT = 1.75


#################################
# orcaslicer precision wall tests
# measured width: 0.89
#################################

# precision wall outer (width 0.45103122648394384)
POS1 = (130.313, 102.93)
POS2 = (168.687, 102.93)
EXTRUSION = (1.23449) / 0.948

# spacing 0.459

# precision wall inner (width 0.45103122648394384)
POS1 = (130.313, 103.381)
POS2 = (168.687, 103.381)
EXTRUSION = (1.23449) / 0.948

# total width according to orca: 0.9100312264839439 ???
# overlap: -0.007968773516056182



#################################
# orcaslicer normal wall tests
# measured width: 0.915
#################################

# precision wall outer (width 0.4725030732164431)
POS1 = (130.335, 102.940)
POS2 = (168.665, 102.940)
EXTRUSION = (1.29795) / 0.948

# spacing 0.448

# precision wall inner (width 0.4295827058959327)
POS1 = (130.335, 103.37)
POS2 = (168.665, 103.37)
EXTRUSION = (1.29795) / 0.948

# total width according to orca: 0.8990428895561879
# overlap: 0.003042889556187811



###############################################
# cura normal weird tests (broken layer height)
# measured width: 0.976
###############################################

# precision wall outer (width 0.5035046618158372)
POS1 = (130.278, 102.931)
POS2 = (168.64, 102.929)
EXTRUSION = (944.16559 - 942.5254) / 0.948

# spacing 0.45

# precision wall inner (width 0.5035046618158372)
POS1 = (168.64, 103.379)
POS2 = (130.317, 103.38)
EXTRUSION = (935.72966 - 934.09114) / 0.948

# total width according to orca: 0.9535046618158372
# overlap: 0.05350466181583724



#################################
# cura normal normal tests
# measured width: 0.9855
#################################

# precision wall outer (width 0.49491963287698704)
POS1 = (168.64, 102.929)
POS2 = (130.278, 102.931)
EXTRUSION = (1062.93201 - 1061.56519) / 0.948

# spacing 0.449

# precision wall inner (width 0.49491948491634113)
POS1 = (130.317, 103.38)
POS2 = (168.64, 103.379)
EXTRUSION = (1071.34802 - 1069.98259) / 0.948

# total width according to orca: 0.943919632876987
# overlap: 0.045919484916341125



#################################
# orca optimized 0.86 shell test
# measured width: XXXXXX
#################################

# precision wall outer (width 0.45575090254030415)
POS1 = (130.347, 102.978)
POS2 = (168.653, 102.978)
EXTRUSION = 1.31493

# spacing 0.413

# precision wall inner (width 0.4557486869323759)
POS1 = (130.144, 103.394)
POS2 = (168.816, 103.394)
EXTRUSION = 1.30903

# total width according to orca: 0.868748686932376
# overlap: 0.042750902540304114



#################################
# orca optimized box with two walls only
# measured width: XXXXXX
#################################

# precision wall inner (width 0.45000897579188437)
POS1 = (130.132, 103.382)
POS2 = (168.868, 103.382)
EXTRUSION = 1.31116

# spacing 0.407

# precision wall outer (width 0.45000036070628796)
POS1 = (129.725, 102.975)
POS2 = (164.39, 102.975)
EXTRUSION = 1.17337

# total width according to orca: 0.857
# overlap: 0.04300933649817229



#################################
# orca optimized 0.86 shell test (classic wall engine)
# measured width: XXXXXX
#################################

# precision wall inner (width 0.45000897579188437)
POS1 = (130.144, 103.394)
POS2 = (168.816, 103.394)
EXTRUSION = 1.30903

# spacing 0.419

# precision wall outer (width 0.4499929994730516)
POS1 = (132.167, 102.975)
POS2 = (169.275, 102.975)
EXTRUSION = 1.25604

# total width according to orca: 0.869000987632468
# overlap: 0.031000987632467947 (which is near the expected 0.031415926535897934)




# just assume for now that width > height)
def get_print_area(width, height):
    return (height / 2) ** 2 * pi + height * (width - height)


def get_width_from_area(area, height):
    return area / height + height / 4 * (4 - pi)


def extrusion_length(pos1, pos2):
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]
    return (diff_x ** 2 + diff_y ** 2) ** 0.5


def extrusion_area(length, extrusion, filament):
    return extrusion / length * (filament / 2) ** 2 * pi


def perimeter_squishing(height):
    return height ** 2 / 4 * pi


def total_width(height, width, perimeters):
    return width * perimeters - perimeter_squishing(height) * (perimeters - 1)


area = get_print_area(WIDTH, HEIGHT)
print(f'area {area}')
width = get_width_from_area(HEIGHT * WIDTH, HEIGHT)
print(f'width {width} and difference {width - WIDTH}')
total = total_width(HEIGHT, WIDTH, 2)
print(f'total width {total}')
print(f'perimeter_squishing {perimeter_squishing(HEIGHT)}')

length = extrusion_length(POS1, POS2)
area = extrusion_area(length, EXTRUSION, FILAMENT)
print(f'move area {area}')
width = get_width_from_area(area, HEIGHT)
print(f'move width {width}')
width_cura = area / HEIGHT
print(f'cura move width {width_cura}')
