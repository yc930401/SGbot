import dialog_config
import numpy as np

inform_venue_name_template = [
    "Tell me about events near {}.",
    "Are there any events near {}?",
    "Does {} have any events?",
    "What events are at {}?",
    "I would like to find an event near {}.",
    "Are there any events at {}?",
    "Could you please tell me some events at {}?",
    "Any events near {}?",
    "Do you know any events near {}?",
    "Can you recommend some events near {}?"]

inform_venue_name_tag = ["B-venue_name", "I-venue_name"]

sample_venue_name = ["Alexandra", "Aljunied", "Geylang", "Ayer Rajah", "Balestier", "Bartley", "Bishan",
                "Marymount", "Sin Ming", "Bukit Timah", "Sixth Avenue", "Buona Vista", "Holland Village",
                "one-north", "Ghim Moh", "Chinatown", "Clarke Quay", "Kreta Ayer", "Telok Ayer", "Kallang",
                "Bendemeer", "Geylang Bahru", "Kallang Bahru", "Kallang Basin", "Kolam Ayer", "Tanjong Rhu",
                "Mountbatten", "Old Airport", "Lavender", "Boon Keng", "Kent Ridge", "Kim Seng",
                "Little India", "Farrer Park", "Jalan Besar", "MacPherson", "Marina Bay", "Esplanade",
                "Marina Bay Sands", "Marina Centre", "Marina East", "Marina South", "Mount Faber",
                "Mount Vernon", "Museum", "Newton", "Novena", "Orchard Road", "Dhoby Ghaut", "Emerald Hill",
                "Peranakan Place", "Tanglin", "Outram", "Pasir Panjang", "Paya Lebar", "Eunos", "Geylang East",
                "Potong Pasir", "Rochor-Kampong Glam", "Bencoolen", "Bras Basah", "Bugis", "Queenstown",
                "Dover", "Commonwealth", "Raffles Place", "River Valley", "Singapore River",
                "Southern Islands", "Tanjong Pagar", "Shenton Way", "Telok Blangah", "Bukit Chandu",
                "Bukit Purmei", "HarbourFront", "Keppel", "Radin Mas", "Mount Faber", "Tiong Bahru",
                "Bukit Ho Swee", "Bukit Merah", "Toa Payoh", "Bukit Brown", "Caldecott Hill", "Thomson",
                "Whampoa", "St. Michael's", "East", "Bedok", "Bedok Reservoir", "Chai Chee", "Kaki Bukit",
                "Tanah Merah", "Changi", "Changi Bay", "Changi East", "Changi Village", "East Coast",
                "Joo Chiat", "Katong", "Kembangan", "Pasir Ris", "Elias", "Lorong Halus", "Loyang",
                "Marine Parade", "Siglap", "Tampines", "Simei", "Ubi", "North", "Central Catchment Nature Reserve",
                "Kranji", "Lentor", "Lim Chu Kang", "Neo Tiew", "Sungei Gedong", "Mandai", "Sembawang",
                "Canberra", "Senoko", "Simpang", "Sungei Kadut", "Woodlands", "Admiralty", "Innova",
                "Marsiling", "Woodgrove", "Yishun", "Chong Pang", "North-East", "Ang Mo Kio", "Cheng San",
                "Chong Boon", "Kebun Baru", "Teck Ghee", "Yio Chu Kang", "Bidadari", "Hougang", "Defu",
                "Kovan", "Lorong Chuan", "North-Eastern Islands", "Punggol", "Punggol Point",
                "Punggol New Town", "Seletar", "Sengkang", "Serangoon", "Serangoon Gardens", "Serangoon North",
                "Boon Lay", "Tukang", "Liu Fang", "Samulun", "Shipyard", "Bukit Batok", "Bukit Gombak",
                "Hillview", "Guilin", "Bukit Panjang", "Choa Chu Kang", "Yew Tee",
                "Clementi", "Toh Tuck", "West Coast", "Jurong East", "Toh Guan", "International Business Park",
                "Teban Gardens", "Pandan Gardens", "Penjuru", "Yuhua", "Jurong Regional Centre", 
                "Jurong West", "Hong Kah", "Taman Jurong", "Boon Lay Place", "Chin Bee",
                "Yunnan", "Central", "Kian Teck", "Safti", "Wenya", "Lim Chu Kang", "Pioneer", "Joo Koon",
                "Gul Circle", "Pioneer Sector", "Tengah", "Tuas", "Wrexham", "Promenade", "Pioneer",
                "Soon Lee", "Tuas South", "Western Islands Planning Area", "Western Water Catchment",
                "Murai", "Sarimbun"]



inform_region_template = [
    "Tell me about events in the {}.",
    "Tell me about events in the {} area.",
    "Tell me about events in the {} region.",
    "Are there any events in the {} area?",
    "Are there any events in the {} region?",
    "What events are in the {}?",
    "What events are in the {} region?",
    "What events are in the {} area?",
    "I would like to find an event in the {}.",
    "I would like to find an event in the {} region.",
    "I would like to find an event in the {} area.",
    "Are there any events in the {}?",
    "Are there any events in the {} region?",
    "Are there any events in the {} area?",
    "Could you please tell me some events in the {}?",
    "Could you please tell me some events in the {} area?",
    "Could you please tell me some events in the {} region?",
    "Any events in the {}?",
    "Any events in the {} area?",
    "Any events in the {} region?",
    "Do you know any events in the {}?",
    "Do you know any events in the {} region?",
    "Can you recommend some events in the {}?",
    "Can you recommend some events in the {} area?",
    "Tell me about events in the {} area of Singapore.",
    "Are there any events in the {} region of Singapore?",
    "What events are in the {} area of Singapore?",
    "I would like to find an event in the {} region of Singapore.",
    "Are there any events in the {} region of Singapore?",
    "Could you please tell me some events in the {} area of Singapore?",
    "Any events in the {} region of Singapore?",
    "Do you know any events in the {} region of Singapore?",
    "Can you recommend some events in the {} area of Singapore?"]


inform_region_tag = ["B-region"]

sample_region = ["City", "South", "West", "Central", "East", "North"]



inform_event_host_template = [
    "Are there events by {}?",
    "What events would be organised by {}?",
    "Is {} organising any events?",
    "What events are {} organising?",
    "Which event is {} an organiser of?",
    "Are there any events by the group {}?",
    "Is the group {} organising any events?",
    "Any events with {}?",
    "Could you please recommend me some events organising by {}?",
    "Can you tell me events by {}?"
]

inform_event_host_tag = ["B-event_host", "I-event_host"]


sample_event_host = [
    "Sg Intl Investors & Social Networking Club. 3,000+ Members", "Badminton Fanatics",
    "Singapore Beauty Workshop by Jo Makeup", "Sg International  Globetrotters Club- SIGC  8,000+ Members",
    "Speed & Blind Dating Club", "Expats Social  Networking Club- ESNC", "Expats Social  Networking Club",
    "Meetup Newbies Gathering & Mingling Club", "SINGAPORE SINGLES & DATING CLUB",
    "I'M SINGLE, YOU'RE SINGLE. LET'S MINGLE & LATER SNUGGLE", "Afterwork Drinks For Friendship & Social Networking Club",
    "Expats & Social Nomads", "Social Networking & Hanging Out With New Friends Club", "Freelancers Singapore Meetup",
    "Singapore Fun Events (SFE)", "Zumba! Singapore (1Fiesta)", "E-Commerce as Easy as 123", "Art Of Movement Meetup",
    "Singapore Fun Events (SFE)", "StrangerSoccer - Daily soccer games for you all over Spore!", "Jo Makeup",
    "EXPAT FRIENDS SINGAPORE", "All My Friends Are in Couples & I'm Single", "Singapore Women's Empowerment",
    "The Golden Space", "LiveLife with Fun Events & Activities", "Badminton Workout",
    "Dance Haven Bellydance & Bellydance Fitness", "Singapore Oyster Crawl",
    "Singapore International Opportunities Networking (SION)", "SBN: Business Networking over Quality Tea (BNQT)",
    "StrangerSoccer", "SBN: B2B2C Global Luncheon Networking", "Singapore International Opportunities Networking (SION)",
    "Innovation Marketing & Sales Group", "Comedy Hub Singapore", "Singapore Squash Players", "Wind Slicer Badminton",
    "JOYCORONA", "Singapore Trekking Group (SgTrek)", "Starz PB", "Culinary Underground Singapore", "Cooking In Singapore",
    "Jiggle Wigs Music", "Isha Kriya", "Lula", "Charissa", "Dwight", "Christoper", "Juana", "Gennie", "Eustolia", "Kip",
    "Diana", "Ophelia", "Hipolito", "Javier", "Angle", "Hui", "Josefine", "Oliva", "Alex", "Reagan", "Mitsue", "Kyoko",
    "Carlton", "Felipa", "Jazmin", "Gilma", "Minnie", "Duncan", "Shaun", "Margurite", "Necole", "Dewayne", "Charlotte",
    "Adrien", "Carissa", "Waldo", "Jillian", "Clemente", "Walker", "Broderick", "Sabrina", "Novella", "Mckenzie",
    "Etsuko", "Jadwiga", "Jerold", "Estelle", "Jetta", "Sierra", "Jacquelyn", "Edgar", "See", "OCBC Bank", "DBS Group",
    "Singtel", "UOB", "Wilmar International", "Trafigura Group", "Flextronics", "2C2P", "Aetos Security Management",
    "AIBI International", "Antlabs", "Aspial Corporation", "Ayam Brand", "Bee Cheng Hiang", "Boustead Singapore",
    "BreadTalk", "Broadcom Limited", "CapitaLand", "Carousell", "Certis CISCO", "Charles & Keith", "China Aviation Oil",
    "ComfortDelGro", "Creative Technology", "DBS Bank", "dnata Singapore", "Far East Orchard", "Far East Organization",
    "FilmTack", "Flextronics", "Fraser and Neave", "Garena", "Genting Singapore", "Golden Agri-Resources", "Grab",
    "Great Eastern Life", "Hyflux", "Jetstar Asia Airways", "Jurong Port", "JTC Corporation", "Keppel Corporation",
    "M1 Limited", "Mediacorp", "MyRepublic", "Near", "Neptune Orient Lines", "NTUC FairPrice", "OCBC Bank",
    "Osim International", "PSA International", "Pacific Century Regional Developments Limited", "Popular Holdings",
    "POSB Bank", "Quest Global", "Renewable Energy Corporation", "SATS Ltd", "SBS Transit", "Scoot", "SearchTrade",
    "SembCorp Marine", "SIA Engineering Company", "Singapore Press Holdings", "SMRT Corporation", "SGAG", "Sheng Siong",
    "SilkAir", "Singapore Airlines", "Singapore Airlines Cargo", "Singapore Exchange", "Singapore Petroleum Company Limited",
    "Singapore Power", "Singapore Post", "Singtel", "ST Engineering", "StarHub", "Systems on Silicon Manufacturing",
    "Tangs", "Tee Yih Jia", "Temasek Holdings", "Thakral Corporation", "Tiger Airways Holdings", "Transocean Singapore",
    "Twelve Cupcakes", "Venture Corporation", "Vertex Venture Holdings", "Ya Kun Kaya Toast", "Yeo Hiap Seng", "Wilmar"]


inform_date_start_template = [
    "I want to know what events are occurring on {}.",
    "Are there any events on {}?",
    "What events are on {}?",
    "Does {} have events I can attend?",
    "Will there be any events on {}?",
    "Can you recommend me some events on {}?",
    "Do you kow any events holding on {}?",
    "Do you have any suggestions on events on {}?"
]

inform_date_start_tag = ["B-date_start", "I-date_start"]


