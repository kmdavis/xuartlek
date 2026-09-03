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
    desc: "Perception +9; (18 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]]) low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Ysoki|Ysoki]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +17, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] +16, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +15, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +16, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +10"
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
    desc: "⬻ longspear +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|Reach]]) __Damage__ 1d8+5 piercing"
  - name: "Melee"
    desc: "⬻ jaws +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d4+5 piercing"
  - name: "Ranged"
    desc: "⬻ alchemical bomb +10 (range increment 20 feet, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|Splash]]) __Damage__ 1d6 persistent acid plus 1 acid [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage"
  - name: "Ranged"
    desc: "⬻ crossbow +10 (range increment 120 feet, reload 1) __Damage__ 1d8+3 piercing"
abilities_bot:
  - name: "Advise Swarm"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The swarm voice issues orders to move. Each ratfolk from the same warren in a 15-foot emanation can spend a reaction to Step, Stride, or [[srd/pf2e/compendium/rules-elements/actions/player-core#Take Cover|Take Cover]]."
  - name: "Chittering Terror"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The swarm voice chitters, creating a terrifying din, and encourages their allies to join in. Each enemy within 30 feet must succeed at a DC 19 Will save or be [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 1]] (or frightened 2 on a critical failure). An enemy takes a –2 circumstance penalty to its save if it's adjacent to one or more [[srd/pf2e/compendium/rules-elements/traits/player-core-2/ratfolk|ratfolk]] allied with the swarm voice. Regardless of the result of a creature's save, it's then temporarily immune for 1 hour."
  - name: "Swarming"
    desc: "A ysoki can end their movement in the same square as an ally that also has this ability. Only two such creatures can share the same space."
sourcebook: "_NPC Core_, page 210."
```

```encounter-table
name: Swarm Voice
creatures:
  - 1: Swarm Voice
```
