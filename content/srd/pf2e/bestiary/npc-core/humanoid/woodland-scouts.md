---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Woodland Scouts"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/elf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Woodland Scouts"
level: 8
source: "NPC Core"
aon_id: "creature-3633"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3633"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Woodland Scouts"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Elf"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +16, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Forest Lore]] +17, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +14, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +16"
abilityMods: [3, 4, 0, 1, 4, 2]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +12; __Ref__: +18; __Will__: +16"
hp: 120
health:
  - name: "HP"
    desc: "120 (4 segments); __Weaknesses__ area damage 8, splash damage 8"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "30 feet; forest passage, troop movement"
abilities_bot:
  - name: "Among the Trees"
    desc: "⬻"
  - name: "Requirements"
    desc: "Every square the woodland scouts occupy is in forest terrain"
  - name: "Effect"
    desc: "The woodland scouts disperse among the trees. They [[srd/pf2e/compendium/rules-elements/actions/player-core#Take Cover|Take Cover]] and then use that cover to [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]], attempting a [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] check."
  - name: "Forest Passage"
    desc: "Woodland scouts ignore any difficult terrain caused by plants and fungi, such as bushes, vines, and undergrowth."
  - name: "Longbow Barrage"
    desc: "⬺ The scouts draw or reload their longbows, then send forth a flurry of arrows. This barrage is a 10-foot burst within 100 feet that deals 3d8 piercing damage with a DC 24 basic Reflex save. If the scouts are [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] or [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]], this deals an additional 2d6 precision damage. When the troop is reduced to 2 or fewer segments, this area decreases to a 5-foot burst."
  - name: "Thicket of Blades"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The scouts engage in a coordinated melee attack against each enemy in a 5-foot emanation, with a DC 24 basic Reflex save. The damage depends on the number of actions. ⬻ 1d8+3 slashing damage ⬺ 2d8+6 slashing damage ⬽ 3d8+9 slashing damage"
  - name: "Stealthy Formation"
    desc: "If the scouts become [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] or [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]], they remain so until they take a hostile action."
sourcebook: "_NPC Core_, page 179."
```

```encounter-table
name: Woodland Scouts
creatures:
  - 1: Woodland Scouts
```
