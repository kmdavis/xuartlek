---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Arboreal Archive"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Arboreal Archive"
level: 12
source: "Monster Core 2"
aon_id: "creature-4063"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4063"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Arboreal Archive"
level: "Creature 12"
size: "Large"
trait_01: "Plant"
trait_02: "Wood"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; low-light vision, tremorsense (imprecise) 60 feet"
languages: "Arboreal, [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|_speak with plants_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +22, [[srd/pf2e/compendium/rules-elements/skills/lore|Forest Lore]] +28, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +25, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +19"
abilityMods: [7, -1, 5, 4, 7, 4]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +23; __Ref__: +17; __Will__: +27"
hp: 230
health:
  - name: "HP"
    desc: "230; __Resistances__ bludgeoning 10, piercing 10; __Weaknesses__ axes 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 15"
abilities_mid:
  - name: "Abeyance Rift"
    desc: "If an arboreal archive dies unexpectedly before passing on their knowledge in a succession ritual, the amassed lore within their roots and boughs explodes out in a shock wave that deals 8d10 mental damage to creatures within 30 feet (DC 32 basic Will save) before dissipating; those who fail also fall [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ branch +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+10 bludgeoning plus Improved Knockdown"
abilities_bot:
  - name: "Memory Maelstrom"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The arboreal archive tries to overwhelm foes with a surge of information they've absorbed over their long life. This surge deals 5d6 mental damage to each enemy within 40 feet, who must attempt a DC 32 Will save."
  - name: "Critical Success"
    desc: "The creature maintains its composure, takes no damage, and is temporarily immune to Memory Maelstrom for 1 minute."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]] and takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and is stunned 3."
  - name: "Critical Failure"
    desc: "The creature takes double damage, is [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] for 2d4 rounds, and is stunned 3. Painting Memories As with all arboreals, no two arboreal archives are identical in appearance. The uniquely patterned bark of arboreal archives makes them even more distinct from one another, painting a mysterious and unique record of their knowledge of Forest Lore. Practitioners of primal magic believe the earthy colors adorning each arboreal archive's body hold clues about the memories and myths the creature collects and preserves."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 32, attack +24 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/entangling-flora|Entangling Flora]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/earthbind|Earthbind]] (at will) - __6th__ [[srd/pf2e/compendium/spells/rank-6/tangling-creepers|Tangling Creepers]] - __Constant (4th)__ [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|Speak with Plants]]"
sourcebook: "_Monster Core 2_, page 34."
```

```encounter-table
name: Arboreal Archive
creatures:
  - 1: Arboreal Archive
```
