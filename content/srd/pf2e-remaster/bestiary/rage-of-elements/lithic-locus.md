---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lithic Locus"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/large
statblock: inline
name: "Lithic Locus"
level: 14
source: "Rage of Elements"
aon_id: "creature-2628"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2628"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Lithic Locus"
level: "Creature 14"
size: "Large"
trait_01: "Construct"
trait_02: "Earth"
trait_03: "Elemental"
trait_04: "Rare"
trait_05: "Spirit"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, tremorsense (imprecise) 60 feet"
languages: "Petran; plus one ancient language"
skills:
  - name: "Skills"
    desc: "Athletics +26, Civilization Lore +29, Society +25"
abilityMods: [6, 0, 6, 7, 6, 2]
abilities_top:
  - name: "Antiques"
    desc: "A lithic locus contains at least one magic item. Any such antiques are durable, permanent items that were part of the locus's site and typify their culture. The locus receives the benefits of such an item as if wearing or holding it and can activate it. A lithic locus typically has an item of their level."
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +27; __Ref__: +21; __Will__: +27"
hp: 260
health:
  - name: "HP"
    desc: "260; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, nonlethal attacks, paralyzed, poison, sickened, unconscious, vitality, void"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ancient stone +28 (Earth, Magical) __Damage__ 3d8+16 bludgeoning plus bury"
abilities_bot:
  - name: "Bury"
    desc: "Any creature hit by the locus's ancient stone Strike is partially buried in a tide of earth and rock, becoming immobilized (Escape DC 34)."
  - name: "Echo the Past"
    desc: "⬺ The locus calls forth a remnant of the past civilization to impart a lesson or control the present. Using this ability again ends any previous manifestation. The locus casts one of the following occult innate spells (DC 34) for the listed purpose. _"
  - name: "Dominate"
    desc: "_ The dominated creature takes on the role of a historical figure or someone in the social hierarchy (such as high priest) from the locus's civilization. _"
  - name: "Illusory Scene"
    desc: "_ The scene reenacts a historical event from the locus's civilization. _"
  - name: "Invoke Spirits"
    desc: "_ The spirits are drawn from the locus's memories of people from their civilization. _"
  - name: "Wall of Stone"
    desc: "_ The locus recreates the wall of a building from their civilization, complete with decorations. Ancient Finds Lithic loci often contain important and valuable items. None of these elemental constructs are likely to agree to be looted, but some loci bestow their antiquities upon worthy successors, proud to see their culture's creations put to effective use in the modern day. Lithic loci can also direct earnest seekers to other lost treasures, helping to restore knowledge of an extinct society."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 34 - __Cantrips (7th)__ Daze - __3rd__ One with Stone"
sourcebook: "_Rage of Elements_, page 107."
```

```encounter-table
name: Lithic Locus
creatures:
  - 1: Lithic Locus
```
