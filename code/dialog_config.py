# Slot names ################################
INFORMATION_SLOTS = ["name", "venue_name", "region", "event_host", "date_start", "time", "price",
                     "is_weekend", "part_of_day", "event"]
REQUEST_SLOTS = ["name", "venue_name", "address", "event_host", "date_start", "time", "price",
                 "is_weekend", "part_of_day", "event_url", "duration", "event"] #request "event" at first round

# Dialog status ################################
DIALOG_STATUS = {
"FAILED_DIALOG" : -50,
"SUCCESS_DIALOG" : 100,
"SUCCESS_TEMP" : 50,
"FAILED_TEMP" : -10,
"PROVIDE_INFO" : 10,
"NO_OUTCOME_YET" : 0}

# Dialog act
DIALOG_ACT = {"REQUEST": 0, "INFORM": 1, "CONFIRM_ANSWER":2, "GREETING":3, "CLOSING": 4, "DENY":5, "THANK":6}

# Special Slot Values
SPECIAL_SLOT_VALUES = {
"I_DO_NOT_CARE" : "I do not care",
"I_DO_NOT_KNOW" : "I also don't know",
"NO_VALUE_MATCH" : "Sorry, no value matches",
"EVENT_AVAILABLE" : "I'm able to find the event."}

# Regions in Singapore
CENTRAL = ["Alexandra", "Aljunied", "Geylang" ,"Ayer Rajah", "Balestier", 
           "Bartley", "Bishan", "Marymount", "Sin Ming", "Bukit Timah", 
           "Buona Vista", "Holland Village", "one-north", "Ghim Moh", "Chinatown",
           "Clarke Quay", "Kreta Ayer", "Telok Ayer", "Kallang", "Bendemeer", 
           "Geylang Bahru", "Kallang Bahru", "Kallang Basin", "Kolam Ayer",
           "Tanjong Rhu", "Mountbatten", "Old Airport", "Lavender", "Boon Keng",
           "Katong", "Kent Ridge", "Kim Seng", "Little India", "Farrer Park",
           "Jalan Besar", "MacPherson", "Marina Bay", "Esplanade", "Marina Bay Sands",
           "Marina Centre", "Marina East", "Marina South", "Marine Parade", "Mount Faber",
           "Mount Vernon", "Museum", "Newton", "Novena", "Orchard Road", "Dhoby Ghaut",
           "Emerald Hill", "Peranakan Place", "Tanglin", "Outram", "Pasir Panjang",
           "Paya Lebar", "Eunos", "Geylang East", "Rochor-Kampong Glam", "Bencoolen",
           "Bras Basah", "Bugis", "Queenstown", "Dover", "Commonwealth", "Raffles Place",
           "River Valley", "Singapore River", "Southern Islands", "Tanjong Pagar",
           "Shenton Way", "Telok Blangah", "Bukit Chandu", "Bukit Purmei", "HarbourFront",
           "Keppel", "Radin Mas", "Mount Faber", "Tiong Bahru", "Bukit Ho Swee",
           "Bukit Merah", "Toa Payoh", "Bidadari", "Bukit Brown", "Caldecott Hill",
           "Potong Pasir", "Thomson", "Whampoa St. Michael's"]
EAST = ["Bedok", "Bedok Reservoir", "Chai Chee", "Kaki Bukit", "Tanah Merah",
        "Changi", "Changi Bay", "Changi East", "Changi Village", "East Coast",
        "Joo Chiat", "Kembangan", "Pasir Ris", "Elias", "Lorong Halus",
        "Loyang", "Siglap", "Tampines", "Simei", "Ubi"]
NORTH = ["Central Catchment Nature Reserve", "Kranji", "Lentor", "Lim Chu Kang",
         "Mandai", "Sembawang", "Senoko", "Simpang", "Sungei Kadut", "Woodlands",
         "Admiralty", "Innova", "Marsiling", "Woodgrove", "Yishun", "Chong Pang"]
NORTH_EAST = ["Ang Mo Kio", "Cheng San", "Chong Boon", "Kebun Baru", "Teck Ghee",
              "Yio Chu Kang", "Hougang", "Defu", "Kovan", "Lorong Chuan",
              "North-Eastern Islands", "Punggol", "Punggol Point", "Punggol New Town",
              "Seletar", "Sengkang", "Serangoon", "Serangoon Gardens", "Serangoon North"]
WEST = ["Boon Lay", "Bukit Batok", "Bukit Gombak", "Hillview Guilin", "Bukit Panjang",
        "Choa Chu Kang", "Yew Tee", "Clementi", "Toh Tuck", "West Coast",
        "Jurong East", "Toh Guan International Business Park", "Teban Gardens",
        "Pandan Gardens", "Penjuru", "Yuhua", "Jurong Regional Centre",
        "Jurong West", "Hong Kah", "Taman Jurong", "Boon Lay Place", "Chin Bee",
        "Yunnan", "Kian Teck", "Safti", "Wenya", "Lim Chu Kang", "Pioneer",
        "Joo Koon", "Gul Circle", "Pioneer Sector", "Tengah", "Tuas", "Pioneer",
        "Soon Lee", "Tuas South", "Western Islands Planning Area", "Western Water Catchment"]
