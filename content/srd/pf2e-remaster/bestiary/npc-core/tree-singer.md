---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tree Singer"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Tree Singer"
level: 13
source: "NPC Core"
aon_id: "creature-3585"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3585"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tree Singer"
level: "Creature 13"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22"
languages: "Common, Wildsong"
skills:
  - name: "Skills"
    desc: "Athletics +23, Diplomacy +25, Intimidation +23, Nature +26, Performance +27, Survival +22"
abilityMods: [4, 3, 1, 2, 3, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 resilient leather armor_, _+1 striking longspear_, _+1 striking composite longbow_"
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +23; __Ref__: +21; __Will__: +25"
hp: 220
health:
  - name: "HP"
    desc: "220"
abilities_mid:
  - name: "Bloodthirsty Plants"
    desc: "⬲ (concentrate)"
  - name: "Trigger"
    desc: "An enemy in the tree singer's Verdant Aria aura (see below) attacks one of the tree singer's allies"
  - name: "Effect"
    desc: "Vines and branches to lash out at the attacker, dealing 3d6 piercing damage."
  - name: "Plant Empathy"
    desc: "The tree singer can ask questions of, receive answers from, and use the Diplomacy skill with plants and fungus."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longspear_ +24 (Magical, reach 10 feet) __Damage__ 2d8+10 piercing plus 2d10 sonic"
  - name: "Melee"
    desc: "⬻ fist +23 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+10 bludgeoning plus 2d10 sonic"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +23 (deadly d10, Magical, Propulsive, range increment 100 feet, reload 0, volley 30 feet) __Damage__ 2d8+8 piercing plus 1d10 sonic"
abilities_bot:
  - name: "Druid Order Spells"
    desc: "DC 33, 1 Focus Point - __7th__ Cornucopia"
  - name: "Verdant Aria"
    desc: "⬻ (Auditory, Aura, Concentrate, Linguistic, Plant, Primal, Wood) The tree singer raises their voice in a haunting melody, creating an aura in a 30-foot emanation. Plants in the aura seem to come to life, swaying and rustling in response to the music. The tree singer's allies in the aura gain a +2 status bonus to AC and saving throws as the foliage around them shields and defends them from harm. The aura lasts until the end of the tree singer's next turn but can be Sustained. It can be Sustained even if the tree singer is polymorphed. The effect ends early if the tree singer stops singing."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 33, attack +25 - __Cantrips (7th)__ Detect Magic, Light, Prestidigitation, Stabilize, Tangle Vine - __1st__ Gentle Landing (×2), Ventriloquism - __2nd__ Entangling Flora, One with Plants (×2) - __3rd__ Earthbind (×2), Slow - __4th__ Oaken Resilience, Resist Energy, Vapor Form - __5th__ Elemental Form (wood only), Nature's Pathway, Plant Form - __6th__ Plant Form, Tangling Creepers, Wall of Thorns - __7th__ Regenerate, Tree of Seasons"
sourcebook: "_NPC Core_, page 135."
```

```encounter-table
name: Tree Singer
creatures:
  - 1: Tree Singer
```
