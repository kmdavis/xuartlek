---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Globster"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/large
statblock: inline
name: "Globster"
level: 5
source: "Monster Core"
aon_id: "creature-3019"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3019"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Globster"
level: "Creature 5"
size: "Large"
trait_01: "Aquatic"
trait_02: "Ooze"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15"
abilityMods: [6, -5, 5, -5, 0, -5]
ac: 12
armorclass:
  - name: "AC"
    desc: "12; __Fort__: +16; __Ref__: +6; __Will__: +9"
hp: 170
health:
  - name: "HP"
    desc: "170; __Immunities__ critical hits, [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 10"
abilities_mid:
  - name: "Stench"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]]) 30 feet, DC 19."
speed: "15 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +15 __Damage__ 2d8+6 bludgeoning plus Grab and nauseating slap"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d8+6, DC 22"
  - name: "Nauseating Slap"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) A living creature struck by a globster's tendril must attempt a DC 19 Fortitude save. On a failure, the creature becomes [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]]. If the creature is already sickened, the condition value increases by 1, to a maximum of sickened 4. Once a creature succeeds at its saving throw, it is temporarily immune for 24 hours."
  - name: "Saturated"
    desc: "A globster can survive for 1 hour out of the water, after which it risks suffocation. Fetid Decomposition When a globster is killed, its body decays into a mass of goo within 24 hours. However, its stench aura can persist long past its destruction, lasting for 1d10 days, centered on the globster’s position at the time of its death."
sourcebook: "_Monster Core_, page 171."
```

```encounter-table
name: Globster
creatures:
  - 1: Globster
```
