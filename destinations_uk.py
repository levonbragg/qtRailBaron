# "ODD" "Even"

SCOTTISH_HIGHLANDS = [
[2,"Wick","Wick"],
[3,"Oban","Kyle of Lochalsh"],
[4,"Oban","Keith"],
[5,"Inverness","Keith"],
[6,"Inverness","Fraserburgh"],
[7,"Montrose","Dundee"],
[8,"Aberdeen","Dundee"],
[9,"Aberdeen","Crianlarich"],
[10,"Fort William","Crianlarich"],
[11,"Fort William","Boat of Garten"],
[12,"Mallaig","Mallaig"],
]
SCOTTISH_LOWLANDS = [
[2,"Hamilton","Dumfries"],
[3,"Perth","Edinburgh"],
[4,"Perth","Edinburgh"],
[5,"Perth","Edinburgh"],
[6,"Hamilton","Edinburgh"],
[7,"Glasgow","Kilmarnock"],
[8,"Glasgow","Stirling"],
[9,"Glasgow","Stirling"],
[10,"Hamilton","Stranraer"],
[11,"Peebles","Dumfries"],
[12,"Peebles","Stranraer"],
]
RED_ROSE_COUNTRY = [
[2,"Tebay","Carlisle"],
[3,"Tebay","Carlisle"],
[4,"Liverpool","Carlisle"],
[5,"Liverpool","Barrow-in-Furness"],
[6,"Liverpool","Whitehaven"],
[7,"Lancaster","Lancaster"],
[8,"Crewe","Manchester"],
[9,"Blackburn","Manchester"],
[10,"Crewe","Manchester"],
[11,"Blackburn","Barrow-in-Furness"],
[12,"Blackburn","Whitehaven"],
]
WALES = [
[2,"Llanidloes","Brecon"],
[3,"Llanidloes","Brecon"],
[4,"Aberystwyth","Brecon"],
[5,"Aberystwyth","Cardiff"],
[6,"Carmarthen","Cardiff"],
[7,"Swansea","Cardiff"],
[8,"Swansea","Bangor"],
[9,"Wrexham","Blaneau Festiniog"],
[10,"Wrexham","Bangor"],
[11,"Neyland","Blaneau Festiniog"],
[12,"Neyland","Llanidloes"],
]
WEST_COUNTRY = [
[2,"Bridgwater","Padstow"],
[3,"Weymouth","Padstow"],
[4,"Bridgwater","Swindon"],
[5,"Weymouth","Bournemouth"],
[6,"Bristol","Bournemouth"],
[7,"Bristol","Gloucester"],
[8,"Plymouth","Gloucester"],
[9,"Barnstaple","Salisbury"],
[10,"Plymouth","Exeter"],
[11,"Penzance","Exeter"],
[12,"Penzance","Salisbury"],
]
WHITE_ROSE_COUNTRY = [
[2,"Berwick","Scarborough"],
[3,"Grimsby","Scarborough"],
[4,"Berwick","Leeds"],
[5,"Sheffield","Leeds"],
[6,"Sheffield","Leeds"],
[7,"Newcastle","York"],
[8,"Hull","York"],
[9,"Grimsby","York"],
[10,"Doncaster","Darlington"],
[11,"Doncaster","Darlington"],
[12,"Hull","Hull"],
]
MIDLANDS = [
[2,"Nottingham","Craven Arms"],
[3,"Rugby","Craven Arms"],
[4,"Nottingham","Hereford"],
[5,"Rugby","Hereford"],
[6,"Birmingham","Stafford"],
[7,"Birmingham","Leicester"],
[8,"Boston","Worcester"],
[9,"Lincoln","Leicester"],
[10,"Derby","Worcester"],
[11,"Derby","Shrewsbury"],
[12,"Stratford-on-Avon","Shrewsbury"],
]
EAST_ANGLIA = [
[2,"Yarmouth","Southend-on-Sea"],
[3,"Yarmouth","Southend-on-Sea"],
[4,"Yarmouth","Peterborough"],
[5,"Cambridge","Hertford"],
[6,"Cambridge","Peterborough"],
[7,"Bedford","Hertford"],
[8,"Bedford","Norwich"],
[9,"Ipswich","King's Lynn"],
[10,"Colchester","King's Lynn"],
[11,"Ipswich","Norwich"],
[12,"Colchester","Norwich"],
]
HOME_COUNTIES = [
[2,"Banbury","Guildford"],
[3,"Dover","Winchester"],
[4,"Canterbury","Winchester"],
[5,"Dover","Guildford"],
[6,"Banbury","Oxford"],
[7,"Brighton","Southampton"],
[8,"Chatham","Portsmouth"],
[9,"Chatham","Reading"],
[10,"Hastings","Tunbridge Wells"],
[11,"Hastings","Portsmouth"],
[12,"Canterbury","Reading"],
]
LONDON = [
[2,"London","London"],
[3,"London","London"],
[4,"London","London"],
[5,"London","London"],
[6,"London","London"],
[7,"London","London"],
[8,"London","London"],
[9,"London","London"],
[10,"London","London"],
[11,"London","London"],
[12,"London","London"],
]
REGIONS_UK_LIST = [SCOTTISH_LOWLANDS, RED_ROSE_COUNTRY, WALES, WEST_COUNTRY, SCOTTISH_HIGHLANDS, WHITE_ROSE_COUNTRY,
                   MIDLANDS, EAST_ANGLIA, HOME_COUNTIES]
REGIONS_UK = [
[2,"White Rose Country","West Country"],
[3,"White Rose Country","West Country"],
[4,"Scottish Lowlands","Home Counties"],
[5,"Scottish Lowlands","West Country"],
[6,"Wite Rose Country","East Anglia"],
[7,"Midlands","Home Counties"],
[8,"Red Rose Country","Wales"],
[9,"Midlands","London"],
[10,"Red Rose Country","Scottish Highlands"],
[11,"East Anglia","Scottish Highlands"],
[12,"Wales","Scottish Highlands"],
]

DESTINATIONS_UK_DICT = {
    '2ODD': WHITE_ROSE_COUNTRY,
    '2EVEN': WEST_COUNTRY,
    '3ODD': WHITE_ROSE_COUNTRY,
    '3EVEN': WEST_COUNTRY,
    '4ODD': SCOTTISH_LOWLANDS,
    '4EVEN': HOME_COUNTIES,
    '5ODD': SCOTTISH_LOWLANDS,
    '5EVEN': WEST_COUNTRY,
    '6ODD': WHITE_ROSE_COUNTRY,
    '6EVEN': EAST_ANGLIA,
    '7ODD': MIDLANDS,
    '7EVEN': HOME_COUNTIES,
    '8ODD': RED_ROSE_COUNTRY,
    '8EVEN': WALES,
    '9ODD': MIDLANDS,
    '9EVEN': LONDON,
    '10ODD': RED_ROSE_COUNTRY,
    '10EVEN': SCOTTISH_HIGHLANDS,
    '11ODD': EAST_ANGLIA,
    '11EVEN': SCOTTISH_HIGHLANDS,
    '12ODD': WALES,
    '12EVEN': SCOTTISH_HIGHLANDS
}