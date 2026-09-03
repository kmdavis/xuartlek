---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Leaf Leshy"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/leshy
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/small
statblock: inline
name: "Leaf Leshy"
level: 0
source: "Monster Core"
aon_id: "creature-3079"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3079"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Leaf Leshy"
level: "Creature 0"
size: "Small"
trait_01: "Leshy"
trait_02: "Plant"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; low-light vision"
languages: "Common, Fey; _speak with plants_ (trees only)"
skills:
  - name: "Skills"
    desc: "Acrobatics +4, Nature +4, Stealth +4"
abilityMods: [-1, 2, 2, -2, 2, 1]
abilities_top:
  - name: "Items"
    desc: "Longspear"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +6; __Will__: +4"
hp: 15
health:
  - name: "HP"
    desc: "15 (Weaknesses fire 2)"
abilities_mid:
  - name: "Verdant Burst"
    desc: "(healing, primal, vitality) When a leaf leshy dies, a burst of primal energy explodes from their body, restoring 1d4 Hit Points to each plant creature in a 30-foot emanation. This area is filled with tree saplings, becoming difficult terrain. If the terrain is not a viable environment for these trees, they wither after 24 hours."
speed: "25 feet; Glide"
attacks:
  - name: "Melee"
    desc: "⬻ longspear +3 (reach 10 feet) __Damage__ 1d8–1 piercing"
  - name: "Ranged"
    desc: "⬻ seedpod +6 (range increment 30 feet) __Damage__ 1d6 bludgeoning plus deafening blow"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Polymorph, Primal) The leaf leshy transforms into a Small tree. This ability otherwise uses the effects of _one with plants_."
  - name: "Deafening Blow"
    desc: "When a leaf leshy hits with their seedpod Strike, the pod explodes loudly. The target must attempt a DC 16 Fortitude save."
  - name: "Critical Success"
    desc: "The target is unaffected and temporarily immune for 24 hours."
  - name: "Success"
    desc: "The target is unaffected."
  - name: "Failure"
    desc: "The target is deafened for 1 round."
  - name: "Critical Failure"
    desc: "The target is deafened for 1 minute."
  - name: "Glide"
    desc: "⬻ (Move) The leshy glides gently through the air, moving 5 feet toward the ground and up to 25 feet forward. As long as the leshy spends at least 1 action gliding each round, they remain in the air at the end of each turn. For the purpose of determining damage from falls, a leaf leshy always treats falls as if they were 20 feet shorter."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 14 - __Constant (3rd)__ Speak with Plants (trees only)"
sourcebook: "_Monster Core_, page 216."
```

```encounter-table
name: Leaf Leshy
creatures:
  - 1: Leaf Leshy
```
