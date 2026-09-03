---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Omox"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Omox"
level: 12
source: "Monster Core"
aon_id: "creature-2898"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2898"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Omox"
level: "Creature 12"
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Ooze"
trait_04: "Unholy"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +21, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +20, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +24"
abilityMods: [7, 6, 7, 2, 4, 4]
abilities_top:
  - name: "Cleanly Vulnerability"
    desc: "An omox embodies filth, and they find the concept of cleanliness abhorrent. An omox subjected to an effect that cleans them, such as the tidy command of [[srd/pf2e/compendium/spells/cantrips/prestidigitation|_prestidigitation_]], takes 2d6 mental damage. They also take this damage the first time each round a creature hit by one of the omox's attacks spends actions cleaning off the filth."
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +23; __Ref__: +21; __Will__: +20 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 395
health:
  - name: "HP"
    desc: "395; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], critical hits, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], precision; __Weaknesses__ cold iron 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 10"
abilities_mid:
  - name: "Absorb Weapon"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]])"
  - name: "Trigger"
    desc: "A creature hits the omox with a melee weapon"
  - name: "Effect"
    desc: "The omox attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Disarm|Disarm]] the creature. On a critical success, the weapon becomes subsumed within the omox's body rather than falling to the ground. Retrieving the weapon requires Disarming the omox of it."
speed: "40 feet, climb 20 feet, swim 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sludge tendril +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d6+13 bludgeoning plus 2d6 acid and Grab"
  - name: "Ranged"
    desc: "⬻ slime ball +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], Brutal, range increment 30 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d4+11 bludgeoning plus 2d6 acid and slime trap"
abilities_bot:
  - name: "Liquid Leap"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|Teleportation]])"
  - name: "Requirements"
    desc: "The omox is in a space of liquid"
  - name: "Effect"
    desc: "The omox teleports from its current space to any unoccupied space of liquid within 120 feet."
  - name: "Slime Trap"
    desc: "A creature hit by an omox's slime ball must succeed at a DC 32 Reflex save or take a –10-foot circumstance penalty to its Speeds for 1 minute or until it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] (DC 35). On a critical failure, the creature is also [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]] for the same duration."
  - name: "Smother"
    desc: "⬻"
  - name: "Requirements"
    desc: "The omox has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]"
  - name: "Effect"
    desc: "The demon flows over the creature, covering it in oozing acidic slime. The creature must succeed at a DC 32 Fortitude save or it becomes [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] and must hold its breath or begin suffocating. These effects lasts as long as the omox has the creature grabbed or restrained."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32 - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/control-water|Control Water]], [[srd/pf2e/compendium/spells/rank-1/create-water|Create Water]] (at will), [[srd/pf2e/compendium/spells/rank-5/toxic-cloud|Toxic Cloud]], [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]]"
  - name: "Rituals"
    desc: "DC 32 - __1st__ [[srd/pf2e/compendium/spells/rituals/demonic-pact|Demonic Pact]]"
sourcebook: "_Monster Core_, page 79."
```

```encounter-table
name: Omox
creatures:
  - 1: Omox
```
