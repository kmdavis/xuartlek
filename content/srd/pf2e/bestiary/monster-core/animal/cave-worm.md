---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cave Worm"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Cave Worm"
level: 13
source: "Monster Core"
aon_id: "creature-2871"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2871"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Cave Worm"
level: "Creature 13"
size: "Gargantuan"
trait_01: "Animal"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision, tremorsense (imprecise) 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +30"
abilityMods: [9, -1, 7, -5, -1, -1]
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +28; __Ref__: +21; __Will__: +21"
hp: 270
health:
  - name: "HP"
    desc: "270"
abilities_mid:
  - name: "Inexorable"
    desc: "The cave worm recovers from the [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]], and [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] conditions at the end of its turn. It's also immune to penalties to its Speeds and the [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] condition, and it ignores difficult terrain and greater difficult terrain."
  - name: "Slough Skin"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The cave worm would be affected by a condition or adverse effect (such as [[srd/pf2e/compendium/spells/rank-6/cursed-metamorphosis|_cursed metamorphosis_]])"
  - name: "Effect"
    desc: "The cave worm negates the triggering condition or effect by sloughing an outer layer of its skin. Effects from [[srd/pf2e/compendium/rules-elements/traits/gm-core/artifact|artifacts]], deities, or a similarly powerful source can't be avoided in this way."
speed: "40 feet, burrow 40 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 2d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+15 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ stinger +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d12+15 piercing plus cave worm venom"
  - name: "Melee"
    desc: "⬻ body +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 1d10+13 bludgeoning"
  - name: "Ranged"
    desc: "⬻ regurgitate +26 (Brutal, range increment 60 feet) __Damage__ varies (see ability)"
abilities_bot:
  - name: "Cave Worm Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 32 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "5d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 2]] (1 round)"
  - name: "Stage 2"
    desc: "6d6 poison damage, and enfeebled 2 (1 round)"
  - name: "Stage 3"
    desc: "8d6 poison damage and enfeebled 2 (1 round)"
  - name: "Fast Swallow"
    desc: "⬲"
  - name: "Trigger"
    desc: "The cave worm Grabs a creature"
  - name: "Effect"
    desc: "The worm uses Swallow Whole."
  - name: "Regurgitate"
    desc: "The cave worm can violently regurgitate a creature or boulder it has swallowed to make a ranged Strike. The Strike deals bludgeoning damage depending on the size of the projectile: Tiny deals 2d6+13, Small 3d6+13, Medium 4d6+13, Large 5d6+13, and Huge 6d6+13. A regurgitated creature takes falling damage from the height of the target or from 20 feet, whichever is greater. Boulders occupy space in the worm's stomach as a creature of equivalent size, and cave worms often have several boulders swallowed. A cave worm can use a single action to swallow a new boulder."
  - name: "Rock Tunneler"
    desc: "A cave worm can burrow through solid stone at a Speed of 20 feet. It can leave a tunnel if it desires, and it usually does."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Huge, 3d6+9 bludgeoning, Rupture 24"
  - name: "Thrash"
    desc: "⬺ The worm attempts one Strike against each creature in its reach. It can Strike up to once with its jaws, up to once with its stinger, and any number of times with its body. Each attack counts toward the worm's multiple attack penalty, but the multiple attack penalty doesn't increase until after it makes all the attacks."
sourcebook: "_Monster Core_, page 54."
```

```encounter-table
name: Cave Worm
creatures:
  - 1: Cave Worm
```
