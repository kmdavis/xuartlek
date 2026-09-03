---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Manticore"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/large
statblock: inline
name: "Manticore"
level: 6
source: "Monster Core"
aon_id: "creature-3093"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3093"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Manticore"
level: "Creature 6"
size: "Large"
trait_01: "Beast"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +12"
abilityMods: [5, 2, 4, -2, 2, -1]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +16; __Ref__: +12; __Will__: +12"
hp: 90
health:
  - name: "HP"
    desc: "90"
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +17 __Damage__ 2d8+8 piercing"
  - name: "Melee"
    desc: "⬻ claw +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+8 slashing"
  - name: "Ranged"
    desc: "⬻ spike +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 40 feet) __Damage__ 1d10+5 piercing"
  - name: "Melee"
    desc: "⬻ stinger +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d8+8 piercing plus manticore venom"
abilities_bot:
  - name: "Spike Volley"
    desc: "⬻ The manticore flings up to two spikes from its tail, targeting either two different creatures or a single creature. If the manticore targets two different creatures, these creatures must be within 20 feet of one another, and the manticore makes a separate Strike against each; this counts as only one Strike for the manticore's multiple attack penalty, and the penalty doesn't increase until after both attacks. If the manticore flings both spikes at the same creature, it makes a single Strike. If the attack hits, it deals the damage of a single spike, but the target is pinned in place, rendering it [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]]. A creature can get free if it [[srd/pf2e/compendium/rules-elements/actions/player-core#Force Open|Forces Open]] the spike or [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]]; either option is DC 23. A manticore can hurl no more than 12 spikes in 24 hours. Scorpion Tails A common variety of manticore has a scorpion-like stinger at the end of its tail instead of quills. Remove Spike Volley and replace their ranged Strike with the following."
  - name: "Manticore Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]])"
  - name: "Saving Throw"
    desc: "DC 22 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d10 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round)"
  - name: "Stage 2"
    desc: "2d10 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 3"
    desc: "2d10 poison damage and enfeebled 2 (1 round)"
sourcebook: "_Monster Core_, page 228."
```

```encounter-table
name: Manticore
creatures:
  - 1: Manticore
```
