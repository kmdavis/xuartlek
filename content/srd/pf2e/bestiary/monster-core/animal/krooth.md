---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Krooth"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Krooth"
level: 8
source: "Monster Core"
aon_id: "creature-3076"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3076"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Krooth"
level: "Creature 8"
size: "Large"
trait_01: "Amphibious"
trait_02: "Animal"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; low-light vision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +17"
abilityMods: [6, 3, 6, -4, 2, 0]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +20; __Ref__: +17; __Will__: +14"
hp: 150
health:
  - name: "HP"
    desc: "150"
abilities_mid:
  - name: "Pain Frenzy"
    desc: "Whenever the krooth is damaged by a critical hit, it gains a +2 status bonus to attack and damage rolls until the end of its next turn. It can't use reactions while this frenzy lasts."
  - name: "Reactive Strike"
    desc: "⬲ Tail only."
speed: "40 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d12+9 piercing plus Poison Tooth"
  - name: "Melee"
    desc: "⬻ claw +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d8+9 slashing"
  - name: "Melee"
    desc: "⬻ tail +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+9 piercing"
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "⬻"
  - name: "Poison Tooth"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Requirements"
    desc: "The krooth damaged a creature with its jaws on its most recent action this turn"
  - name: "Effect"
    desc: "The krooth snaps off one of its teeth in the creature it hit. The creature takes 1d6 persistent bleed damage and is [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]]. Neither can be healed while the tooth remains. Removing the tooth safely requires a successful DC 26 check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Administer First Aid|Administer First Aid]]. Instead of ending bleeding or stabilizing, this removes the tooth and the drained condition, but it doesn't automatically end the bleed damage. Krooth Guts In addition to naturalists, the strange enzymes and other chemicals found in the internal organs of male krooths, particularly the liver, pancreas, and kidneys, are of great value to alchemists who seek to concoct elixirs and potions with transmutation effects. A single male krooth's organs, properly harvested and preserved, can be sold to an interested alchemist or naturalist for as much as 80 gp."
sourcebook: "_Monster Core_, page 213."
```

```encounter-table
name: Krooth
creatures:
  - 1: Krooth
```
