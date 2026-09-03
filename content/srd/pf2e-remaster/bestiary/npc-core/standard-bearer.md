---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Standard Bearer"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Standard Bearer"
level: 4
source: "NPC Core"
aon_id: "creature-3524"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3524"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Standard Bearer"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Diplomacy +11, Medicine +10, Society +8, Warfare Lore +10"
abilityMods: [2, 2, 2, 0, 2, 3]
abilities_top:
  - name: "Items"
    desc: "battle standard (attached to ranseur), Chain Shirt, Healer's Tools, Ranseur, Shortsword"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +10; __Ref__: +8; __Will__: +14"
hp: 60
health:
  - name: "HP"
    desc: "60"
abilities_mid:
  - name: "Inspiring Aura"
    desc: "(aura, emotion, mental, visual) 60 feet. The standard bearer and each ally in the aura who can see their battle standard gains a +1 status bonus to initiative rolls and saves against fear effects. Each time an affected creature gains the frightened condition, reduce the frightened value by 1."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ranseur +12 (Disarm, reach 10 feet) __Damage__ 1d10+8 piercing"
  - name: "Melee"
    desc: "⬻ shortsword+12 (Agile, versatile S) __Damage__ 1d6+8 piercing"
  - name: "Melee"
    desc: "⬻ fist+12 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+8 bludgeoning __Signal the Advance!__ ⬺ (Mental, Visual) The standard bearer raises their flag to the sky, signaling their allies to charge. Each ally affected by inspiring aura can use a reaction to Stand, Step, or Stride. __Stay in the Fight!__ ⬺ (Auditory, Mental) The standard bearer shouts an inspiring cry. Each ally affected by inspiring aura gains 10 temporary Hit Points that last for 1 minute. The Standard's Significance To be a standard bearer is no easy task. On the battlefield, they serve as the premier representative of the organization they serve, and should their standard be captured or destroyed, it would result in a huge loss of morale. If a standard bearer returns to their company alive and without their battle standard, harsh punishments will soon follow. Outside of battle, standard bearers often make great efforts to befriend the rest of their platoon, as they're the soldier who will need the most protection once combat begins."
sourcebook: "_NPC Core_, page 89."
```

```encounter-table
name: Standard Bearer
creatures:
  - 1: Standard Bearer
```
