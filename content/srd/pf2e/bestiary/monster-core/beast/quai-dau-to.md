---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Quai Dau To"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/huge
statblock: inline
name: "Quai Dau To"
level: 13
source: "Monster Core"
aon_id: "creature-3158"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3158"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Quai Dau To"
level: "Creature 13"
size: "Huge"
trait_01: "Beast"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, mist vision, scent (imprecise) 120 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +25, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +24"
abilityMods: [8, 4, 8, -3, 5, -1]
abilities_top:
  - name: "Mist Vision"
    desc: "The quai dau to ignores the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from mist and fog."
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +26; __Ref__: +19; __Will__: +21"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]], [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]] 15"
abilities_mid:
  - name: "Frightful Sight"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 60 feet. This aura functions as a DC 32 frightful presence aura, but a creature doesn't attempt its save until it sees the quai dau to."
  - name: "Reflective Scales"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 30 feet casts a spell with the [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]] trait or uses an ability with the light trait"
  - name: "Effect"
    desc: "The quai dau to adjusts its position to reflect the light off their scales in a blinding display. All creatures in a 30-foot emanation must succeed at a DC 33 Fortitude saving throw or become [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] for 1 round."
speed: "40 feet, swim 30 feet; Inflate"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d12+14 piercing"
  - name: "Melee"
    desc: "⬻ tail +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d8+14 bludgeoning"
  - name: "Melee"
    desc: "⬻ foot +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 3d8+14 bludgeoning"
abilities_bot:
  - name: "Drain Water"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The quai dau to is within 10 feet of a body of water that's at least 10 feet deep and their water sac is empty"
  - name: "Effect"
    desc: "The quai dau to sucks water through their trunk to fill their water sac, lowering the level in the body of water by 10 feet. All creatures in the water within a 30-foot emanation are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] until the start of the quai dau to's next turn."
  - name: "Inflate"
    desc: "⬻ The quai dau to inflates their body. They become Gargantuan, gain a fly Speed of 30 feet until the end of their next turn, and then [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]]. They deflate if they fall [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] or Dismiss this effect."
  - name: "Mist Breath"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|Water]])"
  - name: "Requirements"
    desc: "The quai dau to's water sac is full"
  - name: "Effect"
    desc: "The quai dau to empties their water sac to breathe out mist in a 10-foot emanation. All creatures within the mist become [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]], and all creatures outside the mist become concealed to creatures within it. The mist dissipates after 1 round."
  - name: "Spout Water"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|Water]])"
  - name: "Requirements"
    desc: "The quai dau to's water sac is full"
  - name: "Effect"
    desc: "The quai dau to empties its water sac to blast water from its trunk, dealing 9d10 bludgeoning damage to all creatures in a 90-foot line, with a DC 33 basic Reflex save. A creature that fails is pushed 10 feet (or 20 feet on a critical failure). Impossible Flight Despite the laws of the natural world, this large headed creature can fly. The quai dau to achieves this incredible feat by inflating itself, allowing it to seemingly swim through the air like water. While inflated in this way, the quai dau to somewhat resembles a pufferfish."
sourcebook: "_Monster Core_, page 284."
```

```encounter-table
name: Quai Dau To
creatures:
  - 1: Quai Dau To
```