sample_date_start_weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                     "Sun", "Mon", "Tue", "Tues", "Wed", "Weds", "Thu", "Thurs", "Fri", "Sat"]
sample_date_start_month =[ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                     "November", "December", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Sept", "Oct", "Nov", "Dec"]
np.random.shuffle(sample_date_start_month)
np.random.shuffle(sample_date_start_weekday)
sample_date_start = sample_date_start_weekday + ['next ' + date for date in sample_date_start_weekday[:5]]
sample_date_start += sample_date_start_month + ['next ' + date for date in sample_date_start_month[:5]]
for i in range(2015, 2020):
    np.random.shuffle(sample_date_start_month)
    sample_date_start += [date + ' ' + str(i) for date in sample_date_start_month[:5]]
for i in range(1, 32):
    np.random.shuffle(sample_date_start_month)
    sample_date_start += [date + ' ' + str(i) for date in sample_date_start_month[:5]]
    sample_date_start += [str(i) + ' ' + date for date in sample_date_start_month[:5]]


inform_time_template = [
    "I would like to know about events that are around {}.",
    "Are there any events that start at {}?",
    "Tell me about events around {}.",
    "Will there be any events around {}?",
    "I want to know if there are events at {}?",
    "Do you know any events start at {}?",
    "Can you recommend any event begins around {}?",
    "Can I know some events at around {}?",
    "I would like to know about events holding around {}.",
    "I would like to know about events occurring around {}.",
    "Tell me about events holding around {}.",
    "Tell me about events occurring around {}.",
    "Will there be any events holding around {}?",
    "Will there be any events occurring around {}?",
    "I want to know if there are events holding at {}?",
    "I want to know if there are events occurring at {}?",
    "Can you recommend any event begins around {}?",
    "Can I know some events that begin at around {}?",
    "Can I know some events beginning at around {}?"
]

inform_time_tag = ["B-time", "I-time"]

sample_time = [str(time) for time in range(15,18)]
sample_time = [str(time) + " a.m." for time in range(3,6)]
sample_time = [str(time) + " p.m." for time in range(9,12)]
sample_time = [str(time) + " o'clock" for time in range(12,15)]
sample_time += [str(time) + ':00' for time in range(0,3)]
sample_time += [str(time) + ':00' + " am" for time in range(3, 6)]
sample_time += [str(time) + ':00' + " pm" for time in range(9, 13)]
sample_time += [str(time) + ':15' for time in range(3,6)]
sample_time += [str(time) + ':15' + " pm" for time in range(0, 3)]
sample_time += [str(time) + ':15' + " p.m." for time in range(3, 6)]
sample_time += [str(time) + ':15' + " o'clock" for time in range(18,21)]
sample_time += [str(time) + ':30' for time in range(6,9)]
sample_time += [str(time) + ':30' + " am" for time in range(9, 13)]
sample_time += [str(time) + ':30' + " a.m." for time in range(0,3)]
sample_time += [str(time) + ':30' + " o'clock" for time in range(21,24)]
sample_time += [str(time) + ':45' for time in range(9, 13)]
sample_time += [str(time) + ':45' + " a.m." for time in range(3, 6)]
sample_time += [str(time) + ':45' + " pm" for time in range(6, 9)]



inform_price_template = [
    "Do you know any free events?",
    "Tell me about some free events.",
    "Can you recommend me some free events?",
    "Do you have any suggestions for free events?",
    "Are there any events around {} dollars.",
    "Are there any events around {} SGD.",
    "Are there any events less than {} dollars.",
    "Are there any events less than {} SGD.",
    "Are there any events around ${}.",
    "I would like to find an event that costs {} dollars.",
    "I would like to find an event that costs {} SGD.",
    "I would like to find an event that costs ${}.",
    "Let me know if there are events that are around {} dollars.",
    "Let me know if there are events that are around {} SGD.",
    "Let me know if there are events that are less than {} dollars.",
    "Let me know if there are events that are less than {} SGD.",
    "Let me know if there are events that are around ${}.",
    "Let me know if there are events that are around {} SGD.",
    "Will there be events that cost less than {} dollars?",
    "Will there be events that cost less than {} SGD?",
    "Will there be events that cost around {} dollars?",
    "Will there be events that cost around {} SGD?",
    "Will there be events that cost ${}?",
    "Will there be events that cost {} SGD?"
]

inform_price_tag = ["B-price"]

sample_price = ["1", "2", "3", "4", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "60", "70", "80", "90",
                "100", "150", "200"]




inform_is_weekend_template = [
    "Tell me about events that on {}.",
    "Which events take place on {}.",
    "I would like to find an event that is on {}.",
    "What events are conducted on {}.",
    "Will there be events that take place on {}?",
    "I want to know the events that are available on {}.",
    "Can you recommend some events on {}?",
    "Do you have any suggestions on events on {}?",
    "I want to find some events on {}."
]

inform_is_weekend_tag = ["B-part_of_day", "I-part_of_day"]

sample_is_weekend=["weekend", "weekdays"]



inform_part_of_day_template = [
    "Tell me about events that are in {}.",
    "Which events take place on {}.",
    "I would like to find an event that is in {}.",
    "What events are conducted on {}.",
    "Will there be events that take place in {}?",
    "I want to know the events that are available at {}.",
    "Can you recommend some events start at {}?",
    "Do you know any events begins in {}?",
    "Do you have any suggestions on events in {}?",
    "I want to find some events in {}."
]

inform_part_of_day_tag = ["B-part_of_day", "I-part_of_day"]

sample_part_of_day=["morning", "afternoon", "night", "evening", "noon", "dawn", "dusk", "twilight", "sunrise", "sun rise",
                    "sunset", "sun set", "daybreak", "day break", "night send", "daytime", "nighttime", "daylight",
                    "day light", "mid night", "midnight", "mid day", "midday", "after dark"]



inform_venue_name_and_region_template = [
    "Tell me about events near {venue_name} in the {region}.",
    "Tell me about events near {venue_name} in the {region} area.",
    "Tell me about events near {venue_name} in the {region} region.",
    "Tell me about events near {venue_name} in the {region} region of Singapore.",
    "Tell me about events near {venue_name} in the {region} area of Singapore.",
    "Are there any events near {venue_name} in the {region}?",
    "Are there any events near {venue_name} in the {region} area?",
    "Are there any events near {venue_name} in the {region} region?",
    "Are there any events near {venue_name} in the {region} region of Singapore?",
    "Are there any events near {venue_name} in the {region} area of Singapore?",
    "Does {venue_name} in the {region} have any events?",
    "Does {venue_name} in the {region} area have any events?",
    "Does {venue_name} in the {region} region have any events?",
    "Does {venue_name} in the {region} area of Singapore have any events?",
    "Does {venue_name} in the {region} region of Singapore have any events?",
    "What events are at {venue_name} in the {region}?",
    "What events are at {venue_name} in the {region} area?",
    "What events are at {venue_name} in the {region} region?",
    "What events are at {venue_name} in the {region} area of Singapore?",
    "What events are at {venue_name} in the {region} region of Singapore?",
    "I would like to find an event near {venue_name} in the {region}.",
    "I would like to find an event near {venue_name} in the {region} area.",
    "I would like to find an event near {venue_name} in the {region} region.",
    "I would like to find an event near {venue_name} in the {region} of Singapore.",
    "I would like to find an event near {venue_name} in the {region} region of Singapore.",
    "I would like to find an event near {venue_name} in the {region} area of Singapore.",
    "Are there any events at {venue_name} in the {region}?",
    "Are there any events at {venue_name} in the {region} area?",
    "Are there any events at {venue_name} in the {region} region?",
    "Are there any events at {venue_name} in the {region} of Singapore?",
    "Are there any events at {venue_name} in the {region} area of Singapore?",
    "Are there any events at {venue_name} in the {region} region of Singapore?",
    "Could you please tell me some events at {venue_name} in the {region}?",
    "Could you please tell me some events at {venue_name} in the {region} area?",
    "Could you please tell me some events at {venue_name} in the {region} region?",
    "Could you please tell me some events at {venue_name} in the {region}?",
    "Could you please tell me some events at {venue_name} in the {region} area of Singapore?",
    "Could you please tell me some events at {venue_name} in the {region} region of Singapore?",
    "Any events near {venue_name} in the {region}?",
    "Any events near {venue_name} in the {region} region?",
    "Any events near {venue_name} in the {region} area?",
    "Any events near {venue_name} in the {region} of Singapore?",
    "Any events near {venue_name} in the {region} region of Singapore?",
    "Any events near {venue_name} in the {region} area of Singapore?",
    "Do you know any events near {venue_name} in the {region}?",
    "Do you know any events near {venue_name} in the {region} region?",
    "Do you know any events near {venue_name} in the {region} area?",
    "Do you know any events near {venue_name} in the {region}?",
    "Do you know any events near {venue_name} in the {region} region of Singapore?",
    "Do you know any events near {venue_name} in the {region} area of Singapore?",
    "Can you recommend some events near {venue_name} in the {region}?",
    "Can you recommend some events near {venue_name} in the {region} area?",
    "Can you recommend some events near {venue_name} in the {region} region?",
    "Can you recommend some events near {venue_name} in the {region} of Singaproe?",
    "Can you recommend some events near {venue_name} in the {region} region of Singapore?",
    "Can you recommend some events near {venue_name} in the {region} area of Singapore?"
]


inform_venue_name_and_event_host_template = [
    "Are there events by {event_host} near {venue_name}?",
    "Are there events by {event_host} at {venue_name}?",
    "Are there events near {venue_name} by {event_host} ?",
    "Are there events at {venue_name} by {event_host} ?",
    "What events would be organised by {event_host} near {venue_name}?",
    "What events would be organised by {event_host} at {venue_name}?",
    "What events near {venue_name} would be organised by {event_host}?",
    "What events at {venue_name} would be organised by {event_host}?",
    "Is {event_host} organising any events near {venue_name}?",
    "Is {event_host} organising any events at {venue_name}?",    
    "What events are {event_host} organising near {venue_name}?",
    "What events are {event_host} organising at {venue_name}?",
    "What events near {venue_name} are {event_host} organising?",
    "What events at {venue_name} are {event_host} organising?",
    "Which event near {venue_name} is {event_host} an organiser of?",
    "Which event at {venue_name} is {event_host} an organiser of?",
    "Are there any events by the group {event_host} near {venue_name}?",
    "Are there any events by the group {event_host} at {venue_name}?",
    "Are there any events near {venue_name} by the group {event_host}?", 
    "Are there any events at {venue_name} by the group {event_host}?",
    "Is the group {event_host} organising any events near {venue_name}?",
    "Is the group {event_host} organising any events at {venue_name}?",
    "Any events with {event_host} near {venue_name}?",
    "Any events with {event_host} at {venue_name}?",
    "Could you please recommend me some events organising by {event_host} near {venue_name}?",
    "Could you please recommend me some events organising by {event_host} at {venue_name}?",
    "Could you please recommend me some events near {venue_name} organising by {event_host}?",
    "Could you please recommend me some events at {venue_name} organising by {event_host}?",
    "Can you tell me events by {event_host} near {venue_name}?",
    "Can you tell me events by {event_host} at {venue_name}?",
    "Can you tell me events at {venue_name} by {event_host}?",
    "Can you tell me events near {venue_name} by {event_host}?"
]


inform_venue_name_and_date_start_template = [
    "I want to know what events are occurring on {date_start} at {venue_name}.",
    "I want to know what events are occurring on {date_start} near {venue_name}.",
    "I want to know what events are occurring at {venue_name} on {date_start}.",
    "I want to know what events are occurring near {venue_name} on {date_start}.",
    "Are there any events on {date_start} at {venue_name}?",
    "Are there any events on {date_start} near {venue_name}?",
    "Are there any events at {venue_name} on {date_start}?",
    "Are there any events near {venue_name} on {date_start}?",
    "What events on {date_start} are at {venue_name}?",
    "What events on {date_start} are near {venue_name}?",
    "What events at {venue_name} are on {date_start}?",
    "What events near {venue_name}  are on {date_start}?",
    "Does {date_start} have events I at {venue_name}?",
    "Does {date_start} have events I near {venue_name}?",
    "Will there be any events on {date_start} at {venue_name}?",
    "Will there be any events on {date_start} near {venue_name}?",
    "Will there be any events at {venue_name} on {date_start}?",
    "Will there be any events near {venue_name} on {date_start}?",
    "Can you recommend me some events on {date_start} at {venue_name}?",
    "Can you recommend me some events on {date_start} near {venue_name}?",
    "Can you recommend me some events at {venue_name} on {date_start}?",
    "Can you recommend me some events near {venue_name} on {date_start}?",
    "Do you kow any events holding on {date_start} at {venue_name}?",
    "Do you kow any events holding on {date_start} near {venue_name}?",
    "Do you kow any events holding at {venue_name} on {date_start}?",
    "Do you kow any events holding near {venue_name} on {date_start}?",
    "Do you have any suggestions on events on {date_start} at {venue_name}?",
    "Do you have any suggestions on events on {date_start} near {venue_name}?",
    "Do you have any suggestions on events at {venue_name} on {date_start}?",
    "Do you have any suggestions on events near {venue_name} on {date_start}?"
]


inform_venue_name_and_time_template = [
    "I would like to know about events that are around {time} near {venue_name}.",
    "I would like to know about events that are around {time} at {venue_name}.",
    "I would like to know about events that are near {venue_name} around {time}.",
    "I would like to know about events that are at {venue_name} around {time}.",
    "Are there any events that start at {time} near {venue_name}?",
    "Are there any events near {venue_name} that start at {time}?",
    "Tell me about events around {time} near {venue_name}.",
    "Tell me about events around {time} at {venue_name}.",
    "Tell me about events near {venue_name} around {time}.",
    "Tell me about events at {venue_name} around {time}.",
    "Will there be any events around {time} near {venue_name}?",
    "Will there be any events around {time} at {venue_name}?",
    "Will there be any events near {venue_name} around {time}?",
    "Will there be any events at {venue_name} around {time}?",
    "I want to know if there are events at {time} near {venue_name}?",
    "I want to know if there are events around {time} near {venue_name}?",
    "I want to know if there are events around {time} at {venue_name}?",
    "I want to know if there are events at {venue_name} around {time}?",
    "Do you know any events start at {time} near {venue_name}?",
    "Do you know any events start around {time} near {venue_name}?",
    "Do you know any events start at around {time} near {venue_name}?",
    "Do you know any events at {venue_name} start at around {time}?",
    "Can you recommend any event begins around {time} near {venue_name}?",
    "Can you recommend any event begins around {time} at {venue_name}?",
    "Can you recommend any event begins near {venue_name} around {time}?",
    "Can you recommend any event begins at {venue_name} around {time}?",
    "Can I know some events at around {time} near {venue_name}?",
    "Can I know some events at around {time} at {venue_name}?",
    "Can I know some events near {venue_name} at around {time}?",
    "Can I know some events at {venue_name} around {time}?",
]


inform_venue_name_and_price_template = [
    "Do you know any free events at {venue_name}?",
    "Do you know any free events near {venue_name}?",
    "Tell me about some free events at {venue_name}.",
    "Tell me about some free events near {venue_name}.",
    "Can you recommend me some free events at {venue_name}?",
    "Can you recommend me some free events near {venue_name}?",
    "Do you have any suggestions for free events at {venue_name}?",
    "Do you have any suggestions for free events near {venue_name}?",
    "Are there any events around {price} dollars at {venue_name}.",
    "Are there any events around {price} SGD at {venue_name}.",
    "Are there any events around {price} dollars near {venue_name}.",
    "Are there any events at {venue_name} around {price} dollars.",
    "Are there any events at {venue_name} around {price} SGD.",
    "Are there any events near {venue_name}, around {price} dollars.",
    "Are there any events less than {price} dollars near {venue_name}.",
    "Are there any events less than {price} SGD near {venue_name}.",
    "Are there any events less than {price} dollars at {venue_name}.",
    "Are there any events near {venue_name} less than {price} dollars.",
    "Are there any events at {venue_name} less than {price} dollars.",
    "Are there any events at {venue_name} less than {price} SGD.",
    "Are there any events around ${price} at {venue_name}.",
    "Are there any events around ${price} near {venue_name}.",
    "Are there any events around {price} SGD near {venue_name}.",
    "Are there any events at {venue_name} around ${price}.",
    "Are there any events near {venue_name} around ${price}.",
    "Are there any events near {venue_name} around {price} SGD.",
    "I would like to find an event at {venue_name} that costs {price} dollars.",
    "I would like to find an event near {venue_name} that costs {price} dollars.",
    "I would like to find an event that costs {price} dollars at {venue_name}.",
    "I would like to find an event that costs {price} dollars near {venue_name}.",
    "I would like to find an event that costs {price} SGD near {venue_name}.",
    "I would like to find an event that costs ${price} at {venue_name}.",
    "I would like to find an event that costs ${price} near {venue_name}.",
    "I would like to find an event at {venue_name} that costs ${price}.",
    "Let me know if there are events at {venue_name} that are around {price} dollars.",
    "Let me know if there are events at {venue_name} that are around {price} SGD.",
    "Let me know if there are events near {venue_name} that are around {price} dollars.",
    "Let me know if there are events that are around {price} dollars and are at {venue_name}.",
    "Let me know if there are events that are around {price} dollars and are near {venue_name}.",
    "Let me know if there are events at {venue_name} that are less than {price} dollars.",
    "Let me know if there are events near {venue_name} that are less than {price} dollars.",
    "Let me know if there are events that are less than {price} dollars at {venue_name}.",
    "Let me know if there are events that are less than {price} dollars near {venue_name}.",
    "Let me know if there are events that are around ${price} at {venue_name}.",
    "Let me know if there are events that are around {price} SGD at {venue_name}.",
    "Let me know if there are events that are around ${price} near {venue_name}.",
    "Let me know if there are events that at {venue_name} are around ${price}.",
    "Let me know if there are events that at {venue_name} are around {price} SGD.",
    "Let me know if there are events near {venue_name} that are around ${price}.",
    "Will there be events that cost less than {price} dollars near {venue_name}?",
    "Will there be events that cost less than {price} dollars at {venue_name}?",
    "Will there be events near {venue_name} that cost less than {price} dollars?",
    "Will there be events near {venue_name} that cost less than {price} SGD?",
    "Will there be events at {venue_name} that cost less than {price} dollars?",
    "Will there be events that cost around {price} dollars at {venue_name}?",
    "Will there be events that cost around {price} dollars near {venue_name}?",
    "Will there be events that cost around {price} SGD near {venue_name}?",
    "Will there be events at {venue_name} that cost around {price} dollars?",
    "Will there be events at {venue_name} that cost around {price} SGD?",
    "Will there be events near {venue_name} that cost around {price} dollars?",
    "Will there be events that cost ${price} at {venue_name}?",
    "Will there be events that cost {price} SGD at {venue_name}?",
    "Will there be events that cost ${price} near {venue_name}?",
    "Will there be events at {venue_name} that cost ${price}?",
    "Will there be events near {venue_name} that cost ${price}?",
    "Will there be events near {venue_name} that cost {price} SGD?"
]


inform_venue_name_and_is_weekend_template = [
    "Tell me about events at {venue_name} that are on {is_weekend}.",
    "Tell me about events near {venue_name} that are on {is_weekend}.",
    "Tell me about events that are on {is_weekend} and at {venue_name}.",
    "Tell me about events that are on {is_weekend} and near {venue_name}.",
    "Which events take place on {is_weekend} near {venue_name}.",
    "Which events take place on {is_weekend} at {venue_name}.",
    "Which events at {venue_name} will take place on {is_weekend}.",
    "Which events near {venue_name} will take place on {is_weekend}.",
    "I would like to find an event that is on {is_weekend} at {venue_name}.",
    "I would like to find an event that is on {is_weekend} near {venue_name}.",
    "I would like to find an event at {venue_name} that is on {is_weekend}.",
    "I would like to find an event near {venue_name} that is on {is_weekend}.",
    "What events are conducted on {is_weekend} near {venue_name}.",
    "What events are conducted on {is_weekend} at {venue_name}.",
    "What events near {venue_name} are conducted on {is_weekend}.",
    "What events at {venue_name} are conducted on {is_weekend}.",
    "Will there be events that take place on {is_weekend} near {venue_name}?",
    "Will there be events that take place on {is_weekend} at {venue_name}?",
    "Will there be events near {venue_name} that take place on {is_weekend}?",
    "Will there be events at {venue_name} that take place on {is_weekend}?",
    "I want to know the events near {venue_name} that are available on {is_weekend}.",
    "I want to know the events at {venue_name} that are available on {is_weekend}.",
    "I want to know the events that are available on {is_weekend} and near {venue_name}.",
    "I want to know the events that are available on {is_weekend} and are at {venue_name}.",
    "Can you recommend some events on {is_weekend} near {venue_name}?",
    "Can you recommend some events on {is_weekend} at {venue_name}?",
    "Can you recommend some events near {venue_name} on {is_weekend}?",
    "Can you recommend some events at {venue_name} on {is_weekend}?",
    "Do you have any suggestions on events near {venue_name} on {is_weekend}?",
    "Do you have any suggestions on events at {venue_name} on {is_weekend}?",
    "I want to find some events on {is_weekend} near {venue_name}.",
    "I want to find some events on {is_weekend} at {venue_name}.",
    "I want to find some events near {venue_name} on {is_weekend}.",
    "I want to find some events at {venue_name} on {is_weekend}."
]


inform_venue_name_and_part_of_day_template = [
    "Tell me about events near {venue_name} that are in {part_of_day}.",
    "Tell me about events at {venue_name} that are in {part_of_day}.",
    "Tell me about events that are in {part_of_day} near {venue_name}.",
    "Tell me about events that are in {part_of_day} at {venue_name}.",
    "Which events take place on {part_of_day} at {venue_name}.",
    "Which events take place on {part_of_day} near {venue_name}.",
    "Which events take place at {venue_name} on {part_of_day}.",
    "Which events take place near {venue_name} on {part_of_day}.",
    "Which events at {venue_name} take place on {part_of_day}.",
    "Which events near {venue_name} take place on {part_of_day}.",
    "I would like to find an event that is in {part_of_day} near {venue_name}.",
    "I would like to find an event that is in {part_of_day} at {venue_name}.",
    "I would like to find an event near {venue_name} that is in {part_of_day}.",
    "I would like to find an event at {venue_name} that is in {part_of_day}.",
    "What events are conducted on {part_of_day} near {venue_name}.",
    "What events are conducted on {part_of_day} at {venue_name}.",
    "What events near {venue_name} are conducted on {part_of_day}.",
    "What events at {venue_name} are conducted on {part_of_day}.",
    "Will there be events that take place in {part_of_day} near {venue_name}?",
    "Will there be events that take place in {part_of_day} at {venue_name}?",
    "Will there be events near {venue_name} that take place in {part_of_day}?",
    "Will there be events at {venue_name} that take place in {part_of_day}?",
    "I want to know the events near {venue_name} that are available in {part_of_day}.",
    "I want to know the events at {venue_name} that are available in {part_of_day}.",
    "I want to know the events that are available in {part_of_day} near {venue_name}.",
    "I want to know the events that are available in {part_of_day} at {venue_name}.",
    "Can you recommend some events start at {part_of_day} near {venue_name}?",
    "Can you recommend some events start at {part_of_day} at {venue_name}?",
    "Can you recommend some events near {venue_name} start at {part_of_day}?",
    "Can you recommend some events at {venue_name} start at {part_of_day}?",
    "Do you know any events begins in {part_of_day} near {venue_name}?",
    "Do you know any events begins in {part_of_day} at {venue_name}?",
    "Do you know any events near {venue_name} begins in {part_of_day}?",
    "Do you know any events at {venue_name} begins in {part_of_day}?",
    "Do you have any suggestions on events in {part_of_day} near {venue_name}?",
    "Do you have any suggestions on events in {part_of_day} at {venue_name}?",
    "Do you have any suggestions on events near {venue_name} in {part_of_day}?",
    "Do you have any suggestions on events at {venue_name} in {part_of_day}?",
    "I want to find some events in {part_of_day} near {venue_name}.",
    "I want to find some events in {part_of_day} at {venue_name}.",
    "I want to find some events near {venue_name} in {part_of_day}.",
    "I want to find some events at {venue_name} in {part_of_day}."
]


inform_region_and_event_host_template = [
    "Are there events by {event_host} in the {region} region?",
    "Are there events by {event_host} in the {region} area?",
    "Are there events by {event_host} in the {region} region of Singapore?",
    "Are there events by {event_host} in the {region}?",
    "Are there events in the {region} region by {event_host}?",
    "Are there events in the {region} area by {event_host}?",
    "Are there events in the {region} region of Singapore by {event_host}?",
    "Are there events in the {region} by {event_host}?",
    "What events would be organised by {event_host} in the {region}?",
    "What events would be organised by {event_host} in the {region} region?",
    "What events would be organised by {event_host} in the {region} area?",
    "What events would be organised by {event_host} in the {region} of Singapore?",
    "What events in the {region} would be organised by {event_host}?",
    "What events in the {region} region would be organised by {event_host}?",
    "What events in the {region} area would be organised by {event_host}?",
    "What events in the {region} of Singapore would be organised by {event_host}?",
    "Is {event_host} organising any events in the {region}?",
    "Is {event_host} organising any events in the {region} region?",
    "Is {event_host} organising any events in the {region} area?",
    "Is {event_host} organising any events in the {region} of Singapore?",
    "Is {event_host} organising any events in the {region} area of Singapore?",
    "What events are {event_host} organising in the {region}?",
    "What events are {event_host} organising in the {region} area?",
    "What events are {event_host} organising in the {region} region?",
    "What events are {event_host} organising in the {region} region of Singapore?",
    "What events in the {region} are {event_host} organising?",
    "What events in the {region} area are {event_host} organising?",
    "What events in the {region} region are {event_host} organising?",
    "What events in the {region} region of Singapore are {event_host} organising?",
    "Which event in the {region} is {event_host} an organiser of?",
    "Which event in the {region} region is {event_host} an organiser of?",
    "Which event in the {region} area is {event_host} an organiser of?",
    "Which event in the {region} of Singapore is {event_host} an organiser of?",
    "Which event is {event_host} an organiser of in the {region}?",
    "Which event is {event_host} an organiser of in the {region} region?",
    "Which event is {event_host} an organiser of in the {region} area?",
    "Which event is {event_host} an organiser of in the {region} of Singapore?",
    "Are there any events in the {region} by the group {event_host}?",
    "Are there any events in the {region} region by the group {event_host}?",
    "Are there any events in the {region} area by the group {event_host}?",
    "Are there any events in the {region} area of Singapore by the group {event_host}?",
    "Are there any events in the {region} of Singapore by the group {event_host}?",
    "Are there any events by the group {event_host} in the {region}?",
    "Are there any events by the group {event_host} in the {region} region?",
    "Are there any events by the group {event_host} in the {region} area?",
    "Are there any events by the group {event_host} in the {region} region of Singapore?",
    "Are there any events by the group {event_host} in the {region} of Singapore?",
    "Is the group {event_host} organising any events in the {region}?",
    "Is the group {event_host} organising any events in the {region} area?",
    "Is the group {event_host} organising any events in the {region} region?",
    "Is the group {event_host} organising any events in the {region} of Singapore?",
    "Is the group {event_host} organising any events in the {region} region of Singapore?",
    "Any events with {event_host} in the {region}?",
    "Any events with {event_host} in the {region} region?",
    "Any events with {event_host} in the {region} area?",
    "Any events with {event_host} in the {region} of Singapore?",
    "Any events in the {region} of Singapore with {event_host}?",
    "Any events in the {region} area of Singapore with {event_host}?",
    "Any events in the {region} area with {event_host}?",
    "Any events in the {region} region with {event_host}?",
    "Any events in the {region} with {event_host}?",
    "Could you please recommend me some events organising by {event_host} in the {region}?",
    "Could you please recommend me some events organising by {event_host} in the {region} region?",
    "Could you please recommend me some events organising by {event_host} in the {region} area?",
    "Could you please recommend me some events organising by {event_host} in the {region} of Singapore?",
    "Could you please recommend me some events organising by {event_host} in the {region} area of Singapore?",
    "Could you please recommend me some events organising by {event_host} in the {region} region of Singapore?",
    "Could you please recommend me some events in the {region} organising by {event_host}?",
    "Could you please recommend me some events in the {region} region organising by {event_host}?",
    "Could you please recommend me some events in the {region} area organising by {event_host}?",
    "Could you please recommend me some events in the {region} of Singapore organising by {event_host}?",
    "Could you please recommend me some events in the {region} area of Singapore organising by {event_host}?",
    "Could you please recommend me some events in the {region} region of Singapore organising by {event_host}?",
    "Can you tell me events by {event_host} in the {region}?",
    "Can you tell me events by {event_host} in the {region} region?",
    "Can you tell me events by {event_host} in the {region} area?",
    "Can you tell me events by {event_host} in the {region} of Singapore?",
    "Can you tell me events in the {region} by {event_host}?",
    "Can you tell me events in the {region} region by {event_host}?",
    "Can you tell me events in the {region} area by {event_host}?",
    "Can you tell me events in the {region} of Singapore by {event_host}?"
]


inform_region_and_date_start_template = [
    "I want to know what events are occurring on {date_start} in the {region}.",
    "I want to know what events are occurring on {date_start} in the {region} region.",
    "I want to know what events are occurring on {date_start} in the {region} area.",
    "I want to know what events are occurring on {date_start} in the {region} region of Singapore.",
    "I want to know what events are occurring on {date_start} in the {region} of Singapore.",
    "I want to know what events in the {region} are occurring on {date_start}.",
    "I want to know what events in the {region} region are occurring on {date_start}.",
    "I want to know what events in the {region} area are occurring on {date_start}.",
    "I want to know what events in the {region} area of Singapore are occurring on {date_start}.",
    "I want to know what events in the {region} of Singapore are occurring on {date_start}.",
    "Are there any events on {date_start} in the {region}?",
    "Are there any events on {date_start} in the {region} area?",
    "Are there any events on {date_start} in the {region} region?",
    "Are there any events on {date_start} in the {region} area of Singapore?",
    "Are there any events on {date_start} in the {region} region of Singapore?",
    "Are there any events on {date_start} in the {region} of Singapore?",
    "Are there any events in the {region} on {date_start}?",
    "Are there any events in the {region} area on {date_start}?",
    "Are there any events in the {region} region on {date_start}?",
    "Are there any events in the {region} area of Singapore on {date_start}?",
    "Are there any events in the {region} region of Singapore on {date_start}?",
    "Are there any events in the {region} of Singapore on {date_start}?",
    "What events are on {date_start} in the {region}?",
    "What events are on {date_start} in the {region} area?",
    "What events are on {date_start} in the {region} region?",
    "What events are on {date_start} in the {region} of Singapore?",
    "What events are on {date_start} in the {region} region of Singapore?",
    "What events in the {region} are on {date_start}?",
    "What events in the {region} area are on {date_start}?",
    "What events in the {region} region are on {date_start}?",
    "What events in the {region} of Singapore are on {date_start}?",
    "What events in the {region} region of Singapore are on {date_start}?",
    "Does {date_start} have events in the {region} I can attend?",
    "Does {date_start} have events in the {region} region I can attend?",
    "Does {date_start} have events in the {region} area I can attend?",
    "Does {date_start} have events in the {region} of Singapore I can attend?",
    "Does {date_start} have events in the {region} area of Singapore I can attend?",
    "Will there be any events on {date_start} in the {region}?",
    "Will there be any events on {date_start} in the {region} region?",
    "Will there be any events on {date_start} in the {region} area?",
    "Will there be any events on {date_start} in the {region} region of Singapore?",
    "Will there be any events on {date_start} in the {region} of Singapore?",
    "Will there be any events in the {region} on {date_start}?",
    "Will there be any events in the {region} region on {date_start}?",
    "Will there be any events in the {region} area on {date_start}?",
    "Will there be any events in the {region} area of Singapore on {date_start}?",
    "Will there be any events in the {region} of Singapore on {date_start}?",
    "Can you recommend me some events on {date_start} in the {region}?",
    "Can you recommend me some events on {date_start} in the {region} region?",
    "Can you recommend me some events on {date_start} in the {region} area?",
    "Can you recommend me some events on {date_start} in the {region} of Singapore?",
    "Can you recommend me some events on {date_start} in the {region} region of Singapore?",
    "Can you recommend me some events in the {region} on {date_start}?",
    "Can you recommend me some events in the {region} region on {date_start}?",
    "Can you recommend me some events in the {region} area on {date_start}?",
    "Can you recommend me some events in the {region} of Singapore on {date_start}?",
    "Can you recommend me some events in the {region} area of Singapore on {date_start}?",
    "Do you kow any events holding on {date_start} in the {region}?",
    "Do you kow any events holding on {date_start} in the {region} region?",
    "Do you kow any events holding on {date_start} in the {region} area?",
    "Do you kow any events holding on {date_start} in the {region} region of Singapore?",
    "Do you kow any events holding on {date_start} in the {region} of Singapore?",
    "Do you kow any events holding on {date_start} in the {region} area of Singapore?",
    "Do you kow any events holding in the {region} on {date_start}?",
    "Do you kow any events holding in the {region} region on {date_start}?",
    "Do you kow any events holding in the {region} area on {date_start}?",
    "Do you kow any events holding in the {region} region of Singapore on {date_start}?",
    "Do you kow any events holding in the {region} of Singapore on {date_start}?",
    "Do you kow any events holding in the {region} area of Singapore on {date_start}?",
    "Do you have any suggestions on events on {date_start} in the {region}?",
    "Do you have any suggestions on events on {date_start} in the {region} region?",
    "Do you have any suggestions on events on {date_start} in the {region} area?",
    "Do you have any suggestions on events on {date_start} in the {region} of Singapore?",
    "Do you have any suggestions on events on {date_start} in the {region} region of Singapore?",
    "Do you have any suggestions on events in the {region} on {date_start}?",
    "Do you have any suggestions on events in the {region} region on {date_start}?",
    "Do you have any suggestions on events in the {region} area on {date_start}?",
    "Do you have any suggestions on events in the {region} of Singapore on {date_start}?",
    "Do you have any suggestions on events in the {region} area of Singapore on {date_start}?"
]


inform_region_and_time_template = [
    "I would like to know about events that are around {time} in the {region}.",
    "I would like to know about events that are around {time} in the {region} region.",
    "I would like to know about events that are around {time} in the {region} area.",
    "I would like to know about events that are around {time} in the {region} of Singapore.",
    "I would like to know about events that are around {time} in the {region} region of Singapore.",
    "I would like to know about events in the {region} that are around {time}.",
    "I would like to know about events in the {region} region that are around {time}.",
    "I would like to know about events in the {region} area that are around {time}.",
    "I would like to know about events in the {region} of Singapore that are around {time}.",
    "I would like to know about events in the {region} region of Singapore that are around {time}.",
    "Are there any events that start at {time} in the {region}?",
    "Are there any events that start at {time} in the {region} area?",
    "Are there any events that start at {time} in the {region} region?",
    "Are there any events that start at {time} in the {region} of Singapore?",
    "Are there any events that start at {time} in the {region} area of Singapore?",
    "Are there any events that start at {time} in the {region} region of Singapore?",
    "Are there any events in the {region} that start at {time}?",
    "Are there any events in the {region} area that start at {time}?",
    "Are there any events in the {region} region that start at {time}?",
    "Are there any events in the {region} of Singapore that start at {time}?",
    "Are there any events in the {region} area of Singapore that start at {time}?",
    "Are there any events in the {region} region of Singapore that start at {time}?",
    "Tell me about events around {time} in the {region}.",
    "Tell me about events around {time} in the {region} region.",
    "Tell me about events around {time} in the {region} area.",
    "Tell me about events around {time} in the {region} of Singapore.",
    "Tell me about events around {time} in the {region} region of Singapore.",
    "Tell me about events in the {region} around {time}.",
    "Tell me about events in the {region} region around {time}.",
    "Tell me about events in the {region} area around {time}.",
    "Tell me about events in the {region} of Singapore around {time}.",
    "Tell me about events in the {region} region of Singapore around {time}.",
    "Will there be any events around {time} in the {region}?",
    "Will there be any events around {time} in the {region} region?",
    "Will there be any events around {time} in the {region} area?",
    "Will there be any events around {time} in the {region} of Singapore?",
    "Will there be any events around {time} in the {region} region of Singapore?",
    "Will there be any events around {time} in the {region} area of Singapore?",
    "Will there be any events in the {region} around {time}?",
    "Will there be any events in the {region} region around {time}?",
    "Will there be any events in the {region} area around {time}?",
    "Will there be any events in the {region} of Singapore around {time}?",
    "Will there be any events in the {region} region of Singapore around {time}?",
    "Will there be any events in the {region} area of Singapore around {time}?",
    "I want to know if there are events at {time} in the {region}?",
    "I want to know if there are events at {time} in the {region} region?",
    "I want to know if there are events at {time} in the {region} area?",
    "I want to know if there are events at {time} in the {region} of Singapore?",
    "I want to know if there are events at {time} in the {region} region of Singapore?",
    "I want to know if there are events at {time} in the {region} area of Singapore?",
    "I want to know if there are events in the {region} at {time}?",
    "I want to know if there are events in the {region} region at {time}?",
    "I want to know if there are events in the {region} area at {time}?",
    "I want to know if there are events in the {region} of Singapore at {time}?",
    "I want to know if there are events in the {region} region of Singapore at {time}?",
    "I want to know if there are events in the {region} area of Singapore at {time}?",
    "Do you know any events start at {time} in the {region}?",
    "Do you know any events start at {time} in the {region} region?",
    "Do you know any events start at {time} in the {region} area?",
    "Do you know any events start at {time} in the {region} of Singapore?",
    "Do you know any events start at {time} in the {region} region of Singapore?",
    "Do you know any events start at {time} in the {region} area of Singapore?",
    "Do you know any events in the {region} start at {time}?",
    "Do you know any events in the {region} region start at {time}?",
    "Do you know any events in the {region} area start at {time}?",
    "Do you know any events in the {region} of Singapore start at {time}?",
    "Do you know any events in the {region} region of Singapore start at {time}?",
    "Do you know any events in the {region} area of Singapore start at {time}?",
    "Can you recommend any event begins around {time} in the {region}?",
    "Can you recommend any event begins around {time} in the {region} region?",
    "Can you recommend any event begins around {time} in the {region} area?",
    "Can you recommend any event begins around {time} in the {region} of Singapore?",
    "Can you recommend any event begins around {time} in the {region} area of Singapore?",
    "Can you recommend any event in the {region} begins around {time}?",
    "Can you recommend any event in the {region} region begins around {time}?",
    "Can you recommend any event in the {region} area begins around {time}?",
    "Can you recommend any event in the {region} of Singapore begins around {time}?",
    "Can you recommend any event in the {region} region of Singapore begins around {time}?",
    "Can I know some events at around {time} in the {region}?",
    "Can I know some events at around {time} in the {region} region?",
    "Can I know some events at around {time} in the {region} area?",
    "Can I know some events at around {time} in the {region} of Singapore?",
    "Can I know some events at around {time} in the {region} region of Singapore?",
    "Can I know some events at around {time} in the {region} area of Singapore?",
    "Can I know some events in the {region} at around {time}?",
    "Can I know some events in the {region} region at around {time}?",
    "Can I know some events in the {region} area at around {time}?",
    "Can I know some events in the {region} of Singapore at around {time}?",
    "Can I know some events in the {region} region of Singapore at around {time}?",
    "Can I know some events in the {region} area of Singapore at around {time}?"
]


inform_region_and_price_template = [
    "I would like to know about events that are around {price} dollars in the {region}.",
    "I would like to know about events that are around {price} dollar in the {region} region.",
    "I would like to know about events that are around {price} SGD in the {region} area.",
    "I would like to know about events that are around ${price} in the {region} of Singapore.",
    "I would like to know about events that are around {price} dollars in the {region} region of Singapore.",
    "I would like to know about events that are around {price} dollar in the {region} area of Singapore.",
    "I would like to know about events in the {region} that are around {price} SGD.",
    "I would like to know about events in the {region} region that are around {price} SGD.",
    "I would like to know about events in the {region} area that are around {price} dollar.",
    "I would like to know about events in the {region} of Singapore that are around {price} dollars.",
    "I would like to know about events in the {region} region of Singapore that are around {price} SGD.",
    "I would like to know about events in the {region} area of Singapore that are around ${price}.",
    "Are there any events that start at ${price} in the {region}?",
    "Are there any events that start at {price} dollar in the {region} region?",
    "Are there any events that start at {price} dollars in the {region} area?",
    "Are there any events that start at {price} SGD in the {region} region of Singapore?",
    "Are there any events that start at ${price} in the {region} area of Singapore?",
    "Are there any events that start at {price} SGD in the {region} of Singapore?",
    "Are there any events in the {region} that start at {price} dollars?",
    "Are there any events in the {region} region that start at {price} dollar?",
    "Are there any events in the {region} area that start at ${price}?",
    "Are there any events in the {region} region of Singapore that start at {price} dollars?",
    "Are there any events in the {region} area of Singapore that start at {price} dollar?",
    "Are there any events in the {region} of Singapore that start at {price} SGD?",
    "Tell me about events around ${price} in the {region}.",
    "Tell me about events around {price} dollar in the {region} region.",
    "Tell me about events around {price} dollars in the {region} area.",
    "Tell me about events around {price} SGD in the {region} of Singapore.",
    "Tell me about events around ${price} in the {region} region of Singapore.",
    "Tell me about events around {price} SGD in the {region} area of Singapore.",
    "Tell me about events in the {region} dollar around {price}.",
    "Tell me about events in the {region} dollars region around {price}.",
    "Tell me about events in the {region} area around ${price}.",
    "Tell me about events in the {region} of Singapore around ${price}.",
    "Tell me about events in the {region} SGD region of Singapore around {price}.",
    "Tell me about events in the {region} dollars area of Singapore around {price}.",
    "Will there be any events around ${price} in the {region}?",
    "Will there be any events around {price} dollar in the {region} region?",
    "Will there be any events around {price} SGD in the {region} area?",
    "Will there be any events around {price} dollars in the {region} of Singapore?",
    "Will there be any events around ${price} in the {region} region of Singapore?",
    "Will there be any events in the {region} around {price} dollars?",
    "Will there be any events in the {region} region around {price} dollar?",
    "Will there be any events in the {region} area around {price} SGD?",
    "Will there be any events in the {region} of Singapore around ${price}?",
    "Will there be any events in the {region} area of Singapore around ${price}?",
    "I want to know if there are events at ${price} in the {region}?",
    "I want to know if there are events at {price} SGD in the {region} region?",
    "I want to know if there are events at {price} SGD in the {region} area?",
    "I want to know if there are events at {price} dollars in the {region} of Singapore?",
    "I want to know if there are events at {price} dollar in the {region} region of Singapore?",
    "I want to know if there are events at ${price} in the {region} area of Singapore?",
    "I want to know if there are events in the {region} at ${price}?",
    "I want to know if there are events in the {region} region at {price} SGD?",
    "I want to know if there are events in the {region} area at {price} dollars?",
    "I want to know if there are events in the {region} of Singapore at {price} dollar?",
    "I want to know if there are events in the {region} region of Singapore at ${price}?",
    "I want to know if there are events in the {region} area of Singapore at {price} SGD?",
    "Do you know any events start at {price} SGD in the {region}?",
    "Do you know any events start at {price} dollars in the {region} region?",
    "Do you know any events start at {price} dollar in the {region} area?",
    "Do you know any events start at ${price} in the {region} of Singapore?",
    "Do you know any events start at {price} SGD in the {region} region of Singapore?",
    "Do you know any events in the {region} start at {price} SGD?",
    "Do you know any events in the {region} region start at {price} dollar?",
    "Do you know any events in the {region} area start at {price} dollars?",
    "Do you know any events in the {region} of Singapore start at ${price}?",
    "Do you know any events in the {region} area of Singapore start at ${price}?",
    "Can you recommend any event begins around {price} SGD in the {region}?",
    "Can you recommend any event begins around {price} SGD in the {region} region?",
    "Can you recommend any event begins around {price} dollars in the {region} area?",
    "Can you recommend any event begins around {price} dollar in the {region} of Singapore?",
    "Can you recommend any event begins around ${price} in the {region} region of Singapore?",
    "Can you recommend any event begins around ${price} in the {region} area of Singapore?",
    "Can you recommend any event in the {region} begins around {price} dollar?",
    "Can you recommend any event in the {region} region begins around {price} dollars?",
    "Can you recommend any event in the {region} area begins around {price} SGD?",
    "Can you recommend any event in the {region} of Singapore begins around {price} SGD?",
    "Can you recommend any event in the {region} region of Singapore begins around ${price}?",
    "Can you recommend any event in the {region} area of Singapore begins around ${price}?",
    "Can I know some events at around ${price} in the {region}?",
    "Can I know some events at around {price} SGD in the {region} region?",
    "Can I know some events at around {price} dollars in the {region} area?",
    "Can I know some events at around {price} dollar in the {region} of Singapore?",
    "Can I know some events at around {price} SGD in the {region} region of Singapore?",
    "Can I know some events at around ${price} in the {region} area of Singapore?",
    "Can I know some events in the {region} at around {price} SGD?",
    "Can I know some events in the {region} region at around {price} dollars?",
    "Can I know some events in the {region} area at around {price} dollar?",
    "Can I know some events in the {region} of Singapore at around ${price}?",
    "Can I know some events in the {region} region of Singapore at around ${price}?",
    "Can I know some events in the {region} area of Singapore at around {price} SGD?"
]


inform_region_and_is_weekend_template = [
    "Tell me about events that on {is_weekend} in the {region}.",
    "Tell me about events that on {is_weekend} in the {region} region.",
    "Tell me about events that on {is_weekend} in the {region} area.",
    "Tell me about events that on {is_weekend} in the {region} of Singapore.",
    "Tell me about events that on {is_weekend} in the {region} region of Singapore.",
    "Tell me about events that on {is_weekend} in the {region} area of Singapore.",
    "Tell me about events in the {region} that on {is_weekend}.",
    "Tell me about events in the {region} region that on {is_weekend}.",
    "Tell me about events in the {region} area that on {is_weekend}.",
    "Tell me about events in the {region} of Singapore that on {is_weekend}.",
    "Tell me about events in the {region} region of Singapore that on {is_weekend}.",
    "Tell me about events in the {region} area of Singapore that on {is_weekend}.",
    "Which events take place on {is_weekend} in the {region}.",
    "Which events take place on {is_weekend} in the {region} region.",
    "Which events take place on {is_weekend} in the {region} area.",
    "Which events take place on {is_weekend} in the {region} of Singapore.",
    "Which events take place on {is_weekend} in the {region} region of Singapore.",
    "Which events take place on {is_weekend} in the {region} area of Singapore.",
    "Which events in the {region} take place on {is_weekend}.",
    "Which events in the {region} region take place on {is_weekend}.",
    "Which events in the {region} area take place on {is_weekend}.",
    "Which events in the {region} of Singapore take place on {is_weekend}.",
    "Which events in the {region} region of Singapore take place on {is_weekend}.",
    "Which events in the {region} area of Singapore take place on {is_weekend}.",
    "I would like to find an event that is on {is_weekend} in the {region}.",
    "I would like to find an event that is on {is_weekend} in the {region} region.",
    "I would like to find an event that is on {is_weekend} in the {region} area.",
    "I would like to find an event that is on {is_weekend} in the {region} of Singapore.",
    "I would like to find an event that is on {is_weekend} in the {region} region of Singapore.",
    "I would like to find an event that is on {is_weekend} in the {region} area of Singapore.",
    "I would like to find an event in the {region} that is on {is_weekend}.",
    "I would like to find an event in the {region} region that is on {is_weekend}.",
    "I would like to find an event in the {region} area that is on {is_weekend}.",
    "I would like to find an event in the {region} of Singapore that is on {is_weekend}.",
    "I would like to find an event in the {region} region of Singapore that is on {is_weekend}.",
    "I would like to find an event in the {region} area of Singapore that is on {is_weekend}.",
    "What events are conducted on {is_weekend} in the {region}.",
    "What events are conducted on {is_weekend} in the {region} region.",
    "What events are conducted on {is_weekend} in the {region} area.",
    "What events are conducted on {is_weekend} in the {region} of Singapore.",
    "What events are conducted on {is_weekend} in the {region} region of Singapore.",
    "What events are conducted on {is_weekend} in the {region} area of Singapore.",
    "What events in the {region} are conducted on {is_weekend}.",
    "What events in the {region} region are conducted on {is_weekend}.",
    "What events in the {region} area are conducted on {is_weekend}.",
    "What events in the {region} of Singapore are conducted on {is_weekend}.",
    "What events in the {region} region of Singapore are conducted on {is_weekend}.",
    "What events in the {region} area of Singapore are conducted on {is_weekend}.",
    "Will there be events that take place on {is_weekend} in the {region}?",
    "Will there be events that take place on {is_weekend} in the {region} region?",
    "Will there be events that take place on {is_weekend} in the {region} area?",
    "Will there be events that take place on {is_weekend} in the {region} of Singapore?",
    "Will there be events that take place on {is_weekend} in the {region} region of Singapore?",
    "Will there be events that take place on {is_weekend} in the {region} area of Singapore?",
    "Will there be events in the {region} that take place on {is_weekend}?",
    "Will there be events in the {region} region that take place on {is_weekend}?",
    "Will there be events in the {region} area that take place on {is_weekend}?",
    "Will there be events in the {region} of Singapore that take place on {is_weekend}?",
    "Will there be events in the {region} region of Singapore that take place on {is_weekend}?",
    "Will there be events in the {region} area of Singapore that take place on {is_weekend}?",
    "I want to know the events that are available on {is_weekend} in the {region}.",
    "I want to know the events that are available on {is_weekend} in the {region} region.",
    "I want to know the events that are available on {is_weekend} in the {region} area.",
    "I want to know the events that are available on {is_weekend} in the {region} of Singapore.",
    "I want to know the events that are available on {is_weekend} in the {region} region of Singapore.",
    "I want to know the events that are available in the {region} on {is_weekend}.",
    "I want to know the events that are available in the {region} region on {is_weekend}.",
    "I want to know the events that are available in the {region} area on {is_weekend}.",
    "I want to know the events that are available in the {region} of Singapore on {is_weekend}.",
    "I want to know the events that are available in the {region} area of Singapore on {is_weekend}.",
    "Can you recommend some events on {is_weekend} in the {region}?",
    "Can you recommend some events on {is_weekend} in the {region} region?",
    "Can you recommend some events on {is_weekend} in the {region} area?",
    "Can you recommend some events on {is_weekend} in the {region} of Singapore?",
    "Can you recommend some events on {is_weekend} in the {region} region of Singapore?",
    "Can you recommend some events on {is_weekend} in the {region} area of Singapore?",
    "Can you recommend some events in the {region} on {is_weekend}?",
    "Can you recommend some events in the {region} region on {is_weekend}?",
    "Can you recommend some events in the {region} area on {is_weekend}?",
    "Can you recommend some events in the {region} of Singapore on {is_weekend}?",
    "Can you recommend some events in the {region} region of Singapore on {is_weekend}?",
    "Can you recommend some events in the {region} area of Singapore on {is_weekend}?",
    "Do you have any suggestions on events on {is_weekend} in the {region}?",
    "Do you have any suggestions on events on {is_weekend} in the {region} region?",
    "Do you have any suggestions on events on {is_weekend} in the {region} area?",
    "Do you have any suggestions on events on {is_weekend} in the {region} of Singapore?",
    "Do you have any suggestions on events on {is_weekend} in the {region} region of Singapore?",
    "Do you have any suggestions on events on {is_weekend} in the {region} area of Singapore?",
    "Do you have any suggestions on events in the {region} on {is_weekend}?",
    "Do you have any suggestions on events in the {region} region on {is_weekend}?",
    "Do you have any suggestions on events in the {region} area on {is_weekend}?",
    "Do you have any suggestions on events in the {region} of Singapore on {is_weekend}?",
    "Do you have any suggestions on events in the {region} region of Singapore on {is_weekend}?",
    "Do you have any suggestions on events in the {region} area of Singapore on {is_weekend}?",
    "I want to find some events on {is_weekend} in the {region}.",
    "I want to find some events on {is_weekend} in the {region} region.",
    "I want to find some events on {is_weekend} in the {region} area.",
    "I want to find some events on {is_weekend} in the {region} of Singapore.",
    "I want to find some events on {is_weekend} in the {region} region of Singapore.",
    "I want to find some events on {is_weekend} in the {region} area of Singapore.",
    "I want to find some events in the {region} on {is_weekend}.",
    "I want to find some events in the {region} region on {is_weekend}.",
    "I want to find some events in the {region} area on {is_weekend}.",
    "I want to find some events in the {region} of Singapore on {is_weekend}.",
    "I want to find some events in the {region} region of Singapore on {is_weekend}.",
    "I want to find some events in the {region} area of Singapore on {is_weekend}."
]


inform_region_and_part_of_day_template = [
    "Tell me about events that are in {part_of_day} in the {region}.",
    "Tell me about events that are in {part_of_day} in the {region} region.",
    "Tell me about events that are in {part_of_day} in the {region} area.",
    "Tell me about events that are in {part_of_day} in the {region} of Singapore.",
    "Tell me about events that are in {part_of_day} in the {region} region of Singapore.",
    "Tell me about events that are in {part_of_day} in the {region} area of Singapore.",
    "Tell me about events that are in the {region} in {part_of_day}.",
    "Tell me about events that are in the {region} region in {part_of_day}.",
    "Tell me about events that are in the {region} area in {part_of_day}.",
    "Tell me about events that are in the {region} of Singapore in {part_of_day}.",
    "Tell me about events that are in the {region} region of Singapore in {part_of_day}.",
    "Tell me about events that are in the {region} area of Singapore in {part_of_day}.",
    "Which events take place on {part_of_day} in the {region}.",
    "Which events take place on {part_of_day} in the {region} region.",
    "Which events take place on {part_of_day} in the {region} area.",
    "Which events take place on {part_of_day} in the {region} of Singapore.",
    "Which events take place on {part_of_day} in the {region} region of Singapore.",
    "Which events take place on {part_of_day} in the {region} are of Singapore.",
    "Which events in the {region} take place on {part_of_day}.",
    "Which events in the {region} region take place on {part_of_day}.",
    "Which events in the {region} area take place on {part_of_day}.",
    "Which events in the {region} of Singapore take place on {part_of_day}.",
    "Which events in the {region} region of Singapore take place on {part_of_day}.",
    "Which events in the {region} are of Singapore take place on {part_of_day}.",
    "I would like to find an event in the {region} that is in {part_of_day}.",
    "I would like to find an event in the {region} region that is in {part_of_day}.",
    "I would like to find an event in the {region} area that is in {part_of_day}.",
    "I would like to find an event in the {region} of Singapore that is in {part_of_day}.",
    "I would like to find an event in the {region} region of Singapore that is in {part_of_day}.",
    "I would like to find an event in the {region} area of Singapore that is in {part_of_day}.",
    "What events are conducted on {part_of_day} in the {region}.",
    "What events are conducted on {part_of_day} in the {region} region.",
    "What events are conducted on {part_of_day} in the {region} area.",
    "What events are conducted on {part_of_day} in the {region} of Singapore.",
    "What events are conducted on {part_of_day} in the {region} region of Singapore.",
    "What events are conducted on {part_of_day} in the {region} area of Singapore.",
    "What events in the {region} are conducted on {part_of_day}.",
    "What events in the {region} region are conducted on {part_of_day}.",
    "What events in the {region} area are conducted on {part_of_day}.",
    "What events in the {region} of Singapore are conducted on {part_of_day}.",
    "What events in the {region} region of Singapore are conducted on {part_of_day}.",
    "What events in the {region} area of Singapore are conducted on {part_of_day}.",
    "Will there be events in the {region} that take place in {part_of_day}?",
    "Will there be events in the {region} region that take place in {part_of_day}?",
    "Will there be events in the {region} area that take place in {part_of_day}?",
    "Will there be events in the {region} of Singapore that take place in {part_of_day}?",
    "Will there be events in the {region} region of Singapore that take place in {part_of_day}?",
    "Will there be events in the {region} area of Singapore that take place in {part_of_day}?",
    "Will there be events that take place in {part_of_day} in the {region}?",
    "Will there be events that take place in {part_of_day} in the {region} region?",
    "Will there be events that take place in {part_of_day} in the {region} area?",
    "Will there be events that take place in {part_of_day} in the {region} of Singapore?",
    "Will there be events that take place in {part_of_day} in the {region} region of Singapore?",
    "Will there be events that take place in {part_of_day} in the {region} area of Singapore?",
    "I want to know the events that are available at {part_of_day} in the {region}.",
    "I want to know the events that are available at {part_of_day} in the {region} region.",
    "I want to know the events that are available at {part_of_day} in the {region} area.",
    "I want to know the events that are available at {part_of_day} in the {region} of Singapore.",
    "I want to know the events that are available at {part_of_day} in the {region} region of Singapore.",
    "I want to know the events that are available at {part_of_day} in the {region} area of Singapore.",
    "I want to know the events in the {region} that are available at {part_of_day}.",
    "I want to know the events in the {region} region that are available at {part_of_day}.",
    "I want to know the events in the {region} area that are available at {part_of_day}.",
    "I want to know the events in the {region} of Singapore that are available at {part_of_day}.",
    "I want to know the events in the {region} region of Singapore that are available at {part_of_day}.",
    "I want to know the events in the {region} area of Singapore that are available at {part_of_day}.",
    "Can you recommend some events start at {part_of_day} in the {region}?",
    "Can you recommend some events start at {part_of_day} in the {region} region?",
    "Can you recommend some events start at {part_of_day} in the {region} area?",
    "Can you recommend some events start at {part_of_day} in the {region} of Singapore?",
    "Can you recommend some events start at {part_of_day} in the {region} region of Singapore?",
    "Can you recommend some events in the {region} start at {part_of_day}?",
    "Can you recommend some events in the {region} region start at {part_of_day}?",
    "Can you recommend some events in the {region} area start at {part_of_day}?",
    "Can you recommend some events in the {region} of Singapore start at {part_of_day}?",
    "Can you recommend some events in the {region} area of Singapore start at {part_of_day}?",
    "Do you know any events begins in {part_of_day} in the {region}?",
    "Do you know any events begins in {part_of_day} in the {region} region?",
    "Do you know any events begins in {part_of_day} in the {region} area?",
    "Do you know any events begins in {part_of_day} in the {region} of Singapore?",
    "Do you know any events begins in {part_of_day} in the {region} region of Singapore?",
    "Do you know any events begins in {part_of_day} in the {region} area of Singapore?",
    "Do you know any events in the {region} that begins in {part_of_day}?",
    "Do you know any events in the {region} region that begins in {part_of_day}?",
    "Do you know any events in the {region} area that begins in {part_of_day}?",
    "Do you know any events in the {region} of Singapore that begins in {part_of_day}?",
    "Do you know any events in the {region} region of Singapore that begins in {part_of_day}?",
    "Do you know any events in the {region} area of Singapore that begins in {part_of_day}?",
    "Do you have any suggestions on events in {part_of_day} in the {region}?",
    "Do you have any suggestions on events in {part_of_day} in the {region} region?",
    "Do you have any suggestions on events in {part_of_day} in the {region} area?",
    "Do you have any suggestions on events in {part_of_day} in the {region} of Singapore?",
    "Do you have any suggestions on events in {part_of_day} in the {region} region of Singapore?",
    "Do you have any suggestions on events in the {region} in {part_of_day}?",
    "Do you have any suggestions on events in the {region} region in {part_of_day}?",
    "Do you have any suggestions on events in the {region} area in {part_of_day}?",
    "Do you have any suggestions on events in the {region} of Singapore in {part_of_day}?",
    "Do you have any suggestions on events in the {region} area of Singapore in {part_of_day}?",
    "I want to find some events in {part_of_day} in the {region}.",
    "I want to find some events in {part_of_day} in the {region} region.",
    "I want to find some events in {part_of_day} in the {region} area.",
    "I want to find some events in {part_of_day} in the {region} of Singapore.",
    "I want to find some events in {part_of_day} in the {region} region of Singapore.",
    "I want to find some events in {part_of_day} in the {region} area of Singapore.",
    "I want to find some events in the {region} in {part_of_day}.",
    "I want to find some events in the {region} region in {part_of_day}.",
    "I want to find some events in the {region} area in {part_of_day}.",
    "I want to find some events in the {region} of Singapore in {part_of_day}.",
    "I want to find some events in the {region} region of Singapore in {part_of_day}.",
    "I want to find some events in the {region} area of Singapore in {part_of_day}."
]


inform_event_host_and_date_start_template = [
    "Are there events by {event_host} occuring on {date_start}?",
    "Are there events by {event_host} on {date_start}?",
    "Are there events occurring on {date_start} by {event_host}?",
    "Are there events on {date_start} by {event_host}?",
    "What events would be organised by {event_host} occurring on {date_start}?",
    "What events would be organised by {event_host} on {date_start}?",
    "What events on {date_start} would be organised by {event_host}?",
    "What events occurring on {date_start} would be organised by {event_host}?",
    "Is {event_host} organising any events on {date_start}?",
    "What events are {event_host} organising on {date_start}?",
    "What events on {date_start} are {event_host} organising?",
    "Which event is {event_host} an organiser of on {date_start}?",
    "Which event on {date_start} is {event_host} an organiser of?",
    "Which event occurring on {date_start} is {event_host} an organiser of?",
    "Are there any events by the group {event_host} on {date_start}?",
    "Are there any events by the group {event_host} occurring on {date_start}?",
    "Are there any events on {date_start} by the group {event_host}?",
    "Are there any events occurring on {date_start} by the group {event_host}?",
    "Is the group {event_host} organising any events on {date_start}?",
    "Any events with {event_host} on {date_start}?",
    "Any events on {date_start} with {event_host}?",
    "Could you please recommend me some events organising by {event_host} on {date_start}?",
    "Could you please recommend me some events on {date_start} organising by {event_host}?",
    "Can you tell me events by {event_host} on {date_start}?",
    "Can you tell me events on {date_start} by {event_host}?"
]



inform_event_host_and_time_template = [
    "I would like to know about events that are around {time} organised by {event_host}.",
    "I would like to know about events that are around {time} by {event_host}.",
    "I would like to know about events organised by {event_host} that are around {time}.",
    "I would like to know about events by {event_host} that are around {time}.",
    "Are there any events that start at {time} organised by {event_host}?",
    "Are there any events that start at {time} by {event_host}?",
    "Are there any events organised by {event_host} that start at {time}?",
    "Are there any events by {event_host} that start at {time}?",
    "Tell me about events organised by {event_host}, around {time}.",
    "Tell me about events by {event_host}, around {time}.",
    "Tell me about events around {time} organised by {event_host}.",
    "Tell me about events around {time} by {event_host}.",
    "Will there be any events around {time} organised by {event_host}?",
    "Will there be any events around {time} by {event_host}?",
    "Will there be any events organised by {event_host} around {time}?",
    "Will there be any events by {event_host} around {time}?",
    "I want to know if there are events at {time} organised by {event_host}?",
    "I want to know if there are events at {time} by {event_host}?",
    "I want to know if there are events organised by {event_host} at {time}?",
    "I want to know if there are events by {event_host} at {time}?",
    "Do you know any events start at {time} organised by {event_host}?",
    "Do you know any events start at {time} by {event_host}?",
    "Do you know any events organised by {event_host} start at {time}?",
    "Do you know any events by {event_host} start at {time}?",
    "Can you recommend any event begins around {time} organised by {event_host}?",
    "Can you recommend any event begins around {time} by {event_host}?",
    "Can you recommend any event organised by {event_host} begins around {time}?",
    "Can you recommend any event by {event_host} begins around {time}?",
    "Can I know some events at around {time} organised by {event_host}?",
    "Can I know some events at around {time} by {event_host}?",
    "Can I know some events organised by {event_host} at around {time}?",
    "Can I know some events by {event_host} at around {time}?",
]


inform_event_host_and_price_template = [
    "Do you know any free events organised by {event_host}?",
    "Do you know any free events by {event_host}?",
    "Tell me about some free events organised by {event_host}.",
    "Tell me about some free events by {event_host}.",
    "Can you recommend me some free events organised by {event_host}?",
    "Can you recommend me some free events by {event_host}?",
    "Do you have any suggestions for free events organised by {event_host}?",
    "Do you have any suggestions for free events by {event_host}?",
    "Are there any events around {price} dollars organised by {event_host}?",
    "Are there any events around {price} dollars by {event_host}?",
    "Are there any events organised by {event_host} around {price} dollars?",
    "Are there any events by {event_host} around {price} dollars?",
    "Are there any events less than {price} dollars organised by {event_host}?",
    "Are there any events less than {price} dollars by {event_host}?",
    "Are there any events which is organised by {event_host} and less than {price} dollars?",
    "Are there any events by {event_host} and less than {price} dollars?",
    "Are there any events around ${price} organised by {event_host}.",
    "Are there any events around ${price} by group {event_host}.",
    "Are there any events around ${price} by {event_host}.",
    "I would like to find an event that costs {price} dollars and organised by {event_host}.",
    "I would like to find an event that costs {price} dollars and by {event_host}.",
    "I would like to find an event organised by {event_host} that costs {price} dollars.",
    "I would like to find an event by {event_host} that costs {price} dollars.",
    "I would like to find an event that costs ${price} and is organised by {event_host}.",
    "I would like to find an event that costs ${price} by {event_host}.",
    "I would like to find an event organised by {event_host} that costs ${price}.",
    "I would like to find an event by {event_host} that costs ${price}.",
    "Let me know if there are events organised by {event_host} that are around {price} dollars.",
    "Let me know if there are events by {event_host} that are around {price} dollars.",
    "Let me know if there are events organised by {event_host} that are less than {price} dollars.",
    "Let me know if there are events by the group {event_host} that are less than {price} dollars.",
    "Let me know if there are events organised by {event_host} that are around ${price}.",
    "Let me know if there are events by the group {event_host} that are around ${price}.",
    "Will there be events that cost less than {price} dollars and is organised by {event_host}?",
    "Will there be events that cost less than {price} dollars and is organised by the group {event_host}?",
    "Will there be events organised by {event_host} that cost less than {price} dollars?",
    "Will there be events by {event_host} that cost less than {price} dollars?",
    "Will there be events that cost around {price} dollars and is organised by {event_host}?",
    "Will there be events that cost around {price} dollars by {event_host}?",
    "Will there be events organised by {event_host} that cost around {price} dollars?",
    "Will there be events organised by the group {event_host} that cost around {price} dollars?",
    "Will there be events by {event_host} that cost around {price} dollars?",
    "Will there be events that cost ${price} and is organised by {event_host}?",
    "Will there be events that cost ${price} and is organised by the group {event_host}?",
    "Will there be events organised by {event_host} that cost ${price}?",
    "Will there be events by the group {event_host} that cost ${price}?",
    "Will there be events by {event_host} that cost ${price}?"
]


inform_event_host_and_is_weekend_template = [
    "Tell me about events that on {is_weekend} organised by {event_host}.",
    "Tell me about events that on {is_weekend} by {event_host}.",
    "Tell me about events organised by {event_host} that are on {is_weekend}.",
    "Tell me about events by {event_host} that are on {is_weekend}.",
    "Tell me about events by the group {event_host} that are on {is_weekend}.",
    "Which events take place on {is_weekend} and are organised by {event_host}.",
    "Which events take place on {is_weekend} and are by the group {event_host}.",
    "Which events organised by {event_host} take place on {is_weekend}.",
    "Which events by {event_host} take place on {is_weekend}.",
    "Which events organised by the group {event_host} take place on {is_weekend}.",
    "I would like to find an event that is on {is_weekend} and is organised by {event_host}.",
    "I would like to find an event that is on {is_weekend} and by {event_host}.",
    "I would like to find an event that is on {is_weekend} and is organised by the group {event_host}.",
    "I would like to find an event organised by {event_host} that is on {is_weekend}.",
    "I would like to find an event organised by the group {event_host} that is on {is_weekend}.",
    "I would like to find an event by {event_host} that is on {is_weekend}.",
    "What events organised by {event_host} are conducted on {is_weekend}.",
    "What events by {event_host} are conducted on {is_weekend}.",
    "What events organised by the group {event_host} are conducted on {is_weekend}.",
    "What events are conducted on {is_weekend} and are organised by {event_host}.",
    "Will there be events that take place on {is_weekend}, organised by {event_host}?",
    "Will there be events that take place on {is_weekend}, by the group {event_host}?",
    "Will there be events organised by {event_host} that take place on {is_weekend}?",
    "Will there be events by the group {event_host} that take place on {is_weekend}?",
    "I want to know the events that are available on {is_weekend}, organised by {event_host}.",
    "I want to know the events that are available on {is_weekend}, by {event_host}.",
    "I want to know the events that are available on {is_weekend}, by the group {event_host}.",
    "I want to know the events organised by {event_host} that are available on {is_weekend}.",
    "I want to know the events by the group {event_host} that are available on {is_weekend}.",
    "Can you recommend some events on {is_weekend}, organised by {event_host}?",
    "Can you recommend some events on {is_weekend}, by the group {event_host}?",
    "Can you recommend some events on {is_weekend}, with {event_host}?",
    "Can you recommend some events organised by {event_host} on {is_weekend}?",
    "Can you recommend some events by the group {event_host} on {is_weekend}?",
    "Can you recommend some events with {event_host} on {is_weekend}?",
    "Can you recommend some events with the group {event_host} on {is_weekend}?",
    "Do you have any suggestions on events on {is_weekend} with {event_host}?",
    "Do you have any suggestions on events on {is_weekend} with the group {event_host}?",
    "Do you have any suggestions on events on {is_weekend} organised by the group {event_host}?",
    "Do you have any suggestions on events on {is_weekend} by the group {event_host}?",
    "Do you have any suggestions on events on {is_weekend} by {event_host}?",
    "Do you have any suggestions on events with {event_host} on {is_weekend}?",
    "Do you have any suggestions on events with the group {event_host} on {is_weekend}?",
    "Do you have any suggestions on events organised by the group {event_host} on {is_weekend}?",
    "Do you have any suggestions on events by the group {event_host} on {is_weekend}?",
    "Do you have any suggestions on events by {event_host} on {is_weekend}?",
    "I want to find some events on {is_weekend}, with the group {event_host}.",
    "I want to find some events on {is_weekend}, organised by group {event_host}.",
    "I want to find some events on {is_weekend}, organised by {event_host}.",
    "I want to find some events with {event_host} on {is_weekend}.",
    "I want to find some events with the group {event_host} on {is_weekend}.",
    "I want to find some events organised by group {event_host} on {is_weekend}.",
    "I want to find some events organised by {event_host} on {is_weekend}.",
    "I want to find some events with {event_host} on {is_weekend}."
]


inform_event_host_and_part_of_day_template = [
    "Tell me about events organised by {event_host} that are in {part_of_day}.",
    "Tell me about events with the group {event_host} that are in {part_of_day}.",
    "Tell me about events by {event_host} that are in {part_of_day}.",
    "Tell me about events with {event_host} that are in {part_of_day}.",
    "Tell me about events that are in {part_of_day} and are organised by {event_host}.",
    "Tell me about events that are in {part_of_day} and with the group {event_host}.",
    "Which events take place on {part_of_day} and are organised by {event_host}.",
    "Which events take place on {part_of_day} and are by {event_host}.",
    "Which events take place on {part_of_day} and with the group {event_host}.",
    "Which events organised by {event_host} take place on {part_of_day}.",
    "Which events by {event_host} take place on {part_of_day}.",
    "Which events with the group {event_host} take place on {part_of_day}.",
    "I would like to find an event that is in {part_of_day} and is organised by {event_host}.",
    "I would like to find an event that is in {part_of_day} and by {event_host}.",
    "I would like to find an event organised by {event_host} that is in {part_of_day}.",
    "I would like to find an event by {event_host} that is in {part_of_day}.",
    "I would like to find an event with the group {event_host} that is in {part_of_day}.",
    "What events organised by the group {event_host} are conducted on {part_of_day}.",
    "What events organised by {event_host} are conducted on {part_of_day}.",
    "What events by the group {event_host} are conducted on {part_of_day}.",
    "What events with the group {event_host} are conducted on {part_of_day}.",
    "What events are conducted on {part_of_day} and are organised by the group {event_host}.",
    "What events are conducted on {part_of_day} and are organised by {event_host}.",
    "What events are conducted on {part_of_day} and are by the group {event_host}.",
    "What events are conducted on {part_of_day} with the group {event_host}.",
    "Will there be events that take place in {part_of_day}, organised by {event_host}?",
    "Will there be events that take place in {part_of_day}, by {event_host}?",
    "Will there be events organised by {event_host} that take place in {part_of_day}?",
    "Will there be events by {event_host} that take place in {part_of_day}?",
    "I want to know the events that are available at {part_of_day} with the group {event_host}.",
    "I want to know the events that are available at {part_of_day} organised by the group {event_host}.",
    "I want to know the events that are available at {part_of_day} by the group {event_host}.",
    "I want to know the events that are available at {part_of_day} by {event_host}.",
    "I want to know the events with the group {event_host} that are available at {part_of_day}.",
    "I want to know the events organised by the group {event_host} that are available at {part_of_day}.",
    "I want to know the events by the group {event_host} that are available at {part_of_day}.",
    "I want to know the events by {event_host} that are available at {part_of_day}.",
    "Can you recommend some events start at {part_of_day} and are organised by {event_host}?",
    "Can you recommend some events start at {part_of_day} and are with the group {event_host}?",
    "Can you recommend some events start at {part_of_day}, by {event_host}?",
    "Can you recommend some events organised by {event_host} and start at {part_of_day}?",
    "Can you recommend some events with the group {event_host} which start at {part_of_day}?",
    "Can you recommend some events by {event_host}, which start at {part_of_day}?",
    "Do you know any events begins in {part_of_day} and organised by {event_host}?",
    "Do you know any events begins in {part_of_day}, organised by {event_host}?",
    "Do you know any events begins in {part_of_day} with the group {event_host}?",
    "Do you know any events begins in {part_of_day}, with {event_host}?",
    "Do you know any events organised by {event_host} that begins in {part_of_day}?",
    "Do you know any events organised by {event_host} that begins in {part_of_day}?",
    "Do you know any events with the group {event_host} that begins in {part_of_day}?",
    "Do you know any events with {event_host} which begins in {part_of_day}?",
    "Do you have any suggestions on events by {event_host} in {part_of_day}?",
    "Do you have any suggestions on events organised by {event_host} in {part_of_day}?",
    "Do you have any suggestions on events with {event_host} in {part_of_day}?",
    "Do you have any suggestions on events with the group {event_host} in {part_of_day}?",
    "I want to find some events in {part_of_day}, organised by {event_host}.",
    "I want to find some events in {part_of_day}, by {event_host}.",
    "I want to find some events in {part_of_day}, with {event_host}.",
    "I want to find some events organised by {event_host}, in {part_of_day}.",
    "I want to find some events by {event_host} in {part_of_day}.",
    "I want to find some events with {event_host} in {part_of_day}."
]


inform_date_start_and_time_template = [
    "I want to know what events are occurring on {date_start} at {time}.",
    "I want to know what events are occurring on {date_start} around {time}.",
    "I want to know what events are holding on {date_start} at {time}.",
    "I want to know what events are holding on {date_start} around {time}.",
    "Are there any events on {date_start} at {time}?",
    "Are there any events on {date_start} around {time}?",
    "Are there any events holding on {date_start} at {time}?",
    "Are there any events holding on {date_start} around {time}?",
    "Are there any events occurring on {date_start} at {time}?",
    "Are there any events occurring on {date_start} around {time}?",
    "What events are on {date_start} at {time}?",
    "What events are on {date_start} around {time}?",
    "What events are holding on {date_start} at {time}?",
    "What events are holding on {date_start} around {time}?",
    "What events are occurring on {date_start} at {time}?",
    "What events are occurring on {date_start} around {time}?",
    "Does {date_start} around {time} have events I can attend?",
    "Does {date_start} at {time} have events I can attend?",
    "Will there be any events on {date_start} at {time}?",
    "Will there be any events on {date_start} around {time}?",
    "Will there be any events holding on {date_start} at {time}?",
    "Will there be any events holding on {date_start} around {time}?",
    "Will there be any events occurring on {date_start} at {time}?",
    "Will there be any events occurring on {date_start} around {time}?",
    "Can you recommend me some events on {date_start} at {time}?",
    "Can you recommend me some events on {date_start} around {time}?",
    "Can you recommend me some events holding on {date_start} at {time}?",
    "Can you recommend me some events holding on {date_start} around {time}?",
    "Can you recommend me some events occurring on {date_start} at {time}?",
    "Can you recommend me some events occurring on {date_start} around {time}?",
    "Do you kow any events holding on {date_start} at {time}?",
    "Do you kow any events holding on {date_start} around {time}?",
    "Do you kow any events occurring on {date_start} at {time}?",
    "Do you kow any events occurring on {date_start} around {time}?",
    "Do you kow any events on {date_start} at {time}?",
    "Do you kow any events on {date_start} around {time}?",
    "Do you have any suggestions on events on {date_start} at {time}?",
    "Do you have any suggestions on events on {date_start} around {time}?",
    "Do you have any suggestions on events holding on {date_start} at {time}?",
    "Do you have any suggestions on events holding on {date_start} around {time}?",
    "Do you have any suggestions on events occurring on {date_start} at {time}?",
    "Do you have any suggestions on events occurring on {date_start} around {time}?"
]


inform_date_start_and_price_template = [
    "Do you know any free events holding on {date_start}?",
    "Do you know any free events occurring on {date_start}?",
    "Do you know any free events on on {date_start}?",
    "Tell me about some free events holding on {date_start}.",
    "Tell me about some free events occuring on {date_start}.",
    "Tell me about some free events on {date_start}.",
    "Can you recommend me some free events holding on {date_start}?",
    "Can you recommend me some free events occurring on {date_start}?",
    "Can you recommend me some free events on {date_start}?",
    "Do you have any suggestions for free events holding on {date_start}?",
    "Do you have any suggestions for free events occurring on {date_start}?",
    "Do you have any suggestions for free events on {date_start}?",
    "Are there any events around {price} dollars holding on {date_start}.",
    "Are there any events around {price} dollars occurring on {date_start}.",
    "Are there any events around {price} dollars on {date_start}.",
    "Are there any events holding on {date_start} which are around {price} dollars.",
    "Are there any events occurring on {date_start} that are around {price} dollars.",
    "Are there any events on {date_start} that are around {price} dollars.",
    "Are there any events less than {price} dollars holding on {date_start}.",
    "Are there any events less than {price} dollars occurring on {date_start}.",
    "Are there any events less than {price} dollars on {date_start}.",
    "Are there any events holding on {date_start} that are less than {price} dollars.",
    "Are there any events occurring on {date_start} which are less than {price} dollars.",
    "Are there any events on {date_start} that are less than {price} dollars.",
    "Are there any events around ${price} holding on {date_start}.",
    "Are there any events around ${price} occurring on {date_start}.",
    "Are there any events around ${price} on {date_start}.",
    "Are there any events holding on {date_start} that are around ${price}.",
    "Are there any events occurring on {date_start} that are around ${price}.",
    "Are there any events on {date_start} which are around ${price}.",
    "I would like to find an event that costs {price} dollars, holding on {date_start}.",
    "I would like to find an event that costs {price} dollars, occurring on {date_start}.",
    "I would like to find an event that costs {price} dollars, on {date_start}.",
    "I would like to find an event holding on {date_start} that costs {price} dollars.",
    "I would like to find an event occurring on {date_start} that costs {price} dollars.",
    "I would like to find an event on {date_start} that costs {price} dollars.",
    "I would like to find an event holding on {date_start} that costs ${price}.",
    "I would like to find an event occurring on {date_start} that costs ${price}.",
    "I would like to find an event on {date_start} that costs ${price}.",
    "Let me know if there are events that are around {price} dollars holding on {date_start}.",
    "Let me know if there are events that are around {price} dollars occurring on {date_start}.",
    "Let me know if there are events that are around {price} dollars on {date_start}.",
    "Let me know if there are events holding on {date_start} that are around {price} dollars.",
    "Let me know if there are events occurring on {date_start} that are around {price} dollars.",
    "Let me know if there are events on {date_start} that are around {price} dollars.",
    "Let me know if there are events that are less than {price} dollars holding on {date_start}.",
    "Let me know if there are events that are less than {price} dollars occurring on {date_start}.",
    "Let me know if there are events that are less than {price} dollars on {date_start}.",
    "Let me know if there are events holding on {date_start} that are less than {price} dollars.",
    "Let me know if there are events occurring on {date_start} that are less than {price} dollars.",
    "Let me know if there are events on {date_start} that are less than {price} dollars.",
    "Let me know if there are events that are around ${price} holding on {date_start}.",
    "Let me know if there are events that are around ${price} occurring on {date_start}.",
    "Let me know if there are events that are around ${price} on {date_start}.",
    "Let me know if there are events holding on {date_start} that are around ${price}.",
    "Let me know if there are events occurring on {date_start} that are around ${price}.",
    "Let me know if there are events on {date_start} that are around ${price}.",
    "Will there be events that cost less than {price} dollars holding on {date_start}?",
    "Will there be events that cost less than {price} dollars occurring on {date_start}?",
    "Will there be events that cost less than {price} dollars on {date_start}?",
    "Will there be events holding on {date_start} that cost less than {price} dollars?",
    "Will there be events occurring on {date_start} that cost less than {price} dollars?",
    "Will there be events on {date_start} that cost less than {price} dollars?",
    "Will there be events that cost around {price} dollars holding on {date_start}?",
    "Will there be events that cost around {price} dollars occurring on {date_start}?",
    "Will there be events that cost around {price} dollars on {date_start}?",
    "Will there be events holding on {date_start} that cost around {price} dollars?",
    "Will there be events occurring on {date_start} that cost around {price} dollars?",
    "Will there be events on {date_start} that cost around {price} dollars?",
    "Will there be events that cost ${price} holding on {date_start}?",
    "Will there be events that cost ${price} occurring on {date_start}?",
    "Will there be events that cost ${price} on {date_start}?",
    "Will there be events holding on {date_start} that cost ${price}?",
    "Will there be events occurring on {date_start} that cost ${price}?",
    "Will there be events on {date_start} that cost ${price}?"
]


inform_date_start_and_part_of_day_template = [
    "Tell me about events that are in {part_of_day} of {date_start}.",
    "Tell me about events that are on {date_start} in {part_of_day}.",
    "Tell me about events that are holding on {date_start} in {part_of_day}.",
    "Tell me about events that are occurring on {date_start} in {part_of_day}.",
    "Which events take place on {date_start} in the {part_of_day}.",
    "I would like to find an event holding on {date_start} that is in {part_of_day}.",
    "I would like to find an event on {date_start} that is in {part_of_day}.",
    "I would like to find an event occurring on {date_start} that is in {part_of_day}.",
    "What events are conducted on {date_start} in the {part_of_day}.",
    "What events are conducted on {date_start} at {part_of_day}.",
    "Will there be events that take place on {date_start} in {part_of_day}?",
    "I want to know the events that are available on {date_start} at {part_of_day}.",
    "I want to know the events that are available on {date_start} in the {part_of_day}.",
    "Can you recommend some events holding on {date_start} start at {part_of_day}?",
    "Can you recommend some events occurring on {date_start} start at {part_of_day}?",
    "Can you recommend some events on {date_start} start at {part_of_day}?",
    "Do you know any events on {date_start} begins in {part_of_day}?",
    "Do you know any events holding on {date_start} begins in {part_of_day}?",
    "Do you know any events occurring on {date_start} begins in {part_of_day}?",
    "Do you know any events take palce {date_start} begins in {part_of_day}?",
    "Do you have any suggestions on events holding on {date_start} in {part_of_day}?",
    "Do you have any suggestions on events occurring on {date_start} in {part_of_day}?",
    "I want to find some events holding on {date_start} in {part_of_day}.",
    "I want to find some events occuring on {date_start} in {part_of_day}.",
    "I want to find some events take place on {date_start} in {part_of_day}.",
    "I want to find some events on {date_start} in {part_of_day}."
]


inform_time_and_price_template = [
    "Do you know any free events at {time}?",
    "Do you know any free events around {time}?",
    "Tell me about some free events at {time}.",
    "Tell me about some free events around {time}.",
    "Tell me about some free events at around {time}.",
    "Can you recommend me some free events at {time}?",
    "Can you recommend me some free events around {time}?",
    "Do you have any suggestions for free events at {time}?",
    "Do you have any suggestions for free events at around {time}?",
    "Do you have any suggestions for free events around {time}?",
    "Are there any events around {price} SGD at {time}.",
    "Are there any events around {price} dollars, around {time}.",
    "Are there any events around {price} dollar at around {time}.",
    "Are there any events at {time} around {price} SGD.",
    "Are there any events around {time} around {price} dollars.",
    "Are there any events at around {time} around ${price}.",
    "Are there any events less than {price} SGD at {time}.",
    "Are there any events less than {price} dollars around {time}.",
    "Are there any events less than {price} dollar at around {time}.",
    "Are there any events at {time} less than {price} dollars.",
    "Are there any events around {time} less than {price} SGD.",
    "Are there any events at around {time} less than ${price}.",
    "Are there any events around ${price} at {time}.",
    "Are there any events around ${price} at around {time}.",
    "Are there any events at {time} around ${price}.",
    "Are there any events at around {time}, around ${price}.",
    "I would like to find an event that costs {price} dollars at {time}.",
    "I would like to find an event that costs {price} SGD around {time}.",
    "I would like to find an event that costs {price} dollar at around {time}.",
    "I would like to find an event beginning at {time} that costs {price} dollars.",
    "I would like to find an event holding at {time} that costs {price} dollar.",
    "I would like to find an event occurring at {time} that costs {price} SGD.",
    "I would like to find an event at {time} that costs ${price}.",
    "I would like to find an event around {time} that costs {price} dollars.",
    "I would like to find an event at around {time} that costs {price} dollars.",
    "I would like to find an event that costs ${price} holding at {time}.",
    "I would like to find an event that costs ${price} occurring at {time}.",
    "I would like to find an event that costs ${price} beginning at {time}.",
    "I would like to find an event that costs ${price} ad begins at {time}.",
    "I would like to find an event that costs ${price} at around {time}.",
    "I would like to find an event that costs ${price} around {time}.",
    "I would like to find an event at {time} that costs ${price}.",
    "I would like to find an event at around {time} that costs ${price}.",
    "I would like to find an event around {time} that costs ${price}.",
    "Let me know if there are events that are around {price} SGD holding at {time}.",
    "Let me know if there are events that are around {price} dollars occurring at {time}.",
    "Let me know if there are events that are around {price} dollar at {time}.",
    "Let me know if there are events that are around {price} dollar at around {time}.",
    "Let me know if there are events that are around {price} dollars around {time}.",
    "Let me know if there are events at {time} that are around {price} dollars.",
    "Let me know if there are events at around {time} that are around {price} SGD.",
    "Let me know if there are events around {time} that are around {price} dollars.",
    "Let me know if there are events that are less than {price} dollars at {time}.",
    "Let me know if there are events that are less than {price} SGD around {time}.",
    "Let me know if there are events that are less than {price} dollar at around {time}.",
    "Let me know if there are events at {time} that are less than {price} dollar.",
    "Let me know if there are events around {time} that are less than {price} dollar.",
    "Let me know if there are events at around {time} that are less than {price} SGD.",
    "Let me know if there are events holding around {time} that are less than {price} dollar.",
    "Let me know if there are events holding at around {time} that are less than {price} dollar.",
    "Let me know if there are events that are around ${price} holding at {time}.",
    "Let me know if there are events that are around ${price} holding at around {time}.",
    "Let me know if there are events that are around ${price} at {time}.",
    "Let me know if there are events that are around ${price} at around {time}.",
    "Let me know if there are events holding at {time} that are around ${price}.",
    "Let me know if there are events holding at around {time} that are around ${price}.",
    "Let me know if there are events at {time} that are around ${price}.",
    "Let me know if there are events at around {time} that are around ${price}.",
    "Will there be events that cost less than {price} SGD holding at {time}?",
    "Will there be events that cost less than {price} SGD occurring at {time}?",
    "Will there be events that cost less than {price} dollars at {time}?",
    "Will there be events that cost less than {price} dollars holding at around {time}?",
    "Will there be events holding at {time} that cost less than {price} SGD?",
    "Will there be events occurring at {time} that cost less than {price} SGD?",
    "Will there be events at {time} that cost less than {price} dollar?",
    "Will there be events holding at around {time} that cost less than {price} dollar?",
    "Will there be events beginning at around {time} that cost less than {price} dollars?",
    "Will there be events that cost around {price} dollars, holding at {time}?",
    "Will there be events that cost around {price} dollar, at {time}?",
    "Will there be events that cost around {price} SGD, occuring at {time}?",
    "Will there be events that cost around {price} dollar, at around {time}?",
    "Will there be events holding at {time} that cost around {price} dollars?",
    "Will there be events at {time} that cost around {price} dollars?",
    "Will there be events occuring at {time} that cost around {price} SGD?",
    "Will there be events at around {time} that cost around {price} SGD?",
    "Will there be events that cost ${price} holding at {time}?",
    "Will there be events that cost ${price} occuring at {time}?",
    "Will there be events that cost ${price} at {time}?",
    "Will there be events that cost ${price} holding at around {time}?",
    "Will there be events that cost ${price} begin at around {time}?"
]


inform_time_and_is_weekend_template = [
    "I would like to know about events that are around {time} on {is_weekend}.",
    "I would like to know about events on {is_weekend} that are around {time}.",
    "Are there any events that start at {time} on {is_weekend}?",
    "Are there any events on {is_weekend} that start at {time}?",
    "Tell me about events around {time} on {is_weekend}.",
    "Tell me about events on {is_weekend} around {time}.",
    "Will there be any events around {time} on {is_weekend}?",
    "Will there be any events on {is_weekend} around {time}?",
    "I want to know if there are events at {time} on {is_weekend}?",
    "I want to know if there are events on {is_weekend} at {time}?",
    "Do you know any events start at {time} on {is_weekend}?",
    "Do you know any events on {is_weekend} start at {time}?",
    "Can you recommend any event begins around {time} on {is_weekend}?",
    "Can you recommend any event on {is_weekend} begins around {time}?",
    "Can I know some events at around {time} on {is_weekend}?",
    "Can I know some events on {is_weekend} at around {time}?",
    "I would like to know about events holding around {time} on {is_weekend}.",
    "I would like to know about events holding on {is_weekend} around {time}.",
    "I would like to know about events occurring around {time} on {is_weekend}.",
    "I would like to know about events occurring on {is_weekend} around {time}.",
    "Tell me about events holding around {time} on {is_weekend}.",
    "Tell me about events holding on {is_weekend} around {time}.",
    "Tell me about events occurring around {time} on {is_weekend}.",
    "Tell me about events occurring on {is_weekend} around {time}.",
    "Will there be any events holding around {time} on {is_weekend}?",
    "Will there be any events holding on {is_weekend} around {time}?",
    "Will there be any events occurring around {time} on {is_weekend}?",
    "I want to know if there are events holding at {time} on {is_weekend}?",
    "I want to know if there are events holding on {is_weekend} at {time}?",
    "I want to know if there are events occurring at {time} on {is_weekend}?",
    "I want to know if there are events occurring on {is_weekend} at {time}?",
    "Can you recommend any event begins around {time} on {is_weekend}?",
    "Can you recommend any event on {is_weekend} begins around {time}?",
    "Can I know some events that begin at around {time} on {is_weekend}?",
    "Can I know some events on {is_weekend} that begin at around {time}?",
    "Can I know some events beginning at around {time} on {is_weekend}?",
    "Can I know some events on {is_weekend} beginning at around {time}?"
]


inform_price_and_is_weekend_template = [
    "Do you know any free events on {is_weekend}?",
    "Do you know any free events holding on {is_weekend}?",
    "Do you know any free events occurring on {is_weekend}?",
    "Do you know any free events taking place on {is_weekend}?",
    "Tell me about some free events on {is_weekend}.",
    "Tell me about some free events holding on {is_weekend}.",
    "Tell me about some free events occuring on {is_weekend}.",
    "Tell me about some free events that take place on {is_weekend}.",
    "Tell me about some free events taking place on {is_weekend}.",
    "Can you recommend me some free events taking place on {is_weekend}?",
    "Can you recommend me some free events that take place on {is_weekend}?",
    "Can you recommend me some free events holding on {is_weekend}?",
    "Can you recommend me some free events occurring on {is_weekend}?",
    "Can you recommend me some free events on {is_weekend}?",
    "Do you have any suggestions for free events occurring on {is_weekend}?",
    "Do you have any suggestions for free events holding on {is_weekend}?",
    "Do you have any suggestions for free events on {is_weekend}?",
    "Do you have any suggestions for free events taking place on {is_weekend}?",
    "Do you have any suggestions for free events that take place on {is_weekend}?",
    "Are there any events around {price} dollars taking place on {is_weekend}.",
    "Are there any events around {price} dollars holing on {is_weekend}.",
    "Are there any events around {price} dollars occuring on {is_weekend}.",
    "Are there any events around {price} dollars that take place on {is_weekend}.",
    "Are there any events dollars taking place on {is_weekend} around {price} SGD.",
    "Are there any events dollars holing on {is_weekend} around {price} SGD.",
    "Are there any events dollars occuring on {is_weekend} around {price} SGD.",
    "Are there any events dollars that take place on {is_weekend} around {price} SGD.",
    "Are there any events less than {price} dollars on {is_weekend}.",
    "Are there any events less than {price} dollars holding on {is_weekend}.",
    "Are there any events less than {price} dollars taking place on {is_weekend}.",
    "Are there any events less than {price} dollars occurring on {is_weekend}.",
    "Are there any events less than {price} dollars that take place on {is_weekend}.",
    "Are there any events on {is_weekend} that are less than {price} dollars.",
    "Are there any events holding on {is_weekend} that are less than {price} dollars.",
    "Are there any events taking place on {is_weekend} that are less than {price} dollars.",
    "Are there any events occurring on {is_weekend} that are less than {price} dollars.",
    "Are there any events around ${price} holding on {is_weekend}.",
    "Are there any events around ${price} occurring on {is_weekend}.",
    "Are there any events around ${price} on {is_weekend}.",
    "Are there any events around ${price} taking place on {is_weekend}.",
    "Are there any events holding on {is_weekend} that are around ${price}.",
    "Are there any events occurring on {is_weekend} that are around ${price}.",
    "Are there any events on {is_weekend} around ${price}.",
    "Are there any events taking place on {is_weekend} and are around ${price}.",
    "I would like to find an event that costs {price} dollars on {is_weekend}.",
    "I would like to find an event that costs {price} dollars holding on {is_weekend}.",
    "I would like to find an event that costs {price} dollars occurring on {is_weekend}.",
    "I would like to find an event that costs {price} dollars taking place on {is_weekend}.",
    "I would like to find an event on {is_weekend} that costs {price} dollars.",
    "I would like to find an event holding on {is_weekend} that costs {price} dollars.",
    "I would like to find an event occurring on {is_weekend} that costs {price} dollars.",
    "I would like to find an event taking place on {is_weekend} that costs {price} dollars.",
    "I would like to find an event that costs ${price} on {is_weekend}.",
    "I would like to find an event that costs ${price} holding on {is_weekend}.",
    "I would like to find an event that costs ${price} occurring on {is_weekend}.",
    "I would like to find an event that costs ${price} taking place on {is_weekend}.",
    "I would like to find an event on {is_weekend} that costs ${price}.",
    "I would like to find an event holding on {is_weekend} that costs ${price}.",
    "I would like to find an event occurring on {is_weekend} that costs ${price}.",
    "I would like to find an event taking place on {is_weekend} that costs ${price}.",
    "Let me know if there are events that are around {price} dollars on {is_weekend}.",
    "Let me know if there are events that are around {price} dollars holding on {is_weekend}.",
    "Let me know if there are events that are around {price} dollars occurring on {is_weekend}.",
    "Let me know if there are events that are around {price} dollars taking plae on {is_weekend}.",
    "Let me know if there are events on {is_weekend} that are around {price} dollars.",
    "Let me know if there are events holding on {is_weekend} that are around {price} dollars.",
    "Let me know if there are events occurring on {is_weekend} that are around {price} dollars.",
    "Let me know if there are events taking plae on {is_weekend} that are around {price} dollars.",
    "Let me know if there are events that are less than {price} dollars on {is_weekend}.",
    "Let me know if there are events that are less than {price} dollars holding on {is_weekend}.",
    "Let me know if there are events that are less than {price} dollars occurring on {is_weekend}.",
    "Let me know if there are events that are less than {price} dollars taking place on {is_weekend}.",
    "Let me know if there are events on {is_weekend} that are less than {price} dollars.",
    "Let me know if there are events holding on {is_weekend} that are less than {price} dollars.",
    "Let me know if there are events occurring on {is_weekend} that are less than {price} dollars.",
    "Let me know if there are events taking place on {is_weekend} that are less than {price} dollars.",
    "Let me know if there are events that are around ${price} on {is_weekend}.",
    "Let me know if there are events that are around ${price} holding on {is_weekend}.",
    "Let me know if there are events that are around ${price} occurring on {is_weekend}.",
    "Let me know if there are events that are around ${price} taking plcae on {is_weekend}.",
    "Let me know if there are events on {is_weekend} that are around ${price}.",
    "Let me know if there are events holding on {is_weekend} that are around ${price}.",
    "Let me know if there are events occurring on {is_weekend} that are around ${price}.",
    "Let me know if there are events taking plcae on {is_weekend} that are around ${price}.",
    "Will there be events that cost less than {price} dollars on {is_weekend}?",
    "Will there be events that cost less than {price} dollars holding on {is_weekend}?",
    "Will there be events that cost less than {price} dollars occurring on {is_weekend}?",
    "Will there be events that cost less than {price} dollars taking place on {is_weekend}?",
    "Will there be events on {is_weekend} that cost less than {price} dollars?",
    "Will there be events holding on {is_weekend} that cost less than {price} dollars?",
    "Will there be events occurring on {is_weekend} that cost less than {price} dollars?",
    "Will there be events taking place on {is_weekend} that cost less than {price} dollars?",
    "Will there be events that cost around {price} dollars on {is_weekend}?",
    "Will there be events that cost around {price} dollars holding on {is_weekend}?",
    "Will there be events that cost around {price} dollars occurring on {is_weekend}?",
    "Will there be events that cost around {price} dollars taking place on {is_weekend}?",
    "Will there be events on {is_weekend} that cost around {price} dollars?",
    "Will there be events holding on {is_weekend} that cost around {price} dollars?",
    "Will there be events occurring on {is_weekend} that cost around {price} dollars?",
    "Will there be events taking place on {is_weekend} that cost around {price} dollars?",
    "Will there be events that cost ${price} on {is_weekend}?",
    "Will there be events that cost ${price} holding on {is_weekend}?",
    "Will there be events that cost ${price} occurring on {is_weekend}?",
    "Will there be events that cost ${price} taking plcae on {is_weekend}?",
    "Will there be events on {is_weekend} that cost ${price}?",
    "Will there be events holding on {is_weekend} that cost ${price}?",
    "Will there be events occurring on {is_weekend} that cost ${price}?",
    "Will there be events taking plcae on {is_weekend} that cost ${price}?"
]


inform_price_and_part_of_day_template = [
    "Do you know any free events in the {part_of_day}?",
    "Do you know any free events holding in the {part_of_day}?",
    "Tell me about some free events in the {part_of_day}.",
    "Tell me about some free events occurring in the {part_of_day}.",
    "Can you recommend me some free events at {part_of_day}?",
    "Do you have any suggestions for free events in the {part_of_day}?",
    "Do you have any suggestions for free events holding in the {part_of_day}?",
    "Are there any events around {price} dollars in the {part_of_day}.",
    "Are there any events in the {part_of_day} which are around {price} dollars.",
    "Are there any events holding in the {part_of_day} which are around {price} dollars.",
    "Are there any events around {price} SGD at {part_of_day}.",
    "Are there any events at {part_of_day} around {price} SGD.",
    "Are there any events at {part_of_day} which are around {price} SGD.",
    "Are there any events less than {price} dollars in the {part_of_day}.",
    "Are there any events less than {price} dollars occurring in the {part_of_day}.",
    "Are there any events in the {part_of_day} which are less than {price} dollars.",
    "Are there any events occurring in the {part_of_day} which are less than {price} dollars.",
    "Are there any events less than {price} SGD holding in the {part_of_day}.",
    "Are there any events that hold in the {part_of_day} and are less than {price} SGD.",
    "Are there any events around ${price} in the {part_of_day}.",
    "Are there any events around ${price} holding in the {part_of_day}.",
    "I would like to find an event that costs {price} dollars at {part_of_day}.",
    "I would like to find an event holding at {part_of_day} that costs {price} dollars.",
    "I would like to find an event that costs {price} SGD and is in the {part_of_day}.",
    "I would like to find an event that is in the {part_of_day} and costs {price} SGD.",
    "I would like to find an event in the {part_of_day} that costs ${price}.",
    "I would like to find an event at {part_of_day} that costs ${price}.",
    "Let me know if there are events that are around {price} dollars in the {part_of_day}.",
    "Let me know if there are events in the {part_of_day} that are around {price} dollars.",
    "Let me know if there are events occurring in the {part_of_day} that are around {price} dollars.",
    "Let me know if there are events holding in the {part_of_day} that are around {price} dollars.",
    "Let me know if there are events taking place in the {part_of_day} that are around {price} dollars.",
    "Let me know if there are events taking place at {part_of_day} that are around {price} SGD.",
    "Let me know if there are events holding at {part_of_day} that are around {price} SGD.",
    "Let me know if there are events at {part_of_day} that are around {price} SGD.",
    "Let me know if there are events that are less than {price} dollars in the {part_of_day}.",
    "Let me know if there are events in the {part_of_day} that are less than {price} dollars.",
    "Let me know if there are events holding in the {part_of_day} that are less than {price} dollars.",
    "Let me know if there are events occurring in the {part_of_day} that are less than {price} dollars.",
    "Let me know if there are events in the {part_of_day} that are less than {price} SGD.",
    "Let me know if there are events taking place in the {part_of_day} that are less than {price} SGD.",
    "Let me know if there are events less than {price} SGD that are taking place in the {part_of_day}.",
    "Let me know if there are events less than {price} SGD that are holding in the {part_of_day}.",
    "Let me know if there are events that are around ${price} at {part_of_day}.",
    "Let me know if there are events at {part_of_day} that are around ${price}.",
    "Let me know if there are events that are around {price} SGD in the {part_of_day}.",
    "Let me know if there are events in the {part_of_day} that are around {price} SGD.",
    "Will there be events that cost less than {price} dollars in the {part_of_day}?",
    "Will there be events in the {part_of_day} that cost less than {price} dollars?",
    "Will there be events holding in the {part_of_day} that cost less than {price} dollars?",
    "Will there be events occurring in the {part_of_day} that cost less than {price} dollars?",
    "Will there be events that cost less than {price} SGD in the {part_of_day}?",
    "Will there be events in the {part_of_day} that cost less than {price} SGD?",
    "Will there be events taking place in the {part_of_day} that cost less than {price} SGD?",
    "Will there be events that cost around {price} dollars in the {part_of_day}?",
    "Will there be events in the {part_of_day} that cost around {price} dollars?",
    "Will there be events at {part_of_day} that cost around {price} dollars?",
    "Will there be events that cost around {price} SGD at {part_of_day}?",
    "Will there be events at {part_of_day} that cost around {price} SGD?",
    "Will there be events that cost ${price} holding in the {part_of_day}?",
    "Will there be events holding in the {part_of_day} that cost ${price}?",
    "Will there be events that cost {price} SGD at {part_of_day}?",
    "Will there be events at {part_of_day} that cost {price} SGD?",
    "Will there be events holding at {part_of_day} that cost {price} SGD?"
]


inform_is_weekend_and_part_of_day_template = [
    "Tell me about events that on {is_weekend} in the {part_of_day}.",
    "Tell me about events that on {is_weekend} {part_of_day}.",
    "Tell me about {part_of_day} events that on {is_weekend}.",
    "Tell me about events in the {part_of_day} of {is_weekend}.",
    "Which events take place on {is_weekend} in the {part_of_day}.",
    "Which events take place on {is_weekend} {part_of_day}.",
    "Which {part_of_day} events take place on {is_weekend}.",
    "Which events take place in the {part_of_day} of a {is_weekend}.",
    "I would like to find an event that is on {is_weekend} {part_of_day}.",
    "I would like to find an {part_of_day} event that is on {is_weekend}.",
    "I would like to find an event in the {part_of_day} that is on {is_weekend}.",
    "I would like to find an event in the {part_of_day} of a {is_weekend}.",
    "What events are conducted on {is_weekend} {part_of_day}.",
    "What {part_of_day} events are conducted on {is_weekend}.",
    "What events are conducted in the {part_of_day} of a {is_weekend}.",
    "Will there be events that take place on {is_weekend} {part_of_day}?",
    "Will there be {part_of_day} events that take place on {is_weekend}?",
    "Will there be events that take place at {part_of_day} of a {is_weekend}?",
    "I want to know the events that are available on {is_weekend} {part_of_day}.",
    "I want to know the {part_of_day} events that are available on {is_weekend}.",
    "I want to know the {part_of_day} events that are available on {is_weekend}.",
    "Can you recommend some events on {is_weekend} {part_of_day}?",
    "Can you recommend some {part_of_day} events on {is_weekend}?",
    "Can you recommend some events in the {part_of_day} of a {is_weekend}?",
    "Do you have any suggestions on events on {is_weekend} {part_of_day}?",
    "Do you have any suggestions on {part_of_day} events on {is_weekend}?",
    "I want to find some events on {is_weekend} {part_of_day}.",
    "I want to find some {part_of_day} events on {is_weekend}."
]


file_1 = open('IOB_training.txt', 'w')
file_2 = open('User_intent.txt', 'a+')

count = 0
################## inform 1 slot ###############
for venue_name in sample_venue_name:
    for template in inform_venue_name_template:
        template = template.replace('.', '').replace('?', '').replace(',', '')
        token_list = list(filter(None, template.split(' ')))
        sentence = template.format(venue_name)
        label_list = ['O' for i in range(len(token_list)-1)]
        index = token_list.index("{}")
        label_list.insert(index, inform_venue_name_tag[0])
        for i in range(len(list(filter(None, sentence.split(' ')))) - len(label_list)):
            label_list.insert(index + 1, inform_venue_name_tag[1])
        if len(label_list) != len(sentence.split()):
            print(sentence)
            print(' '.join(label_list))
        else:
            count += 1
            file_1.write(sentence + '\n')
            file_1.write(' '.join(label_list) + '\n')
            file_2.write(sentence + '\n')
            file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')

for region in sample_region:
    for template in inform_region_template:
        template = template.replace('.', '').replace('?', '').replace(',', '')
        token_list = list(filter(None, template.split(' ')))
        sentence = template.format(region)
        label_list = ['O' for i in range(len(token_list)-1)]
        index = token_list.index("{}")
        label_list.insert(index, inform_region_tag[0])
        for i in range(len(list(filter(None, sentence.split(' ')))) - len(label_list)):
            label_list.insert(index + 1, inform_region_tag[1])
        if len(label_list) != len(sentence.split()):
            print(sentence)
            print(' '.join(label_list))
        else:
            count += 1
            file_1.write(sentence + '\n')
            file_1.write(' '.join(label_list) + '\n')
            file_2.write(sentence + '\n')
            file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
        
for event_host in sample_event_host:
    for template in inform_event_host_template:
        template = template.replace('.', '').replace('?', '').replace(',', '')
        token_list = list(filter(None, template.split(' ')))
        sentence = template.format(event_host)
        label_list = ['O' for i in range(len(token_list)-1)]
        index = token_list.index("{}")
        label_list.insert(index, inform_event_host_tag[0])
        for i in range(len(list(filter(None, sentence.split(' ')))) - len(label_list)):
            label_list.insert(index + 1, inform_event_host_tag[1])
        if len(label_list) != len(sentence.split()):
            print(sentence)
            print(' '.join(label_list))
        else:
            count += 1
            file_1.write(sentence + '\n')
            file_1.write(' '.join(label_list) + '\n')
            file_2.write(sentence + '\n')
            file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')

for date_start in sample_date_start:
    for template in inform_date_start_template:
        template = template.replace('.', '').replace('?', '').replace(',', '')
        token_list = list(filter(None, template.split(' ')))
        sentence = template.format(date_start)
        label_list = ['O' for i in range(len(token_list)-1)]
        index = token_list.index("{}")
        label_list.insert(index, inform_date_start_tag[0])
        for i in range(len(list(filter(None, sentence.split(' ')))) - len(label_list)):
            label_list.insert(index + 1, inform_date_start_tag[1])
        if len(label_list) != len(sentence.split()):
            print(sentence)
            print(' '.join(label_list))
        else:
            count += 1
            file_1.write(sentence + '\n')
            file_1.write(' '.join(label_list) + '\n')
            file_2.write(sentence + '\n')
            file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
        
for time in sample_time:
    for template in inform_time_template:
        template = template.replace('.', '').replace('?', '').replace(',', '')
        token_list = list(filter(None, template.split(' ')))
        sentence = template.format(time)
        label_list = ['O' for i in range(len(token_list)-1)]
        index = token_list.index("{}")
        label_list.insert(index, inform_time_tag[0])
        for i in range(len(list(filter(None, sentence.split(' ')))) - len(label_list)):
            label_list.insert(index + 1, inform_time_tag[1])
        if len(label_list) != len(sentence.split()):
            print(sentence)
            print(' '.join(label_list))
        else:
            count += 1
            file_1.write(sentence + '\n')
            file_1.write(' '.join(label_list) + '\n')
            file_2.write(sentence + '\n')
            file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
        
for price in sample_price:
    for template in inform_price_template:
        template = template.replace('.', '').replace('?', '').replace(',', '')
        token_list = list(filter(None, template.split(' ')))
        sentence = template.format(price)
        label_list = ['O' for i in range(len(token_list)-1)]
        try:
            index = token_list.index("{}")
        except:
            try:
                index = token_list.index("${}")
            except:
                index = token_list.index("free")
        label_list.insert(index, inform_price_tag[0])
        for i in range(len(list(filter(None, sentence.split(' ')))) - len(label_list)):
            label_list.insert(index + 1, inform_price_tag[1])
        if len(label_list) != len(sentence.split()):
            print(sentence)
            print(' '.join(label_list))
        else:
            count += 1
            file_1.write(sentence + '\n')
            file_1.write(' '.join(label_list) + '\n')
            file_2.write(sentence + '\n')
            file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
        
for is_weekend in sample_is_weekend:
    for template in inform_is_weekend_template:
        template = template.replace('.', '').replace('?', '').replace(',', '')
        token_list = list(filter(None, template.split(' ')))
        sentence = template.format(is_weekend)
        label_list = ['O' for i in range(len(token_list)-1)]
        index = token_list.index("{}")
        label_list.insert(index, inform_is_weekend_tag[0])
        for i in range(len(list(filter(None, sentence.split(' ')))) - len(label_list)):
            label_list.insert(index + 1, inform_is_weekend_tag[1])
        if len(label_list) != len(sentence.split()):
            print(sentence)
            print(' '.join(label_list))
        else:
            count += 1
            file_1.write(sentence + '\n')
            file_1.write(' '.join(label_list) + '\n')
            file_2.write(sentence + '\n')
            file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
        
for part_of_day in sample_part_of_day:
    for template in inform_part_of_day_template:
        template = template.replace('.', '').replace('?', '').replace(',', '')
        token_list = list(filter(None, template.split(' ')))
        sentence = template.format(part_of_day)
        label_list = ['O' for i in range(len(token_list)-1)]
        index = token_list.index("{}")
        label_list.insert(index, inform_part_of_day_tag[0])
        for i in range(len(list(filter(None, sentence.split(' ')))) - len(label_list)):
            label_list.insert(index + 1, inform_part_of_day_tag[1])
        if len(label_list) != len(sentence.split()):
            print(sentence)
            print(' '.join(label_list))
        else:
            count += 1
            file_1.write(sentence + '\n')
            file_1.write(' '.join(label_list) + '\n')
            file_2.write(sentence + '\n')
            file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')

################## inform 2 slots ###############
for venue_name in sample_venue_name:
    for region in sample_region:
        for template in inform_venue_name_and_region_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(venue_name = venue_name, region = region)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_venue_name = token_list.index("{venue_name}")
            label_list.insert(index_venue_name, inform_venue_name_tag[0])
            for i in range(len(list(filter(None, venue_name.split(' '))))-1):
                label_list.insert(index_venue_name+1, inform_venue_name_tag[1])

            token_list = template.format(venue_name = venue_name, region = "{region}").split(' ')
            index_region = token_list.index("{region}")
            label_list.insert(index_region, inform_region_tag[0])
            for i in range(len(list(filter(None, region.split(' ')))) - 1):
                label_list.insert(index_region + 1, inform_region_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for venue_name in sample_venue_name:
    for event_host in sample_event_host:
        for template in inform_venue_name_and_event_host_template:
            template = template.replace('.', '').replace('?', '').replace(',', '').replace('-','')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(venue_name = venue_name, event_host = event_host)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_venue_name = token_list.index("{venue_name}")
            label_list.insert(index_venue_name, inform_venue_name_tag[0])
            for i in range(len(list(filter(None, venue_name.split(' '))))-1):
                label_list.insert(index_venue_name+1, inform_venue_name_tag[1])

            token_list = template.format(venue_name = venue_name, event_host = "{event_host}").split(' ')
            index_event_host = token_list.index("{event_host}")
            label_list.insert(index_event_host, inform_event_host_tag[0])
            for i in range(len(list(filter(None, event_host.split(' ')))) - 1):
                label_list.insert(index_event_host + 1, inform_event_host_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for venue_name in sample_venue_name:
    for date_start in sample_date_start:
        for template in inform_venue_name_and_date_start_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(venue_name = venue_name, date_start = date_start)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_venue_name = token_list.index("{venue_name}")
            label_list.insert(index_venue_name, inform_venue_name_tag[0])
            for i in range(len(list(filter(None, venue_name.split(' '))))-1):
                label_list.insert(index_venue_name+1, inform_venue_name_tag[1])

            token_list = template.format(venue_name = venue_name, date_start = "{date_start}").split(' ')
            index_date_start = token_list.index("{date_start}")
            label_list.insert(index_date_start, inform_date_start_tag[0])
            for i in range(len(list(filter(None, date_start.split(' ')))) - 1):
                label_list.insert(index_date_start + 1, inform_date_start_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')

for venue_name in sample_venue_name:
    for time in sample_time:
        for template in inform_venue_name_and_time_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(venue_name = venue_name, time = time)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_venue_name = token_list.index("{venue_name}")
            label_list.insert(index_venue_name, inform_venue_name_tag[0])
            for i in range(len(list(filter(None, venue_name.split(' '))))-1):
                label_list.insert(index_venue_name+1, inform_venue_name_tag[1])

            token_list = template.format(venue_name = venue_name, time = "{time}").split(' ')
            index_time = token_list.index("{time}")
            label_list.insert(index_time, inform_time_tag[0])
            for i in range(len(list(filter(None, time.split(' ')))) - 1):
                label_list.insert(index_time + 1, inform_time_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for venue_name in sample_venue_name:
    for price in sample_price:
        for template in inform_venue_name_and_price_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(venue_name = venue_name, price = price)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_venue_name = token_list.index("{venue_name}")
            label_list.insert(index_venue_name, inform_venue_name_tag[0])
            for i in range(len(list(filter(None, venue_name.split(' '))))-1):
                label_list.insert(index_venue_name+1, inform_venue_name_tag[1])

            token_list = template.format(venue_name = venue_name, price = "{price}").split(' ')
            try:
                index_price = token_list.index("{price}")
            except:
                try:
                    index_price = token_list.index("${price}")
                except:
                    index_price = token_list.index("free")
            label_list.insert(index_price, inform_price_tag[0])
            for i in range(len(list(filter(None, price.split(' ')))) - 1):
                label_list.insert(index_price + 1, inform_price_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')

for venue_name in sample_venue_name:
    for is_weekend in sample_is_weekend:
        for template in inform_venue_name_and_is_weekend_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(venue_name = venue_name, is_weekend = is_weekend)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_venue_name = token_list.index("{venue_name}")
            label_list.insert(index_venue_name, inform_venue_name_tag[0])
            for i in range(len(list(filter(None, venue_name.split(' '))))-1):
                label_list.insert(index_venue_name+1, inform_venue_name_tag[1])

            token_list = template.format(venue_name = venue_name, is_weekend = "{is_weekend}").split(' ')
            index_is_weekend = token_list.index("{is_weekend}")
            label_list.insert(index_is_weekend, inform_is_weekend_tag[0])
            for i in range(len(list(filter(None, is_weekend.split(' ')))) - 1):
                label_list.insert(index_is_weekend + 1, inform_is_weekend_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for venue_name in sample_venue_name:
    for part_of_day in sample_part_of_day:
        for template in inform_venue_name_and_part_of_day_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(venue_name = venue_name, part_of_day = part_of_day)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_venue_name = token_list.index("{venue_name}")
            label_list.insert(index_venue_name, inform_venue_name_tag[0])
            for i in range(len(list(filter(None, venue_name.split(' '))))-1):
                label_list.insert(index_venue_name+1, inform_venue_name_tag[1])

            token_list = template.format(venue_name = venue_name, part_of_day = "{part_of_day}").split(' ')
            index_part_of_day = token_list.index("{part_of_day}")
            label_list.insert(index_part_of_day, inform_part_of_day_tag[0])
            for i in range(len(list(filter(None, part_of_day.split(' ')))) - 1):
                label_list.insert(index_part_of_day + 1, inform_part_of_day_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for region in sample_region:
    for event_host in sample_event_host:
        for template in inform_region_and_event_host_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(region = region, event_host = event_host)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_region = token_list.index("{region}")
            label_list.insert(index_region, inform_region_tag[0])
            for i in range(len(list(filter(None, region.split(' '))))-1):
                label_list.insert(index_region+1, inform_region_tag[1])

            token_list = template.format(region = region, event_host = "{event_host}").split(' ')
            index_event_host = token_list.index("{event_host}")
            label_list.insert(index_event_host, inform_event_host_tag[0])
            for i in range(len(list(filter(None, event_host.split(' ')))) - 1):
                label_list.insert(index_event_host + 1, inform_event_host_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
    
for region in sample_region:
    for date_start in sample_date_start:
        for template in inform_region_and_date_start_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(region = region, date_start = date_start)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_region = token_list.index("{region}")
            label_list.insert(index_region, inform_region_tag[0])
            for i in range(len(list(filter(None, region.split(' '))))-1):
                label_list.insert(index_region+1, inform_region_tag[1])

            token_list = template.format(region = region, date_start = "{date_start}").split(' ')
            index_date_start = token_list.index("{date_start}")
            label_list.insert(index_date_start, inform_date_start_tag[0])
            for i in range(len(list(filter(None, date_start.split(' ')))) - 1):
                label_list.insert(index_date_start + 1, inform_date_start_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for region in sample_region:
    for time in sample_time:
        for template in inform_region_and_time_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(region = region, time = time)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_region = token_list.index("{region}")
            label_list.insert(index_region, inform_region_tag[0])
            for i in range(len(list(filter(None, region.split(' '))))-1):
                label_list.insert(index_region+1, inform_region_tag[1])

            token_list = template.format(region = region, time = "{time}").split(' ')
            index_time = token_list.index("{time}")
            label_list.insert(index_time, inform_time_tag[0])
            for i in range(len(list(filter(None, time.split(' ')))) - 1):
                label_list.insert(index_time + 1, inform_time_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for region in sample_region:
    for price in sample_price:
        for template in inform_region_and_price_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(region = region, price = price)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_region = token_list.index("{region}")
            label_list.insert(index_region, inform_region_tag[0])
            for i in range(len(list(filter(None, region.split(' '))))-1):
                label_list.insert(index_region+1, inform_region_tag[1])

            token_list = template.format(region = region, price = "{price}").split(' ')
            try:
                index_price = token_list.index("{price}")
            except:
                try:
                    index_price = token_list.index("${price}")
                except:
                    index_price = token_list.index("free")
            label_list.insert(index_price, inform_price_tag[0])
            for i in range(len(list(filter(None, price.split(' ')))) - 1):
                label_list.insert(index_price + 1, inform_price_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for region in sample_region:
    for is_weekend in sample_is_weekend:
        for template in inform_region_and_is_weekend_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(region = region, is_weekend = is_weekend)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_region = token_list.index("{region}")
            label_list.insert(index_region, inform_region_tag[0])
            for i in range(len(list(filter(None, region.split(' '))))-1):
                label_list.insert(index_region+1, inform_region_tag[1])

            token_list = template.format(region = region, is_weekend = "{is_weekend}").split(' ')
            index_is_weekend = token_list.index("{is_weekend}")
            label_list.insert(index_is_weekend, inform_is_weekend_tag[0])
            for i in range(len(list(filter(None, is_weekend.split(' ')))) - 1):
                label_list.insert(index_is_weekend + 1, inform_is_weekend_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for region in sample_region:
    for part_of_day in sample_part_of_day:
        for template in inform_region_and_part_of_day_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(region = region, part_of_day = part_of_day)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_region = token_list.index("{region}")
            label_list.insert(index_region, inform_region_tag[0])
            for i in range(len(list(filter(None, region.split(' '))))-1):
                label_list.insert(index_region+1, inform_region_tag[1])

            token_list = template.format(region = region, part_of_day = "{part_of_day}").split(' ')
            index_part_of_day = token_list.index("{part_of_day}")
            label_list.insert(index_part_of_day, inform_part_of_day_tag[0])
            for i in range(len(list(filter(None, part_of_day.split(' ')))) - 1):
                label_list.insert(index_part_of_day + 1, inform_part_of_day_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
     
for event_host in sample_event_host:
    for date_start in sample_date_start:
        for template in inform_event_host_and_date_start_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(event_host = event_host, date_start = date_start)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_event_host = token_list.index("{event_host}")
            label_list.insert(index_event_host, inform_event_host_tag[0])
            for i in range(len(list(filter(None, event_host.split(' '))))-1):
                label_list.insert(index_event_host+1, inform_event_host_tag[1])

            token_list = template.format(event_host = event_host, date_start = "{date_start}").split(' ')
            index_date_start = token_list.index("{date_start}")
            label_list.insert(index_date_start, inform_date_start_tag[0])
            for i in range(len(list(filter(None, date_start.split(' ')))) - 1):
                label_list.insert(index_date_start + 1, inform_date_start_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for event_host in sample_event_host:
    for time in sample_time:
        for template in inform_event_host_and_time_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(event_host = event_host, time = time)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_event_host = token_list.index("{event_host}")
            label_list.insert(index_event_host, inform_event_host_tag[0])
            for i in range(len(list(filter(None, event_host.split(' '))))-1):
                label_list.insert(index_event_host+1, inform_event_host_tag[1])

            token_list = template.format(event_host = event_host, time = "{time}").split(' ')
            index_time = token_list.index("{time}")
            label_list.insert(index_time, inform_time_tag[0])
            for i in range(len(list(filter(None, time.split(' ')))) - 1):
                label_list.insert(index_time + 1, inform_time_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for event_host in sample_event_host:
    for price in sample_price:
        for template in inform_event_host_and_price_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(event_host = event_host, price = price)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_event_host = token_list.index("{event_host}")
            label_list.insert(index_event_host, inform_event_host_tag[0])
            for i in range(len(list(filter(None, event_host.split(' '))))-1):
                label_list.insert(index_event_host+1, inform_event_host_tag[1])

            token_list = template.format(event_host = event_host, price = "{price}").split(' ')
            try:
                index_price = token_list.index("{price}")
            except:
                try:
                    index_price = token_list.index("${price}")
                except:
                    index_price = token_list.index("free")
            label_list.insert(index_price, inform_price_tag[0])
            for i in range(len(list(filter(None, price.split(' ')))) - 1):
                label_list.insert(index_price + 1, inform_price_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for event_host in sample_event_host:
    for is_weekend in sample_is_weekend:
        for template in inform_event_host_and_is_weekend_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(event_host = event_host, is_weekend = is_weekend)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_event_host = token_list.index("{event_host}")
            label_list.insert(index_event_host, inform_event_host_tag[0])
            for i in range(len(list(filter(None, event_host.split(' '))))-1):
                label_list.insert(index_event_host+1, inform_event_host_tag[1])

            token_list = template.format(event_host = event_host, is_weekend = "{is_weekend}").split(' ')
            index_is_weekend = token_list.index("{is_weekend}")
            label_list.insert(index_is_weekend, inform_is_weekend_tag[0])
            for i in range(len(list(filter(None, is_weekend.split(' ')))) - 1):
                label_list.insert(index_is_weekend + 1, inform_is_weekend_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
     
for event_host in sample_event_host:
    for part_of_day in sample_part_of_day:
        for template in inform_event_host_and_part_of_day_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(event_host = event_host, part_of_day = part_of_day)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_event_host = token_list.index("{event_host}")
            label_list.insert(index_event_host, inform_event_host_tag[0])
            for i in range(len(list(filter(None, event_host.split(' '))))-1):
                label_list.insert(index_event_host+1, inform_event_host_tag[1])

            token_list = template.format(event_host = event_host, part_of_day = "{part_of_day}").split(' ')
            index_part_of_day = token_list.index("{part_of_day}")
            label_list.insert(index_part_of_day, inform_part_of_day_tag[0])
            for i in range(len(list(filter(None, part_of_day.split(' ')))) - 1):
                label_list.insert(index_part_of_day + 1, inform_part_of_day_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for date_start in sample_date_start:
    for time in sample_time:
        for template in inform_date_start_and_time_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(date_start = date_start, time = time)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_date_start = token_list.index("{date_start}")
            label_list.insert(index_date_start, inform_date_start_tag[0])
            for i in range(len(list(filter(None, date_start.split(' '))))-1):
                label_list.insert(index_date_start+1, inform_date_start_tag[1])

            token_list = template.format(date_start = date_start, time = "{time}").split(' ')
            index_time = token_list.index("{time}")
            label_list.insert(index_time, inform_time_tag[0])
            for i in range(len(list(filter(None, time.split(' ')))) - 1):
                label_list.insert(index_time + 1, inform_time_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for date_start in sample_date_start:
    for price in sample_price:
        for template in inform_date_start_and_price_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(date_start = date_start, price = price)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_date_start = token_list.index("{date_start}")
            label_list.insert(index_date_start, inform_date_start_tag[0])
            for i in range(len(list(filter(None, date_start.split(' '))))-1):
                label_list.insert(index_date_start+1, inform_date_start_tag[1])

            token_list = template.format(date_start = date_start, price = "{price}").split(' ')
            try:
                index_price = token_list.index("{price}")
            except:
                try:
                    index_price = token_list.index("${price}")
                except:
                    index_price = token_list.index("free")
            label_list.insert(index_price, inform_price_tag[0])
            for i in range(len(list(filter(None, price.split(' ')))) - 1):
                label_list.insert(index_price + 1, inform_price_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for date_start in sample_date_start:
    for part_of_day in sample_part_of_day:
        for template in inform_date_start_and_part_of_day_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(date_start = date_start, part_of_day = part_of_day)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_date_start = token_list.index("{date_start}")
            label_list.insert(index_date_start, inform_date_start_tag[0])
            for i in range(len(list(filter(None, date_start.split(' '))))-1):
                label_list.insert(index_date_start+1, inform_date_start_tag[1])

            token_list = template.format(date_start = date_start, part_of_day = "{part_of_day}").split(' ')
            index_part_of_day = token_list.index("{part_of_day}")
            label_list.insert(index_part_of_day, inform_part_of_day_tag[0])
            for i in range(len(list(filter(None, part_of_day.split(' ')))) - 1):
                label_list.insert(index_part_of_day + 1, inform_part_of_day_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for time in sample_time:
    for price in sample_price:
        for template in inform_time_and_price_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(time = time, price = price)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_time = token_list.index("{time}")
            label_list.insert(index_time, inform_time_tag[0])
            for i in range(len(list(filter(None, time.split(' '))))-1):
                label_list.insert(index_time+1, inform_time_tag[1])

            token_list = template.format(time = time, price = "{price}").split(' ')
            try:
                index_price = token_list.index("{price}")
            except:
                try:
                    index_price = token_list.index("${price}")
                except:
                    index_price = token_list.index("free")
            label_list.insert(index_price, inform_price_tag[0])
            for i in range(len(list(filter(None, price.split(' ')))) - 1):
                label_list.insert(index_price + 1, inform_price_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for time in sample_time:
    for is_weekend in sample_is_weekend:
        for template in inform_time_and_is_weekend_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(time = time, is_weekend = is_weekend)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_time = token_list.index("{time}")
            label_list.insert(index_time, inform_time_tag[0])
            for i in range(len(list(filter(None, time.split(' '))))-1):
                label_list.insert(index_time+1, inform_time_tag[1])

            token_list = template.format(time = time, is_weekend = "{is_weekend}").split(' ')
            index_is_weekend = token_list.index("{is_weekend}")
            label_list.insert(index_is_weekend, inform_is_weekend_tag[0])
            for i in range(len(list(filter(None, is_weekend.split(' ')))) - 1):
                label_list.insert(index_is_weekend + 1, inform_is_weekend_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for price in sample_price:
    for is_weekend in sample_is_weekend:
        for template in inform_price_and_is_weekend_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(price = price, is_weekend = is_weekend)
            label_list = ['O' for i in range(len(token_list) - 2)]

            try:
                index_price = token_list.index("{price}")
            except:
                try:
                    index_price = token_list.index("${price}")
                except:
                    index_price = token_list.index("free")
            label_list.insert(index_price, inform_price_tag[0])
            for i in range(len(list(filter(None, price.split(' '))))-1):
                label_list.insert(index_price+1, inform_price_tag[1])

            token_list = template.format(price = price, is_weekend = "{is_weekend}").split(' ')
            index_is_weekend = token_list.index("{is_weekend}")
            label_list.insert(index_is_weekend, inform_is_weekend_tag[0])
            for i in range(len(list(filter(None, is_weekend.split(' ')))) - 1):
                label_list.insert(index_is_weekend + 1, inform_is_weekend_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for price in sample_price:
    for part_of_day in sample_part_of_day:
        for template in inform_price_and_part_of_day_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(price = price, part_of_day = part_of_day)
            label_list = ['O' for i in range(len(token_list) - 2)]

            try:
                index_price = token_list.index("{price}")
            except:
                try:
                    index_price = token_list.index("${price}")
                except:
                    index_price = token_list.index("free")
            label_list.insert(index_price, inform_price_tag[0])
            for i in range(len(list(filter(None, price.split(' '))))-1):
                label_list.insert(index_price+1, inform_price_tag[1])

            token_list = template.format(price = price, part_of_day = "{part_of_day}").split(' ')
            index_part_of_day = token_list.index("{part_of_day}")
            label_list.insert(index_part_of_day, inform_part_of_day_tag[0])
            for i in range(len(list(filter(None, part_of_day.split(' ')))) - 1):
                label_list.insert(index_part_of_day + 1, inform_part_of_day_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
for is_weekend in sample_is_weekend:
    for part_of_day in sample_part_of_day:
        for template in inform_is_weekend_and_part_of_day_template:
            template = template.replace('.', '').replace('?', '').replace(',', '')
            token_list = list(filter(None, template.split(' ')))
            sentence = template.format(is_weekend = is_weekend, part_of_day = part_of_day)
            label_list = ['O' for i in range(len(token_list) - 2)]

            index_is_weekend = token_list.index("{is_weekend}")
            label_list.insert(index_is_weekend, inform_is_weekend_tag[0])
            for i in range(len(list(filter(None, is_weekend.split(' '))))-1):
                label_list.insert(index_is_weekend+1, inform_is_weekend_tag[1])

            token_list = template.format(is_weekend = is_weekend, part_of_day = "{part_of_day}").split(' ')
            index_part_of_day = token_list.index("{part_of_day}")
            label_list.insert(index_part_of_day, inform_part_of_day_tag[0])
            for i in range(len(list(filter(None, part_of_day.split(' ')))) - 1):
                label_list.insert(index_part_of_day + 1, inform_part_of_day_tag[1])

            if len(label_list) != len(sentence.split()):
                print(sentence)
                print(' '.join(label_list))
            else:
                count += 1
                file_1.write(sentence + '\n')
                file_1.write(' '.join(label_list) + '\n')
                file_2.write(sentence + '\n')
                file_2.write(str(dialog_config.DIALOG_ACT['INFORM']) + '\n')
            
file_1.close()
file_2.close()
print(count)