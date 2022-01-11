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

def region_converter_web(region):
    match region:
        case "Oceania":
            return "oce"
        case "North America":
            return "na"
        case "Brazil":
            return "br"
        case "Europe Nordic and East":
            return "eun"
        case "Europe West":
            return "euw"
        case "Japan":
            return "jp"
        case "Russia":
            return "ru"
        case "Turkey":
            return "tr"
        case "Latin America North":
            return "la"
        case "Latin America South":
            return "la"