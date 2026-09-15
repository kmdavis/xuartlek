---
noteType: pf2eMonster
aliases: "Traveling Actor"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Traveling Actor"
level: 3
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3574"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Traveling Actor"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]; up to 4 other languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +10, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +9, [[srd/pf2e/compendium/rules-elements/skills/Lore|Theater Lore]] +9"
abilityMods: [2, 3, 0, 1, 1, 4]
abilities_top:
  - name: "Items"
    desc: "Padded Armor, wooden sword (functions as a [[srd/pf2e/compendium/equipment/weapons/club/Light Mace|light mace]])"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +12; __Will__: +9"
hp: 35
health:
  - name: "HP"
    desc: "35"
abilities_mid:
  - name: "Dramatic Death"
    desc: "⬲"
  - name: "Trigger"
    desc: "The traveling actor takes any damage"
  - name: "Effect"
    desc: "The traveling actor falls [[srd/pf2e/compendium/rules-elements/Conditions#Prone|prone]] and dramatically announces their death. They appear to have died. Anyone who is suspicious of this “death” can [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] to attempt a [[srd/pf2e/compendium/rules-elements/traits/player-core/Secret|secret]] Perception check against the traveling actor's [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] DC. On a success, they see through the ruse."
  - name: "Versatile Performance"
    desc: "The traveling actor can use [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] instead of [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]] and instead of [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]]."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ wooden sword +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|Shove]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
abilities_bot:
  - name: "Overacted Strike"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|Visual]]) The traveling actor puts all their expertise into an attack that strikes fear in those who witness it. The traveling actor Strikes. On a success, the traveling actor chooses another creature within 30 feet who can see the attack, who becomes [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened 1]] (or frightened 2 on a critical success)."
sourcebook: "_NPC Core_, page 127."
```

```encounter-table
name: Traveling Actor
creatures:
  - 1: Traveling Actor
```
