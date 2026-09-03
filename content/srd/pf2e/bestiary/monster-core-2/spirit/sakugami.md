---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sakugami"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/kami
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/medium
statblock: inline
name: "Sakugami"
level: 15
source: "Monster Core 2"
aon_id: "creature-4456"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4456"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sakugami"
level: "Creature 15"
size: "Medium"
trait_01: "Kami"
trait_02: "Rare"
trait_03: "Spirit"
trait_04: "Wood"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|_speak with plants_]], telepathy 150 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +30, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +31, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +28, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +30, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +28, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +30"
abilityMods: [5, 7, 6, 2, 7, 8]
abilities_top:
  - name: "Ward"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) Every kami is bound to a ward: a specific animal, plant, object, or location. A kami can merge with or emerge from their ward as a single action, which has the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait. While merged, the kami can observe their surroundings with their usual senses as well as the senses of their ward, but can't move, communicate with, or control their ward. Additionally, a kami merged with their ward recovers Hit Points each minute as if they spent an entire day resting. A sakugami's ward is a specific deciduous tree with seasonal blossoms, such as a cherry, plum, or wisteria."
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+2 striking]] [[srd/pf2e/compendium/rules-elements/traits/gm-core/staff|staff]]_"
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +25; __Ref__: +28; __Will__: +30"
hp: 350
health:
  - name: "HP"
    desc: "350; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 15"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Sakugami's Foresight"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/prediction|prediction]])"
  - name: "Trigger"
    desc: "The sakugami is subject to a [[srd/pf2e/compendium/rules-elements/conditions#Hostile|hostile]] action or needs to roll to defend itself"
  - name: "Effect"
    desc: "The sakugami rolls twice and uses the higher result for its saving throw or other defense (a [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]] effect) or forces the [[srd/pf2e/compendium/rules-elements/conditions#Hostile|hostile]] creature or danger to roll twice and use the lower result for its attack roll or similar roll (a [[srd/pf2e/compendium/rules-elements/traits/player-core/misfortune|misfortune]] effect)."
speed: "50 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _staff_ +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d8]]) __Damage__ 2d4+13 bludgeoning plus fleeting blossoms and touch of ages"
abilities_bot:
  - name: "Fleeting Blossoms"
    desc: "A sakugami's staff Strikes stir up fleeting blossoms that bloom, wilt, and decay all in the space of an instant. On a hit, they deal an additional 1d6 mental damage, as well as an additional 1d6 void damage to living creatures and an additional 1d6 vitality damage to undead."
  - name: "Swift Staff Strike"
    desc: "⬺ In a rapid series of movements, the sakugami unleashes a deadly assault. The sakugami makes three staff Strikes. The sakugami's multiple attack penalty doesn't increase until after they've made all three Strikes."
  - name: "Touch of Ages"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A sakugami's attacks bestow a curse that alters the very flow of time in those they attack. When a sakugami hits a creature with a melee Strike, the creature must attempt a DC 36 Fortitude save as its perspective shifts rapidly between that of advanced age and an infantile state. Regardless of the outcome, the creature is temporarily immune for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature becomes [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1, [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1, and [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 for 1 round."
  - name: "Failure"
    desc: "The creature becomes clumsy 2, enfeebled 2, and stupefied 2 for 1 minute."
  - name: "Critical Failure"
    desc: "As failure, but the conditions are permanent."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36 - __4th__ [[srd/pf2e/compendium/spells/rank-2/status|Status]] - __5th__ [[srd/pf2e/compendium/spells/rank-1/heal|Heal]] (×3), [[srd/pf2e/compendium/spells/rank-2/one-with-plants|One with Plants]] (flowering trees only), [[srd/pf2e/compendium/spells/rank-2/peaceful-rest|Peaceful Rest]] - __6th__ [[srd/pf2e/compendium/spells/rank-2/cleanse-affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-5/natures-pathway|Nature's Pathway]] (at will; flowering trees only), [[srd/pf2e/compendium/spells/rank-3/slow|Slow]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/execute|Execute]], [[srd/pf2e/compendium/spells/rank-3/haste|Haste]], [[srd/pf2e/compendium/spells/rank-7/regenerate|Regenerate]]"
sourcebook: "_Monster Core 2_, page 207."
```

```encounter-table
name: Sakugami
creatures:
  - 1: Sakugami
```
