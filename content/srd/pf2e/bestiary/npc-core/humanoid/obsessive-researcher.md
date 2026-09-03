---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Obsessive Researcher"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Obsessive Researcher"
level: -1
source: "NPC Core"
aon_id: "creature-3588"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3588"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Obsessive Researcher"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; up to 3 additional uncommon languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Academia Lore]] +19, [[srd/pf2e/compendium/rules-elements/skills/lore|Library Lore]] +23, [[srd/pf2e/compendium/rules-elements/skills/lore|Narrow Lore]] +25, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5"
abilityMods: [0, 1, 2, 5, 0, -1]
abilities_top:
  - name: "Monomania"
    desc: "Each obsessive researcher is preoccupied with a hyper-specialized, niche body of knowledge (their Narrow Lore) in which they are the acknowledged world authority. The catch is that when such an expert goes wrong, they go badly wrong— if an obsessive researcher gets a success on a [[srd/pf2e/compendium/rules-elements/skills/lore|Narrow Lore]] roll, they get a critical success instead. But if they roll a failure, then they get a critical failure instead."
  - name: "World-Class Authority"
    desc: "In their narrow field of interest, the obsessive researcher is a 10th-level challenge."
  - name: "Items"
    desc: "Writing Set, entirely too many books"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +3; __Ref__: +2; __Will__: +7"
hp: 7
health:
  - name: "HP"
    desc: "7 __Idée Fixe__ Nothing gets between the obsessive researcher and their subject. If the obsessive researcher is targeted by a spell or ability with a Will save that would prompt them to give up, ignore, or divert course from the subject of their [[srd/pf2e/compendium/rules-elements/skills/lore|Narrow Lore]] (for example, using a suggestion to get a specialist in Jistkan artificing to give up a construct part), then the obsessive researcher can use their Narrow Lore skill in place of their Will save."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4 bludgeoning"
  - name: "Melee"
    desc: "⬻ pen +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d4 piercing"
abilities_bot:
  - name: "Furious Harangue"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The researcher starts hectoring an enemy within 30 feet, upbraiding them for daring to interrupt such valuable research. The target must attempt a DC 15 Will save. On a failure, they are [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 2]] (frightened 3 and [[srd/pf2e/compendium/rules-elements/conditions#Fleeing|fleeing]] for 1 round on a critical failure). Regardless of the result of its save, the target is temporarily immune for 1 hour."
sourcebook: "_NPC Core_, page 138."
```

```encounter-table
name: Obsessive Researcher
creatures:
  - 1: Obsessive Researcher
```
