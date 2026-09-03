---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Allosaurus"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/huge
statblock: inline
name: "Allosaurus"
level: 7
source: "Monster Core 2"
aon_id: "creature-4336"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4336"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Allosaurus"
level: "Creature 7"
size: "Huge"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17"
abilityMods: [6, 3, 4, 0, 2, 1]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +18; __Ref__: +15; __Will__: +12"
hp: 120
health:
  - name: "HP"
    desc: "120"
abilities_mid:
  - name: "Serrated Teeth"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] by the allosaurus's jaws succeeds at an [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] check"
  - name: "Effect"
    desc: "As the enemy wriggles away, the allosaurus clamps down with its jagged teeth, dealing 2d6 slashing damage."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+9 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claws +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d8+9 slashing"
  - name: "Melee"
    desc: "⬻ tail +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d6+9 bludgeoning plus Knockdown"
abilities_bot:
  - name: "Unexpected Ambush"
    desc: "⬺"
  - name: "Requirements"
    desc: "The allosaurus is [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] or [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] to at least one creature within 40 feet"
  - name: "Effect"
    desc: "The allosaurus dashes forward, knocking its unsuspecting prey to the ground. The allosaurus [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]] up to its Speed toward the required creature to an unoccupied space within reach of its tail Strike. The allosaurus makes a tail Strike against the enemy. If the Strike hits, the allosaurus automatically succeeds at a free action to Knockdown the target."
  - name: "Swallow Whole"
    desc: "⬻ Large, 2d6+3 bludgeoning, Rupture 15 Allosaurus Teeth Allosauruses have serrated teeth, allowing them to more easily slash the flesh of large or slippery prey. These teeth are valuable not only because of their rarity but also because of their multiple practical uses. Larger allosaurus teeth can be made into arrow or spear tips, small knives, or worn as jewelry to indicate social status. While some cultures revere these artifacts, the killing of allosauruses for the express purpose of harvesting their teeth is outlawed in many regions across Golarion."
sourcebook: "_Monster Core 2_, page 108."
```

```encounter-table
name: Allosaurus
creatures:
  - 1: Allosaurus
```
