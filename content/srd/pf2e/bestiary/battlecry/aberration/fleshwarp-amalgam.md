---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fleshwarp Amalgam"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Fleshwarp Amalgam"
level: 8
source: "Battlecry!"
aon_id: "creature-3916"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3916"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Fleshwarp Amalgam"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Aberration"
trait_02: "Mindless"
trait_03: "Troop"
trait_04: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]; can't speak any language"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +16"
abilityMods: [6, 2, 5, -5, 0, 0]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +19; __Ref__: +14; __Will__: +13"
hp: 135
health:
  - name: "HP"
    desc: "135 (4 segments); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]; __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 10"
abilities_mid:
  - name: "Brutal Retaliation"
    desc: "⬲"
  - name: "Trigger"
    desc: "The fleshwarp amalgam loses a segment due to passing a Hit Point threshold"
  - name: "Effect"
    desc: "The fleshwarp amalgam lashes out in retaliation. Each enemy in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] takes 2d10+6 bludgeoning or slashing damage (DC 23 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex). A creature who fails the save is also pushed 5 feet away from the amalgam."
  - name: "Troop Defenses"
    desc: ""
speed: "30 feet; troop movement"
abilities_bot:
  - name: "Acid Spray"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]]) The fleshwarp amalgam sprays acid from their various orifices, combining the streams into a powerful spray. This acid spray is a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] that deals 3d8 acid damage (DC 23 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save) within 60 feet. A creature who critically fails their saving throw takes 1d8 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent acid damage]]. When the troop is reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Frenzy of Tentacles and Claws"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The fleshwarps make wild melee attacks against each enemy in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] (DC 23 basic Reflex save). The damage depends on the number of actions. ⬻ 1d10 bludgeoning or slashing damage ⬺ 2d10+6 bludgeoning or slashing damage ⬽ 2d10+11 bludgeoning or slashing damage"
  - name: "Many-Limbed Stride"
    desc: "While moving on land, the fleshwarp amalgam ignores the effects of non-magical difficult terrain."
sourcebook: "_Battlecry!_, page 180."
```

```encounter-table
name: Fleshwarp Amalgam
creatures:
  - 1: Fleshwarp Amalgam
```
