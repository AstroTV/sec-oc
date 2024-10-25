import ecu
import secoc

def create_ecu(name:str) -> ecu.ECU:
    print(f"Creating {name} ECU")
    created_ecu = ecu.ECU(name)
    return created_ecu

def main():
    # Create 3 ECUs
    ecus = []
    ecus.append(create_ecu("Powertrain"))
    ecus.append(create_ecu("Body"))
    ecus.append(create_ecu("Chassis"))


if __name__ == "__main__":
    main()