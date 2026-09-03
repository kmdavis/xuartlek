---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kuribu"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/angel
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/small
statblock: inline
name: "Kuribu"
level: 3
source: "Monster Core 2"
aon_id: "creature-4028"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4028"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Kuribu"
level: "Creature 3"
size: "Small"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9"
abilityMods: [2, 4, 1, 0, 2, 1]
abilities_top:
  - name: "Items"
    desc: "Composite Shortbow (20 arrows)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +11; __Will__: +9"
hp: 45
health:
  - name: "HP"
    desc: "45; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] 5"
abilities_mid:
  - name: "Sentinel's Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) 30 feet. The kuribu and any other creature in the aura defending the same holy site gain a +1 status bonus to AC. This aura is suppressed while Statue is in effect."
  - name: "Immobilizing Ambush"
    desc: "⬲"
  - name: "Requirements"
    desc: "The kuribu is disguised as a statue"
  - name: "Trigger"
    desc: "A creature moves within 60 feet of the kuribu"
  - name: "Effect"
    desc: "The kuribu springs into action by making a shortbow Strike against the triggering creature. If the Strike hits, the creature is pinned by the arrow, as described in the bow critical specialization."
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ composite shortbow +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 60 feet, reload 0) __Damage__ 1d6+5 piercing"
abilities_bot:
  - name: "Blessed Aspect"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) The kuribu's face transforms and their holy countenance unleashes an attack based on the aspect the kuribu chooses. The kuribu can't use Blessed Aspect again for 1d4 rounds. They can revert back to their humanoid appearance at any time but they still have to wait before using Blessed Aspect again."
  - name: "Eagle"
    desc: "The kuribu unleashes a disorienting screech in a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] that deals 2d10 sonic damage with a DC 19 basic Will save. A creature that critically fails is also [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]]."
  - name: "Lion"
    desc: "The kuribu makes a powerful jaws Strike against an adjacent creature. The attack has a +12 attack modifier and deals 4d6 piercing damage plus 1d4 persistent bleed damage."
  - name: "Ox"
    desc: "The kuribu charges into a creature. The kuribu [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] or Strides. At the end of their movement dealing 4d6 bludgeoning damage to it with a DC 17 basic Fortitude save. If the target critically fails, it is also knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
  - name: "Statue"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) Until the next time they act, the kuribu appears to be a statue. They have an automatic result of 29 on [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks and DCs to pass as a statue. Holy Countenances Kuribus can partially take on the appearance of powerful animals and tap into those creatures' abilities in combat. Though most kuribus manifest the animals featured here, some instead tap into the abilities of other creatures like elephants or wolves. Some divine accounts speak of ancient kuribus who can transform entirely into these creatures and remain vigilant for decades in the guise of animal statues."
sourcebook: "_Monster Core 2_, page 26."
```

```encounter-table
name: Kuribu
creatures:
  - 1: Kuribu
```
