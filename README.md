# Hello World

## Inleiding

Op dit punt heb je als het goed is een beetje een idee welke technologie je in het project gaat gebruiken, heb je de opdrachtgever kort gesproken, en heb je weer een beetje de programmeerspieren opgewarmd. Nu willen we een soortgelijke warming-up doen, maar dan meer richting het project.

Een veel-voorkomend probleem bij vragen is dat studenten aankomen met 'min-of-meer-complexe vragen in zeker-wel-complexe situaties'. Er is dan een redelijk straightforward probleem (bijv. "Waarom doet mijn repository-query het niet?"), maar dat ligt 
dan verstopt onder lagen van Repositories, Adapters, Mapping Code, Plugins, Random-Copy-Pasta-Code-Snippets en meer van dat moois. Dan is de context van het probleem *eigenlijk* veel moeilijker dan het originele probleem zelf, en dat is natuurlijk zonde van iedereens tijd.

Een ander issue is dat in een 'echt project' bepaalde technieken altijd samen voorkomen, waardoor het lastig is om de lijntjes tussen deze LEGO-blokjes te zien. Neem bijv. de Filters, SecurityContext'en en JWT-tokens van BEP1, die krijg je alle drie tegelijk op je bord, en altijd samen. Dan is het handig om ergens een speel-projectje te hebben waarin je ergens ALLEEN een jwt-token maakt (en bijv. naar de System.out print), ergens ALLEEN een filter hebt (om bijv. de requestbodys te loggen?) en probeert om ergens ALLEEN een SecurityContext te zetten (en er dan achter tekomen dat je daar eigenlijk wel een filter voor nodig hebt).

Praktischer bij dit vak: om bepaalde leeruitkomsten te behalen zul je soms 'alternatieve paden' moeten aantonen. Die alternatieve paden in je echte project-code bouwen is waarschijnlijk een stuk tijdrovender dan ze in een versimpelde omgeving maken.

## Budget

In het echt worden dit soort 'speel-repositories' tragisch onderbelicht. In deze eerste week heb je 'de middag van de eerste projectdag' om wat dingetjes uit te proberen. Dat is dus 3-6 uur in de eerste week.

Probeer daarna in de vervolgweken ongeveer 2 uur per week te pakken om hetzij een stukje voor het project eerst in deze zandbak uit te proberen, of juist andersom, een soort minimale versie van een project-feature in deze zandbak na te bouwen.
Vergelijkbaar met de praktijk zou dat dan een (gedeelte van je) onderwijsbudget voorstellen.

In zekere zin geven we je dus de opdracht om niet te hard aan alleen-het-project te werken :).

## Opdracht

Uiteraard is het zeer project-afhankelijk wat je hier precies allemaal moet bouwen. Hoe dan ook zijn er wel een paar algemene zaken die je kan afgaan om te kijken of dat iets is wat hier in hoort.

* Het is het Backend-semester, dus je project heeft ergens een Web-backend. In sommige talen is er '1 gouden standaard' (bijv. Spring in Java heeft een mooie Initializr), maar in bijv. Python of NodeJS zijn er vrij veel concurrerende frameworks en stijlen om zo'n framework op te zetten. Neem dus de rust om er een paar uit te proberen. 
* Zeer waarschijnlijk heb je ergens een database die nodig is. Kies een merkje, en zet er eens één op. Het kan een beetje gedoe zijn om daar bijv. een mooie docker-container van in te checken. Dat is op de iets langere termijn een goed idee, maar in het ergste geval is een kleine markdown textfile waarin je beschrijft wat je hebt gedaan voor nu voldoende.
* Sommige projecten hebben externe API connecties. Dan is het goed om bijv. wat code-snippets in te checken die die externe requests kunnen maken. Let hierbij op dat je geen inlog-gegevens per ongeluk in Git incheckt. Een simpele manier om daarmee om 
te gaan is om iets als een 'credentials.example.json' in te checken, waarin in elk geval het juiste format staat, en de echte 'credentials.json' op je .gitignore lijst te zetten.
* Sommige projecten hebben 'een gek ding' waar je mee moet interacteren (een stuk hardware, een maffe andere applicatie). Het hebben van een simpele commandline applicatie waarmee je -puur- op die verbinding kan focussen kan later veel nut hebben
* Het is welliswaar het Backend-semester, maar een beetje frontend hoort er vast bij. Meestal hangt daar ook weer een grote hoeveelheid framework en/of setup-code aan vast. Experimenteer daar alvast mee.

Voor de beoordelaars is het fijn als de verschillende experimenten in losse directories zitten in deze repository. Per directory kun je dan een kleine README.MD toevoegen waarin je uitlegt wat de relatie is met je project. Dat is iets wat je in het echt niet zou doen (omdat dit soort klad-omgevingen puur voor jezelf zijn), maar in dit geval willen we je helpen, en dat gaat gewoon makkelijker als er even een korte noot over het hoe/wat staat. (dus zeker geen hele werkstukken hier schrijven:P)

Tot slot is het voor je beoordelaars fijn als je ergens in deze README een linkje plaatst naar je -echte- project repository (je weet wel, diegene waar ook non-SDers aan meedoen). Voor jou is het zeker ten aller tijde duidelijk waar je echte project is, maar vanuit het gilde scheelt ons dat een boel zoekwerk.

### Greenfield

Voor een Greenfield project is het aan raden eerst een keer alle onderdeeltjes een keer bij elkaar te Hello Worlden. Je zult zien dat je de eerste keer wat 'stomme foutjes' maakt, en dan is het fijn om daar in het echte project geen last van te hebben.

### Brownfield

Als je een Brownfield project hebt dan staat er al vanalles voor je klaar. Het is dan heel verleidelijk en gevaarlijk om er vanuit te gaan dat er 'belangrijke redenen' achter bepaalde beslissingen zitten.
Sommige stukjes code worden dan 'heilig' terwijl niemand op het team nog weet waar het voor is. Het andere uiterste komt ook voor, dat er zomaar code wordt weggegooid 'omdat het toch allemaal troep is.

In beide gevallen is het dus van belang om 'de geschiedenis' een keer (versimpeld!) na te lopen, zodat je wat meer begrip hebt van de omgeving waarin je verzeild bent geraakt.

## Evaluatie

TODO: Kwaliteitskaart
Zaken waar ik zo aan denk:
* Reductie van echte-projectcode: is het een zinnige versimpeling?
* Reductie van echte-projectcode: zitten alle tech-stukjes er in?
* Reductie van echte-projectcode: zijn alle tech-stukjes goed van elkaar losgekoppeld?