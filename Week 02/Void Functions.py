# Author:       Deirdre Connolly
# Filename:     Void Functions.py
# Description:  Functions - void and with parameters

EDGE_SOLID = "*"
MIDDLE_SOLID = "-"
EDGE_WALLS = "|"
HEIGHT_OF_BOX = 2


def draw_box():
    for i in range (1,4):
        print(EDGE_WALLS, EDGE_WALLS, sep="       ")
    print(EDGE_SOLID + (MIDDLE_SOLID * 7) + EDGE_SOLID)


def draw_nose():
    print("   /" + "\\" +
          "\n  /" + "  \\" +
          "\n /" + "    \\" +
          "\n/" + "      \\")
    print(EDGE_SOLID + (MIDDLE_SOLID * 7) + EDGE_SOLID)


def draw_thrusters():
    print("  // " + "\\\\"
          "\n //  " + " \\\\"
          "\n//   " + "  \\\\")


draw_nose()
draw_box()
draw_box()
draw_box()
draw_thrusters()
