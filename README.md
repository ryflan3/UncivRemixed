# UncivRemixed

An extension mod for [Unciv](https://github.com/yairm210/Unciv) on the **Civ V - Gods & Kings** ruleset.
Rebuilt for Unciv 5.0 (see [CHANGELOG.md](CHANGELOG.md)).

Every civilization gets a wider ability with several upsides and one real drawback, so each one plays differently.
Twenty new civilizations join the base roster, each with three to five unique units, buildings or improvements.

## What is in it

**Civilizations**

- 20 new civs: Tokugawa Shogunate, Sparta, House of Borgia, Red Flag Pirate Confederation, Norseman Vikings,
  Ancient Israel, Scottish Clans, The Order of Assassins, Zulu, Gran Colombia, Cherokee, Knights Templar,
  Safavid Dynasty, Venice, Indonesia, the Inuit, the Swiss Confederacy, the Khmer, Portugal and the
  East India Trading Company. Japan, Denmark and Sweden are replaced by Tokugawa and the Vikings.
  51 playable civs in total.
- Portugal builds **Feitorias**: trading outposts on land nobody owns. Each takes 16 turns, Portugal can hold 12,
  and each one pays Gold into the treasury. Details in the changelog.
- All 31 remaining base-game civs have an extended ability and many gain an extra unique unit or building.
- A custom AI personality for every leader.

**Map**

- **Beach**: a few flat coastal tiles turn into Beach. Build Shipyards, Resorts and Trading posts on them.
- **Volcano**: a rare feature on Mountains. Land next to one yields +1 Food.
- Four natural wonders: Mount Vesuvius, Giant's Causeway, Ha Long Bay and Whitehaven Beach.
- Five extra luxuries (Tea, Caviar, Cocoa, Coffee, Tobacco) and new improvements (Arctic Research Station,
  Rice Paddy, Dry Dock, Canal).
- Cities work tiles up to 4 away, and need 4 tiles between them (3 across water) so they do not crowd each other.

**Systems**

- Three extra policy trees (Exploration, Aesthetics, National Defense) and extra beliefs and religions.
- 44 city-states each have their own friend and ally bonus instead of sharing five types.
- **Religious victory**: become the world religion, enhance it, then buy the Cathedral of World Unity with Faith
  in your holy city. Cultural victory needs 6 completed policy trees.
- **Economic victory**: build the four pillars of the world economy in your capital and out-earn every rival.
  The pillars cost Bullion, which only Mints, Banks and Stock Exchanges produce. Details in the changelog.
- A tax switch in the capital: buy High or Low Taxes with Culture.
- Three technologies (Geoengineering, Urbanization, Geothermal Energy) with a Reservoir, Apartment Block and
  Geothermal Plant, and five wonders. The Geothermal Plant needs a Volcano within 3 tiles of the city.

## Maps

Fourteen ready-made maps come with the mod. In the new game screen choose *Custom* as the map type and pick one;
it switches on this mod and the Gods & Kings ruleset for you. All except North America have 8 start positions.

**Built for particular civs.** Each start sits in country made for one civilization, with the resources and
terrain its abilities want. Tick *Select players from starting locations* to play exactly those eight. If you
pick other civs they are placed by the game as usual, and random AI opponents are drawn from the eight first.

| Map | Size | The eight starts |
|---|---|---|
| Homelands | 88 × 58 | Inuit ice coast, Viking fjords, a Swiss mountain valley, a Portuguese cape with empty islets for Feitorias, Safavid desert, Khmer jungle basin, Zulu savanna, an Indonesian volcano chain |
| The Middle Sea | 88 × 54 | Rome and Sparta on facing peninsulas, Venice in the gulf between them, Carthage, Egypt on its river, Ancient Israel, the Templars on a fortress island, the Assassins in a mountain ring with two passes |
| Monsoon Coast | 86 × 58 | Mongol steppe, the Chinese river plain, Korea, the Tokugawa island arc, India, the East India Trading Company among plantations at the head of the bay, Siam, the Pirates in a maze of beaches |

**Built for war.** Each one gives the defender something to hold and the attacker a problem to solve.

| Map | Size | What it is |
|---|---|---|
| Iron Passes | 80 × 56 | Eight valleys walled off by mountains, each with its own climate. One pass between neighbours, one tile wide, with an old fort standing in it. No sea route |
| Stormwall | 84 × 56 | Two continents across a narrow channel. Both shores are cliffs broken by a few landing beaches, with three fortress islands in mid-channel. 4 starts per side |
| The Moatlands | 80 × 56 | Open cavalry country cut into nine realms by rivers. Every border is a moat with a few fords, and each ford has hills on both banks. The empty realm in the middle holds the best land |

**Unusual country.**

| Map | Size | What it is |
|---|---|---|
| Dune Sea | 84 × 54 | A desert continent with one great river, its flood plains and a tributary. Four starts on the river, four at oases |
| Thousand Lakes | 82 × 54 | Forest, marsh and lakes everywhere. Fresh water for every city, almost no open ground for an army |
| Frostbound | 80 × 56 | A ring of land around a frozen polar sea. Colder with every step inward, and the islands in the ice hold most of the Oil, Uranium and Aluminum |
| Ring of Fire | 84 × 54 | Six lands in a ring around an inner sea, strung along a chain of volcanoes |
| Skull Island | 72 × 58 | An island shaped like a skull over crossed bones: lagoon eyes, a volcano nose, ruins everywhere. Tropical |
| Four Kingdoms | 76 × 61 | Four matching corner kingdoms, each joined by a causeway to a volcano-ringed prize island. Built to be fair |
| Corsair Shoals | 82 × 52 | A tropical sea of small islands, atolls and long beaches. Needs a navy |
| North America XXL | 90 × 75 | The original map from version 1 |

## Installing

In Unciv open *Mods*, paste the repository URL and download. Start a new game with **Civ V - Gods & Kings** as the
base ruleset and tick UncivRemixed. The mod hides itself for other base rulesets because it needs religion.

## Tuning the map features

Both rates are single numbers, so they are easy to change if you want more or less of either.

- **Beach**: in `jsons/Terrains.json`, Grassland, Plains and Desert each have a line
  `Becomes [Beach] when adjacent to [Coast] <in [Featureless] tiles> <with [35]% chance>`.
  The percentage is the share of flat, featureless tiles next to Coast that become Beach
  (35% for Grassland and Plains, 45% for Desert, which works out at roughly one coastal tile in ten).
- **Volcano**: uses the game's own *Rare features richness* slider in the advanced map options
  (default 5% of Mountain tiles).

## Art

Original art made for this mod: emblems and leader portraits for the 20 new civs, icons for 35 unique units and
13 unique improvements, map tiles for the Volcano and the four natural wonders, and map sprites for 21 tile
improvements in both tilesets (HexaRealm and FantasyHex), so they are drawn on the map as buildings.
The vector sources and the sprite script are in `ArtSource/`; the game reads the PNGs in `Images/`, packed into `game.png` / `game.atlas`.
Unciv on desktop repacks the atlas by itself whenever a file in `Images/` changes.

## Credits

Built on work by other modders, adapted to fit together:

- Beach terrain, tax system and Economic victory: hachchch
- Beliefs, religions and policy trees: BNW mod
- City-state overhaul: Ace Hank
- Inspiration: Ravignir (BNW, RekMOD) and A1y0sh4 (Unciv rework)

Third-party icons are listed in [credits.md](credits.md).
