---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Eremite"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/velstrac
  - pf2e/creature/trait/medium
statblock: inline
name: "Eremite"
level: 20
source: "Monster Core 2"
aon_id: "creature-4611"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4611"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Eremite"
level: "Creature 20"
size: "Medium"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
modifier: 34
perception:
  - name: "Perception"
    desc: "Perception +34; greater darkvision, painsight, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Shadowtongue|Shadowtongue]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +38, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +36, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +40, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +36, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +34, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +36, [[srd/pf2e/compendium/rules-elements/skills/lore|Torture Lore]] +36"
abilityMods: [9, 6, 7, 6, 6, 10]
abilities_top:
  - name: "Painsight"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A velstrac automatically knows whether a creature it sees has any of the [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Dying|dying]], and [[srd/pf2e/compendium/rules-elements/conditions#Wounded|wounded]] conditions as well as the value of those conditions."
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +37; __Ref__: +32; __Will__: +34 +1 status to all saves vs. magic"
hp: 375
health:
  - name: "HP"
    desc: "375 , regeneration 25 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] or [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Immunity to Nonlethal|nonlethal]]; __Weaknesses__ holy 20, silver 20"
abilities_mid:
  - name: "Ignore Pain"
    desc: "An eremite's actions can't be [[srd/pf2e/books/player-core/chapter-7-spells/casting-spells#Disrupted and Lost Spells|disrupted]] due to damage or Strikes (such as [[srd/pf2e/compendium/rules-elements/actions/player-core#Reactive Strike|Reactive Strike]])."
  - name: "Paralytic Perfection"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 30 feet. When a creature ends its turn in the aura, it feels compelled to offer pieces of its own flesh to the eremite. The creature must succeed at a DC 40 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]] for 1 round."
speed: "30 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +39 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 4d8+19 piercing plus 2d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed]] and exquisite pain"
  - name: "Melee"
    desc: "⬻ claw +39 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d6+19 slashing plus 2d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed]], exquisite pain, and Improved Grab"
abilities_bot:
  - name: "Evisceration"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]])"
  - name: "Requirements"
    desc: "The eremite has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]"
  - name: "Effect"
    desc: "The eremite excises flesh or bone from a creature they've grabbed or restrained. The target takes 6d10 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]]."
  - name: "Exquisite Pain"
    desc: "An eremite's knowledge of pressure points and pain centers is unsurpassed. A creature hit by an eremite's melee Strikes must succeed at a DC 40 Fortitude save or be [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] 2 (stunned 4 on a critical failure). A creature that critically succeeds is temporarily immune for 24 hours."
  - name: "Focus Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) The eremite stares at a creature they can see within 30 feet. The creature must immediately attempt a Will save against paralytic perfection. In addition, if the creature was already [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], on a failed save, its unnatural longing causes it to become [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]] 1. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the eremite's next turn."
  - name: "Graft Flesh"
    desc: "⬻"
  - name: "Requirements"
    desc: "The eremite holds a piece of flesh they collected via Evisceration"
  - name: "Effect"
    desc: "The eremite attaches the stolen flesh to themself. They either regain 100 Hit Points; reduce the value of their [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]], or [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] condition by 3; or reduce the stage of any affliction affecting them by 3."
  - name: "Shadow Traveler"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) When an eremite uses [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|_interplanar teleport_]], they arrive at exactly their intended destination."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/stabilize|Stabilize]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (to [[srd/pf2e/compendium/gm/planes#The Netherworld|the Netherworld]] or [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]] only), [[srd/pf2e/compendium/spells/rank-7/planar-seal|Planar Seal]], [[srd/pf2e/compendium/spells/rank-5/shadow-blast|Shadow Blast]], [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will), [[srd/pf2e/compendium/spells/rank-7/warp-mind|Warp Mind]] - __9th__ [[srd/pf2e/compendium/spells/rank-6/blessed-boundary|Blessed Boundary]], [[srd/pf2e/compendium/spells/rank-1/harm|Harm]] (×2), [[srd/pf2e/compendium/spells/rank-1/heal|Heal]] (×2), [[srd/pf2e/compendium/spells/rank-9/seize-soul|Seize Soul]], [[srd/pf2e/compendium/spells/rank-5/shadow-blast|Shadow Blast]] - __Constant (9th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
sourcebook: "_Monster Core 2_, page 348."
```

```encounter-table
name: Eremite
creatures:
  - 1: Eremite
```
