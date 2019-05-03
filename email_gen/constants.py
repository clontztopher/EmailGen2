"""
---------------------
    TREC CONSTANTS
---------------------
"""

# County Codes field based on TREC/TALCB counties
# https://www.trec.texas.gov/sites/default/files/high-value-data-sets/county.txt
TREC_COUNTY_CODES = {
    "001": "ANDERSON",
    "002": "ANDREWS",
    "003": "ANGELINA",
    "004": "ARANSAS",
    "005": "ARCHER",
    "006": "ARMSTRONG",
    "007": "ATASCOSA",
    "008": "AUSTIN",
    "009": "BAILEY",
    "010": "BANDERA",
    "011": "BASTROP",
    "012": "BAYLOR",
    "013": "BEE",
    "014": "BELL",
    "015": "BEXAR",
    "016": "BLANCO",
    "017": "BORDEN",
    "018": "BOSQUE",
    "019": "BOWIE",
    "020": "BRAZORIA",
    "021": "BRAZOS",
    "022": "BREWSTER",
    "023": "BRISCOE",
    "024": "BROOKS",
    "025": "BROWN",
    "026": "BURLESON",
    "027": "BURNET",
    "028": "CALDWELL",
    "029": "CALHOUN",
    "030": "CALLAHAN",
    "031": "CAMERON",
    "032": "CAMP",
    "033": "CARSON",
    "034": "CASS",
    "035": "CASTRO",
    "036": "CHAMBERS",
    "037": "CHEROKEE",
    "038": "CHILDRESS",
    "039": "CLAY",
    "040": "COCHRAN",
    "041": "COKE",
    "042": "COLEMAN",
    "043": "COLLIN",
    "044": "COLLINGSWORTH",
    "045": "COLORADO",
    "046": "COMAL",
    "047": "COMANCHE",
    "048": "CONCHO",
    "049": "COOKE",
    "050": "CORYELL",
    "051": "COTTLE",
    "052": "CRANE",
    "053": "CROCKETT",
    "054": "CROSBY",
    "055": "CULBERSON",
    "056": "DALLAM",
    "057": "DALLAS",
    "058": "DAWSON",
    "059": "DEAF",
    "060": "DELTA",
    "061": "DENTON",
    "062": "DEWITT",
    "063": "DICKENS",
    "064": "DIMMIT",
    "065": "DONLEY",
    "066": "DUVAL",
    "067": "EASTLAND",
    "068": "ECTOR",
    "069": "EDWARDS",
    "070": "ELLIS",
    "071": "EL",
    "072": "ERATH",
    "073": "FALLS",
    "074": "FANNIN",
    "075": "FAYETTE",
    "076": "FISHER",
    "077": "FLOYD",
    "078": "FOARD",
    "079": "FORT",
    "080": "FRANKLIN",
    "081": "FREESTONE",
    "082": "FRIO",
    "083": "GAINES",
    "084": "GALVESTON",
    "085": "GARZA",
    "086": "GILLESPIE",
    "087": "GLASSCOCK",
    "088": "GOLIAD",
    "089": "GONZALES",
    "090": "GRAY",
    "091": "GRAYSON",
    "092": "GREGG",
    "093": "GRIMES",
    "094": "GUADALUPE",
    "095": "HALE",
    "096": "HALL",
    "097": "HAMILTON",
    "098": "HANSFORD",
    "099": "HARDEMAN",
    "100": "HARDIN",
    "101": "HARRIS",
    "102": "HARRISON",
    "103": "HARTLEY",
    "104": "HASKELL",
    "105": "HAYS",
    "106": "HEMPHILL",
    "107": "HENDERSON",
    "108": "HIDALGO",
    "109": "HILL",
    "110": "HOCKLEY",
    "111": "HOOD",
    "112": "HOPKINS",
    "113": "HOUSTON",
    "114": "HOWARD",
    "115": "HUDSPETH",
    "116": "HUNT",
    "117": "HUTCHINSON",
    "118": "IRION",
    "119": "JACK",
    "120": "JACKSON",
    "121": "JASPER",
    "122": "JEFF",
    "123": "JEFFERSON",
    "124": "JIM",
    "125": "JIM",
    "126": "JOHNSON",
    "127": "JONES",
    "128": "KARNES",
    "129": "KAUFMAN",
    "130": "KENDALL",
    "131": "KENEDY",
    "132": "KENT",
    "133": "KERR",
    "134": "KIMBLE",
    "135": "KING",
    "136": "KINNEY",
    "137": "KLEBERG",
    "138": "KNOX",
    "139": "LAMAR",
    "140": "LAMB",
    "141": "LAMPASAS",
    "142": "LA",
    "143": "LAVACA",
    "144": "LEE",
    "145": "LEON",
    "146": "LIBERTY",
    "147": "LIMESTONE",
    "148": "LIPSCOMB",
    "149": "LIVE",
    "150": "LLANO",
    "151": "LOVING",
    "152": "LUBBOCK",
    "153": "LYNN",
    "154": "MCCULLOCH",
    "155": "MCLENNAN",
    "156": "MCMULLEN",
    "157": "MADISON",
    "158": "MARION",
    "159": "MARTIN",
    "160": "MASON",
    "161": "MATAGORDA",
    "162": "MAVERICK",
    "163": "MEDINA",
    "164": "MENARD",
    "165": "MIDLAND",
    "166": "MILAM",
    "167": "MILLS",
    "168": "MITCHELL",
    "169": "MONTAGUE",
    "170": "MONTGOMERY",
    "171": "MOORE",
    "172": "MORRIS",
    "173": "MOTLEY",
    "174": "NACOGDOCHES",
    "175": "NAVARRO",
    "176": "NEWTON",
    "177": "NOLAN",
    "178": "NUECES",
    "179": "OCHILTREE",
    "180": "OLDHAM",
    "181": "ORANGE",
    "182": "PALO",
    "183": "PANOLA",
    "184": "PARKER",
    "185": "PARMER",
    "186": "PECOS",
    "187": "POLK",
    "188": "POTTER",
    "189": "PRESIDIO",
    "190": "RAINS",
    "191": "RANDALL",
    "192": "REAGAN",
    "193": "REAL",
    "194": "RED",
    "195": "REEVES",
    "196": "REFUGIO",
    "197": "ROBERTS",
    "198": "ROBERTSON",
    "199": "ROCKWALL",
    "200": "RUNNELS",
    "201": "RUSK",
    "202": "SABINE",
    "203": "SAN",
    "204": "SAN",
    "205": "SAN",
    "206": "SAN",
    "207": "SCHLEICHER",
    "208": "SCURRY",
    "209": "SHACKLEFORD",
    "210": "SHELBY",
    "211": "SHERMAN",
    "212": "SMITH",
    "213": "SOMERVELL",
    "214": "STARR",
    "215": "STEPHENS",
    "216": "STERLING",
    "217": "STONEWALL",
    "218": "SUTTON",
    "219": "SWISHER",
    "220": "TARRANT",
    "221": "TAYLOR",
    "222": "TERRELL",
    "223": "TERRY",
    "224": "THROCKMORTON",
    "225": "TITUS",
    "226": "TOM",
    "227": "TRAVIS",
    "228": "TRINITY",
    "229": "TYLER",
    "230": "UPSHUR",
    "231": "UPTON",
    "232": "UVALDE",
    "233": "VAL",
    "234": "VAN",
    "235": "VICTORIA",
    "236": "WALKER",
    "237": "WALLER",
    "238": "WARD",
    "239": "WASHINGTON",
    "240": "WEBB",
    "241": "WHARTON",
    "242": "WHEELER",
    "243": "WICHITA",
    "244": "WILBARGER",
    "245": "WILLACY",
    "246": "WILLIAMSON",
    "247": "WILSON",
    "248": "WINKLER",
    "249": "WISE",
    "250": "WOOD",
    "251": "YOAKUM",
    "252": "YOUNG",
    "253": "ZAPATA",
    "254": "ZAVALA",
    "000": "Out of State"
}

