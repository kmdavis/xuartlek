---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fungus Leshy"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/fungus
  - pf2e/creature/trait/leshy
  - pf2e/creature/trait/small
statblock: inline
name: "Fungus Leshy"
level: 2
source: "Monster Core"
aon_id: "creature-3081"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3081"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Fungus Leshy"
level: "Creature 2"
size: "Small"
trait_01: "Fungus"
trait_02: "Leshy"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|_speak with plants_]] (fungi only)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [2, 4, 2, -1, 2, 0]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +8; __Ref__: +10; __Will__: +6"
hp: 30
health:
  - name: "HP"
    desc: "30"
abilities_mid:
  - name: "Verdant Burst"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]) When a fungus leshy dies, a burst of primal energy explodes from their body, restoring 2d8 Hit Points to each [[srd/pf2e/compendium/rules-elements/traits/player-core/fungus|fungus]] creature in a 30-foot emanation. This area is filled with fungi, becoming difficult terrain. If the terrain is not a viable environment for these plants, they wither after 24 hours."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ spore pod +10 (range increment 30 feet) __Damage__ 1d6+2 bludgeoning plus spores"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The fungus leshy transforms into a Small giant mushroom or patch of fungi. This ability otherwise uses the effects of [[srd/pf2e/compendium/spells/rank-2/one-with-plants|_one with plants_]]."
  - name: "Spore Cloud"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) A fungus leshy can unleash a cloud of spores that irritates the eyes and throats of non-fungus creatures in a 15-foot emanation. Each creature must succeed at a DC 16 Fortitude save or take 1 persistent poison damage. A creature has its vision reduced as long as the persistent damage continues and can see only within 20 feet."
  - name: "Spores"
    desc: "A creature that takes damage from a fungus leshy's spore pod Strike must attempt a saving throw with the same DC and effect as its Spore Cloud ability."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16 - __Constant (3rd)__ [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|Speak with Plants]] (fungi only)"
sourcebook: "_Monster Core_, page 217."
```

```encounter-table
name: Fungus Leshy
creatures:
  - 1: Fungus Leshy
```
