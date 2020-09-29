import os

import json


a="""Aarhus	Denmark	AAR
Abadan	Iran	ABD
Abeche	Chad	AEH
Aberdeen	United Kingdom	ABZ
Aberdeen (SD)	USA	ABR
Abidjan	Cote d'Ivoire	ABJ
Abilene (TX)	USA	ABI
Abu Dhabi - Abu Dhabi International	United Arab Emirates	AUH
Abuja - Nnamdi Azikiwe International Airport	Nigeria	ABV
Abu Rudeis	Egypt	AUE
Abu Simbel	Egypt	ABS
Acapulco	Mexico	ACA
Accra - Kotoka International Airport	Ghana	ACC
Adana	Turkey	ADA
Addis Ababa - Bole International Airport	Ethiopia	ADD
Adelaide	Australia	ADL
Aden - Aden International Airport	Yemen	ADE
Adiyaman	Turkey	ADF
Adler/Sochi	Russia	AER
Agades	Niger	AJY
Agadir	Morocco	AGA
Agana (Hagåtña)	Guam	SUM
Aggeneys	South Africa	AGZ
Aguadilla	Puerto Rico	BQN
Aguascaliente	Mexico	AGU
Ahmedabad	India	AMD
Aiyura	Papua New Guinea	AYU
Ajaccio	France	AJA
Akita	Japan	AXT
Akron (OH)	USA	CAK
Akrotiri - RAF	Cyprus	AKT
Al Ain	United Arab Emirates	AAN
Al Arish	Egypt	AAC
Albany	Australia	ALH
Albany (GA)	USA	ABY
Albany (NY) - Albany International Airport	USA	ALB
Albi	France	LBI
Alborg	Denmark	AAL
Albuquerque (NM)	USA	ABQ
Albury	Australia	ABX
Alderney	Channel Islands	ACI
Aleppo	Syria	ALP
Alesund	Norway	AES
Alexander Bay - Kortdoorn	South Africa	ALJ
Alexandria - Borg el Arab Airport	Egypt	HBH
Alexandria - El Nhouza Airport	Egypt	ALY
Alexandria - Esler Field	USA (LA)	ESF
Alfujairah (Fujairah)	United Arab Emirates	FJR
Alghero Sassari	Italy	AHO
Algiers, Houari Boumediene Airport	Algeria	ALG
Al Hoceima	Morocco	AHU
Alicante	Spain	ALC
Alice Springs	Australia	ASP
Alldays	South Africa	ADY
Allentown (PA)	USA	ABE
Almaty (Alma Ata) - Almaty International Airport	Kazakhstan	ALA
Almeria	Spain	LEI
Alta	Norway	ALF
Altay	PR China	AAT
Altenrhein	Switzerland	ACH
Altoona (PA)	USA	AOO
Altus	USA	AXS
Amami	Japan	ASJ
Amarillo (TX)	USA	AMA
Amazon Bay	Papua New Guinea	AZB
Amman - Queen Alia International Airport	Jordan	AMM
Amman - Amman-Marka International Airport	Jordan	ADJ
Amritsar	India	ATQ
Amsterdam - Amsterdam Airport Schiphol	Netherlands	AMS
Anand	India	QNB
Anchorage (AK) - Ted Stevens Anchorage International	USA	ANC
Ancona - Ancona Falconara Airport	Italy	AOI
Andorra La Vella - Heliport	Andorra	ALV
Anguilla	Anguilla	AXA
Anjouan - Anjouan Airport	Comoros (Comores)	AJN
Ankara	Turkey	ANK
Ankara - Esenboğa International Airport	Turkey	ESB
Annaba	Algeria	AAE
Ann Arbor (MI)	USA	ARB
Annecy	France	NCY
Anniston (AL)	USA	ANB
Antalya	Turkey	AYT
Antananarivo (Tanannarive) - Ivato International Airport	Madagascar	TNR
Antigua, V.C. Bird International	Antigua and Barbuda	ANU
Antwerp	Belgium	ANR
Aomori	Japan	AOJ
Apia - Faleolo International Airport	Samoa	APW
Appelton/Neenah/Menasha (WI)	USA	ATW
Aqaba	Jordan	AQJ
Aracaju	Brazil	AJU
Arkhangelsk	Russia	ARH
Arusha	Tanzania	ARK
Araxos	Greece	GPA
Arlit	Niger	RLT
Arrecife/Lanzarote	Spain	ACE
Aruba - Reina Beatrix International, Oranjestad	Aruba	AUA
Asheville (NC)	USA	AVL
Ashgabat - Saparmurat Turkmenbashy Int. Airport	Turkmenistan	ASB
Asmara - Asmara International	Eritrea	ASM
Aspen, (CO) - Aspen-Pitkin County Airport	USA	ASE
Assiut	Egypt	ATZ
Astana - Astana International Airport	Kazakhstan	TSE
Asuncion - Asunción International Airport	Paraguay	ASU
Aswan - Daraw Airport	Egypt	ASW
Athens - Elefthérios Venizélos International Airport	Greece	ATH
Athens, Hellinikon Airport	Greece	HEW
Athens (GA)	USA	AHN
Athens (OH)	USA	ATO
Atlanta (GA) - Hartsfield Atlanta International Airport	USA	ATL
Atlantic City (NJ) - Atlantic City International	USA	ACY
Attawapiskat, NT	Canada	YAT
Auckland - Auckland International Airport	New Zealand	AKL
Augsburg - Augsbur gAirport	Germany	AGB
Augusta (GA)	USA	AGS
Augusta (ME) - Augusta State Airport	USA	AUG
Aurillac	France	AUR
Austin (TX) - Austin-Bergstrom Airport	USA	AUS
Ayawasi	Indonesia	AYW
Ayers Rock - Connellan	Australia	AYQ
Ayr	Australia	AYR
Badajoz	Spain	BJZ
Bagdad - Baghdad International Airport	Iraq	BGW
Bagdogra	India	IXB
Bahamas - Lynden Pindling International Airport	The Bahamas	NAS
Bahawalpur	Pakistan	BHV
Bahrain - Bahrain International Airport	Bahrain	BAH
Bakersfield (CA)	USA	BFL
Baku - Heydar Aliyev International Airport	Azerbaijan	BAK
Ballina	Australia	BNK
Baltimore (MD) - Washington International Airport	USA	BWI
Bamaga	Australia	ABM
Bamako - Bamako-Sénou International Airport	Mali	BKO
Bambari	Central African Republic	BBY
Bandar Seri Begawan - Brunei International Airport	Brunei	BWN
Bandung - Husein Sastranegara International Airport	Indonesia	BDO
Bangalore	India	BLR
Bangassou	Central African Republic	BGU
Bangkok, Don Muang	Thailand	DMK
Bangkok, Suvarnabhumi International	Thailand	BKK
Bangor (ME)	USA	BGR
Bangui - M'Poko International Airport	Central African Republic	BGF
Banjul - Banjul International Airport (Yundum International)	Gambia	BJL
Bannu	Pakistan	BNP
Barcelona	Spain	BCN
Barcelona	Venezuela	BLA
Bardufoss	Norway	BDU
Bari	Italy	BRI
Barisal	Bangladesh	BZL
Baroda	India	BDQ
Barra (the famous tidal beach landing)	United Kingdom	BRR
Barranquilla	Colombia	BAQ
Basel	Switzerland	BSL
Basel/Mulhouse	Switzerland/France	EAP
Basra, Basrah	Iraq	BSR
Basse-Terre - Pointe-à-Pitre International Airport	Guadeloupe	PTP
Basseterre - Robert L. Bradshaw International Airport	Saint Kitts and Nevis	SKB
Bastia	France	BIA
Baton Rouge (LA) - Baton Rouge Metropolitan Airport	USA	BTR
Bayreuth - Bindlacher-Berg	Germany	BYU
Beaumont/Pt. Arthur (TX)	USA	BPT
Beckley (WV)	USA	BKW
Beef Island - Terrance B. Lettsome	Virgin Islands (British)	EIS
Beijing	China	PEK
Beijing - Nanyuan Airport	China	NAY
Beira	Mozambique	BEW
Beirut - Beirut Rafic Hariri International Airport	Lebanon	BEY
Belem - Val de Cans International Airport	Brazil	BEL
Belfast - George Best Belfast City Airport	United Kingdom	BHD
Belfast - Belfast International Airport	United Kingdom	BFS
Belgaum	India	IXG
Belgrad (Beograd) - Belgrade Nikola Tesla International	Serbia	BEG
Belize City - Philip S.W.Goldson International	Belize	BZE
Bellingham (WA)	USA	BLI
Belo Horizonte - Tancredo Neves International Airport	Brazil	CNF
Bemidji (MN)	USA	BJI
Benbecula	United Kingdom	BEB
Benghazi (Bengasi)	Libya	BEN
Benguela	Angola	BUG
Benton Harbour (MI)	USA	BEH
Berberati	Central African Republic	BBT
Bergamo/Milan - Orio Al Serio	Italy	BGY
Bergen	Norway	BGO
Bergerac - Roumanieres	France	EGC
Berlin	Germany	BER
Berlin, Schoenefeld	Germany	SXF
Berlin, Tegel	Germany	TXL
Berlin, Tempelhof (ceased operating in 2008)	Germany	THF
Bermuda - L.F. Wade International Airport	Bermuda	BDA
Berne, Bern-Belp	Switzerland	BRN
Berne, Railway Service	Switzerland	ZDJ
Bethel (AK)	USA	BET
Bhopal	India	BHO
Bhubaneswar	India	BBI
Biarritz	France	BIQ
Bilbao	Spain	BIO
Billings (MT)	USA	BIL
Billund	Denmark	BLL
Bintulu	Malaysia	BTU
Biraro	Central African Republic	IRO
Birmingham - Birmingham International Airport	United Kingdom	BHX
Birmingham (AL)	USA	BHM
Bishkek - Manas International Airport	Kyrgyzstan	FRU
Bismarck (ND) - Bismarck Municipal Airport	USA	BIS
Bissau - Osvaldo Vieiro International Airport	Guinea-Bissau	BXO
Blackpool	United Kingdom	BLK
Blackwater	Australia	BLT
Blantyre (Mandala) - Chileka International Airport	Malawi	BLZ
Blenheim	New Zealand	BHE
Bloemfontein - Bloemfontein Airport	South Africa	BFN
Bloomington (IL)	USA	BMI
Bloomington (IN)	USA	BMG
Bluefield (WV)	USA	BLF
Boa Vista	Brazil	BVB
Bobo/Dioulasso	Burkina Faso	BOY
Bodo	Norway	BOO
Bodrum - Milas Airport	Turkey	BJV
Bogota - El Nuevo Dorado International Airport	Colombia	BOG
Boise (ID) - Boise Air Terminal	USA	BOI
Bologna	Italy	BLQ
Bombay (Mumbai) - Chhatrapati Shivaji International	India	BOM
Bonaire	Netherlands Antilles	BON
Bonaventure, PQ	Canada	YVB
Bora Bora	French Polynesia	BOB
Bordeaux - Bordeaux Airport	France	BOD
Borrego Springs (CA)	USA	BXS
Boston (MA) - General Edward Lawrence Logan	USA	BOS
Bouake	Cote d'Ivoire	BYK
Bourgas/Burgas	Bulgaria	BOJ
Bournemouth	United Kingdom	BOH
Bowen	Australia	ZBO
Bozeman (MT)	USA	BZN
Bradford/Warren (PA) /Olean (NY)	USA	BFD
Brainerd (MN)	USA	BRD
Brampton Island	Australia	BMP
Brasilia - President Juscelino Kubitschek International	Brazil	BSB
Bratislava - M. R. Štefánik Airport	Slovakia	BTS
Brazzaville - Maya-Maya Airport	Congo (ROC)	BZV
Bremen - Bremen Airport (Flughafen Bremen)	Germany	BRE
Brescia, Montichiari	Italy	VBS
Brest	France	BES
Bria	Central African Republic	BIV
Bridgeport (CT)	USA	BDR
Bridgetown - Grantley Adams International	Barbados	BGI
Brindisi	Italy	BDS
Brisbane	Australia	BNE
Bristol	United Kingdom	BRS
Broennoeysund	Norway	BNN
Broken Hill	Australia	BHQ
Brookings (SD)	USA	BKX
Broome	Australia	BME
Brunswick (GA)	USA	BQK
Brussels - Brussels Airport	Belgium	BRU
Bucaramanga	Colombia	BGA
Bucharest	Romania	BUH
Bucharest - Henri Coandă International Airport	Romania	OTP
Budapest - Budapest Ferihegy International Airport	Hungary	BUD
Buenos Aires	Argentina	BUE
Buenos Aires, Ezeiza International Airport	Argentina	EZE
Buenos Aires, Jorge Newbery	Argentina	AEP
Buffalo Range	Zimbabwe	BFO
Buffalo/Niagara Falls (NY)	USA	BUF
Bujumbura - Bujumbura International Airport	Burundi	BJM
Bulawayo	Zimbabwe	BUQ
Bullhead City (NV)	USA	BHC
Bundaberg	Australia	BDB
Burbank (CA)	USA	BUR
Burlington IA	USA	BRL
Burlington (VT)	USA	BTV
Burnie (Wynyard)	Australia	BWT
Butte (MT)	USA	BTM
Cabinda	Angola	CAB
Cagliari	Italy	CAG
Cairns	Australia	CNS
Cairo - Cairo International Airport	Egypt	CAI
Calama - El Loa	Chile	CJC
Calcutta (Kolkata) - Netaji Subhas Chandra	India	CCU
Calgary - Calgary International Airport	Canada	YYC
Cali	Colombia	CLO
Calicut	India	CCJ
Calvi	France	CLY
Cambridge Bay	Canada	YCB
Cambrigde	United Kingdom	CBG
Campbeltown	United Kingdom	CAL
Campo Grande	Brazil	CGR
Canberra - Canberra Airport	Australia	CBR
Cancun	Mexico	CUN
Cannes – Mandelieu Airport	France	CEQ
Canouan (island) - Canouan Airport	Saint Vincent & the Grenadines	CIW
Cape Town - Cape Town International Airport	South Africa	CPT
Caracas - Simón Bolívar International Airport	Venezuela	CCS
Cardiff - Cardiff Airport	United Kingdom	CWL
Carlsbad (CA)	USA	CLD
Carnarvon	Australia	CVQ
Carnot	Central African Republic	CRF
Carson City (NV)	USA	CSN
Casablanca	Morocco	CAS
Casablanca, Mohamed V	Morocco	CMN
Casa de Campo - La Romana International Airport	Dominican Republic	LRM
Casino	Australia	CSI
Casper (WY)	USA	CPR
Castaway	Fiji	CST
Cartagena - Rafael Núñez International Airport	Colombia	CTG
Castries - George F. L. Charles Airport	Saint Lucia	SLU
Catania	Italy	CTA
Cayenne - Cayenne-Rochambeau Airport	French Guiana	CAY
Cottbus - Cottbus-Drewitz Airport	Germany	CBU
Cebu City - Mactan-Cebu International	Philippines	CEB
Cedar City (UT)	USA	CDC
Cedar Rapids IA	USA	CID
Ceduna	Australia	CED
Cessnock	Australia	CES
Chabarovsk (Khabarovsk)	Russia	KHV
Chambery	France	CMF
Champaign (IL)	USA	CMI
Chandigarh - Chandigarh International Airport	India	IXC
Changchun	Jilin, PR China	CGQ
Chania	Greece	CHQ
Chaoyang, Beijing - Chaoyang Airport	PR China	CHG
Charleston (SC)	USA	CHS
Charleston (WV) - Yeager Airport	USA	CRW
Charlotte (NC)	USA	CLT
Charlottesville (VA)	USA	CHO
Charters Towers	Australia	CXT
Chattanooga (TN)	USA	CHA
Chengdu - Shuangliu	Sichuan, PR China	CTU
Chennai (Madras)	India	MAA
Cheyenne (WY) - Cheyenne Regional Airport	USA	CYS
Chiang Mai - Chiang Mai International Airport	Thailand	CNX
Chiba City	Japan	QCB
Chicago (IL), Midway	USA	MDW
Chicago (IL), O'Hare International Airport	USA	ORD
Chicago (IL)	USA	CHI
Chichen Itza	Mexico	CZA
Chico (CA)	USA	CIC
Chihuahua - Gen Fierro Villalobos	Mexico	CUU
Chios	Greece	JKH
Chipata	Zambia	CIP
Chisinau - Chişinău International Airport	Moldova	KIV
Chita (Tschita)	Russia	HTA
Sapporo - New Chitose Airport	Japan	CTS
Chitral	Pakistan	CJL
Chittagong	Bangladesh	CGP
Chongqing - Jiangbei International Airport	Sichuan, PR China	CKG
Christchurch	New Zealand	CHC
Chub Cay	Bahamas	CCZ
Churchill	Canada	YYQ
Cienfuegos - Jaime González Airport	Cuba	CFG
Cincinnati (OH) - Cincinnati/Northern Kentucky Int'l	USA	CVG
Ciudad Del Carmen	Mexico	CME
Ciudad Guayana	Venezuela	CGU
Ciudad Juarez	Mexico	CJS
Ciudad Obregon	Mexico	CEN
Ciudad Victoria	Mexico	CVM
Clarksburg (WV)	USA	CKB
Clermont	Australia	CMQ
Clermont Ferrand	France	CFE
Cleveland (OH) , Burke Lakefront	USA	BKL
Cleveland (OH) - Cleveland Hopkins International	USA	CLE
Cochabamba	Bolivia	CBB
Cochin	India	COK
Cody/Powell/Yellowstone (WY)	USA	COD
Coffmann Cove (AK)	USA	KCC
Coffs Harbour	Australia	CFS
Coimbatore	India	CJB
Colima	Mexico	CLQ
College Station/Bryan (TX)	USA	CLL
Collinsville	Australia	KCE
Cologne - Cologne Airport (Flughafen Köln/Bonn)	Germany	CGN
Colombo - Bandaranaike International Airport	Sri Lanka	CMB
Colorado Springs (CO)	USA	COS
Columbia (SC) - Columbia Metropolitan Airport	USA	CAE
Columbus (GA)	USA	CSG
Columbus (OH) - Port Columbus International	USA	CMH
Conakry - Conakry International Airport	Guinea	CKY
Concord (CA) - Buchanan Field	USA	CCR
Concord (NH) - Concord Municipal Airport	USA	CON
Constantine	Algeria	CZL
Constanta (Constanța) - Constanta Int'l Airport	Romania	CND
Coober Pedy	Australia	CPD
Cooktown	Australia	CTN
Cooma	Australia	OOM
Copenhagen - Copenhagen Airport	Denmark	CPH
Cordoba	Argentina	COR
Cordoba	Spain	ODB
Cordova (AK)	USA	CDV
Corfu	Greece	CFU
Cork	Ireland	ORK
Corpus Christi (TX)	USA	CRP
Cotonou - Cotonou Cadjehoun Airport	Benin	COO
Coventry - Baginton	United Kingdom	CVT
Cozmel	Mexico	CZM
Craig (AK)	USA	CGA
Crescent City (CA)	USA	CEC
Cuiaba - Marechal Rondon International Airport	Brazil	CGB
Culiacan	Mexico	CUL
Curacao - Curaçao International Airport	Netherlands Antilles	CUR
Curitiba - Afonso Pena International Airport	Brazil	CWB
Cuyo	Philippines	CYU
Dakar - Léopold Sédar Senghor International Airport	Senegal	DKR
Dalaman	Turkey	DLM
Dalby	Australia	DBY
Dalian - Zhoushuizi International Airport	Liaoning, PR China	DLC
Dallas (TX) , Love Field	USA	DAL
Dallas/Ft. Worth (TX) - Dallas/Fort Worth International	USA	DFW
Daloa	Cote d'Ivoire	DJO
Damascus, International	Syria	DAM
Dammam, King Fahad International	Saudi Arabien	DMM
Danville (VA)	USA	DAN
Dar es Salam (Daressalam) - Julius Nyerere Int'l	Tanzania	DAR
Darwin	Australia	DRW
Daydream Island	Australia	DDI
Dayton (OH)	USA	DAY
Daytona Beach (FL)	USA	DAB
Decatur (IL)	USA	DEC
Deer Lake/Corner Brook	Canada	YDF
Delhi - Indira Gandhi International Airport	India	DEL
Den Haag (The Hague)	Netherlands	HAG
Denizli	Turkey	DNZ
Denpasar/Bali	Indonesia	DPS
Denver (CO) - Denver International Airport	USA	DEN
Dera Ismail Khan - Dera Ismail Khan Airport	Pakistan	DSK
Derby	Australia	DRB
Derry (Londonderry)	United Kingdom	LDY
Des Moines (IA) - Des Moines International Airport	USA	DSM
Detroit (MI) , Coleman A. Young Municipal	USA	DET
Detroit (MI) , Wayne County Airport	USA	DTW
Detroit (MI) , Metropolitan Area	USA	DTT
Devils Lake (ND)	USA	DVL
Devonport	Australia	DPO
Dhahran	Saudi Arabia	DHA
Dhaka - Zia International Airport	Bangladesh	DAC
Dili - Nicolau Lobato International Airport	Timor Leste (East Timor)	DIL
Dillingham (AK)	USA	DLG
Dinard	France	DNR
Disneyland Paris	France	DLP
Djerba	Tunisia	DJE
Djibouti (city) - Djibouti-Ambouli International Airport	Djibouti	JIB
Dodoma - Dodoma Airport	Tanzania	DOD
Doha - Doha International Airport	Qatar	DOH
Doncaster/Sheffield, Robin Hood International Airport	United Kingdom	DSA
Donegal (Carrickfin)	Ireland	CFN
Dortmund	Germany	DTM
Dothan (AL)	USA	DHN
Douala	Cameroon	DLA
Dresden - Dresden Airport	Germany	DRS
Dubai - Dubai International Airport	United Arab Emirates	DXB
Dubbo	Australia	DBO
Dublin - Dublin International Airport	Ireland	DUB
Dubois (PA)	USA	DUJ
Dubrovnik	Croatia (Hrvatska)	DBV
Dubuque IA	USA	DBQ
Duesseldorf - Düsseldorf International Airport	Germany	DUS
Duluth (MN) /Superior (WI)	USA	DLH
Dundee	United Kingdom	DND
Dunedin	New Zealand	DUD
Dunk Island	Australia	DKI
Durango (CO)	USA	DRO
Durban	South Africa	DUR
Dushanbe (Duschanbe) - Dushanbe Airport	Tajikistan	DYU
Dutch Harbor (AK)	USA	DUT
Dysart	Australia	DYA
Dzaoudzi	Mayotte	DZA
East London	South Africa	ELS
Easter Island	Chile	IPC
Eau Clarie (WI)	USA	EAU
Edinburgh - Edinburgh Airport	Scotland, UK	EDI
Edmonton	Canada	YEA
Edmonton, International	Canada	YEG
Edmonton, Municipal	Canada	YXD
Egilsstadir	Iceland	EGS
Eindhoven	Netherlands	EIN
Samana - Samaná El Catey International Airport	Dominican Republic	AZS
Elba Island, Marina Di Campo	Italy	EBA
Elat	Israel	ETH
Elat, Ovula	Israel	VDA
Elkhart (IN)	USA	EKI
Elko (NV)	USA	EKO
Ellisras	South Africa	ELL
El Minya	Egypt	EMY
Elmira (NY)	USA	ELM
El Paso (TX) - El Paso International Airport	USA	ELP
Ely (NV)	USA	ELY
Emerald	Australia	EDR
Emerald	Australia	EMD
Enontekioe	Finland	ENF
Entebbe - Entebbe International Airport	Uganda	EBB
Erfurt - Erfurt Airport (Flughafen Erfurt)	Germany	ERF
Erie (PA)	USA	ERI
Eriwan (Yerevan, Jerevan)	Armenia	EVN
Erzincan	Turkey	ERC
Erzurum	Turkey	ERZ
Esbjerg	Denmark	EBJ
Escanaba (MI)	USA	ESC
Esperance	Australia	EPR
Eugene (OR)	USA	EUG
Eureka (CA)	USA	ACV
Evansville (IN)	USA	EVV
Evenes	Norway	EVE
Exeter	United Kingdom	EXT
Fairbanks (AK)	USA	FAI
Fair Isle (Shetland)	United Kingdom	FIE
Faisalabad	Pakistan	LYP
Fargo (ND) (MN)	USA	FAR
Farmington (NM)	USA	FMN
Faro	Portugal	FAO
Faroer - Vágar Airport	Denmark	FAE
Fayetteville (AR)	USA	FYV
Fayetteville/Ft. Bragg (NC)	USA	FAY
Fes	Morocco	FEZ
Figari	France	FSC
Flagstaff (AZ)	USA	FLG
Flin Flon	Canada	YFO
Flint (MI)	USA	FNT
Florence (Firenze) - Peretola Airport	Italy	FLR
Florence (SC)	USA	FLO
Florianopolis	Brazil	FLN
Floro	Norway	FRO
Fort Albert	Canada	YFA
Fortaleza - Pinto Martins Airport	Brazil	FOR
Fort de France - Martinique Aimé Césaire International	Martinique	FDF
Fort Dodge IA	USA	FOD
Fort Huachuca/Sierra Vista (AZ)	USA	FHU
Fort Lauderdale/Hollywood (FL)	USA	FLL
Fort McMurray	Canada	YMM
Fort Myers, Metropolitan Area (FL)	USA	FMY
Fort Myers, Southwest Florida Reg (FL)	USA	RSW
Fort Riley (KS) - Marshall AAF	USA	FRI
Fort Smith	Canada	YSM
Fort Smith (AR)	USA	FSM
Fort St. John	Canada	YXJ
Fort Walton Beach (FL)	USA	VPS
Fort Wayne (IN)	USA	FWA
Fort Worth (TX) - Dallas/Fort Worth International Airport	USA	DFW
Foula (Shetland)	United Kingdom	FOU
Francistown	Botswana	FRW
Frankfurt/Main - Frankfurt Airport (Rhein-Main-Flughafen)	Germany	FRA
Frankfurt/Hahn	Germany	HHN
Franklin/Oil City (PA)	USA	FKL
Fredericton	Canada	YFC
Freeport - Grand Bahama International Airport	Bahamas	FPO
Freetown - Freetown-Lungi International Airport	Sierra Leone	FNA
Frejus	France	FRJ
Fresno (CA)	USA	FAT
Friedrichshafen - Bodensee-Airport Friedrichshafen	Germany	FDH
Fuerteventura	Spain	FUE
Fujairah, International Airport	United Arab Emirates	FJR
Fukuoka	Japan	FUK
Fukushima - Fukushima Airport	Japan	FKS
Funchal	Portugal	FNC
Futuna	Wallis and Futuna Islands	FUT
Gaborone - Sir Seretse Khama International Airport	Botswana	GBE
Gadsden (AL)	USA	GAD
Gainesville (FL)	USA	GNV
Galway	Ireland	GWY
Gander	Canada	YQX
Garoua	Cameroon	GOU
Gaza City - Gaza International Airport	Palestinian Territory	GZA
Gaziantep	Turkey	GZT
Gdansk	Poland	GDN
Geelong	Australia	GEX
Geneva - Geneva-Cointrin International Airport	Switzerland	GVA
Genoa	Italy	GOA
George	South Africa	GRJ
Georgetown - Cheddi Jagan International Airport	Guyana	GEO
Geraldton	Australia	GET
Gerona	Spain	GRO
Ghent (Gent)	Belgium	GNE
Gibraltar	Gibraltar	GIB
Gilette (WY)	USA	GCC
Gilgit	Pakistan	GIL
Gillam	Canada	YGX
Gladstone	Australia	GLT
Glasgow, Prestwick	United Kingdom	PIK
Glasgow	United Kingdom	GLA
Glasgow (MT)	USA	GGW
Glendive (MT)	USA	GDV
Goa	India	GOI
Goiania, Santa Genoveva Airport	Brazil	GYN
Gold Coast	Australia	OOL
Goondiwindi	Australia	GOO
Goose Bay	Canada	YYR
Gorna	Bulgaria	GOZ
Gothenburg (Göteborg) - Landvetter	Sweden	GOT
Gove (Nhulunbuy)	Australia	GOV
Govenors Harbour	Bahamas	GHB
Granada	Spain	GRX
Grand Bahama International	Bahamas	FPO
Grand Canyon (AZ)	USA	GCN
Grand Cayman - Owen Roberts International	Cayman Islands	GCM
Grand Forks (ND)	USA	GFK
Grand Junction (CO)	USA	GJT
Grand Rapids (MI)	USA	GRR
Grand Rapids (MN)	USA	GPZ
Graz	Austria	GRZ
Great Falls (MT)	USA	GTF
Great Keppel Island	Australia	GKL
Green Bay (WI)	USA	GRB
Greenbrier/Lewisburg (WV)	USA	LWB
Greensboro/Winston Salem (NC)	USA	GSO
Greenville (MS)	USA	GLH
Greenville (NC)	USA	PGV
Greenville/Spartanburg (SC)	USA	GSP
Grenada - Point Salines Airport also Maurice Bishop	Grenada	GND
Grenoble	France	GNB
Griffith	Australia	GFF
Groningen - Eelde	Netherlands	GRQ
Groote Eylandt - Alyangula	Australia	GTE
Groton/New London (CT)	USA	GON
Guadalajara	Mexico	GDL
Guadalcanal	Solomon Islands	GSI
Guam	Guam	GUM
Guangzhou (Canton) - Baiyun International Airport	Guangdong, PR China	CAN
Sao Paulo - Guarulhos International	Brazil	GRU
Guatemala City - La Aurora International Airport	Guatemala	GUA
Guayaquil - Simon Bolivar	Ecuador	GYE
Guernsey	Channel Islands	GCI
Guettin	Germany	GTI
Gulfport/Biloxi (MS)	USA	GPT
Guilin - Liangjiang	Guangxi, PR China	KWL
Gulu	Uganda	ULU
Gunnison/Crested Butte (CO)	USA	GUC
Guwahati	India	GAU
Gwadar	Pakistan	GWD
Gweru	Zimbabwe	GWE
Gympie	Australia	GYP
Hachijo Jima	Japan	HAC
Hagåtña - Guam International Airport	Guam	GUM
Haifa	Israel	HFA
Haines (AK)	USA	HNS
Hakodate	Japan	HKD
Halifax International	Canada	YHZ
Hall Beach	Canada	YUX
Hamburg - Fuhlsbuettel	Germany	HAM
Hamilton	Australia	HLT
Hamilton	Canada	YHM
Hamilton	New Zealand	HLZ
Hamilton Island	Australia	HTI
Hammerfest	Norway	HFT
Hancock (MI)	USA	CMX
Hangchow (Hangzhou)	Zhejiang, PR China	HGH
Hannover	Germany	HAJ
Hanoi - Noi Bai International Airport	Vietnam	HAN
Harare - Harare International Airport	Zimbabwe	HRE
Harbin (Haerbin)	Heilongjiang, PR China	HRB
Harlingen/South Padre Island (TX)	USA	HRL
Harrington Harbour, PQ	Canada	YHR
Harrisburg (PA) - Harrisburg Skyport	USA	HAR
Harrisburg (PA) - Harrisburg International	USA	MDT
Hartford (CT) /Springfield (MA)	USA	BDL
Hatyai (Hat Yai)	Thailand	HDY
Haugesund	Norway	HAU
Havana - José Martí International	Cuba	HAV
Havre (MT)	USA	HVR
Hayman Island	Australia	HIS
Helena (MT)	USA	HLN
Helsingborg	Sweden	JHE
Helsinki - Vantaa	Finland	HEL
Heraklion	Greece	HER
Hermosillo - Gen. Pesqueira Garcia	Mexico	HMO
Hervey Bay	Australia	HVB
Hibbing (MN)	USA	HIB
Hickory (NC)	USA	HKY
Hilo (HI)	USA	ITO
Hilton Head Island (SC)	USA	HHH
Hinchinbrook Island	Australia	HNK
Hiroshima International	Japan	HIJ
Ho Chi Minh City (Saigon) - Tan Son Nhat International	Viet Nam	SGN
Hobart	Australia	HBA
Hof	Germany	HOQ
Holguin	Cuba	HOG
Home Hill	Australia	HMH
Homer (AK)	USA	HOM
Hong Kong - International Airport (HKIA)	Hong Kong	HKG
Hong Kong - Chek Lap Kok	Hong Kong	ZJK
Honiara Henderson International	Solomon Islands	HIR
Honolulu (HI) - Honolulu International Airport	USA	HNL
Hoonah (AK)	USA	HNH
Horta	Portugal	HOR
Houston (TX) , Hobby	USA	HOU
Houston, TX - George Bush Intercontinental Airport	USA	IAH
Huahine	French Polynesia	HUH
Huatulco	Mexico	HUX
Hue - Phu Bai	Viet Nam	HUI
Humberside	United Kingdom	HUY
Huntington (WV)	USA	HTS
Huntsville (AL)	USA	HSV
Hurghada International	Egypt	HRG
Huron (SD)	USA	HON
Hwange National Park	Zimbabwe	HWN
Hyannis (MA)	USA	HYA
Hydaburg (AK)	USA	HYG
Hyderabad - Rajiv Gandhi International Airport	India	HYD
Hyderabad	Pakistan	HDD
Ibiza	Ibiza/Spain	IBZ
Idaho Falls (ID)	USA	IDA
Iguazu, Cataratas	Argentina	IGR
Ile des Pins	New Caledonia	ILP
Ile Ouen	New Caledonia	IOU
Iliamna (AK)	USA	ILI
Imperial (CA)	USA	IPL
Incercargill	New Zealand	IVC
Incheon, Incheon International Airport	Korea South	ICN
Indianapolis (IN) International	USA	IND
Ingham	Australia	IGH
Innisfail	Australia	IFL
Innsbruck - Kranebitten	Austria	INN
International Falls (MN)	USA	INL
Inuvik	Canada	YEV
Invercargill	New Zealand	IVC
Inverness	United Kingdom	INV
Inykern (CA)	USA	IYK
Iqaluit (Frobisher Bay)	Canada	YFB
Iquitos	Peru	IQT
Irkutsk	Russia	IKT
Ishigaki - New Ishigaki Airport	Japan	ISG
Islamabad - Benazir Bhutto International Airport	Pakistan	ISB
Islay	United Kingdom	ILY
Isle of Man	 	IOM
Istanbul - Istanbul Atatürk Airport	Turkey	IST
Istanbul - Sabiha Gokcen	Turkey	SAW
Ithaca/Cortland (NY)	USA	ITH
Ivalo	Finland	IVL
Ixtapa/Zihuatenejo	Mexico	ZIH
Izmir	Turkey	IZM
Izmir - Adnan Menderes Airport	Turkey	ADB
Jackson Hole (WY)	USA	JAC
Jackson (MI) - Reynolds Municipal	USA	JXN
Jackson,  MN  	USA	MJQ
Jackson (MS) - Jackson Internationall	USA	JAN
Jackson (MS) - Hawkins Field   	USA	HKS
Jackson (TN) - Mckellar	USA	MKL
Jackson Hole (WY)	USA	JAC
Jacksonville (AR)  Little Rock AFB   	USA	LRF
Jacksonville (FL) - Cecil Field NAS   	USA	NZC
Jacksonville (FL) Jacksonville NAS   	USA	NIP
Jacksonville (FL) - International	USA	JAX
Jacksonville (FL) - Craig Municipal   	USA	CRG
Jacksonville (IL) - Municipal Airport	USA	IJX
Jacksonville (NC)	USA	OAJ
Jacksonville (TX)	USA	JKV
Jacmel   	Haiti	JAK
Jacobabad	Pakistan	JAG
Jacobina   	Brazil	JCM
Jacquinot Bay	Papua New Guinea	JAQ
Jaffna - Kankesanturai	Sri Lanka	JAF
Jagdalpur	India	JGB
Jaipur - Sanganeer	India	JAI
Jaisalmer   	India	JSA
Jakarta - Halim Perdana Kusuma	Indonesia	HLP
Jakarta - Metropolitan Area	Indonesia	JKT
Jakarta - Soekarno-Hatta International	Indonesia	CGK
Jalalabad    	Afghanistan	JAA
Jalandhar	India	JLR
Jalapa	Mexico	JAL
Jales	Brazil	JLS
Jaluit Island  	Marshall Islands	UIT
Jamba	Angola	JMB
Jambi - Sultan Taha Syarifudn	Indonesia 	DJB
Jambol	Bulgaria	JAM
Jamestown (ND)	USA	JMS
Jamestown (NY)	USA	JHW
Jammu - Satwari	India	IXJ
Jamnagar - Govardhanpur	India	JGA
Jamshedpur - Sonari Airport	India	IXW
Janakpur	Nepal	JKR
Jandakot	Australia	JAD
Janesville (WI) - Rock County	USA	JVL
Januaria	Brazil	JNA
Jaque   	Panama	JQE
Jatai	Brazil	JTI
Jauja	Peru	JAU
Jayapura - Sentani	Indonesia	DJJ
Jeddah - King Abdulaziz International	Saudi Arabia	JED
Jefferson City (MO) - Jefferson Memorial	USA	JEF
Jeremie - Jeremie Airport	Haiti	JEE
Jerez de la Frontera/Cadiz - La Parra	Spain	XRY
Jersey	Channel Islands	JER
Jerusalem - Atarot Airport (closed)	Israel	JRS
Jessore - Jessore Airport	Bangladesh	JSR
Jeypore - Jeypore Airport	India	PYB
Ji'an	Jiangxi, China	JGS
Jiamusi - Jiamusi Airport	PR China	JMU
Jiayuguan - Jiayuguan Airport	PR China	JGN
Jijel	Algeria	GJL
Jijiga	Ethiopia	JIJ
Jilin	PR China	JIL
Jimma	Ethiopia	JIM
Jinan	Shandong, PR China	TNA
Jingdezhen	PR China	JDZ
Jinghong - Gasa Airport	PR China	JHG
Jining	PR China	JNG
Jinja	Uganda	JIN
Jinjiang	PR China	JJN
Jinka - Baco/Jinka Airport	Ethiopia	BCO
Jinzhou - Jinzhou Airport	PR China	JNZ
Jipijapa	Ecuador	JIP
Jiri	Nepal	JIR
Jiujiang - Jiujiang Lushan Airport	PR China	JIU
Jiwani	Pakistan	JIW
Joacaba	Brazil	JCB
Joao Pessoa - Castro Pinto Airport	Brazil	JPA
Jodhpur	India	JDH
Jönköping (Jonkoping) - Axamo Airport	Sweden	JKG
Joensuu	Finland	JOE
Johannesburg - OR Tambo International Airport	South Africa	JNB
Johnson City (NY) - Binghamton/Endicott/Johnson	USA	BGM
Johnston Island	USA	JON
Johnstown (PA)	USA	JST
Johor Bahru - Sultan Ismail International	Malaysia	JHB
Joinville - Cubatao Airport	Brazil	JOI
Jolo	Philippines	JOL
Jomsom	Nepal	JMO
Jonesboro (AR)  Jonesboro Airport	USA	JBR
Joplin (MO)	USA	JLN
Jorhat - Rowriah Airport	India	JRH
Jos	Nigeria	JOS
Jose De San Martin	Argentina	JSM
Jouf	Saudi Arabia	AJF
Juanjui	Peru	JJI
Juba	South Sudan	JUB
Juist (island)	Germany	JUI
Juiz De Fora - Francisco De Assis Airport	Brazil	JDF
Jujuy - El Cadillal Airport	Argentina	JUJ
Julia Creek	Australia	JCK
Juliaca	Peru	JUL
Jumla	Nepal	JUM
Jundah	Australia	JUN
Juneau (AK) - Juneau International Airport	USA	JNU
Junin	Argentina	JNI
Juticalpa	Honduras	JUT
Jwaneng	Botswana	JWA
Jyväskylä (Jyvaskyla)	Finland	JYV
Kabul - Khwaja Rawash Airport	Afghanistan	KBL
Kagoshima	Japan	KOJ
Kahramanmaras	Turkey	KCM
Kahului (HI)	USA	OGG
Kajaani	Finland	KAJ
Kalamata	Greece	KLX
Kalamazoo/Battle Creek (MI)	USA	AZO
Kalgoorlie	Australia	KGI
Kaliningrad	Russia	KGD
Kalispell (MT)	USA	FCA
Kalmar	Sweden	KLR
Kamloops, BC	Canada	YKA
Kamuela (HI)	USA	MUE
Kano	Nigeria	KAN
Kanpur	India	KNU
Kansas City (MO) - Kansas City International Airport	USA	MCI
Kaohsiung International	Taiwan	KHH
Kapalua West (HI)	USA	JHM
Karachi - Jinnah International Airport	Pakistan	KHI
Karlsruhe-Baden - Soellingen	Germany	FKB
Karlstad	Sweden	KSD
Karpathos	Greece	AOK
Karratha	Australia	KTA
Kars	Turkey	KYS
Karumba	Australia	KRB
Karup	Denmark	KRP
Kaschechawan, PQ	Canada	ZKE
Kassala	Sudan	KSL
Katherine	Australia	KTR
Kathmandu - Tribhuvan International Airport	Nepal	KTM
Katima Mulilo/Mpacha	Namibia	MPA
Kauhajoki	Finland	KHJ
Kaunakakai (HI)	USA	MKK
Kavalla	Greece	KVA
Kayseri	Turkey	ASR
Kazan - Kazan International Airport	Russia	KZN
Keetmanshoop	Namibia	KMP
Kelowna, BC	Canada	YLW
Kemi/Tornio	Finland	KEM
Kenai (AK)	USA	ENA
Kent (Manston) Kent International	United Kingdom	MSE
Kerry County	Ireland	KIR
Ketchikan (AK)	USA	KTN
Key West (FL)	USA	EYW
Khamis Mushayat	Saudi Arabia	AHB
Kharga - New Valley	Egypt	UVL
Kharkov	Ukraine	HRK
Khartoum - Khartoum International Airport	Sudan	KRT
Khuzdar	Pakistan	KDD
Kiel - Holtenau	Germany	KEL
Kiev - Borispol	Ukraine	KBP
Kiev - Zhulhany	Ukraine	IEV
Kigali - Gregoire Kayibanda	Rwanda	KGL
Kilimadjaro	Tanzania	JRO
Killeem (TX)	USA	ILE
Kimberley	South Africa	KIM
King Island	King Island (Australia)	KNS
King Salomon (AK)	USA	AKN
Kingscote	Australia	KGC
Kingston - Norman Manley	Jamaica	KIN
Kingston (NC)	USA	ISO
Kingstown - E. T. Joshua Airport	Saint Vincent and the Grenadines	SVD
Kinshasa - N'Djili	Congo (DRC)	FIH
Kiritimati (island) - Cassidy International Airport	Kiribati	CXI
Kirkenes	Norway	KKN
Kirkuk	Iraq	KIK
Kirkwall (Orkney)	United Kingdom	KOI
Kiruna	Sweden	KRN
Kisangani	Congo (DRC)	FKI
Kittilä	Finland	KTT
Kitwe	Zambia	KIW
Klagenfurt	Austria	KLU
Klamath Fall (OR)	USA	LMT
Klawock (AK)	USA	KLW
Kleinsee	South Africa	KLZ
Knock	Ireland	NOC
Knoxville (TN)	USA	TYS
Kobe	Japan	UKB
Kochi	Japan	KCZ
Köln, Köln/Bonn	Germany	CGN
Kodiak (AK)	USA	ADQ
Kohat	Pakistan	OHT
Kokkola/Pietarsaari	Finland	KOK
Kolkata (Calcutta) - Netaji Subhas Chandra	India	CCU
Komatsu	Japan	KMQ
Kona (HI)	USA	KOA
Konya	Turkey	KYA
Korhogo	Cote d'Ivoire	HGO
Kos	Greece	KGS
Kota Kinabalu	Malaysia	BKI
Kotzbue (AK)	USA	OTZ
Kowanyama	Australia	KWM
Krakow (Cracow) - John Paul II International Airport	Poland	KRK
Kristiansand	Norway	KRS
Kristianstad	Sweden	KID
Kristiansund	Norway	KSU
Kuala Lumpur - International Airport	Malaysia	KUL
Kuala Lumpur - Sultan Abdul Aziz Shah	Malaysia	SZB
Kuantan	Malaysia	KUA
Kuching	Malaysia	KCH
Kumamoto	Japan	KMJ
Kununurra	Australia	KNX
Kuopio	Finland	KUO
Kushiro	Japan	KUH
Kuujjuaq (FortChimo)	Canada	YVP
Kuujjuarapik	Canada	YGW
Kuusamo	Finland	KAO
Kuwait - Kuwait International	Kuwait	KWI
Kyoto	Japan	UKY
Labe	Guinea	LEK
Labouchere Bay (AK)	USA	WLB
Labuan	Malaysia	LBU
Lac Brochet, MB	Canada	XLB
La Coruna	Spain	LCG
La Crosse (WI)	USA	LSE
Lae - Lae Nadzab Airport	Papua New Guinea	LAE
La Rochelle	France	LRH
Lafayette (IN)	USA	LAF
Lafayette, La	USA	LFT
Lagos - Murtala Muhammed Airport	Nigeria	LOS
La Grande	Canada	YGL
Lahore	Pakistan	LHE
Lake Charles (LA)	USA	LCH
Lake Havasu City (AZ)	USA	HII
Lake Tahoe (CA)	USA	TVL
Lakselv	Norway	LKL
Lambarene	Gabon	LBQ
Lamezia Terme	Italy	SUF
Lampedusa	Italy	LMP
Lanai City (HI)	USA	LNY
Lancaster (PA)	USA	LNS
Land's End	United Kingdom	LEQ
Langkawi (islands)	Malaysia	LGK
Lannion	France	LAI
Lanseria	South Africa	HLA
Lansing (MI)	USA	LAN
La Paz - El Alto	Bolivia	LPB
La Paz - Leon	Mexico	LAP
Lappeenranta	Finland	LPP
Laramie (WY)	USA	LAR
Laredo (TX)	USA	LRD
Larnaca	Cyprus	LCA
Las Palmas	Spain	LPA
Las Vegas (NV)	USA	LAS
Latrobe (PA)	USA	LBE
Launceston	Australia	LST
Laurel/Hattisburg (MS)	USA	PIB
Laverton	Australia	LVO
Lawton (OK)	USA	LAW
Lazaro Cardenas	Mexico	LZC
Leaf Rapids	Canada	YLR
Learmouth (Exmouth)	Australia	LEA
Lebanon (NH)	USA	LEB
Leeds/Bradford	United Kingdom	LBA
Leinster	Australia	LER
Leipzig	Germany	LEJ
Lelystad	Netherlands	LEY
Leon	Mexico	BJX
Leonora	Australia	LNO
Lerwick/Tingwall (Shetland Islands)	United Kingdom	LWK
Lewiston (ID)	USA	LWS
Lewistown (MT)	USA	LWT
Lexington (KY)	USA	LEX
Libreville	Gabon	LBV
Lidkoeping	Sweden	LDK
Liege	Belgium	LGG
Lifou	Loyaute, Pazifik	LIF
Lihue (HI)	USA	LIH
Lille - Lille Airport	France	LIL
Lilongwe - Lilongwe International	Malawi	LLW
Lima - J Chavez International	Peru	LIM
Limassol	Cyprus	QLI
Limoges	France	LIG
Lincoln (NE)	USA	LNK
Lindeman Island	Australia	LDC
Linz - Hoersching	Austria	LNZ
Lisala	Congo (DRC)	LIQ
Lisbon - Lisboa	Portugal	LIS
Lismore	Australia	LSY
Little Rock (AR)	USA	LIT
Liverpool	United Kingdom	LPL
Lizard Island	Australia	LZR
Ljubljana - Brnik	Slovenia	LJU
Lockhart River	Australia	IRG
Lome	Togo	LFW
London	Canada	YXU
London Metropolitan Area	United Kingdom	LON
London - City Airport	United Kingdom	LCY
London - Gatwick	United Kingdom	LGW
London - Heathrow	United Kingdom	LHR
London - Luton	United Kingdom	LTN
London - Stansted	United Kingdom	STN
Londonderry - Eglinton	United Kingdom	LDY
Long Beach (CA)	USA	LGB
Long Island (AK)	USA	LIJ
Long Island, Islip (NY) - Mac Arthur	USA	ISP
Longreach	Australia	LRE
Longview/Kilgore (TX)	USA	GGG
Longyearbyen - Svalbard	Svalbard/Norway	LYR
Loreto	Mexico	LTO
Lorient	France	LRT
Los Angeles (CA) - International	USA	LAX
Los Cabos	Mexico	SJD
Los Mochis	Mexico	LMM
Los Rodeos	Teneriffa/Spain	TFN
Losinj - Losinj Arpt	Croatia (Hrvatska)	LSZ
Lourdes/Tarbes	France	LDE
Louisville (KY)	USA	SDF
Luanda - 4 de Fevereiro	Angola	LAD
Lubbock (TX)	USA	LBB
Lucknow	India	LKO
Luederitz	Namibia	LUD
Luga	Malta	MLA
Lugano	Switzerland	LUG
Lulea	Sweden	LLA
Lumbumbashi	Congo (DRC)	FBM
Lusaka - Lusaka International Airport	Zambia	LUN
Lusisiki	South Africa	LUJ
Luxembourg	Luxembourg	LUX
Luxi - Mangshi	Yunnan, PR China	LUM
Luxor	Egypt	LXR
Lvov (Lwow, Lemberg)	Ukraine	LWO
Lydd - Lydd International Airport	United Kingdom	LYX
Lynchburg (VA)	USA	LYH
Lyon - Lyon-Saint Exupéry Airport official website	France	LYS
Lyons (KS) - Rice County Municipal	USA	LYO
Maastricht/Aachen	Netherlands	MST
Macapa - Alberto Alcolumbre International Airport	Brazil	MCP
Macau - Macau International Airport	Macau, China SAR	MFM
Maceio - Zumbi dos Palmares International Airport	Brazil	MCZ
Mackay	Australia	MKY
Macon (GA)	USA	MCN
Mactan Island - Nab	Philippines	NOP
Madinah (Medina) - Mohammad Bin Abdulaziz	Saudi Arabia	MED
Madison (WI) - Dane County Regional Airport	USA	MSN
Madras (Chennai) - Chennai International Airport	India	MAA
Madrid - Barajas Airport	Spain	MAD
Mahe - Seychelles International	Seychelles	SEZ
Mahon	Spain	MAH
Maitland	Australia	MTL
Majunga	Madagascar	MJN
Makung	Taiwan	MZG
Malabo - Malabo International Airport	Equatorial Guinea	SSG
Malaga	Spain	AGP
Malatya	Turkey	MLX
Male - Velana International Airport	Maledives	MLE
Malindi	Kenya	MYD
Malmo (Malmoe)	Sweden	MMA
Malmo (Malmö) - Malmö Airport	Sweden	MMX
Man	Cote d'Ivoire	MJC
Managua - Augusto C Sandino	Nicaragua	MGA
Manaus - Eduardo Gomes International Airport	Brazil	MAO
Manchester	United Kingdom	MAN
Manchester (NH)	USA	MHT
Mandalay - Mandalay-Annisaton Airport	Myanmar	MDL
Manguna	Papua New Guinea	MFO
Manihi	French Polynesia	XMH
Manila - Ninoy Aquino International	Philippines	MNL
Manzanillo	Mexico	ZLO
Manzini - Matsapha International	Swaziland	MTS
Maputo - Maputo International	Mozambique	MPM
Mar del Plata	Argentina	MDQ
Maracaibo - La Chinita International	Venezuela	MAR
Maradi	Niger	MFQ
Maras	Turkey	KCM
Marathon (FL)	USA	MTH
Mardin	Turkey	MQM
Mare	New Caledonia	MEE
Margate	South Africa	MGH
Margerita	Venezuela	PMV
Maribor	Slovenia	MBX
Mariehamn (Maarianhamina)	Finland	MHQ
Maroua	Cameroon	MVR
Marquette (MI)	USA	MQT
Marrakesh - Menara Airport	Morocco	RAK
Marsa Alam	Egypt	RMF
Marsa Matrah (Marsa Matruh)	Egypt	MUH
Marseille - Marseille Provence Airport	France	MRS
Marsh Harbour	Bahamas	MHH
Martha's Vineyard (MA)	USA	MVY
Martinsburg (WV)	USA	MRB
Maryborough	Australia	MBH
Maseru - Moshoeshoe International	Lesotho	MSU
Mason City IA	USA	MCW
Masvingo	Zimbabwe	MVZ
Matsumoto, Nagano	Japan	MMJ
Matsuyama	Japan	MYJ
Mattoon (IL)	USA	MTO
Maun	Botswana	MUB
Maupiti	French Polynesia	MAU
Mauritius - S.Seewoosagur Ram International	Mauritius	MRU
Mayaguez	Puerto Rico	MAZ
Mazatlan	Mexico	MZT
McAllen (TX)	USA	MFE
Medan - Polania Int'l (now Soewondo AFB)	Indonesia	MES
Medan - Kualanamu International	Indonesia	KNO
Medellin - José María Córdova International	Colombia	MDE
Medford (OR)	USA	MFR
Medina	Saudi Arabia	MED
Meekatharra	Australia	MKR
Melbourne - Melbourne Airport (Tullamarine)	Australia	MEL
Melbourne (FL)	USA	MLB
Melville Hall	Dominica	DOM
Memphis (TN)	USA	MEM
Mendoza	Argentina	MDZ
Manado	Indonesia	MDC
Merced (CA)	USA	MCE
Merida	Mexico	MID
Meridian (MS)	USA	MEI
Merimbula	Australia	MIM
Messina	South Africa	MEZ
Metlakatla (AK)	USA	MTM
Metz -  Frescaty	France	MZM
Metz/Nancy Metz-Nancy-Lorraine	France	ETZ
Mexicali	Mexico	MXL
Mexico City - Mexico City International Airport	Mexico	MEX
Mexico City - Atizapan	Mexico	AZP
Mexico City - Juarez International	Mexico	MEX
Mexico City - Santa Lucia	Mexico	NLU
Mfuwe	Zambia	MFU
Miami (FL)	USA	MIA
Mianwali	Pakistan	MWD
Middlemount	Australia	MMM
Midland/Odessa (TX)	USA	MAF
Midway Island - Sand Island Field	US Minor Outlying Islands	MDY
Mikkeli	Finland	MIK
Milan	Italy	MIL
Milan - Linate	Italy	LIN
Milan - Malpensa	Italy	MXP
Milan - Orio Al Serio	Italy	BGY
Mildura	Australia	MQL
Miles City (MT)	USA	MLS
Milford Sound	New Zealand	MFN
Milwaukee (WI)	USA	MKE
Minatitlan	Mexico	MTT
Mineralnye Vody	Russia	MRV
Minneapolis - St. Paul International Airport (MN)	USA	MSP
Minot (ND)	USA	MOT
Minsk, International	Belarus	MSQ
Miri	Malaysia	MYY
Mirpur	Pakistan	QML
Missula (MT)	USA	MSO
Mitchell (SD)	USA	MHE
Miyako Jima (Ryuku Islands) - Hirara	Japan	MMY
Miyazaki	Japan	KMI
Mkambati	South Africa	MBM
Moanda	Gabon	MFF
Mobile (AL) - Pascagoula (MS)	USA	MOB
Modesto (CA)	USA	MOD
Moenjodaro	Pakistan	MJD
Mogadishu	Somalia	MGQ
Mokuti	Namibia	OKU
Moline/Quad Cities (IL)	USA	MLI
Mombasa - Moi International	Kenya	MBA
Monastir	Tunisia	MIR
Moncton	Canada	YQM
Monroe (LA)	USA	MLU
Monrovia - Metropolitan Area	Liberia	MLW
Monrovia - Roberts International	Liberia	ROB
Montego Bay - Sangster International	Jamaica	MBJ
Montenegro	Brazil	QGF
Monterey (CA)	USA	MRY
Monterrey - Gen. Mariano Escobedo	Mexico	MTY
Monterrey - Aeropuerto Del Norte	Mexico	NTR
Montevideo - Carrasco International Airport	Uruguay	MVD
Montgomery (AL) - Montgomery Regional Airport	USA	MGM
Montpellier - Montpellier–Méditerranée Airport	France	MPL
Montreal	Canada	YMQ
Montreal - Dorval (Montréal-Trudeau)	Canada	YUL
Montreal - Mirabel	Canada	YMX
Montrose/Tellruide (CO)	USA	MTJ
Moorea	French Polynesia	MOZ
Moranbah	Australia	MOV
Moree	Australia	MRZ
Morelia	Mexico	MLM
Morgantown (WV)	USA	MGW
Morioka, Hanamaki	Japan	HNA
Moroni - Prince Said Ibrahim	Comoros (Comores)	HAH
Moruya	Australia	MYA
Moscow - Metropolitan Area	Russia	MOW
Moscow - Domodedovo	Russia	DME
Moscow - Sheremetyevo	Russia	SVO
Moscow - Vnukovo	Russia	VKO
Moses Lake (WA)	USA	MWH
Mossel Bay	South Africa	MZY
Mostar	Bosnia and Herzegovina	OMO
Mosul	Iraq	OSM
Mouila	Gabon	MJL
Moundou	Chad	MQQ
Mount Cook	New Zealand	GTN
Mount Gambier	Australia	MGB
Mount Magnet	Australia	MMG
Mt. Isa	Australia	ISA
Mt. McKinley (AK)	USA	MCL
Muenchen (Munich) - Franz Josef Strauss	Germany	MUC
Muenster/Osnabrueck	Germany	FMO
Mulhouse	France	MLH
Multan	Pakistan	MUX
Murcia	Spain	MJV
Murmansk	Russia	MMK
Mus	Turkey	MSR
Muscat - Seeb	Oman	MCT
Muscle Shoals (AL)	USA	MSL
Muskegon (MI)	USA	MKG
Muzaffarabad	Pakistan	MFG
Mvengue	Gabon	MVB
Mykonos	Greece	JMK
Myrtle Beach (SC) - Myrtle Beach AFB	USA	MYR
Myrtle Beach (SC) - Grand Strand Airport	USA	CRE
Mysore	India	MYQ
Mytilene (Lesbos)	Greece	MJT
Mzamba	South Africa	MZF
Nadi	Fiji	NAN
Nagasaki	Japan	NGS
Nagoya - Komaki AFB	Japan	NGO
Nagpur	India	NAG
Nairobi	Kenya	NBO
Nakhichevan	Azerbaijan	NAJ
Nakhon Si Thammarat	Thailand	NST
Nancy	France	ENC
Nanisivik	Canada	YSR
Nanning	Guangxi, PR China	NNG
Nantes - Nantes Atlantique Airport	France	NTE
Nantucket (MA)	USA	ACK
Naples - Naples Capodichino Airport	Italy	NAP
Naples (FL)	USA	APF
Narrabri	Australia	NAA
Narrandera	Australia	NRA
Narsarsuaq	Greenland	UAK
Nashville (TN)	USA	BNA
Nassau	Bahamas	NAS
Natal - Augusto Severo International Airport	Brazil	NAT
Nausori	Fiji/Suva	SUV
Nawab Shah	Pakistan	WNS
Naxos - Naxos Airport	Greece	JNX
N'Djamena	Chad	NDJ
N'Dola	Zambia	NLA
Nelson	New Zealand	NSN
Nelspruit	South Africa	NLP
Nelspruit - Kruger Mpumalanga International Airport	South Africa	MQP
Nevis	St. Kitts and Nevis	NEV
New Bern (NC)	USA	EWN
New Haven (CT)	USA	HVN
New Orleans, La	USA	MSY
Newquay	United Kingdom	NQY
New Valley - Kharga	Egypt	UVL
New York - John F. Kennedy (NY)	USA	JFK
New York - LaGuardia (NY)	USA	LGA
New York - Newark (NJ)	USA	EWR
New York (NY)	USA	NYC
Newburgh (NY)	USA	SWF
Newcastle - Belmont	Australia	BEO
Newcastle - Williamtown	Australia	NTL
Newcastle	United Kingdom	NCL
Newcastle	South Africa	NCS
Newman	Australia	ZNE
Newport News/Williamsburg (VA)	USA	PHF
N'Gaoundere	Cameroon	NGE
Niagara Falls International	USA	IAG
Niamey	Niger	NIM
Nice - Cote D'Azur Airport	France	NCE
Nicosia	Cyprus	NIC
Nikolaev	Ukraine	NLV
Niigata	Japan	KIJ
Nimes	France	FNI
Nis	Serbia	INI
Nizhny Novgorod - Strigino International Airport	Russia	GOJ
Nome (AK)	USA	OME
Noosa	Australia	NSA
Norfolk Island	Australia	NLK
Norfolk/Virginia Beach (VA)	USA	ORF
Norman Wells	Canada	YVQ
Norrkoeping	Sweden	NRK
North Bend (OR)	USA	OTH
North Eleuthera	Bahamas	ELH
Norwich	United Kingdom	NWI
Nottingham - East Midlands	United Kingdom	EMA
Nouadhibou	Mauritania	NDB
Nouakchott	Mauritania	NKC
Noumea	New Caledonia	NOU
Novi Sad	Serbia	QND
Novosibirsk - Tolmachevo Airport	Russia	OVB
Nürnberg (Nuremberg)	Germany	NUE
Nuevo Laredo	Mexico	NLD
Nuku'alofa - Fua'Amotu International	Tonga	TBU
Oakland (CA)	USA	OAK
Oaxaca - Xoxocotlan	Mexico	OAX
Odense	Denmark	ODE
Odessa	Ukraine	ODS
Oerebro	Sweden	ORB
Ohrid	Macedonia	OHD
Oita	Japan	OIT
Okayama	Japan	OKJ
Okinawa, Ryukyo Island - Naha	Japan	OKA
Oklahoma City (OK) - Will Rogers World	USA	OKC
Olbia	Italy	OLB
Olympic Dam	Australia	OLP
Omaha (NE)	USA	OMA
Ondangwa	Namibia	OND
Ontario (CA)	USA	ONT
Oran (Ouahran)	Algeria	ORN
Orange	Australia	OAG
Orange County (Santa Ana) (CA)	USA	SNA
Oranjemund	Namibia	OMD
Oranjestad - Reina Beatrix International	Aruba	AUA
Orkney - Kirkwall	United Kingdom	KOI
Orlando Metropolitan Area (FL)	USA	ORL
Orlando - International Airport (FL)	USA	MCO
Orpheus Island	Australia	ORS
Osaka, Metropolitan Area	Japan	OSA
Osaka - Itami	Japan	ITM
Osaka - Kansai International Airport	Japan	KIX
Oshkosh (WI)	USA	OSH
Osijek	Croatia (Hrvatska)	OSI
Oslo - Oslo Airport, Gardermoen	Norway	OSL
Oslo - Fornebu	Norway	FBU
Oslo - Sandefjord	Norway	TRF
Ottawa - Hull	Canada	YOW
Ouadda	Central African Republic	ODA
Ouarzazate	Morocco	OZZ
Oudtshoorn	South Africa	OUH
Ouagadougou	Burkina Faso	OUA
Oujda	Morocco	OUD
Oulu	Finland	OUL
Out Skerries (Shetland)	United Kingdom	OUK
Oviedo	Spain	OVD
Owensboro (KY)	USA	OWB
Oxnard (CA)	USA	OXR
Oyem	Gabon/Loyautte	UVE
Paderborn/Lippstadt	Germany	PAD
Paducah (KY)	USA	PAH
Page/Lake Powell (AZ)	USA	PGA
Pago Pago	American Samoa	PPG
Pakersburg (WV) /Marietta (OH)	USA	PKB
Palermo - Punta Raisi	Italy	PMO
Palma de Mallorca	Spain	PMI
Palmas	Brazil	PMW
Palmdale/Lancaster (CA)	USA	PMD
Palmerston North	New Zealand	PMR
Palm Springs (CA)	USA	PSP
Panama City - Tocumen International	Panama	PTY
Panama City (FL)	USA	PFN
Panjgur	Pakistan	PJG
Pantelleria	Italy	PNL
Papeete - Faaa	French Polynesia (Tahiti)	PPT
Paphos	Cyprus	PFO
Paraburdoo	Australia	PBO
Paramaribo - Zanderij International	Suriname	PBM
Paris	France	PAR
Paris - Charles de Gaulle	France	CDG
Paris - Le Bourget	France	LBG
Paris - Orly	France	ORY
Paro	Bhutan	PBH
Pasco (WA)	USA	PSC
Pasni	Pakistan	PSI
Patna	India	PAT
Pattaya	Thailand	PYX
Pau	France	PUF
Pellston (MI)	USA	PLN
Penang International	Malaysia	PEN
Pendelton (OR)	USA	PDT
Pensacola (FL)	USA	PNS
Peoria/Bloomington (IL)	USA	PIA
Pereira	Colombia	PEI
Perpignan	France	PGF
Perth International	Australia	PER
Perugia	Italy	PEG
Pescara	Italy	PSR
Peshawar	Pakistan	PEW
Petersburg (AK)	USA	PSG
Phalaborwa	South Africa	PHW
Philadelphia (PA) - International	USA	PHL
Phnom Penh - Pochentong	Cambodia	PNH
Phoenix (AZ) - Sky Harbor International	USA	PHX
Phuket	Thailand	HKT
Pierre (SD)	USA	PIR
Pietermaritzburg	South Africa	PZB
Pietersburg	South Africa	PTG
Pilanesberg/Sun City	South Africa	NTY
Pisa - Galileo Galilei	Italy	PSA
Pittsburgh International Airport (PA)	USA	PIT
Plattsburgh (NY)	USA	PLB
Plettenberg Bay	South Africa	PBZ
Pocatello (ID)	USA	PIH
Podgorica	Montenegro	TGD
Pohnpei	Micronesia	PNI
Pointe a Pitre	Guadeloupe	PTP
Pointe Noire	Congo (ROC)	PNR
Poitiers - Biard	France	PIS
Ponce	Puerto Rico	PSE
Ponta Delgada	Portugal	PDL
Pori	Finland	POR
Port Angeles (WA)	USA	CLM
Port au Prince	Haiti	PAP
Port Augusta	Australia	PUG
Port Elizabeth	South Africa	PLZ
Port Gentil	Gabon	POG
Port Harcourt	Nigeria	PHC
Port Hedland	Australia	PHE
Portland	Australia	PTJ
Portland (ME)	USA	PWM
Portland International (OR)	USA	PDX
Port Lincoln	Australia	PLO
Port Macquarie	Australia	PQQ
Port Menier, PQ	Canada	YPN
Port Moresby - Jackson Field	Papua New Guinea	POM
Porto	Portugal	OPO
Porto Alegre - Salgado Filho International Airport	Brazil	POA
Port of Spain - Piarco International	Trinidad and Tobago	POS
Port Said	Egypt	PSD
Porto Santo	Portugal	PXO
Porto Velho	Brazil	PVH
Port Vila	Vanuatu	VLI
Poughkeepsie (NY)	USA	POU
Poznan, Lawica	Poland	POZ
Prague - Václav Havel Airport (formerly Ruzyne)	Czech Republic	PRG
Praia - Nelson Mandela International Airport	Cape Verde	RAI
Presque Island (ME)	USA	PQI
Pretoria - Wonderboom Apt.	South Africa	PRY
Preveza/Lefkas	Greece	PVK
Prince George	Canada	YXS
Prince Rupert/Digby Island	Canada	YPR
Pristina	Serbia	PRN
Prosperpine	Australia	PPP
Providence (RI)	USA	PVD
Prudhoe Bay (AK)	USA	SCC
Puebla	Mexico	PBC
Pueblo (CO)	USA	PUB
Puerto Escondido	Mexico	PXM
Puerto Ordaz	Venezuela	PZO
Puerto Plata	Dominican Republic	POP
Puerto Vallarta	Mexico	PVR
Pukatawagan	Canada	XPK
Pula	Croatia (Hrvatska)	PUY
Pullman (WA)	USA	PUW
Pune	India, Maharashtra	PNQ
Punta Arenas - Presidente Carlos Ibáñez del Campo	Chile	PUQ
Punta Cana - Punta Cana International	Dominican Republic	PUJ
Pu San (Busan) - Gimhae International Airport	South Korea	PUS
Pyongyang - Sunan International Airport	North Korea	FNJ
 
Q
Quebec - Quebec International	Canada	YQB
Queenstown	Australia	UEE
Queenstown	New Zealand	ZQN
Quetta	Pakistan	UET
Qingdao	Shandong, PR China	TAO
Quimper	France	UIP
Quincy (IL)	USA	UIN
Quito - Mariscal Sucre International Airport	Ecuador	UIO
Rabat - Rabat-Salé Airport	Morocco	RBA
Rahim Yar Khan - Shaikh Zayed International Airport	Pakistan	RYK
Raiatea	French Polynesia	RFP
Rainbow Lake, AB	Canada	YOP
Rajkot	India	RAJ
Raleigh/Durham (NC)	USA	RDU
Ranchi	India	IXR
Rangiroa	French Polynesia	RGI
Rangoon (Yangon) - Mingaladon	Myanmar	RGN
Rapid City (SD)	USA	RAP
Rarotonga	Cook Island	RAR
Ras al Khaymah (Ras al Khaimah)	United Arab Emirates	RKT
Rawala Kot	Pakistan	RAZ
Rawalpindi	Pakistan	RWP
Reading (PA)	USA	RDG
Recife - Guararapes-Gilberto Freyre International	Brazil	REC
Redding (CA)	USA	RDD
Redmond (OR)	USA	RDM
Reggio Calabria	Italy	REG
Regina	Canada	YQR
Reina Sofia	Teneriffa/Spain	TFS
Rennes	France	RNS
Reno (NV)	USA	RNO
Resolute Bay	Canada	YRB
Reus	Spain	REU
Reykjavik - Metropolitan Area	Iceland	REK
Reykjavik - Keflavik International	Iceland	KEF
Rhinelander (WI)	USA	RHI
Rhodos	Greece	RHO
Richards Bay	South Africa	RCB
Richmond (VA)	USA	RIC
Riga	Latvia	RIX
Rijeka	Croatia (Hrvatska)	RJK
Rimini	Italy	RMI
Rio Branco - Plácido de Castro International Airport	Brazil	RBR
Rio de Janeiro - Galeao	Brazil	GIG
Rio de Janeiro - Santos Dumont	Brazil	SDU
Rio de Janeiro	Brazil	RIO
Riyadh - King Khaled International	Saudi Arabia	RUH
Roanne	France	RNE
Roanoke (VA)	USA	ROA
Roatan	Honduras	RTB
Rochester (MN)	USA	RST
Rochester (NY)	USA	ROC
Rock Sound	Bahamas	RSD
Rock Springs (WY)	USA	RKS
Rockford (IL)	USA	RFD
Rockhampton	Australia	ROK
Rockland (ME)	USA	RKD
Rocky Mount - Wilson (NC)	USA	RWI
Rodez	France	RDZ
Rodrigues Island	Mauritius	RRG
Roenne	Denmark	RNN
Rome	Italy	ROM
Rome - Ciampino	Italy	CIA
Rome - Fuimicino	Italy	FCO
Ronneby	Sweden	RNB
Rosario	Argentina	ROS
Rostov-on-Don - Rostov-on-Don Airport	Russia	RVI
Rostov-on-Don - Platov International Airport	Russia	ROV
Rotorua	New Zealand	ROT
Rotterdam	Netherlands	RTM
Rovaniemi	Finland	RVN
Rundu	Namibia	NDU
Ruse	Bulgaria	ROU
Saarbruecken	Germany	SCN
Sacramento (CA)	USA	SMF
Sado Shima	Japan	SDS
Saginaw/Bay City/Midland (MI)	USA	MBS
Saidu Sharif	Pakistan	SDT
Saigon (Ho Chi Minh City) - Tan Son Nhat International	Viet Nam	SGN
Saint Brieuc	France	SBK
Saint Denis - Roland Garros Airport	Reunion	RUN
Saint John	Canada	YSJ
Saipan	Northern Mariana Islands	SPN
Sal	Cape Verde	SID
Salalah	Oman	SLL
Salem (OR)	USA	SLE
Salinas (CA)	USA	SNS
Salinas	Ecuador	SNC
Salisbury	Zimbabwe	SAY
Salisbury (MD)	USA	SBY
Saloniki	Greece	SKG
Salta, Gen Belgrano	Argentina	SLA
Salt Lake City (UT)	USA	SLC
Salvador - Salvador International Airport	Brazil	SSA
Salzburg - W.A. Mozart	Austria	SZG
Samara - Kurumoch International Airport	Russia	KUF
Samarkand - Samarkand International Airport	Uzbekistan	SKD
Samos	Greece	SMI
Samsun	Turkey	SZF
San Andres	Colombia	ADZ
San Angelo (TX)	USA	SJT
San Antonio (TX)	USA	SAT
San Carlos de Bariloche	Argentina	BRC
San Diego - Lindberg Field International (CA)	USA	SAN
San Francisco - International Airport, SA	USA	SFO
San Jose Cabo	Mexico	SJD
San Jose	Costa Rica	SJO
San Jose (CA)	USA	SJC
San Juan - Luis Munoz Marin International Airport	Puerto Rico	SJU
San Luis Obisco (CA)	USA	SBP
San Luis Potosi	Mexico	SLP
San Pedro	Cote d'Ivoire	SPY
San Pedro Sula	Honduras	SAP
San Salvador	Bahamas	ZSA
San Salvador	El Salvador	SAL
San Sebastian	Spain	EAS
Sanaa (Sana'a) - Sana'a International	Yemen	SAH
Sandspit	Canada	YZP
Santa Ana - John Wayne Airport (CA)	USA	SNA
Santa Barbara (CA)	USA	SBA
Santa Cruz de la Palma	Spain	SPC
Santa Cruz de la Sierra	Bolivia	SRZ
Santa Katarina - Mount Sinai	Egypt	SKV
Santa Maria	Portugal	SMA
Santa Maria (CA)	USA	SMX
Santander	Spain	SDR
Santa Rosa (CA)	USA	STS
Santa Rosa	Bolivia	SRB
Santa Rosa	Brazil	SRA
Santa Rosa	Argentina	RSA
Santa Rosa, Copan	Honduras	SDH
Santa Rosalia	Colombia	SSL
Santa Rosalia	Mexico	SRL
Santiago - Antonio Maceo Airport	Cuba	SCU
Santiago de Chile - Arturo Merino Benitez	Chile	SCL
Santiago de Compostela	Spain	SCQ
Santo	Vanuatu	SON
Santo Domingo	Dominican Republic	SDQ
Sao Luis - Marechal Cunha Machado International	Brazil	SLZ
Sao Paulo	Brazil	SAO
Sao Paulo - Congonhas	Brazil	CGH
Sao Paulo - Guarulhos	Brazil	GRU
Sao Paulo - Viracopos	Brazil	VCP
Sao Tome	Sao Tome & Principe	TMS
Sapporo	Hokkaido, Japan	SPK
Sapporo - Okadama	Hokkaido, Japan	OKD
Sapporo - New Chitose Airport	Japan	CTS
Sarajevo	Bosnia and Herzegovina	SJJ
Saransk - Saransk Airport	Russia	SKX
Sarasota/Bradenton (FL)	USA	SRQ
Saskatoon	Canada	YXE
Sassandra	Cote d'Ivoire	ZSS
Savannah (GA)	USA	SAV
Savonlinna	Finland	SVL
Scarborough - Crown Point International	Trinidad and Tobago	TAB
Scone	Australia	NSO
Scottsdale (AZ)	USA	SCF
Seattle/Tacoma (WA)	USA	SEA
Sehba	Libya	SEB
Seinaejoki	Finland	SJY
Selibi Phikwe	Botswana	PKW
Sendai	Japan	SDJ
Seoul - Incheon International Airport	South Korea	ICN
Seoul - Kimpo	South Korea	SEL
Sevilla	Spain	SVQ
Sfax	Tunisia	SFA
Shamattawa, MB	Canada	ZTM
Shanghai - Hongqiao	China	SHA
Shanghai - Pu Dong	China	PVG
Shannon (Limerick)	Ireland	SNN
Sharjah	United Arab Emirates	SHJ
Sharm El Sheikh	Egypt	SSH
Sheffield, City Airport	United Kingdom	SZD
Sheffield, Doncaster, Robin Hood International Airport	United Kingdom	DSA
Shenandoah Valley/Stauton (VA)	USA	SHD
Shenyang	Liaoning, PR China	SHE
Shenzhen - Shenzhen Bao'an International	Guangdong, PR China	SZX
Sheridan (WY)	USA	SHR
Shreveport, La	USA	SHV
Shute Harbour	Australia	JHQ
Sibu	Malaysia	SBW
Sidney (MT)	USA	SDY
Silistra	Bulgaria	SLS
Simferopol	Ukraine	SIP
Sindhri	Pakistan	MPD
Singapore - Changi	Singapore	SIN
Singapore - Paya Lebar	Singapore	QPG
Singapore - Seletar	Singapore	XSP
Singleton	Australia	SIX
Sioux City IA	USA	SUX
Sioux Falls (SD)	USA	FSD
Sishen	South Africa	SIS
Sitka (AK)	USA	SIT
Sivas	Turkey	VAS
Siwa	Egypt	SEW
Skagway (AK)	USA	SGY
Skardu	Pakistan	KDU
Skiathos	Greece	JSI
Skopje	Macedonia	SKP
Skrydstrup	Denmark	SKS
Skukuza	South Africa	SZK
Sligo	Ireland	SXL
Smithers	Canada	YYD
Sodankylae	Finland	SOT
Soenderborg	Denmark	SGD
Soendre Stroemfjord	Greenland	SFJ
Sofia - Vrazhdebna	Bulgaria	SOF
Sogndal	Norway	SOG
Southampton - Eastleigh	United Kingdom	SOU
South Bend (IN)	USA	SBN
South Indian Lake, MB	Canada	XSI
South Molle Island	Australia	SOI
Southend (London)	United Kingdom	SEN
Split	Croatia (Hrvatska)	SPU
Spokane (WA)	USA	GEG
Springbok	South Africa	SBU
Springfield (IL)	USA	SPI
Springfield (MO)	USA	SGF
Srinagar	India	SXR
St. Augustin, PQ	Canada	YIF
St. Croix	Virgin Islands (U.S.)	STX
St. Etienne	France	EBU
St. George (UT)	USA	SGU
St. John's	Canada	YYT
St. Kitts	St. Kitts and Nevis	SKB
St. Louis (MO) Lambert–St. Louis International Airport	USA	STL
St. Lucia Hewanorra	Saint Lucia	UVF
St. Lucia Vigle	Saint Lucia	SLU
St. Marteen	Netherlands Antilles	SXM
St. Martin	St. Martin (Guadeloupe)	SFG
St. Petersburg (Leningrad) - Pulkovo	Russia	LED
St. Pierre, NF	Canada	FSP
St. Thomas	Virgin Islands (U.S.)	STT
St. Vincent	Saint Vincent and the Grenadines	SVD
Stansted (London)	United Kingdom	STN
State College/Belefonte (PA)	USA	SCE
Stavanger	Norway	SVG
Steamboat Springs (CO)	USA	HDN
Stettin	Poland	SZZ
Stockholm Metropolitan Area	Sweden	STO
Stockholm - Arlanda	Sweden	ARN
Stockholm - Bromma	Sweden	BMA
Stockton (CA)	USA	SCK
Stornway	United Kingdom	SYY
Strasbourg - Strasbourg Airport	France	SXB
Streaky Bay	Australia	KBY
Stuttgart - Echterdingen	Germany	STR
Sui	Pakistan	SUL
Sukkur	Pakistan	SKZ
Sumburgh (Shetland)	United Kingdom	LSI
Sun Valley (ID)	USA	SUN
Sundsvall	Sweden	SDL
Sunshine Coast	Australia	MCY
Surabaya - Juanda	Indonesia	SUB
Surat	India	STV
Suva - Nausori Airport (Luvuluvu)	Fiji	SUV
Swakopmund	Namibia	SWP
Sydney - Sydney Airport	Australia	SYD
Sylhet	Bangladesh	ZYL
Syracuse (NY)	USA	SYR
Tabuk	Saudi Arabia	TUU
Taif	Saudi Arabia	TIF
Taipei - Chiang Kai Shek	Taiwan	TPE
Taipei - Sung Shan	Taiwan	TAY
Taiyuan	Shanxi, PR China	TYN
Takamatsu	Japan	TAK
Talkeetna (AK)	USA	TKA
Tallahassee (FL)	USA	TLH
Tallinn - Pirita Harbour	Estonia	QUF
Tallinn - Ulemiste	Estonia	TLL
Tampa - International (FL)	USA	TPA
Tampere	Finland	TMP
Tampico - Gen. F. Javier Mina	Mexico	TAM
Tamworth	Australia	TMW
Tangier - Boukhalef	Morocco	TNG
Taree	Australia	TRO
Targovishte	Bulgaria	TGV
Tashkent - International	Uzbekistan	TAS
Tawau	Malaysia	TWU
Tbilisi - Novo Alexeyevka	Georgia	TBS
Te Anau	New Zealand	TEU
Teesside, Durham Tees Valley	United Kingdom	MME
Tegucigalpa	Honduras	TGU
Tehran (Teheran) - Mehrabad	Iran	THR
Tekirdag - Corlu	Turkey	TEQ
Tel Aviv - Ben Gurion International	Israel	TLV
Telluride (CO)	USA	TEX
Temora	Australia	TEM
Tenerife	Spain	TCI
Tenerife - Sur Reina Sofia	Spain	TFS
Tenerife - Norte Los Rodeos	Spain	TFN
Tennant Creek	Australia	TCA
Terceira	Portugal	TER
Teresina	Brazil	THE
Termez (Termes)	Uzbekistan	TMZ
Terrace	Canada	YXT
Terre Haute (IN)	USA	HUF
Texarkana (AR)	USA	TXK
Thaba'Nchu	South Africa	TCU
The Pas	Canada	YQD
Thessaloniki - Makedonia Apt.	Greece	SKG
Thief River Falls (MN)	USA	TVF
Thira	Greece	JTR
Thiruvananthapuram	India	TRV
Thisted	Denmark	TED
Thompson	Canada	YTH
Thorne Bay (AK)	USA	KTB
Thunder Bay	Canada	YQT
Thursday Island	Australia	TIS
Tianjin	China	TSN
Tijuana - Rodriguez	Mexico	TIJ
Tioman	Indonesia	TOD
Tirana - Rinas	Albania	TIA
Tiruchirapally	India	TRZ
Tivat	Montenegro	TIV
Tobago	Trinidad and Tobago	TAB
Tokushima	Japan	TKS
Tokyo	Japan	TYO
Tokyo - Haneda	Japan	HND
Tokyo - Narita	Japan	NRT
Toledo (OH)	USA	TOL
Tom Price	Australia	TPR
Toowoomba	Australia	TWB
Toronto - Billy Bishop Toronto City Airport	Canada	YTZ
Toronto - Toronto Pearson International Airport	Canada	YYZ
Toronto	Canada	YTO
Tortola	British Virgin Islands	TOV
Touho	New Caledonia	TOU
Toulouse - Blagnac Airport	France	TLS
Townsville	Australia	TSV
Toyama	Japan	TOY
Trabzon	Turkey	TZX
Trapani	Italy	TPS
Traverse City (MI)	USA	TVC
Treasure Cay	Bahamas	TCB
Trenton/Princeton (NJ)	USA	TTN
Treviso	Italy	TSF
Tri-Cities Regional (TN) /VA	USA	TRI
Trieste	Italy	TRS
Tripoli - Tripoli International	Libya	TIP
Tromsoe	Norway	TOS
Trondheim	Norway	TRD
Tsumeb	Namibia	TSB
Tucson (AZ)	USA	TUS
Tulepo (MS)	USA	TUP
Tulsa (OK)	USA	TUL
Tunis - Carthage	Tunisia	TUN
Turbat	Pakistan	TUK
Turin	Italy	TRN
Turku	Finland	TKU
Tuscaloosa (AL)	USA	TCL
Tuxtla Gutierrez	Mexico	TGZ
Twin Falls (ID)	USA	TWF
Tyler (TX)	USA	TYR
Ua Huka	French Polynesia	UAH
Ua Pou	French Polynesia	UAP
Ube	Japan	UBJ
Uberaba	Brazil	UBA
Uberlandia - Eduardo Gomes Airport	Brazil	UDI
Ubon Ratchathani - Muang Ubon Airport	Thailand	UBP
Udaipur - Dabok Airport	India	UDR
Uden - Volkel Airport	Netherlands	UDE
Udon Thani	Thailand	UTH
Ufa	Russia	UFA
Uherske Hradiste	Czech Republic	UHE
Uige	Angola	UGO
Ujung Pandang - Hasanudin Airport	Indonesia	UPG
Ukhta	Russia	UCT
Ukiah (CA)	USA	UKI
Ulaanbaatar - Buyant Uhaa Airport	Mongolia	ULN
Ulan-Ude	Russia	UUD
Ulanhot	PR China	HLH
Ulei	Vanuatu	ULB
Ulsan	South Korea	USN
Ulundi	South Africa	ULD
Umea	Sweden	UME
Umiujaq	Canada	YUD
Umtata	South Africa	UTT
Unalakleet (AK)	USA	UNK
Union Island	Saint Vincent and the Grenadines	UNI
Unst (Shetland Island) - Baltasound Airport	United Kingdom	UNT
Upala	Costa Rica	UPL
Upernavik - Upernavik Heliport	Greenland	JUV
Upington	South Africa	UTN
Upolu Point (HI)	USA	UPP
Uranium City	Canada	YBE
Urgench	Uzbekistan	UGC
Uriman	Venezuela	URM
Urmiehm (Orumieh)	Iran	OMH
Uruapan	Mexico	UPN
Urubupunga - Ernesto Pochler Airport	Brazil	URB
Uruguaiana - Ruben Berta Airport	Brazil	URG
Urumqi	Xinjiang, PR China	URC
Uruzgan	Afghanistan	URZ
Ushuaia - Islas Malvinas Airport	Argentina	USH
Utapao (Pattaya)	Thailand	UTP
Utica (NY) - Oneida County Airport	USA	UCA
Utila	Honduras	UII
Uummannaq	Greenland	UMD
Uzhgorod	Ukraine	UDJ
Vaasa	Finland	VAA
Vaexjoe	Sweden	VXO
Vail (CO)	USA	EGE
Val d'Or	Canada	YVO
Valdez (AK)	USA	VDZ
Valdosta (GA)	USA	VLD
Valencia	Spain	VLC
Valencia	Venezuela	VLN
Valladolid	Spain	VLL
Valparaiso	Chile	VAP
Valverde	Spain	VDE
Van - Ferit Melen	Turkey	VAN
Vancouver - Vancouver International	Canada	YVR
Varadero	Cuba	VRA
Varanasi	India	VNS
Varkaus	Finland	VRK
Varna	Bulgaria	VAR
Vasteras	Sweden	VST
Velikiye Luki (Welikije Luki)	Russia	VLU
Venice - Marco Polo	Italy	VCE
Veracruz	Mexico	VER
Vernal (UT)	USA	VEL
Vero Beach/Ft. Pierce (FL)	USA	VRB
Verona (Brescia) Montichiari	Italy	VBS
Verona	Italy	VRN
Victoria	Canada	YYJ
Victoria Falls	Zimbabwe	VFA
Vidin	Bulgaria	VID
Vientiane - Wattay	Lao PDR	VTE
Vigo	Spain	VGO
Villahermosa	Mexico	VSA
Vilnius	Lithuania	VNO
Virgin Gorda	Virgin Islands (British)	VIJ
Visalia (CA)	USA	VIS
Visby	Sweden	VBY
Vitoria	Spain	VIT
Vitoria - Eurico de Aguiar Salles Airport	Brazil	VIX
Vryheid	South Africa	VYD
Wabush	Canada	YWK
Waco (TX)	USA	ACT
Wagga	Australia	WGA
Walla Walla (WA)	USA	ALW
Wallis	Wallis and Futuna Islands	WLS
Walvis Bay	South Africa	WVB
Warrnambool	Australia	WMB
Warsaw - Frédéric Chopin	Poland	WAW
Washington DC - Baltimore Washington International	USA	BWI
Washington DC - Dulles International	USA	IAD
Washington DC - Ronald Reagan National	USA	DCA
Washington DC	USA	WAS
Waterloo IA	USA	ALO
Watertown (SD)	USA	ATY
Wausau/Stevens Point (WI)	USA	CWA
Weipa	Australia	WEI
Welkom	South Africa	WEL
Wellington	New Zealand	WLG
Wenatchee (WA)	USA	EAT
West Palm Beach (FL)	USA	PBI
West Yellowstone (MT)	USA	WYS
Westerland, Sylt Airport	Germany	GWT
Whakatane	New Zealand	WHK
Whale Cove, NT	Canada	YXN
Whangarei	New Zealand	WRE
White Plains (NY)	USA	HPN
Whitehorse	Canada	YXY
Whitsunday Resort	Australia	HAP
Whyalla	Australia	WYA
Wichita Falls (TX)	USA	SPS
Wichita (KS)	USA	ICT
Wick	United Kingdom	WIC
Wickham	Australia	WHM
Wien (Vienna) - Vienna International	Austria	VIE
Wiesbaden, Air Base	Germany	WIE
Wilkes Barre/Scranton (PA)	USA	AVP
Williamsport (PA)	USA	IPT
Williston (ND)	USA	ISL
Wilmington (NC)	USA	ILM
Wilna (Vilnius)	Lithuania	VNO
Wiluna	Australia	WUN
Windhoek - Eros	Namibia	ERS
Windhoek - Hosea Kutako International	Namibia	WDH
Windsor Ontario	Canada	YQG
Winnipeg International	Canada	YWG
Wolf Point (MT)	USA	OLF
Wollongong	Australia	WOL
Woomera	Australia	UMR
Worcester (MA)	USA	ORH
Worland (WY)	USA	WRL
Wrangell (AK)	USA	WRG
Wuhan	Hubei, PR China	WUH
Wyndham	Australia	WYN
Xiamen	Fujian, PR China	XMN
Xi'an - Xianyang	Shaanxi, PR China	XIY
Yakima (WA)	USA	YKM
Yakutat (AK)	USA	YAK
Yakutsk	Russia	YKS
Yamagata, Junmachi	Japan	GAJ
Yamoussoukro	Côte d'Ivoire	ASK
Yanbu	Saudi Arabia	YNB
Yangon (Rangoon) - Mingaladon	Myanmar	RGN
Yaounde	Cameroon	YAO
Yellowknife	Canada	YZF
Yekaterinburg - Koltsovo Airport	Russia	SVX
Yichang	Hubei, PR China	YIH
Yokohama	Japan	YOK
Yuma (AZ)	USA	YUM
Zacatecas	Mexico	ZCL
Zadar	Croatia (Hrvatska)	ZAD
Zagreb - Zagreb Airport Pleso	Croatia (Hrvatska)	ZAG
Zakynthos	Greece	ZTH
Zaragoza	Spain	ZAZ
Zhob	Pakistan	PZH
Zinder	Niger	ZND
Zouerate	Mauritania	OUZ
Zurich (Zürich) - Kloten	Switzerland	ZRH"""

b = a.split("\n")
c={}

for items in b:
    try:
        d = items.split("\t")
        c[d[0]]=d[1:]
    except:
        pass


json_countries = json.dumps(c)

with open("IATA-codes.json", "w") as data_file:
    data_file.write(json_countries)

with open("IATA-codes.json", "r") as data_file:
    raw_json = data_file.readline()
    colors = json.loads(raw_json)
    print(colors["Windsor Ontario"])
    
    
    
    
    
    
    
    
    
    