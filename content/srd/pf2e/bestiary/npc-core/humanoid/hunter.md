---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hunter"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Hunter"
level: 7
source: "NPC Core"
aon_id: "creature-3476"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3476"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Hunter"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Forest Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +15, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +17, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +17"
abilityMods: [4, 4, 2, 1, 4, 0]
abilities_top:
  - name: "Expert Subsistence"
    desc: "While using [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Subsist|Subsist]], if the hunter rolls any result worse than a success, they get a success. On a success, they can provide subsistence living for themselves and sixteen additional creatures, and on a critical success, they can take care of twice as many creatures as on a success."
  - name: "Forest Walker"
    desc: "The hunter ignores the effects of difficult terrain in a forest environment."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/weapons/bow/composite-longbow|composite longbow]]_, Dagger, Leather Armor, Shortsword"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +12; __Ref__: +17; __Will__: +15"
hp: 115
health:
  - name: "HP"
    desc: "115"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+10 piercing"
  - name: "Melee"
    desc: "⬻ shortsword +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ fist +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 100 feet, reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/volley|volley 30 feet]]) __Damage__ 1d8+8 piercing"
abilities_bot:
  - name: "On the Hunt"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The hunter designates one creature they're observing or tracking as their prey. The hunter gains a +2 circumstance bonus to Perception checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] the prey and to [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Track]] the prey. The first time the hunter hits the designated prey in a round, they deal an additional 1d8 precision damage. These effects last until the hunter uses On the Hunt again."
sourcebook: "_NPC Core_, page 57."
```

```encounter-table
name: Hunter
creatures:
  - 1: Hunter
```
