---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sedacthy Marauder"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/sedacthy
  - pf2e/creature/trait/medium
statblock: inline
name: "Sedacthy Marauder"
level: 4
source: "Monster Core"
aon_id: "creature-3179"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3179"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sedacthy Marauder"
level: "Creature 4"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Humanoid"
trait_03: "Sedacthy"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, wavesense 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]; sea speech"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +9"
abilityMods: [6, 3, 4, 0, 1, 3]
abilities_top:
  - name: "Sea Speech"
    desc: "A sedacthy speaking [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]] can be understood by any [[srd/pf2e/compendium/rules-elements/traits/player-core/animal|animal]] that has a swim Speed or the [[srd/pf2e/compendium/rules-elements/traits/player-core/amphibious|amphibious]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/aquatic|aquatic]] trait. By spending a week regularly interacting with such an animal, the sedacthy can make it permanently [[srd/pf2e/compendium/rules-elements/conditions#Helpful|helpful]]."
  - name: "Items"
    desc: "Breastplate, Spear (2)"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +14; __Ref__: +9; __Will__: +9"
hp: 75
health:
  - name: "HP"
    desc: "75"
abilities_mid:
  - name: "Vengeful Throw"
    desc: "⬲"
  - name: "Trigger"
    desc: "The marauder takes damage from a creature 20 feet or further away"
  - name: "Effect"
    desc: "The marauder makes a ranged spear Strike against the triggering creature. This attack doesn't take a range increment penalty if the target is within the second range increment."
speed: "20 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spear +14 __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ jaws +14 __Damage__ 1d4+8 piercing plus 1d4 persistent bleed"
  - name: "Melee"
    desc: "⬻ claw +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d4+8 slashing"
  - name: "Ranged"
    desc: "⬻ spear +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d6+10 piercing"
abilities_bot:
  - name: "Challenging Shriek"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The marauder unleashes a terrifying battle cry. Each enemy in a 30-foot emanation must attempt a DC 21 Will save. Regardless of the results, creatures are temporarily immune for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 1]]."
  - name: "Failure"
    desc: "The creature is frightened 2."
  - name: "Critical Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] for 1 round and frightened 3."
  - name: "Shared Feast"
    desc: "⬺ The sedacthy makes a jaws Strike. If it hits, an ally of their choice can spend a reaction to make a jaws Strike against the same target. Allies with beaks or similar attacks can use those instead of jaws."
sourcebook: "_Monster Core_, page 300."
```

```encounter-table
name: Sedacthy Marauder
creatures:
  - 1: Sedacthy Marauder
```
