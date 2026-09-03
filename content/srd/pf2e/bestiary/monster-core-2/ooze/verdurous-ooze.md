---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Verdurous Ooze"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/medium
statblock: inline
name: "Verdurous Ooze"
level: 6
source: "Monster Core 2"
aon_id: "creature-4498"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4498"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Verdurous Ooze"
level: "Creature 6"
size: "Medium"
trait_01: "Mindless"
trait_02: "Ooze"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; motion sense 60 feet, no vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +4"
abilityMods: [5, -4, 5, -5, 0, -5]
abilities_top:
  - name: "Motion Sense"
    desc: "A verdurous ooze can sense nearby creatures through vibration and air or water movement."
ac: 12
armorclass:
  - name: "AC"
    desc: "12; __Fort__: +17; __Ref__: +8; __Will__: +10"
hp: 157
health:
  - name: "HP"
    desc: "157; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Immunity to Critical Hits|critical hits]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], piercing, precision, slashing, [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]"
abilities_mid:
  - name: "Corrosive Surface"
    desc: "A creature that hits a verdurous ooze with a metal weapon or unarmed attack must attempt a DC 21 Reflex save. On a failure, the weapon or creature takes 2d4 acid damage (after dealing damage to the ooze as normal). Thrown weapons take this damage automatically with no save."
  - name: "Enliven Foliage"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) 20 feet. The verdurous ooze constantly emits supernatural vapors that cause nearby plants to grow rapidly and writhe and grasp at anything and everything within the [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]]. This area becomes [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Difficult Terrain|difficult terrain]] for non–verdurous ooze creatures. When a creature starts its turn in this aura, it must succeed at a DC 21 Reflex save or take a –10-foot circumstance penalty to its Speeds until it leaves the emanation."
  - name: "Split"
    desc: "When a verdurous ooze that has 10 or more HP is hit by an attack that would deal piercing or slashing damage, it splits into two identical oozes, each with half the original's HP. One ooze is in the same space as the original, and the other is in an adjacent, unoccupied space. If no adjacent space is unoccupied, it automatically pushes creatures and objects out of the way to fill a space (the GM decides if an object or creature is too big or heavy to push)."
speed: "15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +15 __Damage__ 2d6+7 bludgeoning plus 1d6 acid and Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d6 bludgeoning plus 1d6 acid, DC 24"
  - name: "Sleep Gas"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|Sleep]]) The verdurous ooze adjusts its aura of supernatural vapors to affect living creatures within a 20-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] forcing them to attempt a DC 24 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected and becomes temporarily immune to Sleep Gas for 24 hours."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 for 1 round."
  - name: "Failure"
    desc: "The creature falls [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]. If it's still unconscious after 1 minute, it wakes up automatically."
  - name: "Critical Failure"
    desc: "The creature falls unconscious. If it's still unconscious after 1 hour, it wakes up automatically."
  - name: "Verdurous Ooze Acid"
    desc: "A verdurous ooze's acid damages only metal and flesh—not bone, stone, or other materials. Verdurous Congregation When verdurous oozes gather in sufficient number, they can merge together into conjoined forms. These enlarged blobs develop red and white connecting vessels that pulse hideously as thick, green fluid moves within them. While conjoined, the oozes move as one creature. Their usual enliven foliage and Sleep Gas auras double in size, and they become even more aggressive, feeding voraciously on any metal or flesh they can find."
sourcebook: "_Monster Core 2_, page 242."
```

```encounter-table
name: Verdurous Ooze
creatures:
  - 1: Verdurous Ooze
```
