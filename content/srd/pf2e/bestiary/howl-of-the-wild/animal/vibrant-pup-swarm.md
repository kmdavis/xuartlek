---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vibrant Pup Swarm"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/huge
statblock: inline
name: "Vibrant Pup Swarm"
level: 11
source: "Howl of the Wild"
aon_id: "creature-3321"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3321"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Vibrant Pup Swarm"
level: "Creature 11"
size: "Huge"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; tremorsense (precise) 60 feet"
skills:
  - name: "Skills"
    desc: "Athletics +16"
abilityMods: [-2, 7, 5, -5, 5, -4]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +24; __Ref__: +21; __Will__: +18"
hp: 140
health:
  - name: "HP"
    desc: "140; __Immunities__ precision, swarm mind; __Resistances__ bludgeoning 5, piercing 10, slashing 10; __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "Reflective Skin"
    desc: "(aura, light, visual) 10 feet. Other creatures in the aura are dazzled. The aura automatically activates when the swarm is in bright light and deactivates in dim light or darkness."
  - name: "Feel No Pain"
    desc: "⬲"
  - name: "Trigger"
    desc: "The vibrant pup swarm is critically hit by a Strike"
  - name: "Effect"
    desc: "The worker pups become insensitive to pain and leap to the front. The swarm gains 10 temporary Hit Points that last for 1 round."
speed: "30 feet, burrow 30"
abilities_bot:
  - name: "Swarming Bites"
    desc: "⬻ Each enemy in the swarm's space takes 2d6 piercing damage (DC 30 basic Reflex save)."
  - name: "Focused Reflection"
    desc: "⬺ (Fire, Light)"
  - name: "Requirements"
    desc: "The vibrant pup swarm is in bright light"
  - name: "Effect"
    desc: "The swarm simultaneously turns to focus the light in an arcing beam, dealing 6d12 fire damage to all creatures in a 30-foot cone (DC 30 basic Reflex save). A creature that fails its save is also blinded for 1 round (or 1 minute on a critical failure). The swarm can't use Focused Reflection again for 1d4 rounds."
sourcebook: "_Howl of the Wild_, page 192."
```

```encounter-table
name: Vibrant Pup Swarm
creatures:
  - 1: Vibrant Pup Swarm
```
