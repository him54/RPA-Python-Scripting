from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver_service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)
driver.get('https://www.thesun.co.uk/sport/football/')

title_list=[]
subtitle_list=[]
link_list=[]
#<div class="teaser__copy-container"><a class="text-anchor-wrap" href="https://www.thesun.co.uk/sport/21296749/chelsea-hire-mental-coach-blacks-winning-culture/"><h3 class="teaser__headline t-p-color">IN-OKA</h3><p class="teaser__subdeck"> Chelsea hire All Blacks' mental skills coach to help create winning culture</p></a></div>
#*[@id="customiser-v2-13503409"]/div[9]/div/div[3]/div/div[2]

containers = driver.find_elements(By.XPATH, value= '//div[@class="teaser__copy-container"]') 
for container in containers:
    title = container.find_element(By.XPATH, value='./a/h3').text
    subtitle = container.find_element(By.XPATH, value='./a/p').text
    link = container.find_element(By.XPATH,value='./a').get_attribute('href')
    title_list.append(title)
    subtitle_list.append(subtitle)
    link_list.append(link)

d={'Title':title_list,'Subtitle':subtitle_list, 'Link': link_list}
dataframe = pd.DataFrame(d)
dataframe.to_csv('news.csv')
driver.quit()


#OUTPUT

								Title	Subtitle	Link
							0	DAVE KIDD	Prem's most iconic moments wiped out if City get points ban including â€˜Agueroooâ€™	https://www.thesun.co.uk/sport/21297973/premier-league-man-city-finances-gerrard-slip-aguerooo/
							1	GUARD OF HONOUR	Guardiola threatened to QUIT Man City if club lied to him about breaches	https://www.thesun.co.uk/sport/21289904/pep-guardiola-quit-man-city-manager-rule-breaches/
							2	TITLE CHALLENGE	City could be STRIPPED of Prem titles if guilty of unprecedented breaches	https://www.thesun.co.uk/sport/21289797/man-city-stripped-titles-rule-breaches/
							3	BAN CITY	Man City face Prem EXPULSION after more than 100 financial breaches charges	https://www.thesun.co.uk/sport/21288970/man-city-charged-financial-rules-breaches/
							4	RED JOKE	Liverpool's nearly-men of 2013-14 brutally troll Man City after FFP breaches	https://www.thesun.co.uk/sport/21297567/liverpools-man-city-premier-league-champions/
							5	OUT OF SIGHT	How Prem table will look if Man City are expelled... and it's good for Arsenal	https://www.thesun.co.uk/sport/21289890/how-prem-table-look-man-city-expelled/
							6	CITY RESPOND	Man City release 79 word statement after being charged with financial breaches	https://www.thesun.co.uk/sport/21290952/man-city-release-statement-charged-financial-breaches/
							7	MAN CITY LIVE	Club could face expulsion or points deduction after Premier League charges	https://www.thesun.co.uk/sport/20652713/man-city-charged-premier-league-live-latest-updates-points-deduction/
							8	GALL-ING THEM OUT	Man City fan Liam Gallagher demands whole of Premier League investigated	https://www.thesun.co.uk/sport/21295918/liam-gallagher-premier-league-manchester-city-financial-charges/
							9	CITY Q&A	What breaches have City been charged with and when will we know the outcome?	https://www.thesun.co.uk/sport/21291739/man-city-financial-breaches/
							10	NUMBERS GAME	Supercomputer reveals final table after shock defeats for Arsenal and Man City	https://www.thesun.co.uk/sport/21288295/premier-league-supercomputer-arsenal-man-city/
							11	FOX IN THE BOX	Fans spot footballer swiping on Tinder on team bus - and he says it worked	https://www.thesun.co.uk/sport/21297455/tinder-non-league-taunton-foulston/
							12	CAMP OUT	Fans in stitches as Sky Sports confuse Championship legend for Chile boss Berizzo	https://www.thesun.co.uk/sport/21298112/fans-sky-sports-eduardo-berizzo-blackburn-wigan/
							13	LINK UP	Arsenal close in on cut price Milinkovic-Savic deal as he decides to leave Lazio	https://www.thesun.co.uk/sport/21299026/arsenal-milinkovic-savic-transfer-man-utd-lazio/
							14	ROLEX	Win an incredible Rolex Starbucks Submariner or Â£12k cash alternative from just 89p	https://www.thesun.co.uk/sport/betting-tips/18922011/win-rolex-7dp/
							15	'OUTRAGEOUS'	Piers Morgan demands Man City are docked points as Arsenal fans eye Prem title	https://www.thesun.co.uk/sport/21289268/piers-morgan-man-city-points-deduction-arsenal/
							16	CARR-TASTROPHE	Carragher trolls City with sarcastic tweet as they're charged with breaches	https://www.thesun.co.uk/sport/21290067/liverpool-jamie-carragher-man-city-charged/
							17	LEAK HALT	Rishi Sunak delays announcing football shake-up after bombshell leak to The Sun	https://www.thesun.co.uk/sport/21297928/rishsi-sunak-delayed-footie-shake-bombshell-leak/
							18	SHOW OF SUPPORT	Jailed Dani Alvesâ€™ wife vows to STICK BY him days after 'demanding divorce'	https://www.thesun.co.uk/sport/21290141/dani-alves-wife-jail-divorce-nightclub-rape/
							19	TEARFUL PLEA	Ex-Turkey ace breaks down in tears during plea for help for earthquake victims	https://www.thesun.co.uk/sport/21292171/fenerbahce-volkan-demirel-tears-turkey-earthquake/
							20	â€˜IMPORTANT WINâ€™	Christian Atsu scored 97th-min goal hours before being buried in quake	https://www.thesun.co.uk/sport/21292536/christian-atsu-joy-winner-buried-turkey-earthquake/
							21	FOOTIE CHARGE	Exeter star charged with assaulting a woman as club suspends him from play	https://www.thesun.co.uk/sport/21293884/jevani-brown-charged-assaulting-woman/
							22	RANKED	Best casino welcome bonuses - UK casino offers for February 2023	https://www.thesun.co.uk/betting/21097803/casino-welcome-bonus/
							23	BEST PALS	Cristiano Ronaldo's inner circle revealed including reporter and two close pals	https://www.thesun.co.uk/sport/21295066/cristiano-ronaldo-inner-circle-revealed-mendes/
							24	ROOM FOR RENT	Fernandez 'only looking to rent in London for 12 months and has huge budget'	https://www.thesun.co.uk/sport/21298424/enzo-fernandez-rent-london-chelsea-budget/
							25	IN-OKA	Chelsea hire All Blacks' mental skills coach to help create winning culture	https://www.thesun.co.uk/sport/21296749/chelsea-hire-mental-coach-blacks-winning-culture/
							26	KICKED OUT	Mason Greenwood dropped as Nike athlete after hinting at sponsorship renewal	https://www.thesun.co.uk/sport/21291252/mason-greenwood-dropped-nike-athlete/
							27	FRENKLY SPEAKING	Frenkie de Jongâ€™s girlfriend trolls Man Utd fans over failed transfer	https://www.thesun.co.uk/sport/21298455/frenkie-de-jong-girlfriend-man-united-transfer/
							28	BALLSY	Watch Arsenal's Saka cheekily throw ball at Everton star Pickford's head in melee	https://www.thesun.co.uk/sport/21288187/everton-arsenal-bukayo-saka-jordan-pickford-melee/
							29	'PR STUNT'	Crawley sign Sideman star Tobi's brother Jed Brown... but fans are NOT happy	https://www.thesun.co.uk/sport/21294445/crawley-sign-sideman-jed-brown-not-happy/
							30	NOT FULL TIME YET	I'm Britain's oldest football ref and I've no plans to hang up my whistle	https://www.thesun.co.uk/sport/21297023/britains-oldest-football-referee/
							31	LOSING NATH	Jones losing the confidence of Southampton squad and unsettled board with rant	https://www.thesun.co.uk/sport/21293856/jones-losing-confidence-southampton-squad-rant/
							32	FOOTBALL TRAGEDY	South African star Andries, 19, stabbed to death and dies in mum's arms	https://www.thesun.co.uk/sport/21288592/oshwin-andries-dead-south-africa-stabbed-attack/
							33	MAKING HIS MARC	Watch Man Utd's stunning 14-pass move for Rashford's goal vs Crystal Palace	https://www.thesun.co.uk/sport/21290065/man-utd-ten-hag-rashford-crystal-palace/
							34	GREAT DEBATE	Carragher, Richards & Souness get heated argument over PL's best-ever striker	https://www.thesun.co.uk/sport/21292970/carragher-richards-souness-argue-premier-league-striker/
							35	AUBA THE LINE	Chelsea 'in talks with LAFC over Pierre-Emerick Aubameyang transfer'	https://www.thesun.co.uk/sport/21290227/chelsea-champions-league-lafc-pierre-emerick-aubameyang/
							36	PLANE CRAZY	Nigerian billionaire linked with Sheff Utd takeover 'owns fake airline company'	https://www.thesun.co.uk/sport/21291137/sheffield-united-dozy-mmobuosi-takeover/
							37	NOT RON	Ronaldo's presence makes Al-Nassr matches 'more difficult', reveals team-mate	https://www.thesun.co.uk/sport/21288095/cristiano-ronaldo-al-nassr-luis-gustavo/
							38	ANYTHING FER YOU	Chelsea ace Enzo Fernandez buys Wag flowers and takes her out for birthday	https://www.thesun.co.uk/sport/21293126/chelsea-enzo-fernandez-wag-valentina-cervantes/
							39	TOP 40	Sheffield United vs Wrexham: Get Â£40 bonus when you stake Â£10 with William Hill	https://www.thesun.co.uk/sport/20695257/william-hill-free-bets-sign-up-bonus-offer-register/
							40	MARSCH HALT	Watch Marsch's last interview as Leeds boss that fans fumed at before sacking	https://www.thesun.co.uk/sport/21293830/watch-jesse-marsch-leeds-manager-fans-sacking/
							41	BREAK THREE	Man Utd â€˜put THREE first-team stars on transfer list ahead of summer window'	https://www.thesun.co.uk/sport/21295098/manchester-united-harry-maguire-anthony-martial-alex-telles/
							42	GONE SOUTH	Southend on brink of extinction as they are unable to pay players and staff	https://www.thesun.co.uk/sport/21290908/southend-united-unpaid-players-staff-debt/
							43	KNOLL STOPPING HER	World Cupâ€™s hottest fan sends followers wild in sexy in sunbed snap	https://www.thesun.co.uk/sport/21288981/ivana-knoll-world-cup-sexiest-fan-bikini-picture/
							44	BIG OFFER	Betfair free bets: Stake Â£10 on football to get Â£30 bonus - 18+ T&Cs apply	https://www.thesun.co.uk/sport/betting-tips/19802970/betfair-free-bets-sign-up-bonus-football/
							45	CAL ON ME	Everton sweat over Calvert-Lewin with ace set for scan ahead of Merseyside derby	https://www.thesun.co.uk/sport/21287214/dominic-calvert-lewin-injury-everton-liverpool-sean-dyche-update/
							46	NEV-ER GONNA WORK	Neville slams Chelsea's crazy spending and says 'it doesnâ€™t sit right'	https://www.thesun.co.uk/sport/21295951/chelsea-gary-neville-todd-boehy-spending/
							47	NOT BLUE	Graham Potter slams Klopp and Guardiola after criticism of Chelsea spending	https://www.thesun.co.uk/sport/21296380/graham-potter-slams-rivals-klopp-guardiola-criticism-chelsea-spending/
							48	KICKING OFF	Newcastle's Â£45m ace 'didn't know about suspension' when caught driving	https://www.thesun.co.uk/sport/21281728/newcastle-united-anthony-gordon-speeding/
							49	PROMOTION	The best casino bonuses for players in the UK: Top 10 sites for 2023	https://www.thesun.co.uk/betting/20754895/casino-bonus/
							50	TIME OUT	Arsenal fans plead for TWO stars to be rested against Brentford after Everton loss	https://www.thesun.co.uk/sport/21290080/arsenal-brentford-everton-players-rested-plea/
							51	NOT IN A HARRY	Kane refuses to commit future to Tottenham amid Man Utd transfer interest	https://www.thesun.co.uk/sport/21293662/harry-kane-tottenham-record-goal-man-utd-transfer/
							52	HAAL GONE WRONG	Carragher suggests that Haaland shouldn't have signed for Manchester City	https://www.thesun.co.uk/sport/21284174/man-city-carragher-haaland/
							53	'YOU MAKE ME PROUD'	Conte rings Kane to congratulate him on breaking Greaves' record	https://www.thesun.co.uk/sport/21284066/tottenham-harry-kane-antonio-conte-record-phone-call/
							54	FREE PLAY	1-2-Free: Win Â£100 in CASH if you correctly predict three scores with Ladbrokes	https://www.thesun.co.uk/sport/21084288/ladbrokes-free-bets-game-bonus-win-100-football/
							55	POWER SERG	Man Utd receive Europa League boost as star man limps off for Barcelona	https://www.thesun.co.uk/sport/21285546/man-utd-barcelona-europa-league-busquets-injury-sevilla/
							56	INTER-VENTION	Inter strip Skriniar of captaincy after star signs pre-contract with PSG	https://www.thesun.co.uk/sport/21295067/inter-milan-skriniar-captain-stripped-psg/
							57	BIG WILLY STYLE	Watch Hughes make cheeky Liverpool gesture to Utd fans after Casemiro red	https://www.thesun.co.uk/sport/21291986/will-hughes-liverpool-gesture-man-utd-fans-casemiro-red/
							58	BALE FORCE	Bale finishes on 16-under par in rainy PGA debut weeks after quitting football	https://www.thesun.co.uk/sport/21285515/bale-gareth-golf-pga-tour-pebble-beach/
							59	FREE BETS	Free bets - Best betting offers in February 2023	https://www.thesun.co.uk/betting/20812234/free-bets/
							60	WORST CASE	Man Utd's Casemiro may still be banned for Carabao Cup final after red card	https://www.thesun.co.uk/sport/21287364/man-utd-casemiro-red-card-appeal-carabao-cup/
							61	CAS CLOSED	De Gea names Man Utd's ideal replacement for suspended Casemiro	https://www.thesun.co.uk/sport/21288231/de-gea-names-man-utd-replacement-suspended-casemiro/
							62	REST IN PEACE	Sunderland pay tribute to fan and British Army captain after shock death	https://www.thesun.co.uk/sport/21287605/sunderland-fan-army-chris-collier-death/
							63	NOT SO GAB FAB	Why Gabriel wasn't given penalty at Everton after Arsenal star was tripped	https://www.thesun.co.uk/sport/21289568/arsenal-gabriel-penalty-everton-maupay/
							64	GLAZE OVER	Billionaire Ratcliffe to bid for Man Utd THIS WEEK but Glazers want Â£8billion	https://www.thesun.co.uk/sport/21281072/man-utd-jim-ratcliffe-bid-glazers-8billion/
							65	MEET THE FAMILY	Jermain Defoe 'serious' with new girlfriend after introducing her to mum	https://www.thesun.co.uk/sport/21275803/jermain-defoe-new-girlfriend-alisha-lemay-meet-mum/
							66	FAB Â£30	Bonus: Get Â£30 in FREE BETS when you stake Â£10 with Sky Bet -18+ T&Cs apply	https://www.thesun.co.uk/sport/betting-tips/19781466/sky-bet-30-free-bets/
							67	HEADS, I WIN	Wolves hero Neves sends message to Rashford over 'his' iconic goal celebration	https://www.thesun.co.uk/sport/21280388/wolves-ruben-neves-man-utd-marcus-rashford-celebration/
							68	A BIT SEV-ERE	Kounde issues statement apologising for 'exaggerated' celebration vs Sevilla	https://www.thesun.co.uk/sport/21294867/barcelona-jules-kounde-apologising-celebration-sevilla/
							69	COURT OUT	Real Madrid keeper Courtois in race against time to be fit to face Liverpool	https://www.thesun.co.uk/sport/21294875/real-madrid-thibaut-courtois-liverpool-champions-league/
							70	GUESS WHO?	Champions League winner is totally unrecognisable 25 years after winning trophy	https://www.thesun.co.uk/sport/17166729/champions-league-winner-unrecognisable-24-years/
							71	THE PRICE IS RICE	Man Utd 'failed in Â£100m Rice bid last summer' as price tag is revealed	https://www.thesun.co.uk/sport/21294452/man-utd-declan-rice-transfer-price-arsenal-chelsea/
							72	DI WAY TO GO	Dalot 'on verge of signing long-term Man Utd contract' despite Barca interest	https://www.thesun.co.uk/sport/21294047/diogo-dalot-contract-man-united-barcelona-transfer/
							73	NO DEAL	Man Utd transfer blow as 'Spurs will NOT sell club Kane to Premier League rival'	https://www.thesun.co.uk/sport/21297351/manutd-transfer-blow-tottenham-harry-kane-premier-league-rival/
							74	KEEP YOUR MITS OFF	Arsenal lead race for Brighton star Mitoma but will have to splash Â£35M	https://www.thesun.co.uk/sport/21281528/arsenal-lead-transfer-brighton-kaoru-mitoma/
							75	HARRY HOPE	Ten Hag says Maguire will get chance to regain place after rejecting Inter loan	https://www.thesun.co.uk/sport/21278506/man-utd-maguire-ten-hag-inter-milan/
							76	ROB THE RICH	Man City & Italian giants told to pay Â£35m for Fulham star Antonee Robinson	https://www.thesun.co.uk/sport/21280480/man-city-transfer-fulham-antonee-robinson/
							77	COUT ME OUT	Coutinho being lined up for loan transfer by Galatasaray after miserable season	https://www.thesun.co.uk/sport/21279516/philippe-coutinho-loan-transfer-galatasaray-aston-villa/
							78	ANT FIGHT	Wolves and Leicester ready to fight for Â£10m-rated Sunderland keeper Patterson	https://www.thesun.co.uk/sport/21278252/patterson-wolves-leicester-transfer-sunderland/
							79	BLADE SHUNNER	Newcastle transfer blow with Berge planning on long stay at Sheffield Utd	https://www.thesun.co.uk/sport/21281530/newcastle-transfer-blow-sander-berge-sheffield-united-stay/
							80	RED DEVILS LIVE	Club willing to pay Â£107million for Osimhen, Harry Kane urged against move	https://www.thesun.co.uk/sport/21284701/man-utd-news-live-osimhen-transfer-harry-kane/
							81	GUNNERS LIVE	Gunners favourite for Tielemans, Â£62million Mac Allister price, Mitoma race	https://www.thesun.co.uk/sport/21158908/arsenal-transfer-news-live-youri-tielemans-mac-allister-karou-mitoma/
							82	RIK AND ROLL	Ten Hag draws up three-man summer wishlist as he plans huge squad overhaul	https://www.thesun.co.uk/sport/21292454/ten-hag-three-man-transfer-wishlist-summer-overhaul/
							83	KOP OUT	Liverpool cult hero looks unrecognisable with tattoos, beard and drastic haircut	https://www.thesun.co.uk/sport/18081871/liverpool-hero-unrecognisable-beard-hair-tattoos/
							84	TAKING THE MIK	Arteta hilariously forgets who Arsenal played after loss to Dyche's Everton	https://www.thesun.co.uk/sport/21280039/arteta-arsenal-dyche-everton/
							85	EUR KIDDING	Under-fire Southampton boss Jones launches into bizarre rant after latest loss	https://www.thesun.co.uk/sport/21281957/southampton-nathan-jones/
							86	HAD A MAR-E	Watch Ferdinand troll Arsenal icon Keown in BT studio as Everton beat Arsenal	https://www.thesun.co.uk/sport/21279759/ferdinand-arsenal-keown-everton/
							87	'NO EGO TRIP'	Man Utd Treble winner 'stops feeling like a fraud' as he turns to management	https://www.thesun.co.uk/sport/21282703/man-utd-treble-winner-manager-non-league/
							88	WEBB SPINNER	Refs chief Howard Webb gives harsh verdict on Rashford offside vs Man City	https://www.thesun.co.uk/sport/21269560/man-utd-webb-rashford-man-city-var/
							89	RETURN BACKLASH	Man Utd stars don't want Greenwood back this season after charges dropped	https://www.thesun.co.uk/sport/21276534/manchester-united-football-rape-mason-greenwoods-club-players/
							90	TOP DEC	Chelsea star Fernandez reveals how Rice inspires him as Moyes sets transfer fee	https://www.thesun.co.uk/sport/21280165/chelsea-enzo-fernandez-declan-rice-west-ham-transfer/
							91	BOSSING IT	Klopp speaks on his Liverpool future amid fears he could go after Wolves loss	https://www.thesun.co.uk/sport/21280577/jurgen-klopp-liverpool-future-wolves-loss/
							92	UNITED STATE	Who will manage Leeds United against Manchester United this week?	https://www.thesun.co.uk/sport/21297607/who-will-manage-leeds-against-man-utd/
							93	PROMOTION	Best football betting sites in the UK: Top online bookies for February 2023	https://www.thesun.co.uk/betting/20574123/best-football-betting-sites/
							94	BETTING TIPS	Best live casinos in the UK: Top 10 sites for 2023	https://www.thesun.co.uk/betting/20833219/live-casinos/
							95	REVIEW	Best online casinos in the UK: Top 15 casino sites for February 2023	https://www.thesun.co.uk/betting/20803800/the-best-online-casinos-in-the-uk/
							96	MAX ANGER	Watch Allegri hilariously lose it on touchline over Di Maria gaffe for Juventus	https://www.thesun.co.uk/sport/21280992/watch-match-allegri-hilariously-lose-it-juventus-di-maria/
							97	GET ME OUT OF HERE	Charlton boss Holden retching for bucket in Bushtucker trial fundraiser	https://www.thesun.co.uk/sport/21281758/charlton-boss-dean-holden-bushtucker-trial-prostate-cancer/
							98	RIP BILLY	Former Rangers and Scotland goalkeeper Billy Thomson dies aged 64	https://www.thesun.co.uk/sport/21290734/rangers-scotland-billy-thomson-dies-st-mirren-dundee-united/
							99	ALL BAY HIMSELF	Watch Bayern's Musiala score incredible solo goal after beating SIX players	https://www.thesun.co.uk/sport/21286577/bayern-munich-jamal-musiala-goal/
							100	OH YESSI	Watch Lionel Messi score stunner for PSG as French champs beat Toulouse	https://www.thesun.co.uk/sport/21276647/watch-lionel-messi-score-stunner-psg-toulouse/
							101	RON AND ONLY	Ronaldo cuddles Georgina Rodriguez in loved-up snap after his birthday	https://www.thesun.co.uk/sport/21288866/ronaldo-cuddles-georgina-celebrate-man-utd-legend-birthday/
							102	ANGEL DELIGHT	Watch Atletico ace mobbed on BENCH as he's taken off then VAR allows his goal	https://www.thesun.co.uk/sport/21282072/atletico-madrid-1-1-getafe-correa-goal/
							103	CHAOS REIGNS	Shocking moment football hooligans unleash chaos in massive street brawl	https://www.thesun.co.uk/sport/21274122/shocking-moment-football-hooligans-massive-brawl/
							104	KING OF THE CASTLE	Watch Hearts star score 'best goal Tynecastle's ever seen' from own half	https://www.thesun.co.uk/sport/football/21282179/hearts-dundee-utd-stephen-humphrys-best-goal-tynecastle-lob/
							105	STOP THE COUNT	Barcelona â€˜confirm titleâ€™ as they achieve feat Real â€˜can never overcomeâ€™	https://www.thesun.co.uk/sport/21292189/barcelona-real-madrid-title-race-over-points-gap/
							106	TIM VICKERY	Clubs from the Americas could soon pose a threat to the powerful European elite	https://www.thesun.co.uk/sport/21252967/americas-clubs-concacaf-european/
							107	GET KANED	Harry Kane has snatched Spurs record but Jimmy Greaves would be miles ahead	https://www.thesun.co.uk/sport/21297917/colin-hart-harry-kane-tottenham-jimmy-greaves-premier-league/
							108	TROY DEENEY	I played with 250 players at Watford - it must be lunacy to be a Chelsea star	https://www.thesun.co.uk/sport/21269995/deeney-watford-chelsea/
							109	SEALED WITH A KISS	Neymar appears to rekindle romance with stunning WAG Bruna Biancardi	https://www.thesun.co.uk/sport/21284319/neymar-wag-bruna-biancardi-paris-saint-germain/
							110	UNBELIEVA-BALL	Alisha Lehmann fans beg her to join their club as she posts stunning pic	https://www.thesun.co.uk/sport/21283756/alisha-lehmann-aston-villa-federer/
							111	PERFECT KAT-CH	Meet new Man Utd signing Marcel Sabitzer's stunning partner Katja	https://www.thesun.co.uk/sport/21226473/manchester-united-marcel-sabitzer-katja-kuhne-bayern-munich/
