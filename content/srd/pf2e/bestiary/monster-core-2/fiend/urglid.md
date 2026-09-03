---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Urglid"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Urglid"
level: 13
source: "Monster Core 2"
aon_id: "creature-4321"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4321"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Urglid"
level: "Creature 13"
size: "Large"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision, tremorsense (imprecise) 60 feet, _truesight_"
languages: "Chthonian, Common, Draconic, Empyrean, Necril; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Athletics +27, Crafting +24, Deception +22, Intimidation +27, Outer Rifts Lore +24, Religion +24, Society +22, Stealth +27"
abilityMods: [8, 4, 5, 4, 3, 4]
abilities_top:
  - name: "Consecration Vulnerability"
    desc: "Dedicated to the desecration of graves, an urglid takes 3d6+6 mental damage each round they're within the area of an effect with the consecration trait. In addition, the demon's weakness to holy increases to 30 for 1 round the first time they take damage from holy water each turn."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +26; __Ref__: +20; __Will__: +20 +1 status to all saves vs. magic"
hp: 290
health:
  - name: "HP"
    desc: "290; __Weaknesses__ cold iron 10, holy 10"
speed: "30 feet, burrow 40 feet, climb 20 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ claw +25 (Agile, deadly 2d10, magical, reach 10 feet, unholy) __Damage__ 3d10+16 slashing"
  - name: "Melee"
    desc: "⬻ leg +25 (Agile, magical, reach 15 feet, unholy) __Damage__ 3d12+16 bludgeoning"
abilities_bot:
  - name: "Divine Rituals"
    desc: "DC 32 - __1st__ Demonic Pact"
  - name: "Earth Glide"
    desc: "The urglid can Burrow through any earthen matter, including rock. When they do so, the urglid moves at their full burrow Speed, leaving no tunnels or signs of its passing unless they choose to do so."
  - name: "Gravechoke"
    desc: "⬺ (Concentrate, divine, earth, olfactory) The urglid emits a putrid pulse that targets all living creatures within a 30-foot emanation. Each creature in this area that fails a DC 30 Fortitude save becomes sickened 1 (sickened 2 on a critical failure)."
  - name: "Ravenous Earth"
    desc: "⬻ (Concentrate, earth, unholy) With a single, devious thought, the urglid causes a mound of grave soil to well up at a creature's feet. That creature must succeed at a DC 30 Reflex save or become restrained (Escape DC 30). The restrained creature then begins sinking below the ground into a spontaneously formed grave. A creature restrained by this ability for 3 rounds is buried 6 feet deep in the ground and begins suffocating within 1 minute. A buried creature must be dug up to be freed (see Burial). A creature that is slain by Ravenous Earth rises as a ghoul the next midnight. Kabriri's Excavators While many loathe urglids for their ravenous appetite for burial and wanton destruction, priests of Kabriri insist that the demon lord blessed and oversaw their creation, trusting the fiends with digging the labyrinthine network of tunnels that connects Everglut with the Universe. It's no surprise, then, that where there's an urglid, there's possibly a pathway to the Outer Rifts—and plenty of ghouls."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30 - __3rd__ Earthbind (at will) - __5th__ Magic Passage (at will), Wall of Stone (×3) - __8th__ Earthquake - __Constant (6th)__ Truesight"
sourcebook: "_Monster Core 2_, page 94."
```

```encounter-table
name: Urglid
creatures:
  - 1: Urglid
```
