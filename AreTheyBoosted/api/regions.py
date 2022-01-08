def region_converter(region):
    match region:
        case "OCE":
            return "OC1"
        case "NA":
            return "NA1"
        case "BR":
            return "BR1"
        case "EUNE":
            return "EUN1"
        case "EUW":
            return "EUW1"
        case "JP":
            return "JP1"
        case "RU":
            return "RU"
        case "TR":
            return "TR1"
        case "LAN":
            return "LA1"
        case "LAS":
            return "LA2"

def region_converter_fullname(region):
    match region:
        case "Oceania":
            return "OC1"
        case "North America":
            return "NA1"
        case "Brazil":
            return "BR1"
        case "Europe Nordic and East":
            return "EUN1"
        case "Europe West":
            return "EUW1"
        case "Japan":
            return "JP1"
        case "Russia":
            return "RU"
        case "Turkey":
            return "TR1"
        case "Latin America North":
            return "LA1"
        case "Latin America South":
            return "LA2"