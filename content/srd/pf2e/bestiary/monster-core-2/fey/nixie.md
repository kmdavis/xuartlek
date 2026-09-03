---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nixie"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/small
statblock: inline
name: "Nixie"
level: 1
source: "Monster Core 2"
aon_id: "creature-4489"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4489"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Nixie"
level: "Creature 1"
size: "Small"
trait_01: "Aquatic"
trait_02: "Fey"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [0, 3, 1, 0, 1, 4]
abilities_top:
  - name: "Wild Empathy"
    desc: "The nixie can use [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]] on and make very simple [[srd/pf2e/compendium/rules-elements/actions/player-core#Request|Requests]] of [[srd/pf2e/compendium/rules-elements/traits/player-core/aquatic|aquatic]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/amphibious|amphibious]] animals."
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +6; __Ref__: +10; __Will__: +6 +1 status to all saves vs. magic"
hp: 22
health:
  - name: "HP"
    desc: "22; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 3"
speed: "20 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d6 slashing"
abilities_bot:
  - name: "Grant Desire"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The nixie can duplicate any 1st-rank spell or produce any effect similar to that of a 1st-rank spell but only in response to the request or desire of a non-[[srd/pf2e/compendium/rules-elements/traits/player-core/fey|fey]] creature. The creature whose desire is granted can never again benefit from that particular nixie's Grant Desire ability. Bog Nixies Nixies who dwell in swampy regions tend to have fouler attitudes and are more eager to turn to violence. Known as bog nixies, these wicked fey prefer dwelling in festering swamps or blighted fens and delight in using their ability to grant desires to tempt visitors into acts of unplanned evil."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17, attack +9 - __1st__ [[srd/pf2e/compendium/spells/rank-1/charm|Charm]] (×3), [[srd/pf2e/compendium/spells/rank-1/hydraulic-push|Hydraulic Push]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/water-breathing|Water Breathing]]"
sourcebook: "_Monster Core 2_, page 235."
```

```encounter-table
name: Nixie
creatures:
  - 1: Nixie
```
