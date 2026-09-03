---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Trollhound"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/troll
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/medium
statblock: inline
name: "Trollhound"
level: 3
source: "Monster Core 2"
aon_id: "creature-4595"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4595"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Trollhound"
level: "Creature 3"
size: "Medium"
trait_01: "Beast"
trait_02: "Troll"
trait_03: "Wood"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6"
abilityMods: [4, 1, 5, -3, 1, -2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +14; __Ref__: +8; __Will__: +6"
hp: 65
health:
  - name: "HP"
    desc: "65 , regeneration 15 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]); __Weaknesses__ electricity 8, fire 8"
abilities_mid:
  - name: "Flailing Bite"
    desc: "⬲"
  - name: "Trigger"
    desc: "The trollhound takes [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] damage; Effect The trollhound makes a jaws Strike against a random creature within reach. If the trollhound has [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire damage]], they attempt a DC 15 flat check to remove it."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 1d12+4 piercing plus Knockdown and bloodfire fever"
abilities_bot:
  - name: "Bloodfire Fever"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]]) Trollhounds and [[srd/pf2e/compendium/gm/creature-families/troll|trolls]] are immune to bloodfire fever"
  - name: "Saving Throw"
    desc: "DC 18 Fortitude"
  - name: "Stage 1"
    desc: "carrier with no ill effect (1 day)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 (1 day)"
  - name: "Stage 3"
    desc: "enfeebled 1 and [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1 (1 day)"
  - name: "Stage 4"
    desc: "enfeebled 2 and clumsy 2 (1 day)"
  - name: "Stage 5"
    desc: "enfeebled 2, clumsy 2, and [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]] (1 day)"
  - name: "Pack Attack"
    desc: "The trollhound's Strikes deals 1d6 extra damage to creatures within reach of at least two of the trollhound's allies. Trollhound Genesis The first trollhound was the result of a clash between a starving [[srd/pf2e/bestiary/monster-core/beast/warg|warg]] and an enraged [[srd/pf2e/bestiary/monster-core/giant/forest-troll|forest troll]]. Though the warg was no match for the troll, it landed several bites before retreating into the nearby woods. The regenerative chunks of troll flesh within the warg's bleeding maw infected the warg's body, slowly and painfully transforming the beast into a proto-trollhound. Stripped of cunning and intelligence, the altered warg attacked an approaching pack of wargs, spreading the unusual infection. Soon, trollhounds became their own species, and successive generations of the beasts have been discovered hunting alongside trolls, sharing an instinctual bond with the lumbering giants. Many modern-day wargs hold a deep-seated animosity toward trollhounds because of this past. This antagonism is exacerbated by the fact that, in rare cases, a warg who reaches stage 5 of bloodfire fever might transform into a trollhound."
sourcebook: "_Monster Core 2_, page 332."
```

```encounter-table
name: Trollhound
creatures:
  - 1: Trollhound
```
