---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Envoy"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Envoy"
level: 0
source: "NPC Core"
aon_id: "creature-3416"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3416"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Envoy"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; (13 to Sense Motive)"
languages: "Common; plus two additional languages"
skills:
  - name: "Skills"
    desc: "Deception +13, Diplomacy +15, Intimidation +7, Society +15"
abilityMods: [0, 1, 0, 4, 3, 3]
abilities_top:
  - name: "Diplomatic Specialist"
    desc: "When dealing with matters of statecraft and negotiation, the envoy is a 6th-level challenge."
  - name: "Items"
    desc: "Dagger, fine clothing, letter of diplomatic status, signet ring"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +2; __Ref__: +3; __Will__: +11"
hp: 12
health:
  - name: "HP"
    desc: "12"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +5 (Agile, Finesse, versatile S) __Damage__ 1d4+2 piercing"
  - name: "Melee"
    desc: "⬻ fist +5 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +5 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+2 piercing"
abilities_bot:
  - name: "Diplomatic Immunity"
    desc: "⬻ (Auditory, Concentrate, Emotion, Linguistic, Mental) The envoy invokes their diplomatic status. Until the end of the envoy's next turn, any creature that attempts to attack them must succeed at a DC 15 Will save or have their attack disrupted. The attacker gains weakness 2 to all damage from the envoy's allies while Diplomatic Immunity lasts, whether their attack was disrupted or not. The envoy can Sustain this ability. If the envoy takes a hostile action, Diplomatic Immunity ends and can't be used again for 1 hour."
sourcebook: "_NPC Core_, page 12."
```

```encounter-table
name: Envoy
creatures:
  - 1: Envoy
```
