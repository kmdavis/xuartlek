---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Jinx Eater"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tengu
  - pf2e/creature/trait/medium
statblock: inline
name: "Jinx Eater"
level: 4
source: "NPC Core"
aon_id: "creature-3671"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3671"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Jinx Eater"
level: "Creature 4"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Tengu"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision"
languages: "Common, Tengu; plus two others"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +9, Deception +12, Intimidation +12, Occultism +10, Sailing Lore +12"
abilityMods: [2, 4, 1, 1, 1, 2]
abilities_top:
  - name: "Items"
    desc: "bottle, Leather Armor, Tengu Gale Blade"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +8; __Ref__: +14; __Will__: +11"
hp: 65
health:
  - name: "HP"
    desc: "65"
abilities_mid:
  - name: "Eat Fortune"
    desc: "⬲ (concentrate, divine)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "A creature within 60 feet uses a fortune or misfortune effect"
  - name: "Effect"
    desc: "The tengu negates the attempt to manipulate fate and fortune. Eat Fortune gains the opposing trait, and the triggering effect is disrupted."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tengu gale blade +13 (Agile, Disarm, Finesse) __Damage__ 1d6+4 slashing"
  - name: "Melee"
    desc: "⬻ beak +13 (Finesse) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Jinxed Call"
    desc: "⬺ (Auditory, Occult) The jinx eater gives an eerie croak. Each non-tengu in a 30-foot emanation must succeed at a DC 21 Will save or be clumsy 1 for 1 round (or 1 minute on a critical failure). Regardless of the results, each creature is then temporarily immune to Jinxed Call for 1 minute."
  - name: "Sneak Attack"
    desc: "The jinx eater deals 1d6 extra precision damage to off-guard creatures."
sourcebook: "_NPC Core_, page 212."
```

```encounter-table
name: Jinx Eater
creatures:
  - 1: Jinx Eater
```
