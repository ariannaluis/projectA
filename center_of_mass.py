import numpy as np
import matplotlib.pyplot as plt

def center_of_mass_2objects(m1, r1, m2, r2):
    """
    m1, m2 : masses (scalars)
    r1, r2 : positions as length-2 arrays or lists [x, y]
    """
    r1 = np.array(r1, dtype=float)
    r2 = np.array(r2, dtype=float)

    # center of mass: R_cm = (m1*r1 + m2*r2) / (m1 + m2)
    R_cm = (m1 * r1 + m2 * r2) / (m1 + m2)

    # displacements from COM
    d1 = r1 - R_cm
    d2 = r2 - R_cm

    return R_cm, d1, d2

def main():
    # ---- read from user input ----
    print("Enter mass and position (x y) for object 1:")
    m1 = float(input("m1 = "))
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))

    print("\nEnter mass and position (x y) for object 2:")
    m2 = float(input("m2 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))

    r1 = [x1, y1]
    r2 = [x2, y2]

    R_cm, d1, d2 = center_of_mass_2objects(m1, r1, m2, r2)

    print("\nCenter of mass (x_cm, y_cm):")
    print(f"R_cm = ({R_cm[0]:.3f}, {R_cm[1]:.3f})")

    print("\nDisplacement of object 1 from COM (r1 - R_cm):")
    print(f"d1 = ({d1[0]:.3f}, {d1[1]:.3f})")

    print("\nDisplacement of object 2 from COM (r2 - R_cm):")
    print(f"d2 = ({d2[0]:.3f}, {d2[1]:.3f})")

    # ---- plotting ----
    # extract coordinates
    x1, y1 = r1
    x2, y2 = r2
    x_cm, y_cm = R_cm

    plt.figure()

    # plot object 1
    plt.scatter(x1, y1, marker='o', s=80, label='Object 1')
    # plot object 2
    plt.scatter(x2, y2, marker='s', s=80, label='Object 2')
    # plot center of mass
    plt.scatter(x_cm, y_cm, marker='*', s=200, label='Center of Mass')

    # arrows from COM to each object (displacements)
    plt.arrow(x_cm, y_cm, d1[0], d1[1],
              length_includes_head=True, head_width=0.1)
    plt.arrow(x_cm, y_cm, d2[0], d2[1],
              length_includes_head=True, head_width=0.1)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Two-Body System and Center of Mass')
    plt.legend()
    plt.gca().set_aspect('equal', 'box')  # equal scaling on both axes
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
