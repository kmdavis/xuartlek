---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cinder Rat"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/small
statblock: inline
name: "Cinder Rat"
level: 3
source: "Monster Core"
aon_id: "creature-2981"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2981"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Cinder Rat"
level: "Creature 3"
size: "Small"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, smoke vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +9"
abilityMods: [2, 3, 2, -4, 2, 0]
abilities_top:
  - name: "Smoke Vision"
    desc: "The cinder rat ignores the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from smoke."
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +12; __Will__: +6"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]] 5"
abilities_mid:
  - name: "Fetid Fumes"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]) 5 feet. A creature that enters the aura or begins its turn there must succeed at a DC 22 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]]. Everything within the aura, including the cinder rat, is [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] by smoke."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d8+4 fire plus 1d4 persistent fire"
sourcebook: "_Monster Core_, page 144."
```

```encounter-table
name: Cinder Rat
creatures:
  - 1: Cinder Rat
```
