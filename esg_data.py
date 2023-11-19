def sp500():
    sp500 = [
        {'name':'3M','stock_name':'MMM', 'ricCode':'MMM', 'esg_value': 0}
        , {'name':'A.O. Smith','stock_name':'AOS', 'ricCode':'AOS', 'esg_value': 0}
        , {'name':'Abbott Laboratories','stock_name':'ABT', 'ricCode':'ABT', 'esg_value': 0}
        , {'name':'AbbVie','stock_name':'ABBV', 'ricCode':'ABBV.K', 'esg_value': 0}
        , {'name':'ABIOMED','stock_name':'ABMD', 'ricCode':'ABMD.O', 'esg_value': 0}
        , {'name':'Accenture','stock_name':'ACN', 'ricCode':'ACN', 'esg_value': 0}
        , {'name':'Activision Blizzard','stock_name':'ATVI', 'ricCode':'ATVI.O', 'esg_value': 0}
        , {'name':'Adobe','stock_name':'ADBE', 'ricCode':'ADBE.O', 'esg_value': 0}
        , {'name':'Advance Auto Parts','stock_name':'AAP', 'ricCode':'AAP', 'esg_value': 0}
        , {'name':'AES','stock_name':'AES', 'ricCode':'AES', 'esg_value': 0}
        , {'name':'Aflac','stock_name':'AFL', 'ricCode':'AFL', 'esg_value': 0}
        , {'name':'Agilent Technologies','stock_name':'A', 'ricCode':'A', 'esg_value': 0}
        , {'name':'Air Products and Chemicals','stock_name':'APD', 'ricCode':'APD', 'esg_value': 0}
        , {'name':'Akamai','stock_name':'AKAM', 'ricCode':'AKAM.O', 'esg_value': 0}
        , {'name':'Alaska Air Group','stock_name':'ALK', 'ricCode':'ALK', 'esg_value': 0}
        , {'name':'Albemarle','stock_name':'ALB', 'ricCode':'ALB', 'esg_value': 0}
        , {'name':'Alexandria Real Estate Equities','stock_name':'ARE', 'ricCode':'ARE', 'esg_value': 0}
        , {'name':'Align Technology','stock_name':'ALGN', 'ricCode':'ALGN.O', 'esg_value': 0}
        , {'name':'Allegion','stock_name':'ALLE', 'ricCode':'ALLE.K', 'esg_value': 0}
        , {'name':'Alliant Energy','stock_name':'LNT', 'ricCode':'LNT.O', 'esg_value': 0}
        , {'name':'Allstate','stock_name':'ALL', 'ricCode':'ALL', 'esg_value': 0}
        , {'name':'Alphabet A','stock_name':'GOOGL', 'ricCode':'GOOGL.O', 'esg_value': 0}
        , {'name':'Alphabet C','stock_name':'GOOG', 'ricCode':'GOOG', 'esg_value': 0}
        , {'name':'Altria','stock_name':'MO', 'ricCode':'MO', 'esg_value': 0}
        , {'name':'Amazon','stock_name':'AMZN', 'ricCode':'AMZN.O', 'esg_value': 0}
        , {'name':'Amcor','stock_name':'AMCR', 'ricCode':'AMCR.K', 'esg_value': 0}
        , {'name':'AMD','stock_name':'AMD', 'ricCode':'AMD.O', 'esg_value': 0}
        , {'name':'Ameren','stock_name':'AEE', 'ricCode':'AEE', 'esg_value': 0}
        , {'name':'American Airlines','stock_name':'AAL', 'ricCode':'AAL.O', 'esg_value': 0}
        , {'name':'American Electric Power','stock_name':'AEP', 'ricCode':'AEP.O', 'esg_value': 0}
        , {'name':'American Express','stock_name':'AXP', 'ricCode':'AXP', 'esg_value': 0}
        , {'name':'American International Group','stock_name':'AIG', 'ricCode':'AIG', 'esg_value': 0}
        , {'name':'American Tower','stock_name':'AMT', 'ricCode':'AMT', 'esg_value': 0}
        , {'name':'American Water Works','stock_name':'AWK', 'ricCode':'AWK', 'esg_value': 0}
        , {'name':'Ameriprise Financial','stock_name':'AMP', 'ricCode':'AMP', 'esg_value': 0}
        , {'name':'AmerisourceBergen','stock_name':'ABC', 'ricCode':'ABC', 'esg_value': 0}
        , {'name':'Ametek','stock_name':'AME', 'ricCode':'AME', 'esg_value': 0}
        , {'name':'Amgen','stock_name':'AMGN', 'ricCode':'AMGN.O', 'esg_value': 0}
        , {'name':'Amphenol','stock_name':'APH', 'ricCode':'APH', 'esg_value': 0}
        , {'name':'Analog Devices','stock_name':'ADI', 'ricCode':'ADI.O', 'esg_value': 0}
        , {'name':'ANSYS','stock_name':'ANSS', 'ricCode':'ANSS.O', 'esg_value': 0}
        , {'name':'Anthem','stock_name':'ANTM', 'ricCode':'ANTM.K', 'esg_value': 0}
        , {'name':'Aon','stock_name':'AON', 'ricCode':'AON', 'esg_value': 0}
        , {'name':'APA Corporation Registered Shs','stock_name':'APA', 'ricCode':'APA.AX', 'esg_value': 0}
        , {'name':'Apple','stock_name':'AAPL', 'ricCode':'AAPL.O', 'esg_value': 0}
        , {'name':'Applied Materials','stock_name':'AMAT', 'ricCode':'AMAT.O', 'esg_value': 0}
        , {'name':'Aptiv','stock_name':'APTV', 'ricCode':'APTV.K', 'esg_value': 0}
        , {'name':'Archer Daniels Midland','stock_name':'ADM', 'ricCode':'ADM', 'esg_value': 0}
        , {'name':'Arista Networks','stock_name':'ANET', 'ricCode':'ANET.K', 'esg_value': 0}
        , {'name':'Arthur J. Gallagher','stock_name':'AJG', 'ricCode':'AJG', 'esg_value': 0}
        , {'name':'Assurant','stock_name':'AIZ', 'ricCode':'AIZ', 'esg_value': 0}
        , {'name':'AT&T','stock_name':'T', 'ricCode':'T', 'esg_value': 0}
        , {'name':'Atmos Energy','stock_name':'ATO', 'ricCode':'ATO', 'esg_value': 0}
        , {'name':'Autodesk','stock_name':'ADSK', 'ricCode':'ADSK.O', 'esg_value': 0}
        , {'name':'Automatic Data Processing','stock_name':'ADP', 'ricCode':'ADP.O', 'esg_value': 0}
        , {'name':'AutoZone','stock_name':'AZO', 'ricCode':'AZO', 'esg_value': 0}
        , {'name':'AvalonBay Communities','stock_name':'AVB', 'ricCode':'AVB', 'esg_value': 0}
        , {'name':'Avery Dennison','stock_name':'AVY', 'ricCode':'AVY', 'esg_value': 0}
        , {'name':'Baker Hughes','stock_name':'BKR', 'ricCode':'BKR', 'esg_value': 0}
        , {'name':'Ball','stock_name':'BALL', 'ricCode':'BLL', 'esg_value': 0}
        , {'name':'Bank of America','stock_name':'BAC', 'ricCode':'BAC', 'esg_value': 0}
        , {'name':'Bank of New York Mellon','stock_name':'BK', 'ricCode':'BK', 'esg_value': 0}
        , {'name':'Bath & Body Works','stock_name':'BBWI', 'ricCode':'BBWI.K', 'esg_value': 0}
        , {'name':'Baxter International','stock_name':'BAX', 'ricCode':'BAX', 'esg_value': 0}
        , {'name':'Becton, Dickinson','stock_name':'BDX', 'ricCode':'BDX', 'esg_value': 0}
        , {'name':'Berkshire Hathaway','stock_name':'BRK-B', 'ricCode':'BRKa', 'esg_value': 0}
        , {'name':'Best Buy','stock_name':'BBY', 'ricCode':'BBY', 'esg_value': 0}
        , {'name':'Biogen','stock_name':'BIIB', 'ricCode':'BIIB.O', 'esg_value': 0}
        , {'name':'Bio-Rad Laboratories','stock_name':'BIO', 'ricCode':'BIO', 'esg_value': 0}
        , {'name':'Bio-Techne','stock_name':'TECH', 'ricCode':'TECH.O', 'esg_value': 0}
        , {'name':'BlackRock','stock_name':'BLK', 'ricCode':'BLK', 'esg_value': 0}
        , {'name':'Boeing','stock_name':'BA', 'ricCode':'BA', 'esg_value': 0}
        , {'name':'Booking Holdings','stock_name':'BKNG', 'ricCode':'BKNG.O', 'esg_value': 0}
        , {'name':'BorgWarner','stock_name':'BWA', 'ricCode':'BWA', 'esg_value': 0}
        , {'name':'Boston Properties','stock_name':'BXP', 'ricCode':'BXP', 'esg_value': 0}
        , {'name':'Boston Scientific','stock_name':'BSX', 'ricCode':'BSX', 'esg_value': 0}
        , {'name':'Bristol-Myers Squibb','stock_name':'BMY', 'ricCode':'BMY', 'esg_value': 0}
        , {'name':'Broadcom','stock_name':'AVGO', 'ricCode':'AVGO.O', 'esg_value': 0}
        , {'name':'Broadridge Financial Solutions','stock_name':'BR', 'ricCode':'BR', 'esg_value': 0}
        , {'name':'Brown-Forman b','stock_name':'BF-B', 'ricCode':'BFb', 'esg_value': 0}
        , {'name':'C.H. Robinson Worldwide','stock_name':'CHRW', 'ricCode':'CHRW.O', 'esg_value': 0}
        , {'name':'Cadence Design Systems','stock_name':'CDNS', 'ricCode':'CDNS.O', 'esg_value': 0}
        , {'name':'Caesars Entertainment','stock_name':'CZR', 'ricCode':'CZR.O', 'esg_value': 0}
        , {'name':'Campbell Soup','stock_name':'CPB', 'ricCode':'CPB', 'esg_value': 0}
        , {'name':'Capital One Financial','stock_name':'COF', 'ricCode':'COF', 'esg_value': 0}
        , {'name':'Cardinal Health','stock_name':'CAH', 'ricCode':'CAH', 'esg_value': 0}
        , {'name':'CarMax','stock_name':'KMX', 'ricCode':'KMX', 'esg_value': 0}
        , {'name':'Carnival','stock_name':'CCL', 'ricCode':'CCL', 'esg_value': 0}
        , {'name':'Carrier Global Corporation Registered Shs When Issued','stock_name':'CARR', 'ricCode':'CAR.O', 'esg_value': 0}
        , {'name':'Catalent','stock_name':'CTLT', 'ricCode':'CTLT.K', 'esg_value': 0}
        , {'name':'Caterpillar','stock_name':'CAT', 'ricCode':'CAT', 'esg_value': 0}
        , {'name':'CBRE Grou a','stock_name':'CBRE', 'ricCode':'CBRE.K', 'esg_value': 0}
        , {'name':'CDW','stock_name':'CDW', 'ricCode':'CDW.O', 'esg_value': 0}
        , {'name':'Celanese','stock_name':'CE', 'ricCode':'CE', 'esg_value': 0}
        , {'name':'Centene','stock_name':'CNC', 'ricCode':'CNC', 'esg_value': 0}
        , {'name':'CenterPoint Energy','stock_name':'CNP', 'ricCode':'CNP', 'esg_value': 0}
        , {'name':'Cabot Oil & Gas','stock_name':'CTRA', 'ricCode':'CTRA.K', 'esg_value': 0}
        , {'name':'CF Industries Holdings','stock_name':'CF', 'ricCode':'CF', 'esg_value': 0}
        , {'name':'Charles River Laboratories International','stock_name':'CRL', 'ricCode':'CRL', 'esg_value': 0}
        , {'name':'Charles Schwab','stock_name':'SCHW', 'ricCode':'SCHW.K', 'esg_value': 0}
        , {'name':'Charter a','stock_name':'CHTR', 'ricCode':'CHTR.O', 'esg_value': 0}
        , {'name':'Chevron','stock_name':'CVX', 'ricCode':'CVX', 'esg_value': 0}
        , {'name':'Chipotle Mexican Grill','stock_name':'CMG', 'ricCode':'CMG', 'esg_value': 0}
        , {'name':'Chubb','stock_name':'CB', 'ricCode':'CB', 'esg_value': 0}
        , {'name':'Church & Dwight','stock_name':'CHD', 'ricCode':'CHD', 'esg_value': 0}
        , {'name':'Cigna','stock_name':'CI', 'ricCode':'CI', 'esg_value': 0}
        , {'name':'Cincinnati Financial','stock_name':'CINF', 'ricCode':'CINF.O', 'esg_value': 0}
        , {'name':'Cintas','stock_name':'CTAS', 'ricCode':'CTAS.O', 'esg_value': 0}
        , {'name':'Cisco','stock_name':'CSCO', 'ricCode':'CSCO.O', 'esg_value': 0}
        , {'name':'Citigroup','stock_name':'C', 'ricCode':'C', 'esg_value': 0}
        , {'name':'Citizens Financial Group','stock_name':'CFG', 'ricCode':'CFG', 'esg_value': 0}
        , {'name':'Citrix Systems','stock_name':'CTXS', 'ricCode':'CTXS.O', 'esg_value': 0}
        , {'name':'Clorox','stock_name':'CLX', 'ricCode':'CLX', 'esg_value': 0}
        , {'name':'CME Grou a','stock_name':'CME', 'ricCode':'CME.O', 'esg_value': 0}
        , {'name':'CMS Energy','stock_name':'CMS', 'ricCode':'CMS', 'esg_value': 0}
        , {'name':'Coca-Cola','stock_name':'KO', 'ricCode':'KO', 'esg_value': 0}
        , {'name':'Cognizant','stock_name':'CTSH', 'ricCode':'CTSH.O', 'esg_value': 0}
        , {'name':'Colgate-Palmolive','stock_name':'CL', 'ricCode':'CL', 'esg_value': 0}
        , {'name':'Comcast','stock_name':'CMCSA', 'ricCode':'CMCSA.O', 'esg_value': 0}
        , {'name':'Comerica','stock_name':'CMA', 'ricCode':'CMA', 'esg_value': 0}
        , {'name':'ConAgra Foods','stock_name':'CAG', 'ricCode':'CAG', 'esg_value': 0}
        , {'name':'ConocoPhillips','stock_name':'COP', 'ricCode':'COP', 'esg_value': 0}
        , {'name':'Consolidated Edison','stock_name':'ED', 'ricCode':'ED', 'esg_value': 0}
        , {'name':'Constellation Brand a','stock_name':'STZ', 'ricCode':'STZ', 'esg_value': 0}
        , {'name':'Cooper Cos','stock_name':'COO', 'ricCode':'COO', 'esg_value': 0}
        , {'name':'Copart','stock_name':'CPRT', 'ricCode':'CPRT.O', 'esg_value': 0}
        , {'name':'Corning','stock_name':'GLW', 'ricCode':'GLW', 'esg_value': 0}
        , {'name':'Corteva','stock_name':'CTVA', 'ricCode':'CTVA.K', 'esg_value': 0}
        , {'name':'Costco Wholesale','stock_name':'COST', 'ricCode':'COST.O', 'esg_value': 0}
        , {'name':'Crown Castle','stock_name':'CCI', 'ricCode':'CCI', 'esg_value': 0}
        , {'name':'CSX','stock_name':'CSX', 'ricCode':'CSX.O', 'esg_value': 0}
        , {'name':'Cummins','stock_name':'CMI', 'ricCode':'CMI', 'esg_value': 0}
        , {'name':'CVS Health','stock_name':'CVS', 'ricCode':'CVS', 'esg_value': 0}
        , {'name':'D.R. Horton','stock_name':'DHI', 'ricCode':'DHI', 'esg_value': 0}
        , {'name':'Danaher','stock_name':'DHR', 'ricCode':'DHR', 'esg_value': 0}
        , {'name':'Darden Restaurants','stock_name':'DRI', 'ricCode':'DRI', 'esg_value': 0}
        , {'name':'DaVita HealthCare Partners','stock_name':'DVA', 'ricCode':'DVA', 'esg_value': 0}
        , {'name':'Deere','stock_name':'DE', 'ricCode':'DE', 'esg_value': 0}
        , {'name':'Delta Air Lines','stock_name':'DAL', 'ricCode':'DAL', 'esg_value': 0}
        , {'name':'DENTSPLY SIRONA','stock_name':'XRAY', 'ricCode':'XRAY.O', 'esg_value': 0}
        , {'name':'Devon Energy','stock_name':'DVN', 'ricCode':'DVN', 'esg_value': 0}
        , {'name':'DexCom','stock_name':'DXCM', 'ricCode':'DXCM.O', 'esg_value': 0}
        , {'name':'Diamondback Energy','stock_name':'FANG', 'ricCode':'FANG.O', 'esg_value': 0}
        , {'name':'Digital Realty Trust','stock_name':'DLR', 'ricCode':'DLR', 'esg_value': 0}
        , {'name':'Discover Financial Services','stock_name':'DFS', 'ricCode':'DFS', 'esg_value': 0}
        , {'name':'Dish Network','stock_name':'DISH', 'ricCode':'DISH.O', 'esg_value': 0}
        , {'name':'Dollar General Corporation','stock_name':'DG', 'ricCode':'DG', 'esg_value': 0}
        , {'name':'Dollar Tree','stock_name':'DLTR', 'ricCode':'DLTR.O', 'esg_value': 0}
        , {'name':'Dominion Energy','stock_name':'D', 'ricCode':'D', 'esg_value': 0}
        , {'name':'Dominos Pizza','stock_name':'DPZ', 'ricCode':'DPZ', 'esg_value': 0}
        , {'name':'Dover','stock_name':'DOV', 'ricCode':'DOV', 'esg_value': 0}
        , {'name':'Dow','stock_name':'DOW', 'ricCode':'DOW', 'esg_value': 0}
        , {'name':'DTE Energy','stock_name':'DTE', 'ricCode':'DTE', 'esg_value': 0}
        , {'name':'Duke Energy','stock_name':'DUK', 'ricCode':'DUK', 'esg_value': 0}
        , {'name':'Duke Realty','stock_name':'DRE', 'ricCode':'DRE', 'esg_value': 0}
        , {'name':'DuPont de Nemours','stock_name':'DD', 'ricCode':'DD', 'esg_value': 0}
        , {'name':'DXC Technology','stock_name':'DXC', 'ricCode':'DXC', 'esg_value': 0}
        , {'name':'Eastman Chemical Company','stock_name':'EMN', 'ricCode':'EMN', 'esg_value': 0}
        , {'name':'Eaton Corporation','stock_name':'ETN', 'ricCode':'ETN', 'esg_value': 0}
        , {'name':'eBay','stock_name':'EBAY', 'ricCode':'EBAY.O', 'esg_value': 0}
        , {'name':'Ecolab','stock_name':'ECL', 'ricCode':'ECL', 'esg_value': 0}
        , {'name':'Edison International','stock_name':'EIX', 'ricCode':'EIX', 'esg_value': 0}
        , {'name':'Edwards Lifesciences','stock_name':'EW', 'ricCode':'EW', 'esg_value': 0}
        , {'name':'Electronic Arts','stock_name':'EA', 'ricCode':'EA.O', 'esg_value': 0}
        , {'name':'Eli Lilly and','stock_name':'LLY', 'ricCode':'LLY', 'esg_value': 0}
        , {'name':'Emerson Electric','stock_name':'EMR', 'ricCode':'EMR', 'esg_value': 0}
        , {'name':'Enphase Energy','stock_name':'ENPH', 'ricCode':'ENPH.O', 'esg_value': 0}
        , {'name':'Entergy','stock_name':'ETR', 'ricCode':'ETR', 'esg_value': 0}
        , {'name':'EOG Resources','stock_name':'EOG', 'ricCode':'EOG', 'esg_value': 0}
        , {'name':'Equifax','stock_name':'EFX', 'ricCode':'EFX', 'esg_value': 0}
        , {'name':'Equinix','stock_name':'EQIX', 'ricCode':'EQIX.O', 'esg_value': 0}
        , {'name':'Equity Residential','stock_name':'EQR', 'ricCode':'EQR', 'esg_value': 0}
        , {'name':'Essex Property Trust','stock_name':'ESS', 'ricCode':'ESS', 'esg_value': 0}
        , {'name':'Estée Lauder Companies','stock_name':'EL', 'ricCode':'EL', 'esg_value': 0}
        , {'name':'Etsy','stock_name':'ETSY', 'ricCode':'ETSY.O', 'esg_value': 0}
        , {'name':'Everest Reinsurance Group','stock_name':'RE', 'ricCode':'RE', 'esg_value': 0}
        , {'name':'Evergy','stock_name':'EVRG', 'ricCode':'EVRG.K', 'esg_value': 0}
        , {'name':'Eversource Energy','stock_name':'ES', 'ricCode':'ES', 'esg_value': 0}
        , {'name':'Exelon','stock_name':'EXC', 'ricCode':'EXC.O', 'esg_value': 0}
        , {'name':'Expedia','stock_name':'EXPE', 'ricCode':'EXPE.O', 'esg_value': 0}
        , {'name':'Expeditors International of Washington','stock_name':'EXPD', 'ricCode':'EXPD.O', 'esg_value': 0}
        , {'name':'Extra Space Storage','stock_name':'EXR', 'ricCode':'EXR', 'esg_value': 0}
        , {'name':'ExxonMobil','stock_name':'XOM', 'ricCode':'XOM', 'esg_value': 0}
        , {'name':'F5 Networks','stock_name':'FFIV', 'ricCode':'FFIV.O', 'esg_value': 0}
        , {'name':'Fastenal','stock_name':'FAST', 'ricCode':'FAST.O', 'esg_value': 0}
        , {'name':'FedEx','stock_name':'FDX', 'ricCode':'FDX', 'esg_value': 0}
        , {'name':'Fidelity National Information Services','stock_name':'FIS', 'ricCode':'FIS', 'esg_value': 0}
        , {'name':'Fifth Third Bancorp','stock_name':'FITB', 'ricCode':'FITB.O', 'esg_value': 0}
        , {'name':'First Republic Bank','stock_name':'FRC', 'ricCode':'FRC', 'esg_value': 0}
        , {'name':'FirstEnergy','stock_name':'FE', 'ricCode':'FE', 'esg_value': 0}
        , {'name':'Fiserv','stock_name':'FISV', 'ricCode':'FISV.O', 'esg_value': 0}
        , {'name':'FleetCor Technologies','stock_name':'FLT', 'ricCode':'FLT', 'esg_value': 0}
        , {'name':'FMC','stock_name':'FMC', 'ricCode':'FMC', 'esg_value': 0}
        , {'name':'Ford Motor','stock_name':'F', 'ricCode':'F', 'esg_value': 0}
        , {'name':'Fortinet','stock_name':'FTNT', 'ricCode':'FTNT.O', 'esg_value': 0}
        , {'name':'Fortive','stock_name':'FTV', 'ricCode':'FTV', 'esg_value': 0}
        , {'name':'Fortune Brands Home & Security','stock_name':'FBHS', 'ricCode':'FBHS.K', 'esg_value': 0}
        , {'name':'Fox A','stock_name':'FOXA', 'ricCode':'FOXA.O', 'esg_value': 0}
        , {'name':'Fox B','stock_name':'FOX', 'ricCode':'FOX', 'esg_value': 0}
        , {'name':'Franklin Resources','stock_name':'BEN', 'ricCode':'BEN', 'esg_value': 0}
        , {'name':'Freeport-McMoRan','stock_name':'FCX', 'ricCode':'FCX', 'esg_value': 0}
        , {'name':'Garmin','stock_name':'GRMN', 'ricCode':'GRMN.O', 'esg_value': 0}
        , {'name':'Gartner','stock_name':'IT', 'ricCode':'IT', 'esg_value': 0}
        , {'name':'Generac Holdings','stock_name':'GNRC', 'ricCode':'GNRC.K', 'esg_value': 0}
        , {'name':'General Dynamics','stock_name':'GD', 'ricCode':'GD', 'esg_value': 0}
        , {'name':'General Electric','stock_name':'GE', 'ricCode':'GE', 'esg_value': 0}
        , {'name':'General Mills','stock_name':'GIS', 'ricCode':'GIS', 'esg_value': 0}
        , {'name':'General Motors','stock_name':'GM', 'ricCode':'GM', 'esg_value': 0}
        , {'name':'Genuine Parts','stock_name':'GPC', 'ricCode':'GPC', 'esg_value': 0}
        , {'name':'Gilead Sciences','stock_name':'GILD', 'ricCode':'GILD.O', 'esg_value': 0}
        , {'name':'Global Payments','stock_name':'GPN', 'ricCode':'GPN', 'esg_value': 0}
        , {'name':'Globe Life','stock_name':'GL', 'ricCode':'GL', 'esg_value': 0}
        , {'name':'Goldman Sachs','stock_name':'GS', 'ricCode':'GS', 'esg_value': 0}
        , {'name':'Halliburton','stock_name':'HAL', 'ricCode':'HAL', 'esg_value': 0}
        , {'name':'Hartford Financial Services Group','stock_name':'HIG', 'ricCode':'HIG', 'esg_value': 0}
        , {'name':'Hasbro','stock_name':'HAS', 'ricCode':'HAS.O', 'esg_value': 0}
        , {'name':'HCA Holdings','stock_name':'HCA', 'ricCode':'HCA', 'esg_value': 0}
        , {'name':'Healthpeak Properties','stock_name':'PEAK', 'ricCode':'PEAK.K', 'esg_value': 0}
        , {'name':'Henry Schein','stock_name':'HSIC', 'ricCode':'HSIC.O', 'esg_value': 0}
        , {'name':'Hess','stock_name':'HES', 'ricCode':'HES', 'esg_value': 0}
        , {'name':'Hewlett Packard Enterprise','stock_name':'HPE', 'ricCode':'HPE', 'esg_value': 0}
        , {'name':'Hilton Worldwide Holdings','stock_name':'HLT', 'ricCode':'HLT', 'esg_value': 0}
        , {'name':'Hologic','stock_name':'HOLX', 'ricCode':'HOLX.O', 'esg_value': 0}
        , {'name':'Home Depot','stock_name':'HD', 'ricCode':'HD', 'esg_value': 0}
        , {'name':'Honeywell','stock_name':'HON', 'ricCode':'HON', 'esg_value': 0}
        , {'name':'Hormel Foods','stock_name':'HRL', 'ricCode':'HRL', 'esg_value': 0}
        , {'name':'Host Hotels & Resorts','stock_name':'HST', 'ricCode':'HST.O', 'esg_value': 0}
        , {'name':'Howmet Aerospace','stock_name':'HWM', 'ricCode':'HWM', 'esg_value': 0}
        , {'name':'HP','stock_name':'HPQ', 'ricCode':'HPQ', 'esg_value': 0}
        , {'name':'Humana','stock_name':'HUM', 'ricCode':'HUM', 'esg_value': 0}
        , {'name':'Huntington Bancstocks','stock_name':'HBAN', 'ricCode':'HBAN.O', 'esg_value': 0}
        , {'name':'Huntington Ingalls Industries','stock_name':'HII', 'ricCode':'HII', 'esg_value': 0}
        , {'name':'IBM','stock_name':'IBM', 'ricCode':'IBM', 'esg_value': 0}
        , {'name':'IDEX','stock_name':'IEX', 'ricCode':'IEX', 'esg_value': 0}
        , {'name':'IDEXX Laboratories','stock_name':'IDXX', 'ricCode':'IDXX.O', 'esg_value': 0}
        , {'name':'Illinois Tool Works','stock_name':'ITW', 'ricCode':'ITW', 'esg_value': 0}
        , {'name':'Illumina','stock_name':'ILMN', 'ricCode':'ILMN.O', 'esg_value': 0}
        , {'name':'Incyte','stock_name':'INCY', 'ricCode':'INCY.O', 'esg_value': 0}
        , {'name':'Ingersoll Rand','stock_name':'IR', 'ricCode':'IR', 'esg_value': 0}
        , {'name':'Intel','stock_name':'INTC', 'ricCode':'INTC.O', 'esg_value': 0}
        , {'name':'IntercontinentalExchange Group','stock_name':'ICE', 'ricCode':'ICE', 'esg_value': 0}
        , {'name':'The Hershey','stock_name':'HSY', 'ricCode':'HSY', 'esg_value': 0}
        , {'name':'Harris','stock_name':'LHX', 'ricCode':'LHX', 'esg_value': 0}
        , {'name':'International Flavors & Fragrances','stock_name':'IFF', 'ricCode':'IFF', 'esg_value': 0}
        , {'name':'International Paper','stock_name':'IP', 'ricCode':'IP', 'esg_value': 0}
        , {'name':'Interpublic Group of Cos','stock_name':'IPG', 'ricCode':'IPG', 'esg_value': 0}
        , {'name':'Intuit','stock_name':'INTU', 'ricCode':'INTU.O', 'esg_value': 0}
        , {'name':'Intuitive Surgical','stock_name':'ISRG', 'ricCode':'ISRG.O', 'esg_value': 0}
        , {'name':'Invesco','stock_name':'IVZ', 'ricCode':'IVZ', 'esg_value': 0}
        , {'name':'IQVIA Holdings','stock_name':'IQV', 'ricCode':'IQV', 'esg_value': 0}
        , {'name':'Iron Mountain','stock_name':'IRM', 'ricCode':'IRM', 'esg_value': 0}
        , {'name':'J. M. Smucker','stock_name':'SJM', 'ricCode':'SJM', 'esg_value': 0}
        , {'name':'J.B. Hunt Transportation Services','stock_name':'JBHT', 'ricCode':'JBHT.O', 'esg_value': 0}
        , {'name':'Jack Henry & Associates','stock_name':'JKHY', 'ricCode':'JKHY.O', 'esg_value': 0}
        , {'name':'Jacobs Engineering Group','stock_name':'J', 'ricCode':'J', 'esg_value': 0}
        , {'name':'Johnson & Johnson','stock_name':'JNJ', 'ricCode':'JNJ', 'esg_value': 0}
        , {'name':'Johnson Controls International','stock_name':'JCI', 'ricCode':'JCI', 'esg_value': 0}
        , {'name':'JPMorgan Chase','stock_name':'JPM', 'ricCode':'JPM', 'esg_value': 0}
        , {'name':'Juniper Networks','stock_name':'JNPR', 'ricCode':'JNPR.K', 'esg_value': 0}
        , {'name':'Kellogg','stock_name':'K', 'ricCode':'K', 'esg_value': 0}
        , {'name':'KeyCorp','stock_name':'KEY', 'ricCode':'KEY', 'esg_value': 0}
        , {'name':'Keysight Technologies','stock_name':'KEYS', 'ricCode':'KEYS.K', 'esg_value': 0}
        , {'name':'Kimberly-Clark','stock_name':'KMB', 'ricCode':'KMB', 'esg_value': 0}
        , {'name':'Kimco Realty','stock_name':'KIM', 'ricCode':'KIM', 'esg_value': 0}
        , {'name':'Kinder Morgan','stock_name':'KMI', 'ricCode':'KMI', 'esg_value': 0}
        , {'name':'KLA-Tencor','stock_name':'KLAC', 'ricCode':'KLAC.O', 'esg_value': 0}
        , {'name':'Kroger','stock_name':'KR', 'ricCode':'KR', 'esg_value': 0}
        , {'name':'Laboratory','stock_name':'LH', 'ricCode':'LH', 'esg_value': 0}
        , {'name':'Lam Research','stock_name':'LRCX', 'ricCode':'LRCX.O', 'esg_value': 0}
        , {'name':'Lamb Weston Holdings','stock_name':'LW', 'ricCode':'LW', 'esg_value': 0}
        , {'name':'Las Vegas Sands','stock_name':'LVS', 'ricCode':'LVS', 'esg_value': 0}
        , {'name':'Leidos Holdings','stock_name':'LDOS', 'ricCode':'LDOS.K', 'esg_value': 0}
        , {'name':'Lennar','stock_name':'LEN', 'ricCode':'LEN', 'esg_value': 0}
        , {'name':'Lincoln National','stock_name':'LNC', 'ricCode':'LNC', 'esg_value': 0}
        , {'name':'Linde','stock_name':'LIN', 'ricCode':'LIN', 'esg_value': 0}
        , {'name':'Live Nation Entertainment','stock_name':'LYV', 'ricCode':'LYV', 'esg_value': 0}
        , {'name':'LKQ','stock_name':'LKQ', 'ricCode':'LKQ.O', 'esg_value': 0}
        , {'name':'Lockheed Martin','stock_name':'LMT', 'ricCode':'LMT', 'esg_value': 0}
        , {'name':'Loews','stock_name':'L', 'ricCode':'L', 'esg_value': 0}
        , {'name':'Lowes Companies','stock_name':'LOW', 'ricCode':'LOW', 'esg_value': 0}
        , {'name':'Lumen Technologies','stock_name':'LUMN', 'ricCode':'LUMN.K', 'esg_value': 0}
        , {'name':'Lyondellbasell Industries','stock_name':'LYB', 'ricCode':'LYB', 'esg_value': 0}
        , {'name':'M&T Bank','stock_name':'MTB', 'ricCode':'MTB', 'esg_value': 0}
        , {'name':'Marathon Oil','stock_name':'MRO', 'ricCode':'MRO', 'esg_value': 0}
        , {'name':'Marathon Petroleum Corporation','stock_name':'MPC', 'ricCode':'MPC', 'esg_value': 0}
        , {'name':'MarketAxess Holdings','stock_name':'MKTX', 'ricCode':'MKTX.O', 'esg_value': 0}
        , {'name':'Marriott','stock_name':'MAR', 'ricCode':'MAR.O', 'esg_value': 0}
        , {'name':'Marsh & McLennan Cos','stock_name':'MMC', 'ricCode':'MMC', 'esg_value': 0}
        , {'name':'Martin Marietta Materials','stock_name':'MLM', 'ricCode':'MLM', 'esg_value': 0}
        , {'name':'Masco','stock_name':'MAS', 'ricCode':'MAS', 'esg_value': 0}
        , {'name':'MasterCard','stock_name':'MA', 'ricCode':'MA', 'esg_value': 0}
        , {'name':'McCormick','stock_name':'MKC', 'ricCode':'MKC', 'esg_value': 0}
        , {'name':'McDonalds','stock_name':'MCD', 'ricCode':'MCD', 'esg_value': 0}
        , {'name':'McKesson','stock_name':'MCK', 'ricCode':'MCK', 'esg_value': 0}
        , {'name':'Medtronic','stock_name':'MDT', 'ricCode':'MDT', 'esg_value': 0}
        , {'name':'Merck','stock_name':'MRK', 'ricCode':'MRK', 'esg_value': 0}
        , {'name':'Meta Platforms','stock_name':'META', 'ricCode':'FB.O', 'esg_value': 0}
        , {'name':'MetLife','stock_name':'MET', 'ricCode':'MET', 'esg_value': 0}
        , {'name':'Mettler-Toledo International','stock_name':'MTD', 'ricCode':'MTD', 'esg_value': 0}
        , {'name':'MGM Resorts International','stock_name':'MGM', 'ricCode':'MGM', 'esg_value': 0}
        , {'name':'Microchip Technology','stock_name':'MCHP', 'ricCode':'MCHP.O', 'esg_value': 0}
        , {'name':'Micron Technology','stock_name':'MU', 'ricCode':'MU.O', 'esg_value': 0}
        , {'name':'Microsoft','stock_name':'MSFT', 'ricCode':'MSFT.O', 'esg_value': 0}
        , {'name':'Mid-America Apartment Communities','stock_name':'MAA', 'ricCode':'MAA', 'esg_value': 0}
        , {'name':'Moderna','stock_name':'MRNA', 'ricCode':'MRNA.O', 'esg_value': 0}
        , {'name':'Mohawk Industries','stock_name':'MHK', 'ricCode':'MHK', 'esg_value': 0}
        , {'name':'Molina Healthcare','stock_name':'MOH', 'ricCode':'MOH', 'esg_value': 0}
        , {'name':'Molson Coors Brewing Company','stock_name':'TAP', 'ricCode':'TAP', 'esg_value': 0}
        , {'name':'Mondelez','stock_name':'MDLZ', 'ricCode':'MDLZ.O', 'esg_value': 0}
        , {'name':'Monolithic Power Systems','stock_name':'MPWR', 'ricCode':'MPWR.O', 'esg_value': 0}
        , {'name':'Monster Beverage','stock_name':'MNST', 'ricCode':'MNST.O', 'esg_value': 0}
        , {'name':'Moodys','stock_name':'MCO', 'ricCode':'MCO', 'esg_value': 0}
        , {'name':'Morgan Stanley','stock_name':'MS', 'ricCode':'MS', 'esg_value': 0}
        , {'name':'Motorola Solutions','stock_name':'MSI', 'ricCode':'MSI', 'esg_value': 0}
        , {'name':'MSCI','stock_name':'MSCI', 'ricCode':'MSCI.K', 'esg_value': 0}
        , {'name':'Nasdaq','stock_name':'NDAQ', 'ricCode':'NDAQ.O', 'esg_value': 0}
        , {'name':'NetApp','stock_name':'NTAP', 'ricCode':'NTAP.O', 'esg_value': 0}
        , {'name':'Netflix','stock_name':'NFLX', 'ricCode':'NFLX.O', 'esg_value': 0}
        , {'name':'Newell Brands','stock_name':'NWL', 'ricCode':'NWL.O', 'esg_value': 0}
        , {'name':'Newmont Mining','stock_name':'NEM', 'ricCode':'NEM', 'esg_value': 0}
        , {'name':'News','stock_name':'NWSA', 'ricCode':'NWSA.O', 'esg_value': 0}
        , {'name':'News b','stock_name':'NWS', 'ricCode':'NWS', 'esg_value': 0}
        , {'name':'NextEra Energy','stock_name':'NEE', 'ricCode':'NEE', 'esg_value': 0}
        , {'name':'Nielsen Holdings','stock_name':'NLSN', 'ricCode':'NLSN.K', 'esg_value': 0}
        , {'name':'Nike','stock_name':'NKE', 'ricCode':'NKE', 'esg_value': 0}
        , {'name':'Nisource','stock_name':'NI', 'ricCode':'NI', 'esg_value': 0}
        , {'name':'Norfolk Southern','stock_name':'NSC', 'ricCode':'NSC', 'esg_value': 0}
        , {'name':'Northern Trust','stock_name':'NTRS', 'ricCode':'NTRS.O', 'esg_value': 0}
        , {'name':'Northrop Grumman','stock_name':'NOC', 'ricCode':'NOC', 'esg_value': 0}
        , {'name':'NortonLifeLock','stock_name':'NLOK', 'ricCode':'NLOK.O', 'esg_value': 0}
        , {'name':'Norwegian Cruise Line','stock_name':'NCLH', 'ricCode':'NCLH.K', 'esg_value': 0}
        , {'name':'NRG Energy','stock_name':'NRG', 'ricCode':'NRG', 'esg_value': 0}
        , {'name':'Nucor','stock_name':'NUE', 'ricCode':'NUE', 'esg_value': 0}
        , {'name':'NVIDIA','stock_name':'NVDA', 'ricCode':'NVDA.O', 'esg_value': 0}
        , {'name':'NVR','stock_name':'NVR', 'ricCode':'NVR', 'esg_value': 0}
        , {'name':'NXP Semiconductors','stock_name':'NXPI', 'ricCode':'NXPI.O', 'esg_value': 0}
        , {'name':'O Reilly Automotive','stock_name':'ORLY', 'ricCode':'ORLY.O', 'esg_value': 0}
        , {'name':'Occidental Petroleum','stock_name':'OXY', 'ricCode':'OXY', 'esg_value': 0}
        , {'name':'The Mosaic','stock_name':'MOS', 'ricCode':'MOS', 'esg_value': 0}
        , {'name':'Public Service Enterprise Groups Inc','stock_name':'PEG', 'ricCode':'PEG', 'esg_value': 0}
        , {'name':'Public Storage','stock_name':'PSA', 'ricCode':'PSA', 'esg_value': 0}
        , {'name':'Old Dominion Freight Line','stock_name':'ODFL', 'ricCode':'ODFL.O', 'esg_value': 0}
        , {'name':'Omnicom Group','stock_name':'OMC', 'ricCode':'OMC', 'esg_value': 0}
        , {'name':'ONEOK','stock_name':'OKE', 'ricCode':'OKE', 'esg_value': 0}
        , {'name':'Oracle','stock_name':'ORCL', 'ricCode':'ORCL.K', 'esg_value': 0}
        , {'name':'Organon & Company','stock_name':'OGN', 'ricCode':'OGN', 'esg_value': 0}
        , {'name':'Otis Worldwide Corporation Registered Shs When Issued','stock_name':'OTIS', 'ricCode':'OTIS.K', 'esg_value': 0}
        , {'name':'Paccar','stock_name':'PCAR', 'ricCode':'PCAR.O', 'esg_value': 0}
        , {'name':'Packaging','stock_name':'PKG', 'ricCode':'PKG', 'esg_value': 0}
        , {'name':'Parker Hannifin','stock_name':'PH', 'ricCode':'PH', 'esg_value': 0}
        , {'name':'Paychex','stock_name':'PAYX', 'ricCode':'PAYX.O', 'esg_value': 0}
        , {'name':'Paycom Software','stock_name':'PAYC', 'ricCode':'PAYC.K', 'esg_value': 0}
        , {'name':'PayPal','stock_name':'PYPL', 'ricCode':'PYPL.O', 'esg_value': 0}
        , {'name':'Penn National Gaming','stock_name':'PENN', 'ricCode':'PENN.O', 'esg_value': 0}
        , {'name':'Pentair','stock_name':'PNR', 'ricCode':'PNR', 'esg_value': 0}
        , {'name':'PepsiCo','stock_name':'PEP', 'ricCode':'PEP.O', 'esg_value': 0}
        , {'name':'PerkinElmer','stock_name':'PKI', 'ricCode':'PKI', 'esg_value': 0}
        , {'name':'Pfizer','stock_name':'PFE', 'ricCode':'PFE', 'esg_value': 0}
        , {'name':'Philip Morris','stock_name':'PM', 'ricCode':'PM', 'esg_value': 0}
        , {'name':'Phillips 66','stock_name':'PSX', 'ricCode':'PSX', 'esg_value': 0}
        , {'name':'Pinnacle West Capital','stock_name':'PNW', 'ricCode':'PNW', 'esg_value': 0}
        , {'name':'Pioneer Natural Resources','stock_name':'PXD', 'ricCode':'PXD', 'esg_value': 0}
        , {'name':'PNC Financial Services Group','stock_name':'PNC', 'ricCode':'PNC', 'esg_value': 0}
        , {'name':'Pool','stock_name':'POOL', 'ricCode':'POOL.O', 'esg_value': 0}
        , {'name':'PPG Industries','stock_name':'PPG', 'ricCode':'PPG', 'esg_value': 0}
        , {'name':'PPL','stock_name':'PPL', 'ricCode':'PPL', 'esg_value': 0}
        , {'name':'Principal Financial Group','stock_name':'PFG', 'ricCode':'PFG.O', 'esg_value': 0}
        , {'name':'Procter & Gamble','stock_name':'PG', 'ricCode':'PG', 'esg_value': 0}
        , {'name':'Progressive','stock_name':'PGR', 'ricCode':'PGR', 'esg_value': 0}
        , {'name':'Prologis','stock_name':'PLD', 'ricCode':'PLD', 'esg_value': 0}
        , {'name':'Prudential Financial','stock_name':'PRU', 'ricCode':'PRU', 'esg_value': 0}
        , {'name':'PTC','stock_name':'PTC', 'ricCode':'PTC.O', 'esg_value': 0}
        , {'name':'PulteGroup','stock_name':'PHM', 'ricCode':'PHM', 'esg_value': 0}
        , {'name':'PVH','stock_name':'PVH', 'ricCode':'PVH', 'esg_value': 0}
        , {'name':'Qorvo','stock_name':'QRVO', 'ricCode':'QRVO.O', 'esg_value': 0}
        , {'name':'QUALCOMM','stock_name':'QCOM', 'ricCode':'QCOM.O', 'esg_value': 0}
        , {'name':'Quanta Services','stock_name':'PWR', 'ricCode':'PWR', 'esg_value': 0}
        , {'name':'Quest Diagnostics','stock_name':'DGX', 'ricCode':'DGX', 'esg_value': 0}
        , {'name':'Ralph Lauren a','stock_name':'RL', 'ricCode':'RL', 'esg_value': 0}
        , {'name':'Raymond James Financial','stock_name':'RJF', 'ricCode':'RJF', 'esg_value': 0}
        , {'name':'Raytheon Technologies','stock_name':'RTX', 'ricCode':'RTX', 'esg_value': 0}
        , {'name':'Realty Income','stock_name':'O', 'ricCode':'O', 'esg_value': 0}
        , {'name':'Regency Centers','stock_name':'REG', 'ricCode':'REG.O', 'esg_value': 0}
        , {'name':'Regeneron Pharmaceuticals','stock_name':'REGN', 'ricCode':'REGN.O', 'esg_value': 0}
        , {'name':'Regions Financial','stock_name':'RF', 'ricCode':'RF', 'esg_value': 0}
        , {'name':'Republic Services','stock_name':'RSG', 'ricCode':'RSG', 'esg_value': 0}
        , {'name':'ResMed','stock_name':'RMD', 'ricCode':'RMD', 'esg_value': 0}
        , {'name':'ViacomCBS','stock_name':'PARA', 'ricCode':'VIAC.O', 'esg_value': 0}
        , {'name':'Robert Half','stock_name':'RHI', 'ricCode':'RHI', 'esg_value': 0}
        , {'name':'Rockwell Automation','stock_name':'ROK', 'ricCode':'ROK', 'esg_value': 0}
        , {'name':'Rollins','stock_name':'ROL', 'ricCode':'ROL', 'esg_value': 0}
        , {'name':'Roper Industries','stock_name':'ROP', 'ricCode':'ROP', 'esg_value': 0}
        , {'name':'Ross Stores','stock_name':'ROST', 'ricCode':'ROST.O', 'esg_value': 0}
        , {'name':'Royal Caribbean Cruises','stock_name':'RCL', 'ricCode':'RCL', 'esg_value': 0}
        , {'name':'S&P Global','stock_name':'SPGI', 'ricCode':'SPGI.K', 'esg_value': 0}
        , {'name':'Salesforce','stock_name':'CRM', 'ricCode':'CRM', 'esg_value': 0}
        , {'name':'SBA Communications REIT','stock_name':'SBAC', 'ricCode':'SBAC.O', 'esg_value': 0}
        , {'name':'Schlumberger','stock_name':'SLB', 'ricCode':'SLB', 'esg_value': 0}
        , {'name':'Seagate Technology Holdings','stock_name':'STX', 'ricCode':'STX.O', 'esg_value': 0}
        , {'name':'Sealed Air','stock_name':'SEE', 'ricCode':'SEE', 'esg_value': 0}
        , {'name':'Sempra Energy','stock_name':'SRE', 'ricCode':'SRE', 'esg_value': 0}
        , {'name':'ServiceNow','stock_name':'NOW', 'ricCode':'NOW', 'esg_value': 0}
        , {'name':'Sherwin-Williams','stock_name':'SHW', 'ricCode':'SHW', 'esg_value': 0}
        , {'name':'Simon Property Group','stock_name':'SPG', 'ricCode':'SPG', 'esg_value': 0}
        , {'name':'Skyworks Solutions','stock_name':'SWKS', 'ricCode':'SWKS.O', 'esg_value': 0}
        , {'name':'Snap-On','stock_name':'SNA', 'ricCode':'SNA', 'esg_value': 0}
        , {'name':'Southern','stock_name':'SO', 'ricCode':'SO', 'esg_value': 0}
        , {'name':'Southwest Airlines','stock_name':'LUV', 'ricCode':'LUV', 'esg_value': 0}
        , {'name':'Stanley Black & Decker','stock_name':'SWK', 'ricCode':'SWK', 'esg_value': 0}
        , {'name':'Starbucks','stock_name':'SBUX', 'ricCode':'SBUX.O', 'esg_value': 0}
        , {'name':'State Street','stock_name':'STT', 'ricCode':'STT', 'esg_value': 0}
        , {'name':'STERIS','stock_name':'STE', 'ricCode':'STE', 'esg_value': 0}
        , {'name':'Stryker','stock_name':'SYK', 'ricCode':'SYK', 'esg_value': 0}
        , {'name':'SVB Financial Group Shs','stock_name':'SIVB', 'ricCode':'SIVB.O', 'esg_value': 0}
        , {'name':'Synchrony Financial','stock_name':'SYF', 'ricCode':'SYF', 'esg_value': 0}
        , {'name':'Synopsys','stock_name':'SNPS', 'ricCode':'SNPS.O', 'esg_value': 0}
        , {'name':'Sysco','stock_name':'SYY', 'ricCode':'SYY', 'esg_value': 0}
        , {'name':'T. Rowe Price Group','stock_name':'TROW', 'ricCode':'TROW.O', 'esg_value': 0}
        , {'name':'Take Two','stock_name':'TTWO', 'ricCode':'TTWO.O', 'esg_value': 0}
        , {'name':'Tapestry','stock_name':'TPR', 'ricCode':'TPR', 'esg_value': 0}
        , {'name':'Target','stock_name':'TGT', 'ricCode':'TGT', 'esg_value': 0}
        , {'name':'TE Connectivity','stock_name':'TEL', 'ricCode':'TEL', 'esg_value': 0}
        , {'name':'Teledyne Technologies','stock_name':'TDY', 'ricCode':'TDY', 'esg_value': 0}
        , {'name':'Teleflex','stock_name':'TFX', 'ricCode':'TFX', 'esg_value': 0}
        , {'name':'Teradyne','stock_name':'TER', 'ricCode':'TER.O', 'esg_value': 0}
        , {'name':'Tesla','stock_name':'TSLA', 'ricCode':'TSLA.O', 'esg_value': 0}
        , {'name':'Texas Instruments','stock_name':'TXN', 'ricCode':'TXN.O', 'esg_value': 0}
        , {'name':'Textron','stock_name':'TXT', 'ricCode':'TXT', 'esg_value': 0}
        , {'name':'The Kraft Heinz Company','stock_name':'KHC', 'ricCode':'KHC.O', 'esg_value': 0}
        , {'name':'Thermo Fisher Scientific','stock_name':'TMO', 'ricCode':'TMO', 'esg_value': 0}
        , {'name':'TJX Cos','stock_name':'TJX', 'ricCode':'TJX', 'esg_value': 0}
        , {'name':'T-Mobile US','stock_name':'TMUS', 'ricCode':'TMUS.O', 'esg_value': 0}
        , {'name':'Tractor Supply','stock_name':'TSCO', 'ricCode':'TSCO.O', 'esg_value': 0}
        , {'name':'Trane Technologies','stock_name':'TT', 'ricCode':'TT', 'esg_value': 0}
        , {'name':'TransDigm Group','stock_name':'TDG', 'ricCode':'TDG', 'esg_value': 0}
        , {'name':'Travelers','stock_name':'TRV', 'ricCode':'TRV', 'esg_value': 0}
        , {'name':'Grainger','stock_name':'GWW', 'ricCode':'GWW', 'esg_value': 0}
        , {'name':'Trimble Navigation','stock_name':'TRMB', 'ricCode':'TRMB.O', 'esg_value': 0}
        , {'name':'Truist Financial Corporation','stock_name':'TFC', 'ricCode':'TFC', 'esg_value': 0}
        , {'name':'Twitter','stock_name':'TWTR', 'ricCode':'TWTR.K', 'esg_value': 0}
        , {'name':'Tyler Technologies','stock_name':'TYL', 'ricCode':'TYL', 'esg_value': 0}
        , {'name':'Tyson Foods','stock_name':'TSN', 'ricCode':'TSN', 'esg_value': 0}
        , {'name':'U.S. Bancorp','stock_name':'USB', 'ricCode':'USB', 'esg_value': 0}
        , {'name':'UDR','stock_name':'UDR', 'ricCode':'UDR', 'esg_value': 0}
        , {'name':'Ulta Beauty','stock_name':'ULTA', 'ricCode':'ULTA.O', 'esg_value': 0}
        , {'name':'Union Pacific','stock_name':'UNP', 'ricCode':'UNP', 'esg_value': 0}
        , {'name':'United Airlines Holdings','stock_name':'UAL', 'ricCode':'UAL.O', 'esg_value': 0}
        , {'name':'United Parcel Service','stock_name':'UPS', 'ricCode':'UPS', 'esg_value': 0}
        , {'name':'United Rentals','stock_name':'URI', 'ricCode':'URI', 'esg_value': 0}
        , {'name':'UnitedHealth','stock_name':'UNH', 'ricCode':'UNH', 'esg_value': 0}
        , {'name':'Universal Health Services','stock_name':'UHS', 'ricCode':'UHS', 'esg_value': 0}
        , {'name':'V.F','stock_name':'VFC', 'ricCode':'VFC', 'esg_value': 0}
        , {'name':'Valero Energy','stock_name':'VLO', 'ricCode':'VLO', 'esg_value': 0}
        , {'name':'Ventas','stock_name':'VTR', 'ricCode':'VTR', 'esg_value': 0}
        , {'name':'VeriSign','stock_name':'VRSN', 'ricCode':'VRSN.O', 'esg_value': 0}
        , {'name':'Verisk Analytic a','stock_name':'VRSK', 'ricCode':'VRSK.O', 'esg_value': 0}
        , {'name':'Verizon','stock_name':'VZ', 'ricCode':'VZ', 'esg_value': 0}
        , {'name':'Vertex Pharmaceuticals','stock_name':'VRTX', 'ricCode':'VRTX.O', 'esg_value': 0}
        , {'name':'Viatris','stock_name':'VTRS', 'ricCode':'VTRS.O', 'esg_value': 0}
        , {'name':'Visa','stock_name':'V', 'ricCode':'V', 'esg_value': 0}
        , {'name':'Vornado Realty Trust','stock_name':'VNO', 'ricCode':'VNO', 'esg_value': 0}
        , {'name':'Vulcan Materials','stock_name':'VMC', 'ricCode':'VMC', 'esg_value': 0}
        , {'name':'W. R. Berkley','stock_name':'WRB', 'ricCode':'WRB', 'esg_value': 0}
        , {'name':'Wabtec','stock_name':'WAB', 'ricCode':'WAB', 'esg_value': 0}
        , {'name':'Walgreens Boots Alliance','stock_name':'WBA', 'ricCode':'WBA.O', 'esg_value': 0}
        , {'name':'Walmart','stock_name':'WMT', 'ricCode':'WMT', 'esg_value': 0}
        , {'name':'Walt Disney','stock_name':'DIS', 'ricCode':'DIS', 'esg_value': 0}
        , {'name':'Waste Management','stock_name':'WM', 'ricCode':'WM', 'esg_value': 0}
        , {'name':'Waters','stock_name':'WAT', 'ricCode':'WAT', 'esg_value': 0}
        , {'name':'WEC Energy Group','stock_name':'WEC', 'ricCode':'WEC', 'esg_value': 0}
        , {'name':'Wells Fargo','stock_name':'WFC', 'ricCode':'WFC', 'esg_value': 0}
        , {'name':'Welltower','stock_name':'WELL', 'ricCode':'WELL.K', 'esg_value': 0}
        , {'name':'West Pharmaceutical Services','stock_name':'WST', 'ricCode':'WST', 'esg_value': 0}
        , {'name':'Western Digital','stock_name':'WDC', 'ricCode':'WDC.O', 'esg_value': 0}
        , {'name':'WestRock','stock_name':'WRK', 'ricCode':'WRK', 'esg_value': 0}
        , {'name':'Weyerhaeuser','stock_name':'WY', 'ricCode':'WY', 'esg_value': 0}
        , {'name':'Whirlpool','stock_name':'WHR', 'ricCode':'WHR', 'esg_value': 0}
        , {'name':'Williams Companies','stock_name':'WMB', 'ricCode':'WMB', 'esg_value': 0}
        , {'name':'Willis Towers Watson','stock_name':'WTW', 'ricCode':'WLTW.O', 'esg_value': 0}
        , {'name':'Wynn Resorts','stock_name':'WYNN', 'ricCode':'WYNN.O', 'esg_value': 0}
        , {'name':'Xcel Energy','stock_name':'XEL', 'ricCode':'XEL.O', 'esg_value': 0}
        , {'name':'Xylem','stock_name':'XYL', 'ricCode':'XYL', 'esg_value': 0}
        , {'name':'YUM! Brands','stock_name':'YUM', 'ricCode':'YUM', 'esg_value': 0}
        , {'name':'Zebra Technologies','stock_name':'ZBRA', 'ricCode':'ZBRA.O', 'esg_value': 0}
    ]

    return sp500
