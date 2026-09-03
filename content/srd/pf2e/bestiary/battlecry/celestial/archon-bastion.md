---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Archon Bastion"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Archon Bastion"
level: 16
source: "Battlecry!"
aon_id: "creature-3903"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3903"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Archon Bastion"
level: "Creature 16"
size: "Gargantuan"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: "Troop"
trait_05: "Uncommon"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Utopian; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +32, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +28, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +28, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +28, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +26"
abilityMods: [6, 2, 9, 3, 5, 5]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +30; __Ref__: +25; __Will__: +28 +1 status to all saves vs. magic"
hp: 300
health:
  - name: "HP"
    desc: "300 (4 segments); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]; __Weaknesses__ area damage 15, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] 15"
abilities_mid:
  - name: "Archon's Aegis"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages an ally of the archon bastion and both are within 15 feet of the archon bastion"
  - name: "Effect"
    desc: "The ally gains [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance|resistance]] 20 to all damage against the triggering damage and the enemy takes 1d8+4 piercing damage (DC 34 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save)."
  - name: "Troop Defenses"
    desc: ""
speed: "30 feet, fly 60 feet; troop movement"
abilities_bot:
  - name: "Fearless Switch"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|Teleportation]]) The archon bastion Strides so that at least one of its segments occupies the same space of a Large or smaller willing ally. That willing ally is then teleported to any open space it can fit into that is adjacent to any of the archon bastion's segments, using teleportation magic innate to the troop's individual shield archons. The archon bastion can move up to three allies in this fashion."
  - name: "Living Shields"
    desc: "⬻ The archon bastion grants each ally within a 5-foot emanation a +2 circumstance bonus to AC until that ally is no longer within the area or until the start of the archon bastion's next turn, whichever comes first. If the archon bastion uses Archon's Aegis against an attack against one of the shielded allies, the archon bastion gains the resistance and takes the damage rather than the ally."
  - name: "Smiting Lances"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The archon bastion engages in a uniform melee attack against each enemy in 10-foot emanation (DC 34 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). The damage depends on the number of actions. An [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] creature that fails its save against this effect takes an additional 2d6 spirit damage (or 1d6 spirit damage for the one-action version). ⬻ 1d8+4 piercing damage [two-actions] 3d8+14 piercing damage [three-actions] 4d8+19 piercing damage"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/divine-lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/message|Message]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/share-life|Share Life]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Battlecry!_, page 174."
```

```encounter-table
name: Archon Bastion
creatures:
  - 1: Archon Bastion
```
