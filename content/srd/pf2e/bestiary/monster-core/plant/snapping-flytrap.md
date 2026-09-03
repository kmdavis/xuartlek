---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Snapping Flytrap"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/large
statblock: inline
name: "Snapping Flytrap"
level: 3
source: "Monster Core"
aon_id: "creature-2999"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2999"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Snapping Flytrap"
level: "Creature 3"
size: "Large"
trait_01: "Mindless"
trait_02: "Plant"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; tremorsense (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10"
abilityMods: [2, 3, 5, -5, 2, -2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +12; __Ref__: +8; __Will__: +7"
hp: 50
health:
  - name: "HP"
    desc: "50; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 5; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 5"
abilities_mid:
  - name: "Quick Capture"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature hits or touches the flytrap"
  - name: "Effect"
    desc: "The flytrap makes a leaf Strike against the triggering creature. If it hits, the creature is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] in that leaf."
speed: "15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ leaf +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d8+2 piercing plus 1d6 acid and Improved Grab"
abilities_bot:
  - name: "Focused Assault"
    desc: "⬺ The flytrap attacks a single target with both its two leaves. The flytrap makes one leaf Strike. On a success, the flytrap deals the damage from one leaf Strike plus an additional 1d8 damage for every leaf beyond the first. On a failure, the flytrap deals the damage from one leaf Strike, but it can't use Improved Grab. It deals no damage on a critical failure. This counts toward the flytrap's multiple attack penalty as a number of attacks equal to the number of leaves the flytrap has."
  - name: "Hungry Flurry"
    desc: "⬺ The flytrap makes two leaf Strikes at a –2 penalty, each against a different target. These attacks count toward the flytrap's multiple attack penalty, but the multiple attack penalty doesn't increase until after it makes all its attacks."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Medium, 1d8+1 bludgeoning plus 1d6 acid, Rupture 5"
sourcebook: "_Monster Core_, page 154."
```

```encounter-table
name: Snapping Flytrap
creatures:
  - 1: Snapping Flytrap
```
