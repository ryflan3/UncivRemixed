# UncivRemixed

An extension mod for [Unciv](https://github.com/yairm210/Unciv) on the **Civ V - Gods & Kings** ruleset.
Rebuilt for Unciv 5.0 (version 2.0 of the mod, see [CHANGELOG.md](CHANGELOG.md)).

Every civilization gets a wider ability with several upsides and one real drawback, so each one plays differently.
Fourteen new civilizations join the base roster, each with three or four unique units, buildings or improvements.

## What is in it

**Civilizations**

- 14 new civs: Tokugawa Shogunate, Sparta, House of Borgia, Red Flag Pirate Confederation, Norseman Vikings,
  Ancient Israel, Scottish Clans, The Order of Assassins, Zulu, Gran Colombia, Cherokee, Knights Templar,
  Safavid Dynasty and Venice. Japan, Denmark and Sweden are replaced by Tokugawa and the Vikings.
- All 31 remaining base-game civs have an extended ability and many gain an extra unique unit or building.
- A custom AI personality for every leader.

**Map**

- **Beach**: a few flat coastal tiles turn into Beach. Build Shipyards, Resorts and Trading posts on them.
- **Volcano**: a rare feature on Mountains. Land next to one yields +1 Food.
- Five extra luxuries (Tea, Caviar, Cocoa, Coffee, Tobacco) and new improvements (Arctic Research Station,
  Rice Paddy, Dry Dock, Canal).
- Cities work tiles up to 4 away.

**Systems**

- Three extra policy trees (Exploration, Aesthetics, National Defense) and extra beliefs and religions.
- 48 city-states each have their own friend and ally bonus instead of sharing five types.
- Economic and Religious victories; Cultural victory needs 6 completed policy trees.
- A tax switch in the capital: buy High or Low Taxes with Culture.
- Two technologies (Geoengineering, Urbanization) and five wonders.

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

Icons for the 14 new civs and 26 new unique units are original art made for this mod. The vector sources are in
`ArtSource/`; the game reads the 100 px PNGs in `Images/`, packed into `game.png` / `game.atlas`.
Unciv on desktop repacks the atlas by itself whenever a file in `Images/` changes.

## Credits

Built on work by other modders, adapted to fit together:

- Beach terrain, tax system and Economic victory: hachchch
- Beliefs, religions and policy trees: BNW mod
- City-state overhaul: Ace Hank
- Inspiration: Ravignir (BNW, RekMOD) and A1y0sh4 (Unciv rework)

Third-party icons are listed in [credits.md](credits.md).
