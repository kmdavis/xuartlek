---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Storm Hag"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/air
  - pf2e/creature/trait/electricity
  - pf2e/creature/trait/hag
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Storm Hag"
level: 5
source: "Monster Core 2"
aon_id: "creature-4433"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4433"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Storm Hag"
level: "Creature 5"
size: "Medium"
trait_01: "Air"
trait_02: "Electricity"
trait_03: "Hag"
trait_04: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision, stormsight"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]], [[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]; voice of the storm"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +11, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/lore|Weather Lore]] +13"
abilityMods: [4, 2, 4, 2, 3, 4]
abilities_top:
  - name: "Coven"
    desc: "A storm hag adds [[srd/pf2e/compendium/spells/rank-4/hydraulic-torrent|_hydraulic torrent_]], [[srd/pf2e/compendium/spells/rank-5/lightning-storm|_lightning storm_]], and [[srd/pf2e/compendium/spells/rank-5/mariners-curse|_mariner's curse_]] to their coven's spells."
  - name: "Stormsight"
    desc: "Wind, precipitation, and clouds don't impair a storm hag's vision; they ignore the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from storms, mist, precipitation, and the like."
  - name: "Voice of the Storm"
    desc: "A storm hag can send spoken messages or sounds on the wind to any spot that they've seen and the wind can reach within a 50-mile radius. They decide whether it's clearly audible or barely heard above the wind. The message is delivered regardless of whether anyone is present to hear it. The hag can use this ability to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] creatures that hear their message with dire threats or unnerving whispers of doom."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +15; __Ref__: +9; __Will__: +12"
hp: 90
health:
  - name: "HP"
    desc: "90; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], wind mastery; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 5"
abilities_mid:
  - name: "Wind Mastery"
    desc: "A storm hag is unaffected by strong winds, natural or magical."
speed: "25 feet, fly 40 feet; storm passage"
attacks:
  - name: "Melee"
    desc: "⬻ claw +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d4+4 slashing plus 1d12 electricity"
  - name: "Ranged"
    desc: "⬻ cutting gale +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], range 60 feet) __Damage__ 4d6 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]) The storm hag can take on the appearance of any Medium humanoid woman. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Storm Passage"
    desc: "The storm hag ignores difficult terrain caused by wind, rain, and other stormy weather."
  - name: "Stormcalling"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/downtime|Downtime]]) A storm hag can perform a special control weather ritual, which requires no secondary casters, to change the weather within 5 miles of their location for 4d12 hours. The primary check is a DC 23 [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] check, and they can't get an outcome worse than a failure. The storm hag can create only hurricanes, thunderstorms, and tornadoes, but they can do so regardless of the current season. They can also quell natural weather events but almost never willingly do so."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 22 - __3rd__ [[srd/pf2e/compendium/spells/rank-1/gust-of-wind|Gust of Wind]] (at will), [[srd/pf2e/compendium/spells/rank-3/lightning-bolt|Lightning Bolt]], [[srd/pf2e/compendium/spells/rank-2/summon-elemental|Summon Elemental]] (air or water only), [[srd/pf2e/compendium/spells/rank-3/wall-of-wind|Wall of Wind]]"
sourcebook: "_Monster Core 2_, page 186."
```

```encounter-table
name: Storm Hag
creatures:
  - 1: Storm Hag
```
