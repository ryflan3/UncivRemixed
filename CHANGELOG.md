# Changelog

## 2.5 — Nine maps and map sprites for improvements

### Maps

Nine new maps, fourteen in all. The README has the full table.

- **Built for particular civs** (Homelands, The Middle Sea, Monsoon Coast): eight starts each, every one in terrain
  shaped for a named civilization and stocked with resources its abilities use. For example the Swiss start in a
  valley of hills ringed by mountains (Alpine Pastures need a Hill next to a Mountain), the Inuit on a snow coast
  with Fish, Whales and Furs, Portugal on a cape with unowned islets for Feitorias, and the Company among Tea,
  Cotton, Sugar and Spices. The starts are stored per nation, so the new game option
  *Select players from starting locations* fills the game with exactly those civs.
- **Built for war** (Iron Passes, Stormwall, The Moatlands): single-tile mountain passes with forts in them,
  cliff coasts with a handful of landing beaches, and river moats crossed only at fords.
- **Unusual country** (Dune Sea, Thousand Lakes, Frostbound): a desert with one great river, a land of lakes,
  and a ring of tundra around a frozen sea that holds the late-game resources.

The forts on Iron Passes and Stormwall are ordinary Fort improvements on unowned land: +50% defence for whoever
stands in them, and they can be pillaged.

### Map sprites

21 tile improvements now have their own sprite on the map in both tilesets, HexaRealm and FantasyHex:
Alpine Pasture, Arctic Research Station, Canal, Caravanserai, Council Mound, Distillery, Dry Dock, Feitoria,
Feitoria Port, Fortress, Hidden Cove, Hillfort, Inuksuk, Isibaya, Kampung, Longphort, Mountain Citadel,
Olive Grove, Onsen, Preceptory and Rice Paddy. Before this they had no sprite of their own.
Shipyard and Resort, which only had HexaRealm sprites, now have FantasyHex ones as well.
The script that draws them is in `ArtSource/TileSprites/`.

## 2.4 — East India Trading Company

**East India Trading Company** (Robert Clive) — *Company Rule*. A firm that conquers but never governs.

- Captured cities always become puppets. The Company cannot annex them, and it cannot buy things in them or
  choose what they build.
- Puppet cities produce +25% Gold, and each captured city pays 100 Gold on the spot (scaled by game speed).
- Plantations yield +1 Gold.
- Drawback: -2 Happiness for every puppet city, on top of the normal unhappiness. Each conquest has to pay for
  itself, and a long run of them will tip the empire into revolt unless Happiness is built up first.
- The Company can still found its own cities with Settlers and runs those normally.
- Sepoy (Musketman; costs 130 instead of 150 and half the Gold upkeep),
  East Indiaman (Frigate; needs no Iron, +1 Sight, 26 ranged Strength instead of 28, costs 170 instead of 185),
  Presidency Fort (Castle; +2 Gold, +1 Happiness).

How it differs from Venice, the other civ that cannot annex: Venice cannot build Settlers but may buy items in its
puppets. The Company can settle but has no say in its puppets at all, and pays Happiness for each one.

The nation is called "East India Trading Company" because the mod already has a national wonder named
"East India Company".

## 2.3 — Swiss Confederacy, Khmer and Portugal

Three civilizations built around how they hold land rather than what they fight with.

**Swiss Confederacy** (Henri Dufour) — *Armed Neutrality*. Small, rich and very hard to invade.

- +15% Gold in all cities while at peace. Military units cost 33% less Gold to buy. Cities have +25% Strength.
- Drawback: military units fight at -25% Strength on foreign land, so the Swiss defend well and conquer badly.
- Reislaufer (Pikeman; +15% Strength next to another Reislaufer, can move on the turn it is bought),
  Private Bank (Bank; +3 Gold and 1 extra Bullion per turn, which speeds up an Economic victory),
  Alpine Pasture (improvement on Hills next to a Mountain; +1 Food, +1 Gold, +1 Food at Fertilizer).

**Khmer** (Suryavarman II) — *Grand Barays*. One enormous capital and very few other cities.

- In the capital: -33% Unhappiness from population, +15% growth and +1 Production per 4 population.
- Drawback: no more Settlers once the Khmer have 4 cities. Conquered cities still count as normal.
- Domrey (Trebuchet; 14 Strength, needs no set-up before firing), Baray (Aqueduct; +2 Food, +1 Faith),
  Prasat (Temple; +1 Faith per 4 population in the city).

**Portugal** (Henry the Navigator) — *Carreira da India*. A trading empire of outposts on land nobody owns.

- Every Feitoria pays +2 Gold to the treasury, +2 more if it has a road or railroad on its tile, and a
  Feitoria Port pays +1 on top. Sea resources yield +1 Gold.
- Drawback: -20% Production towards land military units.
- Nau (Caravel; 5 movement, +2 Sight), Casa da India (Harbor; +3 Gold).

### The Feitoria

- A Worker builds it on land **no one owns**, outside your borders, from Compass. Not on city-state or rival land.
- It takes **16 turns** to build (a Trading post takes about 7), so each one is a real commitment of a Worker.
- Portugal can hold **12** in total: Feitorias and Feitoria Ports are counted together.
- When finished it claims its own tile for the nearest Portuguese city. It claims nothing around it.
- It yields +1 Gold as a tile, gives +25% defence to a unit standing on it and cannot be pillaged.
- From Navigation a coastal Feitoria can be rebuilt as a **Feitoria Port** (10 turns): +2 Gold as a tile,
  +50% defence, and the extra treasury income above.
- A Feitoria belongs to the city that holds its tile. If that city is captured, the post goes with it.

Limits of the current engine, so you know what to expect:

- The post attaches to the nearest city, not to the city that trained the Worker.
- A captured city hands its posts to the conqueror; they are not destroyed. Only Portugal earns the treasury income.
- The cap is checked when a Worker starts building. Several Workers started on the same turn can end one or two over.
- The AI rarely sends Workers outside its borders, so an AI Portugal will build few of them.

### Other changes

- Knights Templar: the cities Lisbon and Venice are renamed Almourol and La Rochelle, since Portugal and Venice
  now have those capitals.

## 2.2 — Indonesia, the Inuit, technology and religion

### New civilizations

**Indonesia** (Gajah Mada) — *Palapa Oath*. Built for many small cities spread across islands.

- Cities on other landmasses than the capital get +2 Gold, +1 Culture and +1 Happiness.
- Land tiles next to a Volcano or Mount Vesuvius yield +1 Faith.
- +25% Production towards Settlers. Drawback: -15% Production in the capital.
- Kris Swordsman (Swordsman; needs no Iron, +15% when attacking, heals 10 on a kill), Jong (Caravel; 22 Strength,
  heals outside friendly territory), Candi (Garden; +2 Faith, needs no fresh water),
  Kampung (improvement on flat coastal land including Beach; +1 Food, +1 Food at Civil Service, +1 Gold at Compass).

**Inuit** (Ekeuhnick) — *People of the Ice*. Lives where nobody else will.

- Snow tiles yield +1 Food and +1 Production; sea resources yield +1 Food.
- Enemy land units pay 1 extra movement point inside Inuit territory.
- Drawback: -25% growth in cities with no Snow or Tundra next to the city.
- Dog Sled (Scout; 3 movement, double movement in Snow and Tundra), Umiak (Trireme; can enter ice),
  Qaggiq (Monument; +1 Happiness), Inuksuk (improvement on Snow and Tundra; +1 Culture, +1 Faith).

### Technology

- Geoengineering now also unlocks the **Reservoir** (river cities: +2 Food, +10% growth).
- Urbanization now also unlocks the **Apartment Block** (+15% growth, -10% unhappiness from population in the city)
  and the Resort, which used to come with Refrigeration.
- New technology **Geothermal Energy** (Atomic era, after Urbanization) unlocks the **Geothermal Plant**:
  +4 Production, +2 Science, +15% Production, for cities with a Volcano or Mount Vesuvius within 3 tiles.

### Religion

- Five new follower beliefs: Fire Temples (Faith and Culture from land next to volcanoes), Sea Shrines (Faith and
  Gold from Beach), Blessing of the Fleet (Production and Faith in coastal cities), Harvest Festivals (Culture from
  Plantations), Mountain Hermitages (Faith for cities next to Mountains).
- New founder belief: Pilgrim Harbor (+3 Gold, +2 Culture in a coastal holy city).
- Atheism is no longer a pantheon. It cut your Faith before you had a religion to found. It is now the founder
  belief **Scholastic Tradition** (+1 Science per Shrine, +2 per Temple) with no penalty.
- **Religious victory**: the Cathedral of World Unity can no longer be built with Production. It costs 2,500 Faith
  (scaled by game speed), is bought in your holy city, and needs an enhanced religion.

### Other changes

