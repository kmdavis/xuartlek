---
noteType: pf2eMonster
aliases: "Jorogumo"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Jorogumo"
level: 13
source: "Monster Core 2"
other_sources: "Pathfinder #160: Assault on Hunting Lodge Seven"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4450"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Jorogumo"
level: "Creature 13"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Uncommon"
modifier: 26
perception:
  - name: "Perception"
    desc: "+26; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +22, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +28, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +26, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +24, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +23, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +24"
abilityMods: [6, 4, 5, 3, 5, 7]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +22; __Ref__: +23; __Will__: +26"
hp: 270
health:
  - name: "HP"
    desc: "270; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 15; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/Peachwood|peachwood]] 10"
abilities_mid:
  - name: "Darting Legs"
    desc: "⬲"
  - name: "Requirements"
    desc: "The jorogumo has their spider legs extended or has Changed Shape"
  - name: "Trigger"
    desc: "The jorogumo is targeted with an attack"
  - name: "Effect"
    desc: "The jorogumo raises a leg, gaining a +2 circumstance bonus to AC against the triggering attack."
speed: "30 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +27 __Damage__ 3d12+14 piercing plus jorogumo venom"
  - name: "Melee"
    desc: "⬻ claw +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 3d8+14 slashing"
  - name: "Ranged"
    desc: "⬻ web +23 (range increment 60 feet) __Damage__ web trap"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|polymorph]]) The jorogumo takes on the appearance of any Small or Medium spider. This doesn't change their Speed or Strikes."
  - name: "Jorogumo Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]])"
  - name: "Saving Throw"
    desc: "DC 32 Fortitude"
  - name: "Maximum Duration"
    desc: "4 hours"
  - name: "Stage 1"
    desc: "3d6 poison damage and [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied]] 1 (1 round)"
  - name: "Stage 2"
    desc: "3d6 poison damage and stupefied 2 (1 round)"
  - name: "Stage 3"
    desc: "4d6 poison damage and stupefied 2 (1 round)"
  - name: "Stage 4"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]] for 1d4 hours"
  - name: "Spider Legs"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|polymorph]])"
  - name: "Requirement"
    desc: "The jorogumo is in humanoid form"
  - name: "Effect"
    desc: "Eight large spider legs sprout from the jorogumo's back, granting a 40-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Movement#Climb Speed|climb Speed]] and allowing them to use the Darting Legs reaction."
  - name: "Web Trap"
    desc: "A creature hit by the jorogumo's web attack is [[srd/pf2e/compendium/rules-elements/Conditions#Immobilized|immobilized]] and stuck to the nearest surface, preventing the creature from moving. The DC to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Force Open|Force Open]] the web trap is 32. Peachwood Vulnerability [[srd/pf2e/compendium/equipment/materials/Peachwood|Peachwood]], often cultivated by [[srd/pf2e/compendium/deities/gods-of-the-inner-sea/Pharasma|Pharasmin]] priests, is used to ward away the undead. However, jorogumo also despise this auburn-tinged wood, despite being quite clearly a living creature. This has led many to speculate on the origins of these arachnid ambushers, but their secretive nature has made further research difficult. Learn more about peachwood in Lost Omens Tian Xia Character Guide."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 34 - __1st__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]] (at will) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Speak with Animals|Speak with Animals]] (spiders only) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Mind Reading|Mind Reading]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Outcast's Curse|Outcast's Curse]] (×3), [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] (×3) - __7th__ [[srd/pf2e/compendium/spells/rank-1/Summon Animal|Summon Animal]] (spiders only) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 201."
```

```encounter-table
name: Jorogumo
creatures:
  - 1: Jorogumo
```