TREC_COUNTY_CODES_BY_REGION = {
    "Austin": ["011", "014", "016", "026", "027", "028", "046", "050", "075", "086", "093", "105", "130", "141",
               "150", "166", "198", "206", "227", "239", "246"],
    "Dallas": ["005", "012", "018", "025", "030", "042", "043", "047", "051", "057", "061", "067", "070", "072",
               "076", "078", "099", "104", "109", "111", "116", "119", "126", "127", "129", "132", "138", "168",
               "169", "175", "177", "182", "184", "199", "200", "209", "215", "217", "220", "221", "224", "243",
               "244", "249", "252"],
    "Houston": ["020", "021", "029", "036", "079", "101", "120", "157", "161", "170", "204", "235", "236", "237"],
    "San Antonio": ["010", "015", "062", "064", "082", "094", "128", "133", "142", "149", "156", "163", "232",
                    "247", "254"],
    "Rural": ["001", "002", "003", "004", "006", "008", "009", "013", "017", "019", "022", "023", "024", "031",
              "032", "033", "034", "035", "037", "038", "039", "040", "041", "044", "045", "048", "049", "052",
              "053", "054", "055", "056", "058", "059", "060", "063", "065", "066", "068", "069", "071", "073",
              "073", "074", "077", "080", "081", "083", "084", "085", "087", "090", "091", "092", "095", "096",
              "097", "098", "100", "102", "103", "106", "107", "108", "110", "112", "113", "114", "115", "117",
              "118", "121", "122", "123", "124", "125", "131", "134", "135", "136", "137", "139", "140", "143",
              "144", "145", "147", "148", "151", "152", "153", "154", "155", "158", "159", "162", "163", "164",
              "165", "167", "171", "172", "173", "174", "176", "178", "179", "180", "181", "183", "185", "186",
              "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "201", "202", "203",
              "205", "207", "208", "210", "211", "212", "213", "214", "216", "218", "219", "222", "223", "225",
              "226", "228", "229", "230", "231", "233", "234", "238", "240", "241", "242", "245", "248", "250",
              "251", "253"]
}

