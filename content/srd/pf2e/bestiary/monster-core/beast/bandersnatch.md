---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bandersnatch"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/tane
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Bandersnatch"
level: 17
source: "Monster Core"
aon_id: "creature-2844"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2844"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Bandersnatch"
level: "Creature 17"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Rare"
trait_03: "Tane"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision, scent (precise) 120 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +30, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +32, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +32, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +28"
abilityMods: [9, 6, 6, -4, 6, 6]
abilities_top:
  - name: "Planar Acclimation"
    desc: "The bandersnatch treats the plane it is on as its home plane."
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +32; __Ref__: +30; __Will__: +27 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 335
health:
  - name: "HP"
    desc: "335 (fast healing 15); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]]"
abilities_mid:
  - name: "Confusing Gaze"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 20 feet. When a creature ends its turn in the aura, it must succeed at a DC 35 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] for 1 round."
  - name: "Quick Recovery"
    desc: "The bandersnatch recovers with frightening speed. At the end of its turn, it reduces the value of one debilitating condition it suffers (with the exception of [[srd/pf2e/compendium/rules-elements/conditions#Dying|dying]] by 1. If it's [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]], [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]], [[srd/pf2e/compendium/rules-elements/conditions#Deafened|deafened]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/conditions#Fleeing|fleeing]], or [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]], it can instead succeed at a DC 16 flat check to end one of these conditions of its choice) it can't use quick recovery on other conditions that lack values."
  - name: "Reactive Strike"
    desc: "⬲ tail only."
speed: "50 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d12+19 piercing"
  - name: "Melee"
    desc: "⬻ claw +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d8+19 slashing"
  - name: "Melee"
    desc: "⬻ tail +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d4+19 piercing plus pain"
  - name: "Ranged"
    desc: "⬻ quill +30 (range increment 100 feet) __Damage__ 3d4+19 piercing plus Pain"
abilities_bot:
  - name: "Focus Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]]) The bandersnatch fixes its gaze at a creature it can see within 20 feet. The target must immediately attempt a Will save against the bandersnatch's Confusing Gaze. After attempting the save, the creature is temporarily immune to a bandersnatch's Confusing Gaze until the start of the bandersnatch's next turn."
  - name: "Frumious Charge"
    desc: "⬺ The bandersnatch Strides, ignoring difficult terrain, then makes two claw Strikes at the end of its movement."
  - name: "Pain"
    desc: "A bandersnatch's quills create exceptionally painful wounds. The wounded creature must succeed at a DC 38 Fortitude save to resist becoming [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] (drained 2 on a critical failure) by this pain. Further bandersnatch Strikes that cause pain increase the amount of drain by 1 for each failed save to a maximum of drained 4."
  - name: "Relentless Tracker"
    desc: "The bandersnatch can [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Track]] while moving at its full speed. Rare Hunters While a bandersnatch can live for thousands of years, a female only becomes fertile once or twice a century. If they are able to find a mate, they will give birth to only one or two kittens per litter. The mother will only protect their young for a year, after which they are left to grow and hunt on their own. Bandersnatches have also been known to hunt their own kind if they roam too near. All of these factors lead to a very small population."
sourcebook: "_Monster Core_, page 36."
```

```encounter-table
name: Bandersnatch
creatures:
  - 1: Bandersnatch
```
