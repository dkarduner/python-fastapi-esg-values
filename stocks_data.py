# B"H
# data from stocks

def get():
    data = [
         {'name': '3M' ,'stock_name': 'MMM'}
        ,{'name': 'A.O. Smith' ,'stock_name': 'AOS'}
        ,{'name': 'Abbott Laboratories' ,'stock_name': 'ABT'}
        ,{'name': 'AbbVie' ,'stock_name': 'ABBV'}
        ,{'name': 'ABIOMED' ,'stock_name': 'ABMD'}
        ,{'name': 'Accenture' ,'stock_name': 'ACN'}
        ,{'name': 'Activision Blizzard' ,'stock_name': 'ATVI'}
        ,{'name': 'Adobe' ,'stock_name': 'ADBE'}
        ,{'name': 'Advance Auto Parts' ,'stock_name': 'AAP'}
        ,{'name': 'AES' ,'stock_name': 'AES'}
        ,{'name': 'Aflac' ,'stock_name': 'AFL'}
        ,{'name': 'Agilent Technologies' ,'stock_name': 'A'}
        ,{'name': 'Air Products and Chemicals' ,'stock_name': 'APD'}
        ,{'name': 'Akamai' ,'stock_name': 'AKAM'}
        ,{'name': 'Alaska Air Group' ,'stock_name': 'ALK'}
        ,{'name': 'Albemarle' ,'stock_name': 'ALB'}
        ,{'name': 'Alexandria Real Estate Equities' ,'stock_name': 'ARE'}
        ,{'name': 'Align Technology' ,'stock_name': 'ALGN'}
        ,{'name': 'Allegion' ,'stock_name': 'ALLE'}
        ,{'name': 'Alliant Energy' ,'stock_name': 'LNT'}
        ,{'name': 'Allstate' ,'stock_name': 'ALL'}
        ,{'name': 'Alphabet A' ,'stock_name': 'GOOGL'}
        ,{'name': 'Alphabet C' ,'stock_name': 'GOOG'}
        ,{'name': 'Altria' ,'stock_name': 'MO'}
        ,{'name': 'Amazon' ,'stock_name': 'AMZN'}
        ,{'name': 'Amcor' ,'stock_name': 'AMCR'}
        ,{'name': 'AMD' ,'stock_name': 'AMD'}
        ,{'name': 'Ameren' ,'stock_name': 'AEE'}
        ,{'name': 'American Airlines' ,'stock_name': 'AAL'}
        ,{'name': 'American Electric Power' ,'stock_name': 'AEP'}
        ,{'name': 'American Express' ,'stock_name': 'AXP'}
        ,{'name': 'American International Group' ,'stock_name': 'AIG'}
        ,{'name': 'American Tower' ,'stock_name': 'AMT'}
        ,{'name': 'American Water Works' ,'stock_name': 'AWK'}
        ,{'name': 'Ameriprise Financial' ,'stock_name': 'AMP'}
        ,{'name': 'AmerisourceBergen' ,'stock_name': 'ABC'}
        ,{'name': 'Ametek' ,'stock_name': 'AME'}
        ,{'name': 'Amgen' ,'stock_name': 'AMGN'}
        ,{'name': 'Amphenol' ,'stock_name': 'APH'}
        ,{'name': 'Analog Devices' ,'stock_name': 'ADI'}
        ,{'name': 'ANSYS' ,'stock_name': 'ANSS'}
        ,{'name': 'Anthem' ,'stock_name': 'ANTM'}
        ,{'name': 'Aon' ,'stock_name': 'AON'}
        ,{'name': 'APA Corporation Registered Shs' ,'stock_name': 'APA'}
        ,{'name': 'Apple' ,'stock_name': 'AAPL'}
        ,{'name': 'Applied Materials' ,'stock_name': 'AMAT'}
        ,{'name': 'Aptiv' ,'stock_name': 'APTV'}
        ,{'name': 'Archer Daniels Midland' ,'stock_name': 'ADM'}
        ,{'name': 'Arista Networks' ,'stock_name': 'ANET'}
        ,{'name': 'Arthur J. Gallagher' ,'stock_name': 'AJG'}
        ,{'name': 'Assurant' ,'stock_name': 'AIZ'}
        ,{'name': 'AT&T' ,'stock_name': 'T'}
        ,{'name': 'Atmos Energy' ,'stock_name': 'ATO'}
        ,{'name': 'Autodesk' ,'stock_name': 'ADSK'}
        ,{'name': 'Automatic Data Processing' ,'stock_name': 'ADP'}
        ,{'name': 'AutoZone' ,'stock_name': 'AZO'}
        ,{'name': 'AvalonBay Communities' ,'stock_name': 'AVB'}
        ,{'name': 'Avery Dennison' ,'stock_name': 'AVY'}
        ,{'name': 'Baker Hughes' ,'stock_name': 'BKR'}
        ,{'name': 'Ball' ,'stock_name': 'BALL'}
        ,{'name': 'Bank of America' ,'stock_name': 'BAC'}
        ,{'name': 'Bank of New York Mellon' ,'stock_name': 'BK'}
        ,{'name': 'Bath & Body Works' ,'stock_name': 'BBWI'}
        ,{'name': 'Baxter International' ,'stock_name': 'BAX'}
        ,{'name': 'Becton, Dickinson' ,'stock_name': 'BDX'}
        ,{'name': 'Berkshire Hathaway' ,'stock_name': 'BRK-B'}
        ,{'name': 'Best Buy' ,'stock_name': 'BBY'}
        ,{'name': 'Biogen' ,'stock_name': 'BIIB'}
        ,{'name': 'Bio-Rad Laboratories' ,'stock_name': 'BIO'}
        ,{'name': 'Bio-Techne' ,'stock_name': 'TECH'}
        ,{'name': 'BlackRock' ,'stock_name': 'BLK'}
        ,{'name': 'Boeing' ,'stock_name': 'BA'}
        ,{'name': 'Booking Holdings' ,'stock_name': 'BKNG'}
        ,{'name': 'BorgWarner' ,'stock_name': 'BWA'}
        ,{'name': 'Boston Properties' ,'stock_name': 'BXP'}
        ,{'name': 'Boston Scientific' ,'stock_name': 'BSX'}
        ,{'name': 'Bristol-Myers Squibb' ,'stock_name': 'BMY'}
        ,{'name': 'Broadcom' ,'stock_name': 'AVGO'}
        ,{'name': 'Broadridge Financial Solutions' ,'stock_name': 'BR'}
        ,{'name': 'Brown-Forman b' ,'stock_name': 'BF-B'}
        ,{'name': 'C.H. Robinson Worldwide' ,'stock_name': 'CHRW'}
        ,{'name': 'Cadence Design Systems' ,'stock_name': 'CDNS'}
        ,{'name': 'Caesars Entertainment' ,'stock_name': 'CZR'}
        ,{'name': 'Campbell Soup' ,'stock_name': 'CPB'}
        ,{'name': 'Capital One Financial' ,'stock_name': 'COF'}
        ,{'name': 'Cardinal Health' ,'stock_name': 'CAH'}
        ,{'name': 'CarMax' ,'stock_name': 'KMX'}
        ,{'name': 'Carnival' ,'stock_name': 'CCL'}
        ,{'name': 'Carrier Global Corporation Registered Shs When Issued' ,'stock_name': 'CARR'}
        ,{'name': 'Catalent' ,'stock_name': 'CTLT'}
        ,{'name': 'Caterpillar' ,'stock_name': 'CAT'}
        ,{'name': 'CBRE Grou a' ,'stock_name': 'CBRE'}
        ,{'name': 'CDW' ,'stock_name': 'CDW'}
        ,{'name': 'Celanese' ,'stock_name': 'CE'}
        ,{'name': 'Centene' ,'stock_name': 'CNC'}
        ,{'name': 'CenterPoint Energy' ,'stock_name': 'CNP'}
        ,{'name': 'Cabot Oil & Gas' ,'stock_name': 'CTRA'}
        ,{'name': 'CF Industries Holdings' ,'stock_name': 'CF'}
        ,{'name': 'Charles River Laboratories International' ,'stock_name': 'CRL'}
        ,{'name': 'Charles Schwab' ,'stock_name': 'SCHW'}
        ,{'name': 'Charter a' ,'stock_name': 'CHTR'}
        ,{'name': 'Chevron' ,'stock_name': 'CVX'}
        ,{'name': 'Chipotle Mexican Grill' ,'stock_name': 'CMG'}
        ,{'name': 'Chubb' ,'stock_name': 'CB'}
        ,{'name': 'Church & Dwight' ,'stock_name': 'CHD'}
        ,{'name': 'Cigna' ,'stock_name': 'CI'}
        ,{'name': 'Cincinnati Financial' ,'stock_name': 'CINF'}
        ,{'name': 'Cintas' ,'stock_name': 'CTAS'}
        ,{'name': 'Cisco' ,'stock_name': 'CSCO'}
        ,{'name': 'Citigroup' ,'stock_name': 'C'}
        ,{'name': 'Citizens Financial Group' ,'stock_name': 'CFG'}
        ,{'name': 'Citrix Systems' ,'stock_name': 'CTXS'}
        ,{'name': 'Clorox' ,'stock_name': 'CLX'}
        ,{'name': 'CME Grou a' ,'stock_name': 'CME'}
        ,{'name': 'CMS Energy' ,'stock_name': 'CMS'}
        ,{'name': 'Coca-Cola' ,'stock_name': 'KO'}
        ,{'name': 'Cognizant' ,'stock_name': 'CTSH'}
        ,{'name': 'Colgate-Palmolive' ,'stock_name': 'CL'}
        ,{'name': 'Comcast' ,'stock_name': 'CMCSA'}
        ,{'name': 'Comerica' ,'stock_name': 'CMA'}
        ,{'name': 'ConAgra Foods' ,'stock_name': 'CAG'}
        ,{'name': 'ConocoPhillips' ,'stock_name': 'COP'}
        ,{'name': 'Consolidated Edison' ,'stock_name': 'ED'}
        ,{'name': 'Constellation Brand a' ,'stock_name': 'STZ'}
        ,{'name': 'Cooper Cos' ,'stock_name': 'COO'}
        ,{'name': 'Copart' ,'stock_name': 'CPRT'}
        ,{'name': 'Corning' ,'stock_name': 'GLW'}
        ,{'name': 'Corteva' ,'stock_name': 'CTVA'}
        ,{'name': 'Costco Wholesale' ,'stock_name': 'COST'}
        ,{'name': 'Crown Castle' ,'stock_name': 'CCI'}
        ,{'name': 'CSX' ,'stock_name': 'CSX'}
        ,{'name': 'Cummins' ,'stock_name': 'CMI'}
        ,{'name': 'CVS Health' ,'stock_name': 'CVS'}
        ,{'name': 'D.R. Horton' ,'stock_name': 'DHI'}
        ,{'name': 'Danaher' ,'stock_name': 'DHR'}
        ,{'name': 'Darden Restaurants' ,'stock_name': 'DRI'}
        ,{'name': 'DaVita HealthCare Partners' ,'stock_name': 'DVA'}
        ,{'name': 'Deere' ,'stock_name': 'DE'}
        ,{'name': 'Delta Air Lines' ,'stock_name': 'DAL'}
        ,{'name': 'DENTSPLY SIRONA' ,'stock_name': 'XRAY'}
        ,{'name': 'Devon Energy' ,'stock_name': 'DVN'}
        ,{'name': 'DexCom' ,'stock_name': 'DXCM'}
        ,{'name': 'Diamondback Energy' ,'stock_name': 'FANG'}
        ,{'name': 'Digital Realty Trust' ,'stock_name': 'DLR'}
        ,{'name': 'Discover Financial Services' ,'stock_name': 'DFS'}
        ,{'name': 'Dish Network' ,'stock_name': 'DISH'}
        ,{'name': 'Dollar General Corporation' ,'stock_name': 'DG'}
        ,{'name': 'Dollar Tree' ,'stock_name': 'DLTR'}
        ,{'name': 'Dominion Energy' ,'stock_name': 'D'}
        ,{'name': 'Dominos Pizza' ,'stock_name': 'DPZ'}
        ,{'name': 'Dover' ,'stock_name': 'DOV'}
        ,{'name': 'Dow' ,'stock_name': 'DOW'}
        ,{'name': 'DTE Energy' ,'stock_name': 'DTE'}
        ,{'name': 'Duke Energy' ,'stock_name': 'DUK'}
        ,{'name': 'Duke Realty' ,'stock_name': 'DRE'}
        ,{'name': 'DuPont de Nemours' ,'stock_name': 'DD'}
        ,{'name': 'DXC Technology' ,'stock_name': 'DXC'}
        ,{'name': 'Eastman Chemical Company' ,'stock_name': 'EMN'}
        ,{'name': 'Eaton Corporation' ,'stock_name': 'ETN'}
        ,{'name': 'eBay' ,'stock_name': 'EBAY'}
        ,{'name': 'Ecolab' ,'stock_name': 'ECL'}
        ,{'name': 'Edison International' ,'stock_name': 'EIX'}
        ,{'name': 'Edwards Lifesciences' ,'stock_name': 'EW'}
        ,{'name': 'Electronic Arts' ,'stock_name': 'EA'}
        ,{'name': 'Eli Lilly and' ,'stock_name': 'LLY'}
        ,{'name': 'Emerson Electric' ,'stock_name': 'EMR'}
        ,{'name': 'Enphase Energy' ,'stock_name': 'ENPH'}
        ,{'name': 'Entergy' ,'stock_name': 'ETR'}
        ,{'name': 'EOG Resources' ,'stock_name': 'EOG'}
        ,{'name': 'Equifax' ,'stock_name': 'EFX'}
        ,{'name': 'Equinix' ,'stock_name': 'EQIX'}
        ,{'name': 'Equity Residential' ,'stock_name': 'EQR'}
        ,{'name': 'Essex Property Trust' ,'stock_name': 'ESS'}
        ,{'name': 'Estée Lauder Companies' ,'stock_name': 'EL'}
        ,{'name': 'Etsy' ,'stock_name': 'ETSY'}
        ,{'name': 'Everest Reinsurance Group' ,'stock_name': 'RE'}
        ,{'name': 'Evergy' ,'stock_name': 'EVRG'}
        ,{'name': 'Eversource Energy' ,'stock_name': 'ES'}
        ,{'name': 'Exelon' ,'stock_name': 'EXC'}
        ,{'name': 'Expedia' ,'stock_name': 'EXPE'}
        ,{'name': 'Expeditors International of Washington' ,'stock_name': 'EXPD'}
        ,{'name': 'Extra Space Storage' ,'stock_name': 'EXR'}
        ,{'name': 'ExxonMobil' ,'stock_name': 'XOM'}
        ,{'name': 'F5 Networks' ,'stock_name': 'FFIV'}
        ,{'name': 'Fastenal' ,'stock_name': 'FAST'}
        ,{'name': 'FedEx' ,'stock_name': 'FDX'}
        ,{'name': 'Fidelity National Information Services' ,'stock_name': 'FIS'}
        ,{'name': 'Fifth Third Bancorp' ,'stock_name': 'FITB'}
        ,{'name': 'First Republic Bank' ,'stock_name': 'FRC'}
        ,{'name': 'FirstEnergy' ,'stock_name': 'FE'}
        ,{'name': 'Fiserv' ,'stock_name': 'FISV'}
        ,{'name': 'FleetCor Technologies' ,'stock_name': 'FLT'}
        ,{'name': 'FMC' ,'stock_name': 'FMC'}
        ,{'name': 'Ford Motor' ,'stock_name': 'F'}
        ,{'name': 'Fortinet' ,'stock_name': 'FTNT'}
        ,{'name': 'Fortive' ,'stock_name': 'FTV'}
        ,{'name': 'Fortune Brands Home & Security' ,'stock_name': 'FBHS'}
        ,{'name': 'Fox A' ,'stock_name': 'FOXA'}
        ,{'name': 'Fox B' ,'stock_name': 'FOX'}
        ,{'name': 'Franklin Resources' ,'stock_name': 'BEN'}
        ,{'name': 'Freeport-McMoRan' ,'stock_name': 'FCX'}
        ,{'name': 'Garmin' ,'stock_name': 'GRMN'}
        ,{'name': 'Gartner' ,'stock_name': 'IT'}
        ,{'name': 'Generac Holdings' ,'stock_name': 'GNRC'}
        ,{'name': 'General Dynamics' ,'stock_name': 'GD'}
        ,{'name': 'General Electric' ,'stock_name': 'GE'}
        ,{'name': 'General Mills' ,'stock_name': 'GIS'}
        ,{'name': 'General Motors' ,'stock_name': 'GM'}
        ,{'name': 'Genuine Parts' ,'stock_name': 'GPC'}
        ,{'name': 'Gilead Sciences' ,'stock_name': 'GILD'}
        ,{'name': 'Global Payments' ,'stock_name': 'GPN'}
        ,{'name': 'Globe Life' ,'stock_name': 'GL'}
        ,{'name': 'Goldman Sachs' ,'stock_name': 'GS'}
        ,{'name': 'Halliburton' ,'stock_name': 'HAL'}
        ,{'name': 'Hartford Financial Services Group' ,'stock_name': 'HIG'}
        ,{'name': 'Hasbro' ,'stock_name': 'HAS'}
        ,{'name': 'HCA Holdings' ,'stock_name': 'HCA'}
        ,{'name': 'Healthpeak Properties' ,'stock_name': 'PEAK'}
        ,{'name': 'Henry Schein' ,'stock_name': 'HSIC'}
        ,{'name': 'Hess' ,'stock_name': 'HES'}
        ,{'name': 'Hewlett Packard Enterprise' ,'stock_name': 'HPE'}
        ,{'name': 'Hilton Worldwide Holdings' ,'stock_name': 'HLT'}
        ,{'name': 'Hologic' ,'stock_name': 'HOLX'}
        ,{'name': 'Home Depot' ,'stock_name': 'HD'}
        ,{'name': 'Honeywell' ,'stock_name': 'HON'}
        ,{'name': 'Hormel Foods' ,'stock_name': 'HRL'}
        ,{'name': 'Host Hotels & Resorts' ,'stock_name': 'HST'}
        ,{'name': 'Howmet Aerospace' ,'stock_name': 'HWM'}
        ,{'name': 'HP' ,'stock_name': 'HPQ'}
        ,{'name': 'Humana' ,'stock_name': 'HUM'}
        ,{'name': 'Huntington Bancstocks' ,'stock_name': 'HBAN'}
        ,{'name': 'Huntington Ingalls Industries' ,'stock_name': 'HII'}
        ,{'name': 'IBM' ,'stock_name': 'IBM'}
        ,{'name': 'IDEX' ,'stock_name': 'IEX'}
        ,{'name': 'IDEXX Laboratories' ,'stock_name': 'IDXX'}
        ,{'name': 'Illinois Tool Works' ,'stock_name': 'ITW'}
        ,{'name': 'Illumina' ,'stock_name': 'ILMN'}
        ,{'name': 'Incyte' ,'stock_name': 'INCY'}
        ,{'name': 'Ingersoll Rand' ,'stock_name': 'IR'}
        ,{'name': 'Intel' ,'stock_name': 'INTC'}
        ,{'name': 'IntercontinentalExchange Group' ,'stock_name': 'ICE'}
        ,{'name': 'The Hershey' ,'stock_name': 'HSY'}
        ,{'name': 'Harris' ,'stock_name': 'LHX'}
        ,{'name': 'International Flavors & Fragrances' ,'stock_name': 'IFF'}
        ,{'name': 'International Paper' ,'stock_name': 'IP'}
        ,{'name': 'Interpublic Group of Cos' ,'stock_name': 'IPG'}
        ,{'name': 'Intuit' ,'stock_name': 'INTU'}
        ,{'name': 'Intuitive Surgical' ,'stock_name': 'ISRG'}
        ,{'name': 'Invesco' ,'stock_name': 'IVZ'}
        ,{'name': 'IQVIA Holdings' ,'stock_name': 'IQV'}
        ,{'name': 'Iron Mountain' ,'stock_name': 'IRM'}
        ,{'name': 'J. M. Smucker' ,'stock_name': 'SJM'}
        ,{'name': 'J.B. Hunt Transportation Services' ,'stock_name': 'JBHT'}
        ,{'name': 'Jack Henry & Associates' ,'stock_name': 'JKHY'}
        ,{'name': 'Jacobs Engineering Group' ,'stock_name': 'J'}
        ,{'name': 'Johnson & Johnson' ,'stock_name': 'JNJ'}
        ,{'name': 'Johnson Controls International' ,'stock_name': 'JCI'}
        ,{'name': 'JPMorgan Chase' ,'stock_name': 'JPM'}
        ,{'name': 'Juniper Networks' ,'stock_name': 'JNPR'}
        ,{'name': 'Kellogg' ,'stock_name': 'K'}
        ,{'name': 'KeyCorp' ,'stock_name': 'KEY'}
        ,{'name': 'Keysight Technologies' ,'stock_name': 'KEYS'}
        ,{'name': 'Kimberly-Clark' ,'stock_name': 'KMB'}
        ,{'name': 'Kimco Realty' ,'stock_name': 'KIM'}
        ,{'name': 'Kinder Morgan' ,'stock_name': 'KMI'}
        ,{'name': 'KLA-Tencor' ,'stock_name': 'KLAC'}
        ,{'name': 'Kroger' ,'stock_name': 'KR'}
        ,{'name': 'Laboratory' ,'stock_name': 'LH'}
        ,{'name': 'Lam Research' ,'stock_name': 'LRCX'}
        ,{'name': 'Lamb Weston Holdings' ,'stock_name': 'LW'}
        ,{'name': 'Las Vegas Sands' ,'stock_name': 'LVS'}
        ,{'name': 'Leidos Holdings' ,'stock_name': 'LDOS'}
        ,{'name': 'Lennar' ,'stock_name': 'LEN'}
        ,{'name': 'Lincoln National' ,'stock_name': 'LNC'}
        ,{'name': 'Linde' ,'stock_name': 'LIN'}
        ,{'name': 'Live Nation Entertainment' ,'stock_name': 'LYV'}
        ,{'name': 'LKQ' ,'stock_name': 'LKQ'}
        ,{'name': 'Lockheed Martin' ,'stock_name': 'LMT'}
        ,{'name': 'Loews' ,'stock_name': 'L'}
        ,{'name': 'Lowes Companies' ,'stock_name': 'LOW'}
        ,{'name': 'Lumen Technologies' ,'stock_name': 'LUMN'}
        ,{'name': 'Lyondellbasell Industries' ,'stock_name': 'LYB'}
        ,{'name': 'M&T Bank' ,'stock_name': 'MTB'}
        ,{'name': 'Marathon Oil' ,'stock_name': 'MRO'}
        ,{'name': 'Marathon Petroleum Corporation' ,'stock_name': 'MPC'}
        ,{'name': 'MarketAxess Holdings' ,'stock_name': 'MKTX'}
        ,{'name': 'Marriott' ,'stock_name': 'MAR'}
        ,{'name': 'Marsh & McLennan Cos' ,'stock_name': 'MMC'}
        ,{'name': 'Martin Marietta Materials' ,'stock_name': 'MLM'}
        ,{'name': 'Masco' ,'stock_name': 'MAS'}
        ,{'name': 'MasterCard' ,'stock_name': 'MA'}
        ,{'name': 'McCormick' ,'stock_name': 'MKC'}
        ,{'name': 'McDonalds' ,'stock_name': 'MCD'}
        ,{'name': 'McKesson' ,'stock_name': 'MCK'}
        ,{'name': 'Medtronic' ,'stock_name': 'MDT'}
        ,{'name': 'Merck' ,'stock_name': 'MRK'}
        ,{'name': 'Meta Platforms' ,'stock_name': 'META'}
        ,{'name': 'MetLife' ,'stock_name': 'MET'}
        ,{'name': 'Mettler-Toledo International' ,'stock_name': 'MTD'}
        ,{'name': 'MGM Resorts International' ,'stock_name': 'MGM'}
        ,{'name': 'Microchip Technology' ,'stock_name': 'MCHP'}
        ,{'name': 'Micron Technology' ,'stock_name': 'MU'}
        ,{'name': 'Microsoft' ,'stock_name': 'MSFT'}
        ,{'name': 'Mid-America Apartment Communities' ,'stock_name': 'MAA'}
        ,{'name': 'Moderna' ,'stock_name': 'MRNA'}
        ,{'name': 'Mohawk Industries' ,'stock_name': 'MHK'}
        ,{'name': 'Molina Healthcare' ,'stock_name': 'MOH'}
        ,{'name': 'Molson Coors Brewing Company' ,'stock_name': 'TAP'}
        ,{'name': 'Mondelez' ,'stock_name': 'MDLZ'}
        ,{'name': 'Monolithic Power Systems' ,'stock_name': 'MPWR'}
        ,{'name': 'Monster Beverage' ,'stock_name': 'MNST'}
        ,{'name': 'Moodys' ,'stock_name': 'MCO'}
        ,{'name': 'Morgan Stanley' ,'stock_name': 'MS'}
        ,{'name': 'Motorola Solutions' ,'stock_name': 'MSI'}
        ,{'name': 'MSCI' ,'stock_name': 'MSCI'}
        ,{'name': 'Nasdaq' ,'stock_name': 'NDAQ'}
        ,{'name': 'NetApp' ,'stock_name': 'NTAP'}
        ,{'name': 'Netflix' ,'stock_name': 'NFLX'}
        ,{'name': 'Newell Brands' ,'stock_name': 'NWL'}
        ,{'name': 'Newmont Mining' ,'stock_name': 'NEM'}
        ,{'name': 'News' ,'stock_name': 'NWSA'}
        ,{'name': 'News b' ,'stock_name': 'NWS'}
        ,{'name': 'NextEra Energy' ,'stock_name': 'NEE'}
        ,{'name': 'Nielsen Holdings' ,'stock_name': 'NLSN'}
        ,{'name': 'Nike' ,'stock_name': 'NKE'}
        ,{'name': 'Nisource' ,'stock_name': 'NI'}
        ,{'name': 'Norfolk Southern' ,'stock_name': 'NSC'}
        ,{'name': 'Northern Trust' ,'stock_name': 'NTRS'}
        ,{'name': 'Northrop Grumman' ,'stock_name': 'NOC'}
        ,{'name': 'NortonLifeLock' ,'stock_name': 'NLOK'}
        ,{'name': 'Norwegian Cruise Line' ,'stock_name': 'NCLH'}
        ,{'name': 'NRG Energy' ,'stock_name': 'NRG'}
        ,{'name': 'Nucor' ,'stock_name': 'NUE'}
        ,{'name': 'NVIDIA' ,'stock_name': 'NVDA'}
        ,{'name': 'NVR' ,'stock_name': 'NVR'}
        ,{'name': 'NXP Semiconductors' ,'stock_name': 'NXPI'}
        ,{'name': 'O Reilly Automotive' ,'stock_name': 'ORLY'}
        ,{'name': 'Occidental Petroleum' ,'stock_name': 'OXY'}
        ,{'name': 'The Mosaic' ,'stock_name': 'MOS'}
        ,{'name': 'Public Service Enterprise Groups Inc' ,'stock_name': 'PEG'}
        ,{'name': 'Public Storage' ,'stock_name': 'PSA'}
        ,{'name': 'Old Dominion Freight Line' ,'stock_name': 'ODFL'}
        ,{'name': 'Omnicom Group' ,'stock_name': 'OMC'}
        ,{'name': 'ONEOK' ,'stock_name': 'OKE'}
        ,{'name': 'Oracle' ,'stock_name': 'ORCL'}
        ,{'name': 'Organon & Company' ,'stock_name': 'OGN'}
        ,{'name': 'Otis Worldwide Corporation Registered Shs When Issued' ,'stock_name': 'OTIS'}
        ,{'name': 'Paccar' ,'stock_name': 'PCAR'}
        ,{'name': 'Packaging' ,'stock_name': 'PKG'}
        ,{'name': 'Parker Hannifin' ,'stock_name': 'PH'}
        ,{'name': 'Paychex' ,'stock_name': 'PAYX'}
        ,{'name': 'Paycom Software' ,'stock_name': 'PAYC'}
        ,{'name': 'PayPal' ,'stock_name': 'PYPL'}
        ,{'name': 'Penn National Gaming' ,'stock_name': 'PENN'}
        ,{'name': 'Pentair' ,'stock_name': 'PNR'}
        ,{'name': 'PepsiCo' ,'stock_name': 'PEP'}
        ,{'name': 'PerkinElmer' ,'stock_name': 'PKI'}
        ,{'name': 'Pfizer' ,'stock_name': 'PFE'}
        ,{'name': 'Philip Morris' ,'stock_name': 'PM'}
        ,{'name': 'Phillips 66' ,'stock_name': 'PSX'}
        ,{'name': 'Pinnacle West Capital' ,'stock_name': 'PNW'}
        ,{'name': 'Pioneer Natural Resources' ,'stock_name': 'PXD'}
        ,{'name': 'PNC Financial Services Group' ,'stock_name': 'PNC'}
        ,{'name': 'Pool' ,'stock_name': 'POOL'}
        ,{'name': 'PPG Industries' ,'stock_name': 'PPG'}
        ,{'name': 'PPL' ,'stock_name': 'PPL'}
        ,{'name': 'Principal Financial Group' ,'stock_name': 'PFG'}
        ,{'name': 'Procter & Gamble' ,'stock_name': 'PG'}
        ,{'name': 'Progressive' ,'stock_name': 'PGR'}
        ,{'name': 'Prologis' ,'stock_name': 'PLD'}
        ,{'name': 'Prudential Financial' ,'stock_name': 'PRU'}
        ,{'name': 'PTC' ,'stock_name': 'PTC'}
        ,{'name': 'PulteGroup' ,'stock_name': 'PHM'}
        ,{'name': 'PVH' ,'stock_name': 'PVH'}
        ,{'name': 'Qorvo' ,'stock_name': 'QRVO'}
        ,{'name': 'QUALCOMM' ,'stock_name': 'QCOM'}
        ,{'name': 'Quanta Services' ,'stock_name': 'PWR'}
        ,{'name': 'Quest Diagnostics' ,'stock_name': 'DGX'}
        ,{'name': 'Ralph Lauren a' ,'stock_name': 'RL'}
        ,{'name': 'Raymond James Financial' ,'stock_name': 'RJF'}
        ,{'name': 'Raytheon Technologies' ,'stock_name': 'RTX'}
        ,{'name': 'Realty Income' ,'stock_name': 'O'}
        ,{'name': 'Regency Centers' ,'stock_name': 'REG'}
        ,{'name': 'Regeneron Pharmaceuticals' ,'stock_name': 'REGN'}
        ,{'name': 'Regions Financial' ,'stock_name': 'RF'}
        ,{'name': 'Republic Services' ,'stock_name': 'RSG'}
        ,{'name': 'ResMed' ,'stock_name': 'RMD'}
        ,{'name': 'ViacomCBS' ,'stock_name': 'PARA'}
        ,{'name': 'Robert Half' ,'stock_name': 'RHI'}
        ,{'name': 'Rockwell Automation' ,'stock_name': 'ROK'}
        ,{'name': 'Rollins' ,'stock_name': 'ROL'}
        ,{'name': 'Roper Industries' ,'stock_name': 'ROP'}
        ,{'name': 'Ross Stores' ,'stock_name': 'ROST'}
        ,{'name': 'Royal Caribbean Cruises' ,'stock_name': 'RCL'}
        ,{'name': 'S&P Global' ,'stock_name': 'SPGI'}
        ,{'name': 'Salesforce' ,'stock_name': 'CRM'}
        ,{'name': 'SBA Communications REIT' ,'stock_name': 'SBAC'}
        ,{'name': 'Schlumberger' ,'stock_name': 'SLB'}
        ,{'name': 'Seagate Technology Holdings' ,'stock_name': 'STX'}
        ,{'name': 'Sealed Air' ,'stock_name': 'SEE'}
        ,{'name': 'Sempra Energy' ,'stock_name': 'SRE'}
        ,{'name': 'ServiceNow' ,'stock_name': 'NOW'}
        ,{'name': 'Sherwin-Williams' ,'stock_name': 'SHW'}
        ,{'name': 'Simon Property Group' ,'stock_name': 'SPG'}
        ,{'name': 'Skyworks Solutions' ,'stock_name': 'SWKS'}
        ,{'name': 'Snap-On' ,'stock_name': 'SNA'}
        ,{'name': 'Southern' ,'stock_name': 'SO'}
        ,{'name': 'Southwest Airlines' ,'stock_name': 'LUV'}
        ,{'name': 'Stanley Black & Decker' ,'stock_name': 'SWK'}
        ,{'name': 'Starbucks' ,'stock_name': 'SBUX'}
        ,{'name': 'State Street' ,'stock_name': 'STT'}
        ,{'name': 'STERIS' ,'stock_name': 'STE'}
        ,{'name': 'Stryker' ,'stock_name': 'SYK'}
        ,{'name': 'SVB Financial Group Shs' ,'stock_name': 'SIVB'}
        ,{'name': 'Synchrony Financial' ,'stock_name': 'SYF'}
        ,{'name': 'Synopsys' ,'stock_name': 'SNPS'}
        ,{'name': 'Sysco' ,'stock_name': 'SYY'}
        ,{'name': 'T. Rowe Price Group' ,'stock_name': 'TROW'}
        ,{'name': 'Take Two' ,'stock_name': 'TTWO'}
        ,{'name': 'Tapestry' ,'stock_name': 'TPR'}
        ,{'name': 'Target' ,'stock_name': 'TGT'}
        ,{'name': 'TE Connectivity' ,'stock_name': 'TEL'}
        ,{'name': 'Teledyne Technologies' ,'stock_name': 'TDY'}
        ,{'name': 'Teleflex' ,'stock_name': 'TFX'}
        ,{'name': 'Teradyne' ,'stock_name': 'TER'}
        ,{'name': 'Tesla' ,'stock_name': 'TSLA'}
        ,{'name': 'Texas Instruments' ,'stock_name': 'TXN'}
        ,{'name': 'Textron' ,'stock_name': 'TXT'}
        ,{'name': 'The Kraft Heinz Company' ,'stock_name': 'KHC'}
        ,{'name': 'Thermo Fisher Scientific' ,'stock_name': 'TMO'}
        ,{'name': 'TJX Cos' ,'stock_name': 'TJX'}
        ,{'name': 'T-Mobile US' ,'stock_name': 'TMUS'}
        ,{'name': 'Tractor Supply' ,'stock_name': 'TSCO'}
        ,{'name': 'Trane Technologies' ,'stock_name': 'TT'}
        ,{'name': 'TransDigm Group' ,'stock_name': 'TDG'}
        ,{'name': 'Travelers' ,'stock_name': 'TRV'}
        ,{'name': 'Grainger' ,'stock_name': 'GWW'}
        ,{'name': 'Trimble Navigation' ,'stock_name': 'TRMB'}
        ,{'name': 'Truist Financial Corporation' ,'stock_name': 'TFC'}
        ,{'name': 'Twitter' ,'stock_name': 'TWTR'}
        ,{'name': 'Tyler Technologies' ,'stock_name': 'TYL'}
        ,{'name': 'Tyson Foods' ,'stock_name': 'TSN'}
        ,{'name': 'U.S. Bancorp' ,'stock_name': 'USB'}
        ,{'name': 'UDR' ,'stock_name': 'UDR'}
        ,{'name': 'Ulta Beauty' ,'stock_name': 'ULTA'}
        ,{'name': 'Union Pacific' ,'stock_name': 'UNP'}
        ,{'name': 'United Airlines Holdings' ,'stock_name': 'UAL'}
        ,{'name': 'United Parcel Service' ,'stock_name': 'UPS'}
        ,{'name': 'United Rentals' ,'stock_name': 'URI'}
        ,{'name': 'UnitedHealth' ,'stock_name': 'UNH'}
        ,{'name': 'Universal Health Services' ,'stock_name': 'UHS'}
        ,{'name': 'V.F' ,'stock_name': 'VFC'}
        ,{'name': 'Valero Energy' ,'stock_name': 'VLO'}
        ,{'name': 'Ventas' ,'stock_name': 'VTR'}
        ,{'name': 'VeriSign' ,'stock_name': 'VRSN'}
        ,{'name': 'Verisk Analytic a' ,'stock_name': 'VRSK'}
        ,{'name': 'Verizon' ,'stock_name': 'VZ'}
        ,{'name': 'Vertex Pharmaceuticals' ,'stock_name': 'VRTX'}
        ,{'name': 'Viatris' ,'stock_name': 'VTRS'}
        ,{'name': 'Visa' ,'stock_name': 'V'}
        ,{'name': 'Vornado Realty Trust' ,'stock_name': 'VNO'}
        ,{'name': 'Vulcan Materials' ,'stock_name': 'VMC'}
        ,{'name': 'W. R. Berkley' ,'stock_name': 'WRB'}
        ,{'name': 'Wabtec' ,'stock_name': 'WAB'}
        ,{'name': 'Walgreens Boots Alliance' ,'stock_name': 'WBA'}
        ,{'name': 'Walmart' ,'stock_name': 'WMT'}
        ,{'name': 'Walt Disney' ,'stock_name': 'DIS'}
        ,{'name': 'Waste Management' ,'stock_name': 'WM'}
        ,{'name': 'Waters' ,'stock_name': 'WAT'}
        ,{'name': 'WEC Energy Group' ,'stock_name': 'WEC'}
        ,{'name': 'Wells Fargo' ,'stock_name': 'WFC'}
        ,{'name': 'Welltower' ,'stock_name': 'WELL'}
        ,{'name': 'West Pharmaceutical Services' ,'stock_name': 'WST'}
        ,{'name': 'Western Digital' ,'stock_name': 'WDC'}
        ,{'name': 'WestRock' ,'stock_name': 'WRK'}
        ,{'name': 'Weyerhaeuser' ,'stock_name': 'WY'}
        ,{'name': 'Whirlpool' ,'stock_name': 'WHR'}
        ,{'name': 'Williams Companies' ,'stock_name': 'WMB'}
        ,{'name': 'Willis Towers Watson' ,'stock_name': 'WTW'}
        ,{'name': 'Wynn Resorts' ,'stock_name': 'WYNN'}
        ,{'name': 'Xcel Energy' ,'stock_name': 'XEL'}
        ,{'name': 'Xylem' ,'stock_name': 'XYL'}
        ,{'name': 'YUM! Brands' ,'stock_name': 'YUM'}
        ,{'name': 'Zebra Technologies' ,'stock_name': 'ZBRA'}
    ]

    return data
