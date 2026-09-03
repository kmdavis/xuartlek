---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mercurial"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/medium
statblock: inline
name: "Mercurial"
level: 2
source: "Rage of Elements"
aon_id: "creature-2645"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2645"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Mercurial"
level: "Creature 2"
size: "Medium"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Talican|Talican]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +8, Plane of Metal Lore +8"
abilityMods: [3, 4, 3, 2, 2, 4]
abilities_top:
  - name: "Items"
    desc: "shuriken (5)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +11; __Will__: +8"
hp: 30
health:
  - name: "HP"
    desc: "30; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d10+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ shuriken +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], range increment 20 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|Thrown]]) __Damage__ 1d6+3 piercing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The mercurial takes on the appearance of any Small or Medium humanoid. This transformation allows for significant detail and can reproduce the features of a specific individual, but the mercurial retains a shiny, liquid-metal appearance that renders the transformation unsuitable as a disguise unless they're impersonating another mercurial. It doesn't change the mercurial's Speed or the attack and damage bonuses of their Strikes, but it does allow them to transform their limbs into metal tools or melee weapons, potentially changing the damage type dealt by their Strikes."
  - name: "Metallurgic Adaptation"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The mercurial transmutes their liquid metal body into cold iron, copper, gold, iron, silver, or steel. Their unarmed melee Strikes are made of that material until they use Metallurgic Adaptation again. Many Faces, Many Names As immortal beings with comparatively short attention spans, mercurials invariably become bored with their current identities sooner or later and seek a change by adopting a new face and persona. To avoid confusion among friends and acquaintances, a mercurial's name typically consists not only of their current moniker, but a list of the last few names used, presented in chronological order as far back as the mercurial can remember."
sourcebook: "_Rage of Elements_, page 153."
```

```encounter-table
name: Mercurial
creatures:
  - 1: Mercurial
```
