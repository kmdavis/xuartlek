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
languages: "Common"
skills:
  - name: "Skills"
    desc: "Forest Lore +13, Medicine +15, Nature +17, Stealth +17, Survival +17"
abilityMods: [4, 4, 2, 1, 4, 0]
abilities_top:
  - name: "Expert Subsistence"
    desc: "While using Survival to Subsist, if the hunter rolls any result worse than a success, they get a success. On a success, they can provide subsistence living for themselves and sixteen additional creatures, and on a critical success, they can take care of twice as many creatures as on a success."
  - name: "Forest Walker"
    desc: "The hunter ignores the effects of difficult terrain in a forest environment."
  - name: "Items"
    desc: "_+1 composite longbow_, Dagger, Leather Armor, Shortsword"
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
    desc: "⬻ dagger +17 (Agile, Finesse, versatile S) __Damage__ 1d4+10 piercing"
  - name: "Melee"
    desc: "⬻ shortsword +17 (Agile, Finesse, versatile S) __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ fist +17 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +18 (deadly d10, Magical, Propulsive, range increment 100 feet, reload 0, volley 30 feet) __Damage__ 1d8+8 piercing"
abilities_bot:
  - name: "On the Hunt"
    desc: "⬻ (Concentrate) The hunter designates one creature they're observing or tracking as their prey. The hunter gains a +2 circumstance bonus to Perception checks to Seek the prey and to Survival checks to Track the prey. The first time the hunter hits the designated prey in a round, they deal an additional 1d8 precision damage. These effects last until the hunter uses On the Hunt again."
sourcebook: "_NPC Core_, page 57."
```

```encounter-table
name: Hunter
creatures:
  - 1: Hunter
```
