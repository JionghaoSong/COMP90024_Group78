import json

# Melbourne related keywords
melbourne_keywords = {
    "Melbourne", "Victoria", "Melbourne", "Melbourne Victoria", "Melbourne", "#Melbourne", "Melb", "#Melb",
    "Melbourne CBD", "Melbourne city", "Melbourne Australia", "#MelbourneAustralia", "Melbourne VIC",
    "Melbourne Victoria", "Melbournian", "Melbourne life", "Melbourne events", "Melbourne news",
    "Melbourne weather", "Melbourne traffic", "Yarra River", "Melbourne park", "Melbourne sport",
    "Melbourne culture", "Melbourne food", "Melbourne nightlife", "Melbourne suburbs", "#VisitMelbourne",
    "#DiscoverMelbourne", "#MelbourneLife", "#MelbourneEvents", "Carlton", "Docklands", "Southbank",
    "Fitzroy", "St Kilda", "Richmond", "South Yarra", "Brunswick", "Collingwood", "Hawthorn", "Prahran",
    "Toorak", "Footscray", "North Melbourne", "East Melbourne", "West Melbourne", "Port Melbourne",
    "Albert Park", "Williamstown", "Essendon", "Brighton", "Malvern", "Kew", "Glen Waverley", "Caulfield",
    "Coburg", "Preston", "Reservoir", "Mordialloc", "Elwood",
    "Federation Square", "Flinders Street", "Melbourne Cricket Ground", "MCG", "Royal Botanic Gardens",
    "Queen Victoria Market", "QV Market", "Eureka Tower", "St Kilda Beach", "Lygon Street", "Chapel Street",
    "Bourke Street Mall", "South Melbourne Market", "Docklands Stadium", "Marvel Stadium", "State Library of Victoria",
    "Melbourne Museum", "NGV", "National Gallery of Victoria", "Crown Casino", "Crown Melbourne", "Luna Park",
    "Melbourne Zoo", "Melbourne Aquarium", "SEA LIFE Melbourne", "Royal Exhibition Building", "Parliament House",
    "Flemington Racecourse", "Melbourne Cup", "Australian Open", "Grand Prix",
    "Melbourne International Comedy Festival",
    "Midsumma Festival", "Melbourne Fringe", "Melbourne International Film Festival", "White Night Melbourne",
    "Moomba Festival", "Melbourne Spring Fashion Week", "RMIT", "University of Melbourne", "Monash University",
    "La Trobe University", "Swinburne University", "Melbourne Polytechnic", "Deakin University",
    "Public Transport Victoria", "Myki", "Melbourne Tram", "Melbourne Train", "Melbourne Bus",
    "CityLink", "Tullamarine Freeway", "West Gate Bridge", "Bolte Bridge", "EastLink", "Monash Freeway",
    "Eastern Freeway", "South Eastern Suburbs", "Northern Suburbs", "Western Suburbs", "Eastern Suburbs",
    "Inner city Melbourne", "Outer Melbourne", "Greater Melbourne", "Melbourne Bay", "Port Phillip Bay",
    "Mornington Peninsula", "Yarra Valley", "Dandenong Ranges", "Phillip Island", "Great Ocean Road",
    "Healesville Sanctuary", "Puffing Billy", "Sovereign Hill", "Werribee Open Range Zoo", "Scienceworks",
    "Melbourne Star", "Harbour Town", "Birrarung Marr", "Melbourne Laneways", "Hosier Lane", "ACMI",
    "Arts Centre Melbourne", "Melbourne Recital Centre", "Hamer Hall", "Princess Theatre", "Regent Theatre",
    "Comedy Theatre", "Her Majesty's Theatre", "Athenaeum Theatre", "Chinatown Melbourne", "Little Bourke Street",
    "Italian Precinct", "Greek Precinct", "Melbourne Airport", "Tullamarine Airport", "Avalon Airport",
    "Southern Cross Station", "Flinders Street Station", "Melbourne Central", "Parliament Station",
    "Flagstaff Station", "Melbourne Bike Share", "Bundoora", "Parkville", "Clayton", "Dandenong",
    "Frankston", "Moonee Ponds", "Sunshine", "Altona", "Point Cook", "Werribee", "Bayside Melbourne",
    "Hampton", "Sandringham", "Beaumaris", "Black Rock", "Mentone", "Cheltenham", "Bentleigh", "Moorabbin",
    "Highett", "Ormond", "McKinnon", "Carnegie", "Glen Huntly", "Murrumbeena", "Oakleigh", "Huntingdale",
    "Chadstone", "Ashwood", "Mount Waverley", "Burwood", "Camberwell", "Surrey Hills", "Box Hill",
    "Doncaster", "Templestowe", "Balwyn", "Balwyn North", "Mont Albert", "Glen Iris", "Armadale", "Kooyong",
    "Glenferrie", "Deepdene", "Ashburton", "Wheelers Hill", "Rowville", "Mulgrave", "Noble Park",
    "Springvale", "Keysborough", "Dandenong North", "Endeavour Hills", "Hallam", "Berwick", "Narre Warren",
    "Cranbourne", "Lynbrook", "Langwarrin", "Skye", "Seaford", "Carrum Downs", "Patterson Lakes",
    "Bonbeach", "Chelsea", "Edithvale", "Aspendale", "Parkdale", "Heatherton", "Heathmont", "Vermont",
    "Vermont South", "Wantirna", "Wantirna South", "Boronia", "Bayswater", "Knoxfield", "Ferntree Gully",
    "Scoresby", "Lysterfield", "Narre Warren North", "Narre Warren South", "Endeavour Hills", "Eumemmerring",
    "Doveton", "Hampton Park", "Lynbrook", "Dingley Village", "Carrum", "Bangholme", "Bonbeach", "Chelsea Heights",
    "Edithvale", "Heatherton", "Heidelberg", "Rosanna", "Viewbank", "Macleod", "Watsonia", "Yallambie",
    "Bundoora", "Greensborough", "St Helena", "Montmorency", "Eltham", "Research", "Lower Plenty",
    "Templestowe Lower", "Donvale", "Warrandyte", "Warrandyte South", "Park Orchards", "Ringwood", "Ringwood East",
    "Ringwood North", "Croydon", "Croydon Hills", "Croydon North", "Croydon South", "Mooroolbark", "Kilsyth",
    "Bayswater North", "Heathmont", "Vermont", "Mitcham", "Nunawading", "Forest Hill", "Blackburn",
    "Blackburn North", "Blackburn South", "Box Hill South", "Box Hill North", "Surrey Hills", "Mont Albert",
    "Doncaster East", "Templestowe", "Templestowe Lower", "Bulleen", "Balwyn North", "Balwyn", "Deepdene",
    "Canterbury", "Camberwell", "Hawthorn East", "Kew East", "Kew", "Ivanhoe", "Eaglemont", "Ivanhoe East",
    "Banyule", "Rosanna", "Viewbank", "Heidelberg West", "Heidelberg Heights", "Bellfield", "Preston",
    "Thornbury", "Northcote", "Fairfield", "Alphington", "Clifton Hill", "Fitzroy North", "Collingwood",
    "Abbotsford", "Richmond", "Burnley", "Cremorne", "South Melbourne", "South Wharf", "Southbank",
    "Docklands", "West Melbourne", "Melbourne CBD", "East Melbourne", "North Melbourne", "Kensington",
    "Flemington", "Ascot Vale", "Moonee Ponds", "Essendon", "Essendon North", "Strathmore", "Strathmore Heights",
    "Pascoe Vale", "Pascoe Vale South", "Coburg North", "Hadfield", "Glenroy", "Oak Park", "Jacana",
    "Broadmeadows", "Dallas", "Coolaroo", "Meadow Heights", "Roxburgh Park", "Somerton", "Westmeadows",
    "Attwood", "Greenvale", "Bulla", "Keilor", "Keilor East", "Niddrie", "Airport West", "Tullamarine",
    "Gladstone Park", "Gowanbrae", "Fawkner", "Campbellfield", "Somerton", "Roxburgh Park", "Craigieburn",
    "Mickleham", "Kalkallo", "Donnybrook", "Beveridge", "Wallan", "Whittlesea", "Mernda", "Doreen", "South Morang",
    "Mill Park", "Epping", "Epping North", "Wollert", "Lalor", "Thomastown", "Bundoora", "Kingsbury",
    "Reservoir", "Preston", "Bellfield", "Ivanhoe", "Eaglemont", "Heidelberg", "Rosanna", "Viewbank",
    "Macleod", "Watsonia", "Bundoora", "Montmorency", "Lower Plenty", "Greensborough", "Yallambie", "Plenty",
    "Doreen", "Diamond Creek", "Hurstbridge", "Wattle Glen", "Smiths Gully", "Panton Hill", "St Andrews",
    "Kinglake", "Kinglake West", "Yarra Glen", "Healesville", "Badger Creek", "Yarra Junction", "Warburton",
    "Millgrove", "Launching Place", "Don Valley", "Hoddles Creek", "Seville", "Seville East", "Wandin North",
    "Wandin East", "Lilydale", "Chirnside Park", "Mooroolbark", "Kilsyth", "Montrose", "Kalorama", "Mount Dandenong",
    "Olinda", "Sassafras", "Kallista", "Sherbrooke", "Tecoma", "Belgrave", "Belgrave Heights", "Belgrave South",
    "Upwey", "Upper Ferntree Gully", "Ferntree Gully", "Lysterfield", "Lysterfield South", "Rowville",
    "Scoresby", "Knoxfield", "Boronia", "The Basin", "Wantirna", "Wantirna South", "Vermont", "Vermont South",
    "Ringwood", "Ringwood East", "Ringwood North", "Croydon", "Croydon Hills", "Croydon North", "Croydon South",
    "Mooroolbark"
}


def contains_melbourne_keywords(tokens, tags):
    """ Check if any token or tag contains Melbourne related keywords """
    for keyword in melbourne_keywords:
        if any(keyword.lower() in token.lower() for token in tokens):
            return True
        if any(keyword.lower() in tag.lower() for tag in tags):
            return True
    return False


def filter_mastodon_social(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            data = json.loads(line)
            tokens = data.get("tokens", [])
            tags = data.get("tags", [])
            if contains_melbourne_keywords(tokens, tags):
                outfile.write(json.dumps(data) + '\n')


if __name__ == "__main__":
    input_file = "filtered_mastodon_social.json"
    output_file = "../elastic/data/filtered_melbourne_mastodon_social.json"
    filter_mastodon_social(input_file, output_file)
