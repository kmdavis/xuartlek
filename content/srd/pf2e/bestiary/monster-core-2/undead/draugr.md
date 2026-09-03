---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Draugr"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/water
  - pf2e/creature/trait/medium
statblock: inline
name: "Draugr"
level: 2
source: "Monster Core 2"
aon_id: "creature-4374"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4374"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Draugr"
level: "Creature 2"
size: "Medium"
trait_01: "Undead"
trait_02: "Water"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [4, 2, 3, -1, 1, 1]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/axe/greataxe|Greataxe]], [[srd/pf2e/compendium/equipment/armor#Leather Armor|Leather Armor]]"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +11; __Ref__: +6; __Will__: +7"
hp: 35
health:
  - name: "HP"
    desc: "35 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 3; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] 5"
abilities_mid:
  - name: "The Sea's Revenge"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A creature that slays a draugr is subjected to a mariner's curse spell with a DC of 17. The [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]] ends if the draugr is buried in a calm sea or after 1 week passes."
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greataxe +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d12+4 slashing plus grotesque gift"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d4+4 bludgeoning plus grotesque gift"
abilities_bot:
  - name: "Grotesque Gift"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|Olfactory]]) A draugr's attacks spatter their targets with rancid flesh and rotting seaweed. A creature damaged by a draugr's Strike must succeed at a DC 15 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1 (sickened 2 on a critical failure)."
  - name: "Swipe"
    desc: "⬺ The draugr powers their hate into attacking as many foes as possible. The draugr makes a melee Strike and compares the attack roll result to the AC of up to two foes, each of whom must be within its melee reach and adjacent to each other. Roll damage only once and apply it to each creature hit. A Swipe counts as two attacks for the draugr's multiple attack penalty. Draugr Ships When an entire ship's crew dies in one calamity, they might rise simultaneously, bound together in death. Tirelessly plaguing the seas, these draugr crews slowly corrupt their vessels. The cursed ships often exhibit unsettling phenomena, such as being able to sail against the wind or leaving schools of dead fish in their wake. Sea shanties tell of draugr raiders approaching during the night, wreathed in fog pierced by only the green glow emanating from their eyes."
sourcebook: "_Monster Core 2_, page 140."
```

```encounter-table
name: Draugr
creatures:
  - 1: Draugr
```