- Cities need 4 tiles between them on the same landmass (was 3) and 3 across water (was 2), to go with the
  4-tile work range.
- **The Order of Assassins**: units earn Gold equal to the Strength of each enemy unit they kill, so the civ has an
  identity when espionage is switched off. Their Science penalty now applies only when espionage is enabled.
- The Volcano feature and Mount Vesuvius share a "Volcanic" tag, so one rule covers both.

## 2.1 — Economic victory, wonders, improvements, portraits and maps

### Economic victory

The old version was four gold purchases totalling 100,000 Gold, which a rich player could simply save up for and
which the AI never attempted. It now works like this:

- The four pillars are national wonders **built in the capital**, so the AI can go for them as well.
- Each pillar costs **Bullion**, a new stockpile that cannot be traded, gifted or bought. Every Mint and Bank adds
  1 Bullion per turn and every Stock Exchange adds 2. The four pillars cost 150, 250, 400 and 700 (1,500 in total,
  scaled by game speed).
- Each pillar needs a commercial building in every non-puppet city and a later technology than the one before:
  World's Gold Mines (Markets, Economics), World's Diamond Mines (Banks, Industrialization),
  World Stock Market (Stock Exchanges, Electricity), World Bank (the other three, Globalization).
- To win you must also have **more Gold per turn than every other civilization** when the last pillar is done.
- Every completed pillar is announced to all players.

### Natural wonders

- **Mount Vesuvius**: a lone volcano by the coast. Land next to it yields +1 Food.
- **Giant's Causeway**: basalt columns on a cool coast. Culture and Faith.
- **Ha Long Bay**: two tiles of limestone towers in warm coastal water. Food and Culture.
- **Whitehaven Beach**: turns the flat land around it into Beach. Gold, Culture and Happiness.

### Unique improvements

| Civ | Improvement | Where | Yield |
|---|---|---|---|
| Norseman Vikings | Longphort | flat coastal land, including Beach | +1 Production, +1 Gold, +25% defence; +1 Gold at Compass |
| Red Flag Pirates | Hidden Cove | Beach, also outside your borders | +2 Gold, +1 Production, +25% defence; +1 Gold at Navigation |
| Tokugawa Shogunate | Onsen | next to a Mountain | +1 Culture, +1 Gold, +1 Culture per adjacent Volcano; +1 Gold at Archaeology |
| Zulu | Isibaya | Grassland, Plains | +1 Food, +1 Production; +1 Food at Fertilizer |
| Ancient Israel | Olive Grove | Plains, Grassland, Desert, Hill | +1 Food, +1 Gold; +1 Faith at Theology |
| Scottish Clans | Distillery | next to fresh water | +2 Gold; +1 Culture at Economics |
| Cherokee | Council Mound | Grassland, Plains | +1 Culture, +1 Faith; +1 Culture at Archaeology |
| Knights Templar | Preceptory | Grassland, Plains, Hill, Desert | +1 Gold, +1 Faith; +1 Gold at Banking |

### Art

- Leader portraits for the 14 new civilizations.
- Colour icons for the eight improvements and Bullion, and map tiles for the four wonders (HexaRealm and FantasyHex).
- Gran Colombia's leader is spelled "Simon Bolivar" so his portrait loads on every platform.

### Maps

Four maps in the mod's `maps` folder, picked like any custom map. See the README.

## 2.0 — rebuilt for Unciv 5.0

### Compatibility

- Every JSON file is now strict JSON. The old files relied on the game tolerating missing commas.
- About 60 rules that current Unciv rejects were replaced with their current form or removed: deprecated uniques
  (`Double quantity of [X] produced`, `New [X] units start with [N] Experience`, `Hidden when religion is disabled`,
  `May withdraw before melee`, and others) and invalid filters (`[Faith Building]`, `[Forrest]`,
  `[in all occupied cities]`, `[Military Water]`, `[Luxury]`).
- "Circus Maximus" is now a base-game National Wonder, so Rome's building of that name is renamed **Thermae**.
- Venice and Camel Archer were each defined twice; one definition remains.
- Units left without an owner by removing Japan, Denmark and Sweden are removed (Samurai, Zero, Carolean,
  Hakkapeliitta) or given to the Vikings (Berserker, Norwegian Ski Infantry).
- City-states Jerusalem and Vatican City are removed because they are the capitals of Ancient Israel and the Borgia.
  The Scottish capital is now Scone, since Edinburgh belongs to the Celts.
- Stale copies of base-game objects are gone, so they follow the base game again: Coast, Ocean, Lakes, Fish,
  40 unique units and 14 unique buildings (listed below).
- Policies and technologies copied from the base game get back what the copies had lost: AI weighting,
  leader titles and branch priorities. The three new policy trees have priorities and titles too.
- Ten base-game policies that the mod's reworked trees leave out (Trade Unions, Constitution, Fascism, Communism
  and six more) are now removed properly. Before, they stayed in the ruleset as policies nobody could pick.
- Leaders have the `denounceWillingness` and `denounced` fields the game now uses.
- The mod declares that it needs the Gods & Kings ruleset.

### Map

- **Beach no longer floods the map.** It had two causes. Beach had no climate limits, so the generator used it
  as ordinary ground anywhere on land; and every Coast tile next to Plains was turned into Beach.
  Beach is now excluded from normal generation and only appears where a flat, featureless Grassland, Plains or
  Desert tile touches Coast, with a 35% chance (45% for Desert). Coast tiles are no longer converted.
- Beach yields 1 Food and 1 Gold (was 1 Gold).
- **Volcano** returns as a rare feature on Mountains with new tile art. Land tiles next to one yield +1 Food.
- Coffee no longer lists Hill as a valid terrain while also being barred from Hills. Coffee and Tobacco are
  visible from the start like other luxuries.

### Images

- One atlas (`game`) packed from `Images/`, replacing five hand-edited atlases with wrong sizes and a duplicate
  region. Art that existed only inside those atlases is back in `Images/` as source files.
- New original icons for the 14 new civs and 26 unique units, plus Thermae, Geoengineering and the three new
  policy trees. Icons are 100 px like the base game's.
- Policy and tech icons that were black are white, so the game can tint them.

### Balance

The aim: about four upsides and one drawback that matters per civ, no flat per-city yields above +1,
combat bonuses of 10–15% that need a condition, and unique units within about 10% of the unit they replace.

- Flat yields that scaled with city count are cut back (Sparta +3 Production per city, Tokugawa +3 Culture per
  city, Ottomans +2 Happiness per city, Siam +2 Food +1 Production on every river tile, India +50% yield on
  every Grassland).
