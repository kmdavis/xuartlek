---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Tardigrade"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Giant Tardigrade"
level: 9
source: "Howl of the Wild"
aon_id: "creature-3316"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3316"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Giant Tardigrade"
level: "Creature 9"
size: "Huge"
trait_01: "Amphibious"
trait_02: "Animal"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; tremorsense (imprecise) 30 ft"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +14, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +18"
abilityMods: [4, 3, 6, -5, 3, 1]
abilities_top:
  - name: "Eyespots"
    desc: "A giant tardigrade can't see anything beyond 30 feet."
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +23; __Ref__: +16; __Will__: +16"
hp: 120
health:
  - name: "HP"
    desc: "120; __Resistances__ all damage 10"
abilities_mid:
  - name: "Tun State"
    desc: "⭓"
  - name: "Trigger"
    desc: "The tardigrade would be reduced to 0 Hit Points or would die due to [[srd/pf2e/books/gm-core/chapter-1-running-the-game/running-exploration#Starvation and Thirst|starvation]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/encounter-mode#Mounted Defenses|suffocation]], or similar environmental causes"
  - name: "Frequency"
    desc: "once per week"
  - name: "Requirements"
    desc: "The tardigrade isn't already in tun state"
  - name: "Effect"
    desc: "The giant tardigrade doesn't die but instead remains at 1 Hit Point and curls into a dry ball, called a tun. While in this tun state, the giant tardigrade is [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], doesn't need to eat, drink, or breathe, and doubles its resistance to 20. It remains in tun state indefinitely until covered in significant amounts of water, at which point it begins to rehydrate, gaining regeneration 5. The regeneration persists until it reaches maximum Hit Points. The giant tardigrade then exits its tun state."
speed: "25 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ stylet +19 __Damage__ 3d8+6 piercing plus 1d8 persistent bleed"
  - name: "Melee"
    desc: "⬻ claws +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d6+6 slashing plus Grab"
abilities_bot:
  - name: "Vacuum Mouth"
    desc: "⬺"
  - name: "Requirements"
    desc: "The giant tardigrade doesn't have a target [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The giant tardigrade draws in air with its mouth. All creatures in a 20-foot cone must succeed at a DC 25 Reflex save or be pulled adjacent to the giant tardigrade. The tardigrade chooses one creature that failed its save, Grabbing the target in its claws and making a stylet Strike."
sourcebook: "_Howl of the Wild_, page 187."
```

```encounter-table
name: Giant Tardigrade
creatures:
  - 1: Giant Tardigrade
```
