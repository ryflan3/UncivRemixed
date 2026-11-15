# UncivRemixed

An extension mod for [Unciv](https://github.com/yairm210/Unciv) on the **Civ V - Gods & Kings** ruleset.
Rebuilt for Unciv 5.0 (see [CHANGELOG.md](CHANGELOG.md)).

Every civilization gets a wider ability with several upsides and one real drawback, so each one plays differently.
Nineteen new civilizations join the base roster, each with three to five unique units, buildings or improvements.

## What is in it

**Civilizations**

- 19 new civs: Tokugawa Shogunate, Sparta, House of Borgia, Red Flag Pirate Confederation, Norseman Vikings,
  Ancient Israel, Scottish Clans, The Order of Assassins, Zulu, Gran Colombia, Cherokee, Knights Templar,
  Safavid Dynasty, Venice, Indonesia, the Inuit, the Swiss Confederacy, the Khmer and Portugal.
  Japan, Denmark and Sweden are replaced by Tokugawa and the Vikings. 50 playable civs in total.
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
- 48 city-states each have their own friend and ally bonus instead of sharing five types.
- **Religious victory**: become the world religion, enhance it, then buy the Cathedral of World Unity with Faith
  in your holy city. Cultural victory needs 6 completed policy trees.
- **Economic victory**: build the four pillars of the world economy in your capital and out-earn every rival.
  The pillars cost Bullion, which only Mints, Banks and Stock Exchanges produce. Details in the changelog.
- A tax switch in the capital: buy High or Low Taxes with Culture.
- Three technologies (Geoengineering, Urbanization, Geothermal Energy) with a Reservoir, Apartment Block and
  Geothermal Plant, and five wonders. The Geothermal Plant needs a Volcano within 3 tiles of the city.

## Maps

Five ready-made maps come with the mod. In the new game screen choose *Custom* as the map type and pick one;
it switches on this mod and the Gods & Kings ruleset for you. All except North America have 8 start positions.

| Map | Size | What it is |
|---|---|---|
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

Original art made for this mod: emblems and leader portraits for the 19 new civs, icons for 33 unique units and
13 unique improvements, and map tiles for the Volcano and the four natural wonders. The vector sources are in
`ArtSource/`; the game reads the PNGs in `Images/`, packed into `game.png` / `game.atlas`.
Unciv on desktop repacks the atlas by itself whenever a file in `Images/` changes.

## Credits

Built on work by other modders, adapted to fit together:

- Beach terrain, tax system and Economic victory: hachchch
- Beliefs, religions and policy trees: BNW mod
- City-state overhaul: Ace Hank
- Inspiration: Ravignir (BNW, RekMOD) and A1y0sh4 (Unciv rework)

Third-party icons are listed in [credits.md](credits.md).
