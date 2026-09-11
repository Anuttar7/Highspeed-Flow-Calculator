from flowCalculator import calculator
import sys

calc = calculator()

while (True):
    print("--Flow Calculator--\n")
    print("1. Calculate isentropic flow parameters.")
    print("2. Calculate normal shock parameters.")
    print("3. Calculate oblique shock parameters.")
    print("4. Change built in properties.")
    print("5. Exit.")
    print("Choose an option: ")
    choice = int(input())
    if (choice == 1):
        while (True):
            print("Which parameter do you want to use as input?")
            print("1. Mach number")
            print("2. Pressure ratio (p/p0)")
            print("3. Temperature ratio (T/T0)")
            print("4. Density ratio (rho/rho0)")
            print("5. Mach Angle (mu)")
            print("6. Prandtl-Meyer Angle (nu)")
            print("7. Area ratio in subsonic flow (A/A*)")
            print("8. Area ratio in supersonic flow (A/A*)")
            print("9. Back to main menu")
            print("10. Exit")
            print("Choose an option: ")
            choice = int(input())
            if (choice == 1):
                print("Enter Mach number: ")
                value = float(input())
                calc.isentropic_Mach(value)
                input("Press Enter to continue...")
            elif (choice == 2):
                print("Enter Pressure Ratio (p/p0): ")
                value = float(input())
                calc.isentropic_pp0(value)
                input("Press Enter to continue...")
            elif (choice == 3):
                print("Enter Temperature Ratio (T/T0): ")
                value = float(input())
                calc.isentropic_TT0(value)
                input("Press Enter to continue...")
            elif (choice == 4):
                print("Enter Density Ratio (rho/rho0): ")
                value = float(input())
                calc.isentropic_RhoRho0(value)
                input("Press Enter to continue...")
            elif (choice == 5):
                print ("Enter Mach Angle (mu) in degrees: ")
                value = float(input())
                calc.isentropic_MachAngle(value)
                input("Press Enter to continue...")
            elif (choice == 6):
                print("Enter Prandtl-Meyer Angle (nu) in degrees: ")
                value = float(input())
                calc.isentropic_PMAngle(value)
                input("Press Enter to continue...")
            elif (choice == 7):
                print("Enter Area Ratio in subsonic flow (A/A*): ")
                value = float(input())
                calc.isentropic_AAstar_subsonic(value)
                input("Press Enter to continue...")
            elif (choice == 8):
                print("Enter Area Ratio in supersonic flow (A/A*): ")
                value = float(input())
                calc.isentropic_AAstar_supersonic(value)
                input("Press Enter to continue...")
            elif (choice == 9):
                break
            elif (choice == 10):
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

    elif (choice == 2):
        while (True):
            print("Which parameter do you want to use as input?")
            print("1. Mach number (M1)")
            print("2. Mach number (M2)")
            print("3. Pressure ratio (P2/P1)")
            print("4. Temperature ratio (T2/T1)")
            print("5. Density ratio (rho2/rho1)")
            print("6. Pressure ratio (P02/P01)")
            print("7. Pressure ratio (P1/P02)")
            print("8. Back to main menu")
            print("9. Exit")
            choice = int(input())
            if (choice == 1):
                print("Enter M1: ")
                value = float(input())
                calc.normalShock_M1(value)
                input("Press Enter to continue...")
            elif (choice == 2):
                print("Enter M2: ")
                value = float(input())
                calc.normalShock_M2(value)
                input("Press Enter to continue...")
            elif (choice == 3):
                print("Enter P2/P1: ")
                value = float(input())
                calc.normalShock_P2P1(value)
                input("Press Enter to continue...")
            elif (choice == 4):
                print("Enter T2/T1: ")
                value = float(input())
                calc.normalShock_T2T1(value)
                input("Press Enter to continue...")
            elif (choice == 5):
                print("Enter rho2/rho1: ")
                value = float(input())
                calc.normalShock_Rho2Rho1(value)
                input("Press Enter to continue...")
            elif (choice == 6):
                print("Enter P02/P01: ")
                value = float(input())
                calc.normalShock_P02P01(value)
                input("Press Enter to continue...")
            elif (choice == 7):
                print("Enter P1/P02: ")
                value = float(input())
                calc.normalShock_P1P02(value)
                input("Press Enter to continue...")
            elif (choice == 8):
                break
            elif (choice == 9):
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

    elif (choice == 3):
        while (True):
            print("Which parameter do you want to use as input?")
            print("1. Mach number (M1) and Wave Angle (B)")
            print("2. Mach number (M1) and normal Mach number (M1n)")
            print("3. Mach number (M1) and Turn Angle (delta) for weak shocks")
            print("4. Mach number (M1) and Turn Angle (delta) for strong shocks")
            print("5. Back to main menu")
            print("6. Exit")
            choice = int(input())
            if (choice == 1):
                M1 = float(input("Enter M1: "))
                value = float(input("Enter Wave Angle (B) in degrees: "))
                calc.obliqueShock_WaveAngle(M1, value)
                input("Press Enter to continue...")
            elif (choice == 2):
                M1 = float(input("Enter M1: "))
                value = float(input("Enter normal Mach number (M1n): "))
                calc.obliqueShock_M1n(M1, value)
                input("Press Enter to continue...")
            elif (choice == 3):
                M1 = float(input("Enter M1: "))
                value = float(input("Enter Turn Angle (delta) in degrees: "))
                calc.obliqueShock_TurnAngle_weak(M1, value)
                input("Press Enter to continue...")
            elif (choice == 4):
                M1 = float(input("Enter M1: "))
                value = float(input("Enter Turn Angle (delta) in degrees: "))
                calc.obliqueShock_TurnAngle_strong(M1, value)
                input("Press Enter to continue...")
            elif (choice == 5):
                break
            elif (choice == 6):
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

    elif (choice == 4):
        while (True):
            print ("Which property do you want to change?")
            print("1. Ratio of specific heats (gamma) [Current value: {}]".format(calc.gamma))
            print("2. Gas constant (R) [Current value: {} J/(Kg*K)]".format(calc.R))
            print("3. Back to main menu")
            print("4. Exit")
            print("Choose an option: ")
            choice = int(input())
            if (choice == 1):
                print("Enter new gamma: ")
                value = float(input())
                if (value <= 1.0):
                    print("Invalid value. Please enter a value greater than 1.0.")
                    continue
                calc.gamma = value
                print("Gamma updated to: {}".format(calc.gamma))
                input("Press Enter to continue...")
            elif (choice == 2):
                print("Enter new gas constant (R) in J/(Kg*K): ")
                value = float(input())
                if (value <= 0.0):
                    print("Are you illiterate?")
                    continue
                calc.R = value
                print("Gas constant updated to: {} J/(Kg*K)".format(calc.R))
                input("Press Enter to continue...")
            elif (choice == 3):
                break
            elif (choice == 4):
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

    elif (choice == 5):
        sys.exit()

    else:
        print("Invalid choice. Please try again.")