---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Moray Eel"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/large
statblock: inline
name: "Giant Moray Eel"
level: 5
source: "Monster Core"
aon_id: "creature-2971"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2971"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Moray Eel"
level: "Creature 5"
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13"
abilityMods: [6, 2, 3, -4, 2, -1]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +14; __Ref__: +13; __Will__: +9"
hp: 65
health:
  - name: "HP"
    desc: "65; __Resistances__ bludgeoning 5, piercing 5"
abilities_mid:
  - name: "Ambush"
    desc: "⬲"
  - name: "Trigger"
    desc: "A target creature passes within 20 feet of the giant moray eel's hiding place and has not detected the giant moray eel"
  - name: "Effect"
    desc: "The giant moray eel lunges out of its hiding place, Swims directly toward the triggering creature, and makes a jaws Strike against it. The target creature is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to this attack."
speed: "10 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+8 piercing plus Grab"
abilities_bot:
  - name: "Pharyngeal Jaws"
    desc: "⬺"
  - name: "Requirements"
    desc: "The giant moray eel has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] in its jaws"
  - name: "Effect"
    desc: "The giant moray eel uses its second set of jaws to pull the prey into its gullet. The eel deals 1d6+4 piercing damage to the grabbed creature and gains a +2 circumstance bonus to its Swallow Whole attempts and to the DC for the creature to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]]. This effect ends if the target Escapes or the giant moray eel Swallows it Whole."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Small, 1d6+6 bludgeoning, Rupture 12."
sourcebook: "_Monster Core_, page 138."
```

```encounter-table
name: Giant Moray Eel
creatures:
  - 1: Giant Moray Eel
```