- Abilities copied between civs are removed from the copy (Borgia had all of Greece's; Scots had the Inca's
  and Germany's).
- Drawbacks that did nothing are replaced with ones that work (Austria, Carthage, Celts, Egypt, China,
  Ethiopia, Siam).
- Building bonuses that stacked once per city across the whole empire now apply to their own city
  (trade-route gold on Smugglers Cove, Silk Routes, Apadana, Qhapaq Nan, Hanse; Rialto Port; Kraal; Highland Hall;
  Royal Elephant Stable).
- The Red Flag Pirates can build Settlers again, at -33% Production, so an AI pirate civ can grow.
- Venice keeps "cannot build Settlers" and gains the Merchant of Venice's city-state takeover and purchasing in
  puppet cities.
- The tax buildings are a single switch in the capital. Buying one removes the other.

## Civilization abilities

Only changed lines are listed. "removed" lines were either broken in current Unciv, duplicates of another civ, or over budget.

### Tokugawa Shogunate — Isolationism
- removed: `[+15]% Strength <for [All] units> <when fighting in [Friendly Land] tiles>`
- removed: `[+3 Culture] [in all cities]`
- removed: `[+2 Gold, +2 Production, +1 Food] from [Fish] tiles [in all cities]`
- removed: `[-70]% Gold from Great Merchant trade missions`
- added: `[+15]% Strength <for [Military] units> <when fighting in [Friendly Land] tiles>`
- added: `[+1 Culture] [in all cities]`
- added: `[+1 Gold, +1 Production] from [Fish] tiles [in all cities]`
- added: `[-50]% Gold from Great Merchant trade missions`

### Sparta — Spartan Supremacy
- removed: `[+15]% Strength <for [All] units> <when fighting in [Enemy Land] tiles>`
- removed: `[+3 Production] [in all cities]`
- removed: `Upon capturing a city, receive [2] times its [Culture] production as [Culture] immediately`
- removed: `[+50]% City-State Influence degradation`
- added: `[+15]% Strength <for [Land] units> <when fighting in [Enemy Land] tiles>`
- added: `[+15]% Production when constructing [Melee] units [in all cities]`
- added: `[+1 Production] [in all cities]`
- added: `Upon capturing a city, receive [5] times its [Culture] production as [Culture] immediately`
- added: `[-15]% [Gold] [in all cities]`

### House of Borgia — Web of Influence
- removed: `[+75]% [Food] from City-States`
- removed: `[+75]% [Culture] from City-States`
- removed: `[+75]% [Faith] from City-States`
- removed: `Military Units gifted from City-States start with [+15] XP`
- removed: `[-50]% City-State Influence degradation`
- removed: `City-State Influence recovers at twice the normal rate`
- removed: `City-State territory always counts as friendly territory`
- removed: `[+15]% Unhappiness from [Population] [in all cities]`
- added: `[+40]% [Faith] from City-States`
- added: `[+40]% [Culture] from City-States`
- added: `Gifts of Gold to City-States generate [+25]% more Influence`
- added: `Military Units gifted from City-States start with [15] XP`
- added: `Gain [150] [Gold] <upon expending a [Cardinal Protector] unit> <(modified by game speed)>`
- added: `[+10]% Unhappiness from [Population] [in all cities]`

### Rome — The Glory of Rome
- removed: `[+5]% Production when constructing [All] buildings [in all cities]`
- removed: `[-15]% construction time for [All] improvements`
- removed: `[Faith] cost of purchasing items in cities [+75]%`
- removed: `[-3 Faith, -3 Happiness] from every [Holy site]`
- added: `[-25]% construction time for [All] improvements`
- added: `[-25]% maintenance on road & railroads`
- added: `[Faith] cost of purchasing items in cities [+50]%`

### Red Flag Pirate Confederation — Pirates Code
- removed: `[+1] Movement <for [Water] units>`
- removed: `[+10]% Strength <for [Water] units>`
- removed: `Earn [50]% of the damage done to [Water] units as [Gold]`
- removed: `Earn [50]% of killed [Military Water] unit's [Strength] as [Gold]`
- removed: `[-10]% Strength <for [Land] units>`
- removed: `Cannot build [Settler] units`
- added: `[+1] Movement <for [{Military} {Water}] units>`
- added: `[+10]% Strength <for [{Military} {Water}] units>`
- added: `Earn [25]% of the damage done to [Water] units as [Gold]`
- added: `Earn [100]% of killed [{Military} {Water}] unit's [Strength] as [Gold]`
- added: `[-10]% Strength <for [{Military} {Land}] units>`
- added: `[-33]% Production when constructing [Settler] units [in all cities]`

### Norseman Vikings — Viking Fury
- removed: `[+2] Movement <for [Embarked] units>`
- removed: `[0] Movement point cost to disembark <for [All] units>`
- removed: `No movement cost to pillage <for [All] units>`
- removed: `Defense bonus when embarked <for [All] units>`
- removed: `Earn [60]% of the damage done to [City] units as [Gold]`
- removed: `Upon capturing a city, receive [10] times its [Gold] production as [Gold] immediately`
- removed: `[{Military}] units gain the [Amphibious] promotion`
- added: `[+1] Movement <for [Embarked] units>`
- added: `[1] Movement point cost to disembark <for [All] units>`
- added: `No movement cost to pillage <for [Melee] units>`
- added: `Earn [25]% of the damage done to [City] units as [Gold]`
- added: `Upon capturing a city, receive [5] times its [Gold] production as [Gold] immediately`

### Greece — Hellenic League
- removed: `Allied City-States provide [Science] equal to [15]% of what they produce for themselves`
- removed: `Allied City-States provide [Gold] equal to [15]% of what they produce for themselves`
- removed: `Allied City-States provide [Food] equal to [15]% of what they produce for themselves`
- removed: `[+10]% Unhappiness from [Population] [in all occupied cities]`
- added: `Allied City-States provide [Science] equal to [10]% of what they produce for themselves`
- added: `Allied City-States provide [Culture] equal to [10]% of what they produce for themselves`
- added: `[+15]% unhappiness from the number of cities`

### Ancient Israel — Promised Land
- removed: `[+7]% [Food] [in all cities]`

### Scottish Clans — Bagpipes of War
- removed: `[+30]% Strength decreasing with distance from the capital <for [All] units>`
- removed: `Units ignore terrain costs when moving into any tile with Hills`
- removed: `When conquering an encampment, earn [10] Gold and recruit a Barbarian unit`
- removed: `[+25]% construction time for [All] improvements`
- added: `[+20]% Strength decreasing with distance from the capital <for [Military] units>`
- added: `[+10]% [Production] [in all cities] <while the empire is happy>`
- added: `[+5]% [Science] [in all cities] <while the empire is happy>`
- added: `[+33]% construction time for [All] improvements`

### America — Manifest Destiny
- removed: `[+2] Sight <for [{Military} {Land}] units>`
- removed: `[+1] Movement  <for [{Military} {Land}] units>`
- added: `[+1] Sight <for [{Military} {Land}] units>`

### Babylon — Ingenuity
- removed: `[+2 Happiness] from every [Courthouse]`
- removed: `[+2 Gold] from each Trade Route`
- removed: `[-15]% Strength <for [All] units> <when fighting in [Friendly Land] tiles>`
- added: `[+1 Happiness] from every [Courthouse]`
- added: `[-15]% Strength <for [Military] units> <when fighting in [Foreign Land] tiles>`

### The Order of Assassins — Web of Shadows
- removed: `Gain an extra spy <upon entering the [Ancient era]>`
- removed: `[-25]% enemy spy effectiveness [in all cities]`
- removed: `[-99]% enemy spy effectiveness [in capital]`
- removed: `[-15]% [Science] [in all cities]`
- added: `[-33]% enemy spy effectiveness [in all cities]`
- added: `Earn [100]% of killed [Military] unit's [Strength] as [Gold]`
- added: `[-10]% [Science] [in all cities] <when espionage is enabled>`

### Zulu — Warrior Culture
- removed: `[+15]% Strength <when fighting units from a Civilization with more Cities than you>`
- removed: `[+2 Production, +2 Gold, +1 Food] from every [Pasture]`
- removed: `[-5]% Unhappiness from [Population] [in all cities]`
- added: `[-33]% maintenance costs <for [Melee] units>`
- added: `[-20]% XP required for promotions`

### England — Sun Never Sets
- removed: `[+2] Sight <for [Water] units>`
- removed: `[+2] Happiness from each type of luxury resource <on foreign continents>`
- removed: `[+35]% [Gold] from Trade Routes`
- removed: `[+20]% Unhappiness from [Population] [in all cities] <on foreign continents>`
- added: `[+2] Movement <for [{Military} {Water}] units>`
- added: `Gain an extra spy <upon entering the [Renaissance era]>`
- added: `[+15]% [Gold] from Trade Routes`
- added: `[+15]% Unhappiness from [Population] [in all cities] <on foreign continents>`

### Spain — Age of Discovery
- removed: `[+400 Gold] for discovering a Natural Wonder (bonus enhanced to [+500 Gold] if first to discover it)`
- removed: `[+50]% Golden Age length`
- removed: `[+2] Sight <for [All] units>`
- removed: `[+10]% Strength <on foreign continents>`
- added: `[+200 Gold] for discovering a Natural Wonder (bonus enhanced to [+500 Gold] if first to discover it)`
- added: `[+1 Happiness] for every known Natural Wonder`
- added: `[+100]% Yield from every [Natural Wonder]`
- added: `[+10]% Strength <for [Military] units> <on foreign continents>`

### France — Vive la France!
- removed: `[+25]% [Culture] from City-States`
- removed: `[+1 Culture] from every [Wine]`
- removed: `[+3 Gold] from every [Luxury resource]`
- removed: `[+50]% Unhappiness from [Population] [in capital] <when at war>`
- added: `[+2 Culture] from every [Wine]`
- added: `[+1 Gold] from every [Luxury resource]`
- added: `[+10]% Unhappiness from [Population] [in all cities] <when at war>`

### The Netherlands — Gilded Prosperity
- removed: `[+50]% [Gold] from Trade Routes`
- removed: `[+2 Food] from each Trade Route`
- removed: `[+50]% [Gold] <during a Golden Age>`
- removed: `[+15]% [Science] <during a Golden Age>`
- removed: `[-2 Happiness] [in capital] <after founding a Pantheon>`
- removed: `[-5 Happiness] [in capital] <after founding a religion>`
- added: `[+25]% [Gold] from Trade Routes`
- added: `[+1 Food] from each Trade Route`
- added: `[+20]% [Gold] [in all cities] <during a Golden Age>`
- added: `[+50]% Gold cost of acquiring tiles [in all cities]`
- added: `[+25]% Culture cost of natural border growth [in all cities]`

### Iroquois — The Great Warpath
- removed: `[+1 Happiness] per [3] social policies adopted <in [in all cities] cities>`
- removed: `[+1 Gold, +2 Production, +1 Culture] in cities on [Forrest] tiles`
- removed: `Science gained from research agreements [-80]%`
- added: `[+1 Happiness] per [4] social policies adopted`
- added: `[+1 Gold] from [Forest] tiles [in all cities]`

### Egypt — Monument Builders
- removed: `[+2 Production] from every specialist [in all cities]`
- removed: `[+1 Gold, +2 Food] from every [Flood Plain, River]`
- removed: `[+2 Faith, +2 Culture] from all [Faith] buildings`
- removed: `[-20]% Strength for cities <in [non capital] cities>`
- added: `[+1 Food] from [Flood plains] tiles [in all cities]`
- added: `[+1 Culture] from all [Faith] buildings`
- added: `[-20]% Strength for cities <in [non-[Capital]] cities>`

### Persia — Achaemenid Legacy
- removed: `Empire enters golden age <upon conquering a city>`
- removed: `[-15]% Unhappiness from [Population] [in all occupied cities]`
- removed: `[-20]% maintenance on road & railroads`
- removed: `[-15]% [Culture] <in [in all cities] cities>`
- added: `[+50]% Golden Age length`
- added: `[-15]% [Culture] [in all cities]`

### Mongolia — Mongol Terror
- removed: `[+35]% Strength <vs [City-States]>`
- removed: `[+2] Movement <for [Mounted] units>`
- removed: `New [Mounted] units start with [10] Experience [in all cities]`
- removed: `When defeating a [Mounted] unit, earn [5] Gold and recruit it <with [50]% chance>`
- removed: `Double quantity of [Horses] produced`
- added: `[+30]% Strength <vs [City-States]>`
- added: `[+1] Movement <for [Mounted] units>`
- added: `New [Mounted] units start with [10] XP [in all cities]`
- added: `[+100]% [Horses] resource production`

### The Huns — Scourge of God
- removed: `[+2 Production, +1 Food] from every [Pasture]`
- removed: `Cities are razed [3] times as fast`
- removed: `Receive triple Gold from Barbarian encampments and pillaging Cities`
- removed: `When conquering an encampment, earn [30] Gold and recruit a Barbarian unit`
- removed: `Notified of new Barbarian encampments`
- removed: `When defeating a [Barbarian] unit, earn [5] Gold and recruit it`
- added: `[+1 Production] from every [Pasture]`
- added: `Cities are razed [2] times as fast`
- added: `Receive [+100]% Gold from Barbarian encampments and pillaging Cities`
- added: `When defeating a [Barbarian] unit, earn [5] Gold and recruit it <with [33]% chance>`

### Gran Colombia — Ejército Patriota
- removed: `All healing effects doubled <for [Military] units>`
- removed: `[+2 Gold, +2 Food] from [Plantation] tiles [in all cities]`
- removed: `Rebel units may spawn <when at war>`
- added: `[+5] HP when healing <for [Military] units>`
- added: `[+1 Gold, +1 Food] from [Plantation] tiles [in all cities]`
- added: `Rebel units may spawn <when below [-5] [Happiness]>`

### Cherokee — Council of Peace
- removed: `[+1 Faith, +1 Food] from [Forest] tiles [in all cities]`
- removed: `[+2 Happiness, +2 Production, +1 Food] from each Trade Route`
- removed: `When declaring friendship, both parties gain a [+3]% boost to great person generation`
- added: `[+1 Food] from [Forest] tiles [in all cities]`
- added: `[+1 Production, +1 Food] from each Trade Route`
- added: `When declaring friendship, both parties gain a [+10]% boost to great person generation`

### Austria — Habsburg Diplomacy
- removed: `Can spend Gold to annex or puppet a City-State that has been your ally for [5] turns.`
- removed: `[+20]% Happiness from luxury resources gifted by City-States`
- removed: `Gain [15] Influence with a [Melee] gift to a City-State`
- removed: `[+2 Production] [in all cities] <starting from the [Industrial era]>`
- removed: `[-50]% Golden Age length`
- removed: `[+10]% Unhappiness from [Population] [in all cities] <when at war> <for [25] turns>`
- added: `Can spend Gold to annex or puppet a City-State that has been your Ally for [5] turns`
- added: `[+25]% Happiness from luxury resources gifted by City-States`
- added: `[-10]% Strength <for [Military] units> <when fighting in [Foreign Land] tiles>`

### Knights Templar — Holy Crusade
- removed: `[+15]% Strength <for [All] units> <when above [250] [Faith]>`
- removed: `[+10]% Strength <for [All] units> <during the [Medieval era]>`
- removed: `[+10]% of excess happiness converted to [Faith]`
- removed: `[-15]% Strength <for [All] units> <when below [50] [Faith]>`
- added: `[+10]% Strength <for [Military] units> <when above [200] [Faith]>`
- added: `May buy [Templar Knight] units with [Faith] for [2] times their normal Production cost`
- added: `[+15]% of excess happiness converted to [Faith]`
- added: `[-10]% Strength <for [Military] units> <when below [30] [Faith]>`

### Safavid Dynasty — Silk and Steel
- removed: `[+3 Gold, +1 Happiness, +2 Culture] from all [World] buildings`
- removed: `[+3 Gold, +1 Happiness, +2 Culture] from all [National] buildings`
- removed: `[+10]% Production when constructing [World] buildings [in all cities]`
- removed: `[+10]% Production when constructing [National] buildings [in all cities]`
- removed: `[+15]% Strength <for [Gunpowder] units>`
- removed: `[+1 Gold, +2 Faith] <in cities following our religion>`
- removed: `[-40]% [Production] <when number of [Happiness] is less than [1]>`
- added: `[+2 Gold, +1 Culture] from all [National Wonder] buildings`
- added: `[+10]% Production when constructing [All] wonders [in capital]`
- added: `[+10]% Strength <for [Gunpowder] units>`
- added: `[+1 Gold, +1 Faith] [in cities following our religion]`
- added: `[-25]% [Production] [in all cities] <when below [0] [Happiness]>`

### Venice — Ducats of Power
- removed: `[+100]% [Gold] [in capital]`
- removed: `[+40]% of excess happiness converted to [Gold]`
- removed: `Gifts of Gold to City-States generate [+35]% more Influence`
- removed: `Free [Merchant of Venice] appears <after discovering [Optics]>`
- removed: `[-15]% Production when constructing [Land] units [in all cities]`
- added: `[+50]% [Gold] [in capital]`
- added: `[+25]% of excess happiness converted to [Gold]`
- added: `Gifts of Gold to City-States generate [+25]% more Influence`
- added: `Free [Merchant of Venice] appears <upon discovering [Optics] technology>`
- added: `May buy items in puppet cities`
- added: `May not annex cities`

### The Maya — The Long Count
- removed: `Free Social Policy <every [100] turns> <(modified by game speed)>`
- removed: `Free Technology <every [110] turns> <(modified by game speed)>`
- removed: `[+1 Food] from [Farm] tiles [in all cities]`
- removed: `[-1 Food, -1 Production] from [Lumber mill] tiles [in all cities]`
- added: `[+1 Production] from [Jungle] tiles [in all cities]`
- added: `[-15]% Strength <for [Military] units> <when fighting in [Open terrain] tiles>`

### Aztecs — Sacrificial Captives
- removed: `[+20]% [Gold] [in annexed cities]`
- removed: `[+15]% [Science] [in annexed cities]`
- removed: `[+60]% maintenance costs <when not at war>`
- added: `[+10]% [Gold] [in annexed cities]`
- added: `[+10]% [Science] [in annexed cities]`
- added: `[+33]% maintenance costs <for [Military] units> <when not at war>`

### Byzantium — Heaven's Favor
- removed: `[+50]% [Faith] from every [Faith Building]`
- removed: `[+2 Gold, +1 Culture] from every [Faith Building]`
- removed: `[-15]% [Production] [in all cities] <when at war>`
- added: `[+1 Gold, +1 Culture] from every [Temple]`
- added: `[+1 Faith] from every [Shrine]`
- added: `[-10]% [Production] [in all cities] <when at war>`

### Carthage — Phoenician Heritage
- removed: `[+15]% [Gold] <in [Coastal] cities>`
- removed: `[+15]% [Culture] <in [Coastal] cities>`
- removed: `[-20]% [Happiness] <in [non-[Coastal]] cities>`
- added: `Comment [Units ending their turn on [Mountain] tiles take [50] damage]`
- added: `[+10]% [Gold] [in all coastal cities]`
- added: `[-15]% [Production] [in all cities] <in [non-[Coastal]] cities>`

### Germany — Furor Teutonicus
- removed: `[-30]% maintenance costs <for [Land] units>`
- removed: `[+15]% [Production] <in cities with a [Factory]>`
- removed: `[+10]% [Gold] <in cities with a [Bank]>`
- removed: `Upon capturing a city, receive [10] times its [Culture] production as [Gold] immediately`
- removed: `[-25]% [Gold] <in [Puppeted] cities>`
- removed: `[-25]% [Culture] <in [Puppeted] cities>`
- removed: `[-25]% [Production] <in [Puppeted] cities>`
- added: `When conquering an encampment, earn [25] Gold and recruit a Barbarian unit <with [67]% chance>`
- added: `[-25]% maintenance costs <for [Land] units>`
- added: `[+10]% [Production] [in all cities] <in cities with a [Factory]>`
- added: `[-20]% [Faith] [in all cities]`

### Russia — Siberian Riches
- removed: `Double quantity of [Horses] produced`
- removed: `Double quantity of [Iron] produced`
- removed: `Double quantity of [Uranium] produced`
- removed: `[+15]% Strength <when fighting in [Snow] tiles>`
- removed: `[+15]% Strength <when fighting in [Tundra] tiles>`
- removed: `[+1 Food, +1 Production] from [Snow] tiles [in all cities]`
- removed: `[+1 Food, +1 Production] from [Tundra] tiles [in all cities]`
- removed: `[-15]% [Happiness] <in cities with at least [15] [Population]>`
- removed: `[-15]% [Production] <in cities with at least [15] [Population]>`
- added: `[+100]% [Horses] resource production`
- added: `[+100]% [Iron] resource production`
- added: `[+100]% [Uranium] resource production`
- added: `[+1 Food] from [Tundra] tiles [in all cities]`
- added: `[+15]% Strength <for [Military] units> <when fighting in [Tundra] tiles>`
- added: `[+15]% Strength <for [Military] units> <when fighting in [Snow] tiles>`
- added: `[+15]% Unhappiness from [Population] [in all cities] <in cities with at least [15] [Population]>`

### Korea — Scholars of the Jade Hall
- removed: `Science gained from research agreements [+20]%`
- removed: `[+15]% [Production] <in [Coastal] cities>`
- removed: `[-15]% Strength <in [Plains] tiles>`
- added: `[+25]% City-State Influence degradation`

### Celts — Druidic Lore
- removed: `Gain a free [Pantheon] belief <upon founding a Pantheon>`
- removed: `[+1 Faith, +1 Culture] from every [Quarry]`
- removed: `[+15]% Strength <when below [100] HP>`
- removed: `[-15]% [Happiness] <in [non-[Garrisoned]] cities>`
- added: `[+1 Culture] from every [Quarry]`
- added: `[+10]% Strength <for [Melee] units> <when fighting in [Forest] tiles>`
- added: `[-15]% Production when constructing [All] wonders [in all cities]`

### Arabia — Trade Caravans
- removed: `[+2 Gold] from each Trade Route`
- removed: `Double quantity of [Oil] produced`
- removed: `[+25]% [Gold] <during a Golden Age>`
- removed: `[+1 Gold, +1 Culture, +1 Faith] from every [Faith Building]`
- removed: `[+50]% City-State Influence degradation`
- added: `[+1 Gold] from each Trade Route`
- added: `[+100]% [Oil] resource production`
- added: `[+15]% [Gold] [in all cities] <during a Golden Age>`
- added: `[+1 Culture] from every [Temple]`
- added: `[-15]% Strength <for [Water] units>`

### India — Infinite Abundance
- removed: `[+50]% Yield from every [Grassland]`
- removed: `[+20]% [Food] <in [Coastal] cities>`
- removed: `[-25]% construction time for [All] improvements`
- removed: `[-25]% [Gold] <in [non-[in all cities connected to capital]] cities>`
- removed: `[-25]% [Culture] <in [non-[in all cities connected to capital]] cities>`
- added: `[+10]% growth [in all cities]`

### Polynesia — Wayfinding
- removed: `[+2] Sight <for [Embarked] units>`
- removed: `[+20]% Strength <within [2] tiles of a [Moai]>`
- removed: `[+15]% Strength <in [Beach] tiles>`
- removed: `[+75]% Yield from every [Beach]`
- removed: `[-25]% [Gold] <in cities without a [Harbor]>`
- added: `[+1] Sight <for [Embarked] units>`
- added: `[+10]% Strength <within [2] tiles of a [Moai]>`
- added: `[+1 Food, +1 Culture] from [Beach] tiles [in all cities]`
- added: `[-20]% [Gold] [in all cities] <in cities without a [Harbor]>`

### China — Mandate of Heaven
- removed: `[+1 Culture] from every [Science Building]`
- removed: `[+15]% Strength <for [Ranged] units>`
- removed: `[-25]% maintenance cost for buildings [in all cities]`
- removed: `[-25]% Yield from every [non-[Resource]]`
- added: `[Great Admiral] is earned [50]% faster`
- added: `[+1 Culture] from every [Library]`
- added: `[-15]% maintenance cost for [All] buildings [in all cities]`
- added: `[+20]% Culture cost of adopting new Policies`

### Ethiopia — Legacy of the Lion
- removed: `[+15]% Strength <when fighting units from a Civilization with more Cities than you>`
- removed: `[+1 Faith] from every [Palace]`
- removed: `[+1 Food, +1 Production] from [{Hill} {Farm}] tiles [in all cities]`
- removed: `[+1 Food, +1 Gold] from [Plantation] tiles [in all cities]`
- removed: `[+1 Culture] [in all cities] <when at war>`
- removed: `[+100]% maintenance costs <in cities with a [Courthouse]>`
- added: `[+20]% Strength <when fighting units from a Civilization with more Cities than you>`
- added: `[+2 Faith] [in capital]`
- added: `[+1 Food] from [Plantation] tiles [in all cities]`
- added: `[+50]% maintenance on road & railroads`

### Siam — Jewel of the East
- removed: `[+2 Food, +1 Production] from [River] tiles [in all cities]`
- removed: `[+15]% Strength <for [Mounted] units>`
- removed: `[+2 Culture, +1 Happiness] from every [Wonder]`
- removed: `Allied City-States will occasionally gift Great People`
- removed: `[-10]% [Science] [non-[Capital]]`
- removed: `[-10]% [Production] [non-[Capital]]`
- added: `[+50]% [Food] from City-States`
- added: `[+50]% [Culture] from City-States`
- added: `[+50]% [Faith] from City-States`
- added: `Military Units gifted from City-States start with [10] XP`
- added: `[-10]% [Production] [in all cities] <in [non-[Capital]] cities>`

### Songhai — Citadel of Gold
- removed: `Receive triple Gold from Barbarian encampments and pillaging Cities`
- removed: `Defense bonus when embarked <for [All] units>`
- removed: `[+1 Culture, +1 Science] from every [Science Building]`
- removed: `[+100]% Yield from every [Gold Ore]`
- removed: `[+25]% Yield from every [Mine]`
- removed: `[-2] Happiness from each type of luxury resource`
- added: `Receive [+200]% Gold from Barbarian encampments and pillaging Cities`
- added: `[+100]% Strength <when defending> <for [Embarked] units>`
- added: `[+2 Gold] from every [Gold Ore]`
- added: `[-1] Happiness from each type of luxury resource`

### Inca — Children of the Sun
- removed: `[+15]% [Production] [in all cities connected to capital]`
- removed: `[+10]% [Food] [in capital]`
- removed: `[+100]% Yield from every [Quarry]`
- removed: `[-15]% [Science] [in all cities] <before discovering [Scientific Theory]>`
- added: `[+10]% [Production] [in all cities connected to capital]`
- added: `[-10]% [Science] [in all cities] <before discovering [Scientific Theory]>`

### The Ottomans — Empire of Sail and Song
- removed: `[+2 Happiness] [in all cities]`
- removed: `[+10]% [Science] <during a Golden Age>`
- removed: `[+10]% [Culture] <during a Golden Age>`
- removed: `[+50]% maintenance costs <for [Military] units>`
- added: `[+15]% Production when constructing [Gunpowder] units [in all cities]`
- added: `[-33]% Gold cost of upgrading <for [Military] units>`
- added: `[+25]% maintenance costs <for [Land] units>`

## Unique units

- **Daimyo** (Tokugawa Shogunate)
  - strength 24 → 22; cost 100 → 120; upgradesTo Rifleman → Musketman; obsoleteTech Rifling → Gunpowder
  - removed: `Can move after attacking`
  - removed: `promotion: Great Generals II`
  - added: `promotion: Great Generals I`
- **Spartan Hoplite** (Sparta)
  - strength 15 → 13; upgradesTo Lancer → Pikeman; obsoleteTech Metallurgy → Civil Service
  - removed: `[+20]% to Flank Attack bonuses`
  - added: `[+15]% Strength <when adjacent to a [Melee] unit>`
- **Papal Guard** (House of Borgia)
  - strength 18 → 16; cost 45 → 90
  - removed: `Can move immediately once bought`
  - added: `Can be purchased with [Faith] [in all cities]`
- **Cardinal Protector** (House of Borgia)
  - religiousStrength 1500 → 1250
  - removed: `Can Spread Religion <for [3] movement> <[5] times> <after which this unit is consumed>`
  - removed: `Hidden when religion is disabled`
  - removed: `Gain [300] [Gold] <upon expending a [Cardinal Protector] unit>`
  - added: `Can Spread Religion <for [2] movement> <[5] times> <after which this unit is consumed>`
  - added: `Is part of Great Person group [Prophet]`
  - added: `[This Unit] gets a name from the [Prophet] group`
  - added: `[-1] Sight`
  - added: `Only available <when religion is enabled>`
- **Junk Ship** (Red Flag Pirate Confederation)
  - strength 30 → 25; rangedStrength 35 → 28; cost 185 → 170
  - removed: `[+1] Sight`
  - removed: `Can move after attacking`
  - added: `promotion: Coastal Raider I`
- **Berserker** (Norseman Vikings)
  - strength 22 → 21
  - removed: `[+25]% Strength <vs [Wounded] units>`
  - removed: `[+10]% Strength <when fighting in [Snow] tiles>`
  - removed: `[+10]% Strength <when fighting in [Tundra] tiles>`
  - removed: `[+10]% Strength <when fighting in [Hill] tiles>`
  - removed: `promotion: Blitz`
- **Longship** (Norseman Vikings)
  - strength 19 → 11; movement 4 → 5; cost 100 → 45; replaces Galleass → Trireme; requiredTech Compass → Sailing; upgradesTo Frigate → Caravel; obsoleteTech Navigation → Astronomy
  - removed: `Can move after attacking`
  - removed: `May withdraw before melee ([80]%)`
  - removed: `[+50]% Strength <vs cities> <when attacking>`
  - added: `[+25]% Strength <vs cities> <when attacking>`
  - added: `Never appears as a Barbarian unit`
- **Maccabee** (Ancient Israel)
  - strength 12 → 9; obsoleteTech Iron Working → Metal Casting; requiredTech – → Agriculture
  - removed: `Invisible to non-adjacent units`
  - removed: `May upgrade to [Longswordsman] through ruins-like effects`
  - added: `May upgrade to [Spearman] through ruins-like effects`
  - added: `[+20]% Strength <when fighting in [Friendly Land] tiles>`
- **Highland Warrior** (Scottish Clans)
  - strength 16 → 14
  - removed: `[+15]% Strength <when fighting in [Rough terrain] tiles>`
  - added: `[+20]% Strength <when fighting in [Rough terrain] tiles>`
- **Clan Chieftain** (Scottish Clans) — renamed from "Clan Chieftan"
  - removed: `Empire enters a [8]-turn Golden Age <by consuming this unit>`
  - removed: `[+15]% Strength bonus for [Military] units within [2] tiles`
  - removed: `[+15]% Strength bonus for [Military] units within [2] tiles <when fighting in [Rough terrain] tiles>`
  - removed: `Can be earned through combat`
  - added: `[+15]% Strength bonus for [{Military} {Land}] units within [2] tiles`
  - added: `Can be earned through combat <for [Land] units>`
  - added: `Is part of Great Person group [General]`
  - added: `[This Unit] gets a name from the [General] group`
  - added: `All adjacent units heal [+10] HP when healing`
- **Babylonian Bowman** (Babylon)
  - strength 8 → 9
  - removed: `[1] additional attacks per turn`
  - added: `[+25]% Strength <when defending>`
- **Assassin** (The Order of Assassins)
  - strength 21 → 18
  - removed: `[+150]% Strength <when attacking>`
  - removed: `[-50]% Strength <when defending>`
  - added: `[+50]% Strength <when attacking>`
  - added: `[-25]% Strength <when defending>`
- **Impi** (Zulu)
  - strength 18 → 16
  - removed: `[1] additional attacks per turn`
  - removed: `May withdraw before melee ([25]%)`
  - added: `Before engaging in combat performs an extra ranged attack with [50]% of melee combat strength`
- **Spanish Inquisitor** (Spain)
  - movement 4 → 3
  - removed: `Can remove other religions from cities <[3] times> <after which this unit is consumed>`
  - removed: `Hidden when religion is disabled`
  - removed: `May enter foreign tiles without open borders`
  - added: `Can remove other religions from cities <in [Friendly] tiles> <[2] times> <after which this unit is consumed>`
  - added: `Only available <when religion is enabled>`
- **Great Admiral** (all civs)
  - movement 6 → 4
  - removed: `[+15]% Strength bonus for [{Military} {Water}] units within [3] tiles`
  - removed: `Great Person - [Navy]`
  - added: `May Paradrop to [{your} {Coastal} {City center}] tiles up to [25] tiles away <in [City center] tiles>`
  - added: `[+15]% Strength bonus for [{Military} {Water}] units within [2] tiles`
  - added: `Is part of Great Person group [Admiral]`
  - added: `[This Unit] gets a name from the [Admiral] group`
  - added: `Great Person - [War]`
- **Onondaga Scout** (Iroquois)
  - strength 8 → 6; movement 3 → 2; requiredTech – → Agriculture
  - removed: `May upgrade to [Composite Bowman] through ruins-like effects`
  - removed: `[+2] Sight`
  - added: `May upgrade to [Archer] through ruins-like effects`
  - added: `[+1] Sight`
- **Llanero** (Gran Colombia)
  - strength 37 → 34; cost 200 → 225
  - added: `No defensive terrain bonus`
  - added: `[-33]% Strength <vs cities> <when attacking>`
  - added: `[+10]% Strength <when adjacent to a [Llanero] unit>`
- **Templar Knight** (Knights Templar)
  - strength 23 → 21; movement 5 → 4
  - removed: `[+15]% Strength <vs cities> <when attacking>`
  - added: `[-33]% Strength <vs cities> <when attacking>`
  - added: `Earn [50]% of killed [Military] unit's [Strength] as [Faith]`
- **Templar Crossbowman** (Knights Templar)
  - strength 15 → 14; rangedStrength 19 → 18
  - removed: `Earn [10]% of the damage done to [City] units as [Faith]`
  - added: `Earn [25]% of the damage done to [City] units as [Faith]`
- **Zamburak** (Safavid Dynasty)
  - strength 17 → 15; rangedStrength 21 → 19; movement 5 → 4
  - removed: `[+15]% Strength <vs [Melee]>`
  - added: `Never appears as a Barbarian unit`
- **Qizilbash** (Safavid Dynasty)
  - strength 37 → 34; movement 5 → 4
  - removed: `[+15]% Strength <vs [Mounted]>`
  - added: `No defensive terrain bonus`
  - added: `[-33]% Strength <vs cities> <when attacking>`
  - added: `Never appears as a Barbarian unit`
  - added: `[+1] Sight`
  - added: `promotion: Formation I`
- **Great Galleass** (Venice)
  - strength 19 → 18; rangedStrength 22 → 20; movement 4 → 3
  - removed: `[-2] Movement <in [Ocean] tiles>`
  - removed: `Double movement in [Coast]`
  - removed: `Can move immediately once bought`
  - added: `Cannot enter ocean tiles`
- **Merchant of Venice** (Venice)
  - removed: `Can undertake a trade mission with City-State, giving a large sum of gold and [90] Influence`
  - removed: `Double movement in [Coast]`
  - added: `Can undertake a trade mission with City-State, giving a large sum of gold and [60] Influence`
  - added: `Is part of Great Person group [Great Person]`
  - added: `[This Unit] gets a name from the [Merchant] group`
  - added: `[This Unit] takes over the City-State owning the tile it's standing on <by consuming this unit>`
- **Russian Winter Guard** (Russia)
  - strength 52 → 50
  - removed: `[+20]% Strength <in [Friendly Land] tiles>`
  - added: `[+20]% Strength <when fighting in [Friendly Land] tiles>`
- **Gurkha Soldier** (India)
  - strength 27 → 24
  - removed: `[+15]% Strength <in [Hill] tiles>`
  - added: `[+25]% Strength <when fighting in [Hill] tiles>`
- **Waka War Canoe** (Polynesia)
  - strength 14 → 10; cost 30 → 40
  - removed: `Double movement in [Coast]`
- **Oromo Cavalry** (Ethiopia)
  - strength 31 → 32; movement 6 → 5
  - removed: `[1] additional attacks per turn`
  - added: `[-33]% Strength <vs cities> <when attacking>`
  - added: `Ignores Zone of Control`
- **Norwegian Ski Infantry** (Norseman Vikings) — newly assigned: the base game unit, re-homed from a removed civ
- **Kris Swordsman** (Indonesia) — new unit, replaces Swordsman
- **Jong** (Indonesia) — new unit, replaces Caravel
- **Dog Sled** (Inuit) — new unit, replaces Scout
- **Umiak** (Inuit) — new unit, replaces Trireme
- **Reislaufer** (Swiss Confederacy) — new unit, replaces Pikeman
- **Domrey** (Khmer) — new unit, replaces Trebuchet
- **Nau** (Portugal) — new unit, replaces Caravel
- **Sepoy** (East India Trading Company) — new unit, replaces Musketman
- **East Indiaman** (East India Trading Company) — new unit, replaces Frigate

The mod no longer ships its own copies of these base-game units, so they use the current Unciv definition again (the old copies were stale and mostly +2 Strength over the base game):

African Forest Elephant, Atlatlist, Ballista, Battering Ram, Camel Archer, Cataphract, Chu-Ko-Nu, Companion Cavalry, Conquistador, Cossack, Dromon, Foreign Legion, Hoplite, Horse Archer, Hussar, Hwach'a, Jaguar, Janissary, Keshik, Khan, Landsknecht, Legion, Longbowman, Mandekalu Cavalry, Maori Warrior, Mehal Sefari, Mohawk Warrior, Musketeer, Naresuan's Elephant, Panzer, Persian Immortal, Pictish Warrior, Quinquereme, Sea Beggar, Ship of the Line, Sipahi, Slinger, Turtle Ship, War Chariot, War Elephant.

## Unique buildings and wonders

- **Dojo** (Tokugawa Shogunate)
  - cost 150 → –; culture 2 → 1; happiness 2 → –; requiredBuilding – → Barracks
  - removed: `New [Military] units start with [15] Experience [in this city]`
  - added: `New [Military] units start with [15] XP [in this city]`
- **Geisha House** (Tokugawa Shogunate)
  - cost 90 → –; culture 4 → 3; happiness 3 → 1; maintenance 1 → 2; specialistSlots – → {Artist: 1}; requiredBuilding – → Monument
  - added: `Destroyed when the city is captured`
- **Spartan Barracks** (Sparta)
  - culture 2 → –; maintenance 3 → 1
  - removed: `New [Military] units start with [25] Experience [in this city]`
  - added: `New [Military] units start with [20] XP [in this city]`
  - added: `[+10]% Production when constructing [Melee] units [in this city]`
- **Palace of the Popes** (House of Borgia)
  - gold 6 → 3; science 2 → 3; culture 3 → 1; faith 3 → 2; cityStrength 2 → 2.5
- **Thermae** (Rome) — renamed from "Circus Maximus"
  - requiredTech Horseback Riding → Construction; culture 2 → 1; happiness 4 → 2; maintenance 3 → 1
  - removed: `Cost increases by [10] per owned city`
  - removed: `Destroyed when the city is captured`
  - added: `[+10]% growth [in this city]`
- **Smugglers Cove** (Red Flag Pirate Confederation)
  - gold 4 → 3; specialistSlots {Merchant: 2} → {Merchant: 1}; percentStatBonus {gold: 30} → {gold: 25}
  - removed: `[+1 Gold] from each Trade Route`
  - removed: `[+2 Gold] from [Luxury] tiles [in this city]`
  - removed: `[+3 Gold] from [Oasis] tiles [in this city]`
  - added: `[+1 Gold] from [Water resource] tiles [in this city]`
- **Sea Fort** (Red Flag Pirate Confederation)
  - cityStrength – → 3
  - removed: `[+1 Gold] from [Water resource] tiles [in this city]`
  - removed: `New [Military Water] units start with [15] Experience [in this city]`
  - added: `New [Water] units start with [15] XP [in this city]`
- **Great Hall** (Norseman Vikings)
  - cost 90 → –; culture 4 → 3; faith 1 → –; maintenance 1 → 2; specialistSlots – → {Artist: 1}; requiredBuilding – → Monument
  - added: `Destroyed when the city is captured`
- **Royal Library** (Greece)
  - science 2 → 1; happiness 1 → –; greatPersonPoints – → {Great Scientist: 1}
- **Synagogue** (Ancient Israel)
  - cost 100 → –; requiredTech Theology → Philosophy; culture 2 → 1; happiness 2 → 1; faith 3 → 2; maintenance – → 2
  - added: `Only available <when religion is enabled>`
  - added: `Destroyed when the city is captured`
- **Solomon's Temple** (Ancient Israel)
  - faith 10 → 8
  - removed: `Cost increases by [20] per owned city`
  - removed: `Hidden when religion is disabled`
  - removed: `[+25]% Spread Religion Strength <for [Great Prophet] units>`
  - removed: `[-25]% Faith cost of generating Great Prophet equivalents`
  - added: `Cost increases by [30] per owned city`
  - added: `Only available <when religion is enabled>`
  - added: `[-15]% Faith cost of generating Great Prophet equivalents`
- **Highland Hall** (Scottish Clans)
  - culture 5 → 4; happiness 3 → 1
  - removed: `[+5]% [Culture] [in capital]`
- **Wall Street** (America)
  - gold 5 → 4; happiness 1 → –; percentStatBonus {gold: 35} → {gold: 33}
- **Silicon Valley** (America)
  - science 6 → 5; percentStatBonus {science: 60} → {science: 50}
- **Smithsonian** (America)
  - percentStatBonus {culture: 15} → –; science – → 2
- **Fortress of Alamut** (The Order of Assassins)
  - cityStrength 12 → 9; cityHealth 75 → 40
  - added: `[-50]% enemy spy effectiveness [in this city]`
- **Kraal** (Zulu)
  - food 3 → 2
  - removed: `[+1 Food] from every [Pasture]`
  - removed: `[+5]% [Food] [in this city]`
  - added: `[+1 Food] from [Bananas] tiles [in this city]`
  - added: `[+1 Food] from [Pasture] tiles [in this city]`
- **Ikhanda** (Zulu)
  - removed: `New [Military] units start with [15] Experience [in this city]`
  - removed: `New [Melee] units start with [15] Experience [in this city]`
  - added: `New [Military] units start with [15] XP [in this city]`
  - added: `New [Melee] units start with [10] XP [in this city]`
- **Globe Theatre** (England)
  - culture 3 → 2
- **Mission** (Spain)
  - faith 3 → 2
  - removed: `Hidden when religion is disabled`
  - removed: `[+10]% Natural religion spread [in this city]`
  - added: `Only available <when religion is enabled>`
  - added: `[+25]% Natural religion spread [in this city]`
- **+10% Tax**
  - removed: `Instantly provides [5] [Taxation(%)]`
  - added: `Can only be built <in [Capital] cities>`
  - added: `Remove [Down Tax] [in this city]`
- **-10% Tax**
  - removed: `Instantly consumes [5] [Taxation(%)]`
  - added: `Can only be built <in [Capital] cities>`
  - added: `Remove [Rise Tax] [in this city]`
- **Chateau** (France)
  - gold 3 → 1; culture 1 → 2; cityStrength 8 → 7; cityHealth 30 → 25
  - added: `Destroyed when the city is captured`
- **Versailles** (France)
  - gold 7 → 5; science 4 → 3; faith 0 → –; cityStrength 2 → 2.5
  - removed: `[+1 Gold] from every [Luxury resource]`
- **Dutch Windmill** (The Netherlands)
  - production 3 → 2; maintenance 1 → 2
  - added: `Must not be on [Hill]`
- **Amsterdam Exchange Bank** (The Netherlands)
  - removed: `[+1 Gold] per [8] population [in this city]`
- **Nilometer** (Egypt)
  - food 4 → 3; production 2 → 1
  - removed: `[+20]% Yield from every [River]`
  - added: `[+1 Food] from [Flood plains] tiles [in this city]`
- **Apadana** (Persia)
  - gold 1 → 2; culture 1 → –
  - removed: `[+1 Gold] from each Trade Route`
- **Silk Routes** (Mongolia)
  - gold 3 → 2; specialistSlots {Merchant: 2} → {Merchant: 1}
  - removed: `[+1 Gold] from each Trade Route`
  - added: `[+1 Gold] from each Trade Route <in this city>`
- **Ger Camp** (The Huns)
  - removed: `[+1 Production, +1 Food] from [Cattle] tiles [in this city]`
  - removed: `[+2 Production] from [Horses] tiles [in this city]`
  - removed: `[+1 Production, +1 Food] from [Sheep] tiles [in this city]`
  - added: `[+1 Production] from [Cattle] tiles [in this city]`
  - added: `[+1 Production] from [Horses] tiles [in this city]`
  - added: `[+1 Production] from [Sheep] tiles [in this city]`
  - added: `[+1 Food] from [Cattle] tiles [in this city]`
  - added: `[+1 Food] from [Sheep] tiles [in this city]`
- **Hacienda** (Gran Colombia)
  - gold 2 → 1
  - removed: `[+1 Production, +1 Food] <if [Hacienda] is constructed in all [in all cities] cities>`
- **Libertador's Plaza** (Gran Colombia) — renamed from "Libertador’s Plaza"
  - gold 1 → –; happiness 4 → 3; maintenance – → 1
  - removed: `Gifts of Gold to City-States generate [+5]% more Influence`
- **Green Corn Ceremonial Ground** (Cherokee)
  - food 3 → 2; culture 1 → –
  - removed: `[+2 Food] from [Deer] tiles [in this city]`
  - added: `[+1 Food] from [Deer] tiles [in this city]`
- **Three Sisters Farm** (Cherokee)
  - cost 100 → –; production 3 → 2; maintenance 1 → 2
  - removed: `[+1 Production] from [Forest] tiles [in this city]`
- **Sequoyah's Syllabary** (Cherokee)
  - gold 1 → –; science 1 → –; culture – → 1
- **Mozart's Concert Hall** (Austria)
  - culture 5 → 4
- **Gregor Mendel's Research Lab** (Austria)
  - science 5 → 4; specialistSlots {Scientist: 2} → {Scientist: 1}; percentStatBonus {science: 52} → {science: 50}
  - added: `[+1 Science] from [Farm] tiles [in this city]`
- **Commandery** (Knights Templar)
  - gold 4 → 2; faith – → 2
  - removed: `[+3]% [Gold] from Trade Routes`
- **World's Gold Mines**
  - cost 99999999 → 300; requiredTech Geoengineering → Economics; gold – → 4
  - removed: `Can be purchased with [Gold] [in capital]`
  - removed: `Can be purchased for [30000] [Gold] [in capital]`
  - removed: `Unbuildable`
  - removed: `[+3 Gold] from [Gold Ore] tiles [in all cities]`
  - added: `Only available <when [Economic] Victory is enabled>`
  - added: `Only available <if [Market] is constructed in all [non-[Puppeted]] cities>`
  - added: `Can only be built <in [Capital] cities>`
  - added: `Costs [150] [Bullion] <(modified by game speed)>`
  - added: `Cost increases by [30] per owned city`
  - added: `Cannot be hurried`
  - added: `Triggers a global alert upon completion`
  - added: `[+2 Gold] from [Gold Ore] tiles [in all cities]`
- **World's Diamond Mines**
  - cost 99999999 → 400; requiredTech Geoengineering → Industrialization; gold – → 4
  - removed: `Can be purchased with [Gold] [in capital]`
  - removed: `Can be purchased for [10000] [Gold] [in capital]`
  - removed: `Unbuildable`
  - removed: `[+3 Gold] from [Gems] tiles [in all cities]`
  - added: `Only available <when [Economic] Victory is enabled>`
  - added: `Only available <if [Bank] is constructed in all [non-[Puppeted]] cities>`
  - added: `Can only be built <in [Capital] cities>`
  - added: `Costs [250] [Bullion] <(modified by game speed)>`
  - added: `Cost increases by [30] per owned city`
  - added: `Cannot be hurried`
  - added: `Triggers a global alert upon completion`
  - added: `[+2 Gold] from [Gems] tiles [in all cities]`
- **World Stock Market**
  - cost 99999999 → 500; requiredTech Geoengineering → Electricity
  - removed: `Can be purchased with [Gold] [in capital]`
  - removed: `Can be purchased for [10000] [Gold] [in capital]`
  - removed: `Unbuildable`
  - removed: `[+50]% [Gold] from every [Stock Exchange]`
  - added: `Only available <when [Economic] Victory is enabled>`
  - added: `Only available <if [Stock Exchange] is constructed in all [non-[Puppeted]] cities>`
  - added: `Can only be built <in [Capital] cities>`
  - added: `Costs [400] [Bullion] <(modified by game speed)>`
  - added: `Cost increases by [30] per owned city`
  - added: `Cannot be hurried`
  - added: `Triggers a global alert upon completion`
  - added: `[+10]% [Gold] [in all cities]`
- **World Bank**
  - cost 99999999 → 800; requiredTech Geoengineering → Globalization
  - removed: `Can be purchased with [Gold] [in capital]`
  - removed: `Can be purchased for [50000] [Gold] [in capital]`
  - removed: `Unbuildable`
  - removed: `Production to [Gold] conversion in cities changed by [+75]%`
  - added: `Only available <when [Economic] Victory is enabled>`
  - added: `Only available <if [World's Gold Mines] is constructed>`
  - added: `Only available <if [World's Diamond Mines] is constructed>`
  - added: `Only available <if [World Stock Market] is constructed>`
  - added: `Can only be built <in [Capital] cities>`
  - added: `Costs [700] [Bullion] <(modified by game speed)>`
  - added: `Cost increases by [30] per owned city`
  - added: `Cannot be hurried`
  - added: `Triggers a global alert upon completion`
  - added: `[+15]% [Gold] [in all cities]`
  - added: `Production to [Gold] conversion in cities changed by [+25]%`
- **Rialto Port** (Venice)
  - gold – → 2
  - removed: `[+15]% [Gold] from Trade Routes`
- **El Caracol** (The Maya)
  - science 2 → 1
- **Huey Teocalli** (Aztecs)
  - culture 1 → –; happiness 3 → 2
- **Hippodrome** (Byzantium)
  - gold 1 → –; culture 1 → –
- **Cathedral of World Unity**
  - removed: `Hidden when [Religious] Victory is disabled`
  - removed: `Cannot be hurried`
  - removed: `Hidden when religion is disabled`
  - added: `Only available <when [Religious] Victory is enabled>`
  - added: `Only available <when religion is enabled>`
  - added: `Only available <after enhancing a religion>`
  - added: `Unbuildable`
  - added: `Can be purchased for [2500] [Faith] [in holy cities]`
  - added: `Unsellable`
  - added: `Triggers a global alert upon completion`
- **Cothon** (Carthage)
  - removed: `[+2 Production] from [Water resource] tiles [in this city]`
  - added: `[+1 Production] from [Water resource] tiles [in this city]`
- **Hanse** (Germany)
  - gold 3 → 2
  - removed: `[+2 Production] from each Trade Route`
  - added: `[+2 Production] from each Trade Route <in this city>`
- **Seowon** (Korea)
  - science 4 → 3; culture 1 → 2; faith 1 → –
- **Hammam** (Arabia)
  - happiness 4 → 2; faith – → 1
- **Jade Workshop** (China)
  - production 3 → 2
  - removed: `[+50]% Yield from every [Luxury]`
  - added: `[+1 Gold] from [Luxury resource] tiles [in this city]`
- **Royal Elephant Stable** (Siam)
  - removed: `[+2 Production] from [Horses] tiles [in this city]`
  - removed: `Double quantity of [Horses] produced`
  - added: `[+1 Production] from [Horses] tiles [in this city]`
  - added: `[+1 Production] from [Ivory] tiles [in this city]`
- **Sankore Madrasah** (Songhai)
  - science 1 → –; culture 2 → 1; faith – → 1
- **Temple of the Sun** (Inca)
  - maintenance 1 → 2
  - removed: `Hidden when religion is disabled`
  - removed: `[+5]% [Food] [in this city]`
  - added: `Only available <when religion is enabled>`
- **Qhapaq Nan** (Inca)
  - cost 120 → –; replaces Harbor → Market; requiredTech Compass → Currency; maintenance 2 → –; gold – → 2; specialistSlots – → {Merchant: 1}; percentStatBonus – → {gold: 25}
  - removed: `[+1 Production] from [Water resource] tiles [in this city]`
  - removed: `Connects trade routes over water`
  - removed: `[+3 Gold] from each Trade Route`
  - added: `[+2 Gold] from each Trade Route <in this city>`
- **Grand Bazaar** (The Ottomans)
  - gold 4 → 3; specialistSlots {Merchant: 1} → {Merchant: 2}; percentStatBonus {gold: 30} → {gold: 25}
- **Panama Canal**
  - removed: `[+4 Gold] from [Sea Trade Route (Gold)] tiles [in this city]`
  - added: `[+2 Gold] from each Trade Route`
- **Hoover Dam**
  - removed: `[+25]% [Food] [in all cities]`
  - added: `Must be next to [River]`
  - added: `[+10]% [Food] [in all cities]`
- **Burj Khalifa**
  - removed: `[+25]% [Gold] [in all cities]`
  - added: `[+15]% [Gold] [in all cities]`
- **Hadron Collider**
  - removed: `[+25]% [Science] [in all cities]`
  - added: `[+15]% [Science] [in all cities]`

Back on the current base-game definition (stale copies removed): Bazaar, Burial Tomb, Ceilidh Hall, Floating Gardens, Krepost, Longhouse, Mud Pyramid Mosque, Mughal Fort, Paper Maker, Pyramid, Satrap's Court, Stele, Walls of Babylon, Wat.

## Policies

- **Mercenary Army**: `May buy [Landsknecht] units with [Gold] for [5] times their normal Production cost` → `[Gold] cost of purchasing [Military] units [-25]%`
- **Volunteer Army**: `[10] units cost no maintenance`, `[6] free [Foreign Legion] units appear` → `[10] units cost no maintenance`, `[4] free [Great War Infantry] units appear`
