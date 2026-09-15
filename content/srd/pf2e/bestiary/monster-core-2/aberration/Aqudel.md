---
noteType: pf2eMonster
aliases: "Aqudel"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Aqudel"
level: 7
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4024"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Aqudel"
level: "Creature 7"
size: "Large"
trait_01: "Aberration"
trait_02: "Aquatic"
trait_03: "Uncommon"
modifier: 18
perception:
  - name: "Perception"
    desc: "+18; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], Alghollthu, [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]], [[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/Lore|Lore]] +16, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +18, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +15"
abilityMods: [6, 2, 5, 5, 3, 4]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +18; __Ref__: +11; __Will__: +16 all-around vision"
hp: 120
health:
  - name: "HP"
    desc: "120"
speed: "10 feet, swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 2d10+9 bludgeoning"
  - name: "Melee"
    desc: "⬻ cirrus +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 2d8+6 bludgeoning"
abilities_bot:
  - name: "Barbed Cirri"
    desc: "⬺ The aqudel makes up to four cirrus Strikes, each against a different target. These attacks count toward the aqudel's multiple attack penalty, but the multiple attack penalty doesn't increase until after they makes all of their attacks."
  - name: "Strobe"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|Visual]]) The aqudel changes the intensity and pattern of their skin in a rapid pulse, attempting to disorient any creatures that can see them. Creatures within 30 feet of the aqudel must attempt a DC 25 Will save. The aqudel can't use Strobe again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/Conditions#Dazzled|dazzled]] for 1 round."
  - name: "Failure"
    desc: "The target is dazzled for 1 minute and [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned 1]]."
  - name: "Critical Failure"
    desc: "The target is dazzled for 1 minute and stunned 2. Alghollthu Hierarchy [[srd/pf2e/bestiary/monster-core/aberration/Vidileth|Vidileths]] are the leaders of the [[srd/pf2e/compendium/gm/creature-families/Alghollthu|alghollthu]], subtly influencing events to foster what they consider the most favorable outcome, and some of their plots are centuries in the making. They control vast networks of their kin, directing them to influence lower alghollthu and leverage their knowledge to manipulate lesser beings than themselves (which is how they see all others). Aqudels and nymoluses fill the role of mid-ranking administrators, taking orders from veiled masters and then enacting their plans with resources derived from their own networks. An aqudel might supervise only one small cell, while a nymolus might oversee a dozen."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 26, attack +17 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Telekinetic Maneuver|Telekinetic Maneuver]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Mind Reading|Mind Reading]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]] (×3), [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] (×3) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 22."
```

```encounter-table
name: Aqudel
creatures:
  - 1: Aqudel
```
