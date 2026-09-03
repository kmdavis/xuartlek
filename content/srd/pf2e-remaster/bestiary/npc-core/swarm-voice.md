---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Swarm Voice"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/ratfolk
  - pf2e/creature/trait/small
statblock: inline
name: "Swarm Voice"
level: 3
source: "NPC Core"
aon_id: "creature-3668"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3668"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Swarm Voice"
level: "Creature 3"
size: "Small"
trait_01: "Humanoid"
trait_02: "Ratfolk"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; (18 to Sense Motive) low-light vision"
languages: "Common, Ysoki"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +9, Diplomacy +17, Intimidation +15, Legal Lore +16, Performance +15, Society +16, Survival +10"
abilityMods: [2, 1, 0, 3, 3, 4]
abilities_top:
  - name: "Voice of the Swarm"
    desc: "For encounters involving negotiation or diplomacy, the swarm voice is a 7th-level challenge."
  - name: "Items"
    desc: "lesser acid flask (4), Crossbow (20 bolts), Longspear"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +8; __Will__: +11"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "25 feet; swarming"
attacks:
  - name: "Melee"
    desc: "⬻ longspear +11 (Reach) __Damage__ 1d8+5 piercing"
  - name: "Melee"
    desc: "⬻ jaws +11 (Agile) __Damage__ 1d4+5 piercing"
  - name: "Ranged"
    desc: "⬻ alchemical bomb +10 (range increment 20 feet, Splash) __Damage__ 1d6 persistent acid plus 1 acid splash damage"
  - name: "Ranged"
    desc: "⬻ crossbow +10 (range increment 120 feet, reload 1) __Damage__ 1d8+3 piercing"
abilities_bot:
  - name: "Advise Swarm"
    desc: "⬺ (Auditory, Linguistic, Mental) The swarm voice issues orders to move. Each ratfolk from the same warren in a 15-foot emanation can spend a reaction to Step, Stride, or Take Cover."
  - name: "Chittering Terror"
    desc: "⬺ (Auditory, Emotion, Fear, Mental) The swarm voice chitters, creating a terrifying din, and encourages their allies to join in. Each enemy within 30 feet must succeed at a DC 19 Will save or be frightened 1 (or frightened 2 on a critical failure). An enemy takes a –2 circumstance penalty to its save if it's adjacent to one or more ratfolk allied with the swarm voice. Regardless of the result of a creature's save, it's then temporarily immune for 1 hour."
  - name: "Swarming"
    desc: "A ysoki can end their movement in the same square as an ally that also has this ability. Only two such creatures can share the same space."
sourcebook: "_NPC Core_, page 210."
```

```encounter-table
name: Swarm Voice
creatures:
  - 1: Swarm Voice
```