TREC_LIC_STATUS = [
    ('20', 'Current and Active'),
    ('21', 'Current and Inactive'),
    ('30', 'Probation and Active'),
    ('31', 'Probation and Inactive'),
    ('45', 'Expired'),
    ('47', 'Suspended'),
    ('56', 'Relinquished'),
    ('57', 'Revoked'),
    ('80', 'Deceased')
]

TREC_LIC_TYPES = [
    ('SALE', 'Sales Agent'),
    ('BRK', 'Individual Broker'),
    ('BLLC', 'Limited Liability Corporation Broker'),
    ('BCRP', 'Corporation Broker'),
    ('6', 'Partnership Broker'),
    ('REB', 'Broker Organization Branch'),
    ('PRIN', 'Professional Inspector'),
    ('REIN', 'Real Estate Inspector'),
    ('APIN', 'Apprentice Inspector'),
    ('ILLC', 'Professional Inspector, LLC'),
    ('ICRP', 'Professional Inspector, Corporation'),
    ('ERWI', 'Easement and Right-of-Way, Individual'),
    ('ERWO', 'Easement and Right-of-Way, Business')
]

TREC_ED_STATUS = [
    ('0', 'No Non-elective CE Requirement'),
    ('1', 'Non-elective CE Requirements Outstanding'),
    ('2', 'Non-elective CE Requirements Met')
]

TREC_MCE_STATUS = [
    ('0', 'No MCE Requirement'),
    ('1', 'MCE Requirements Outstanding'),
    ('2', 'MCE Requirements Met')
]

APTX_LIC_STATUS = TREC_LIC_STATUS

APTX_LIC_TYPES = [
    ('APCR', 'Certified Residential Appraiser'),
    ('APGN', 'Certified General Appraiser'),
    ('APOS', 'Temporary Out of State Appraiser'),
    ('APPV', 'Provisional Licensed Appraiser'),
    ('APSC', 'Licensed Residential Appraiser'),
    ('APTR', 'Appraiser Trainee')
]
