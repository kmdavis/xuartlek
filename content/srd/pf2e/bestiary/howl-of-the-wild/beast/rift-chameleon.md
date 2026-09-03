---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rift Chameleon"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/air
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/ethereal
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/small
statblock: inline
name: "Rift Chameleon"
level: 3
source: "Howl of the Wild"
aon_id: "creature-3271"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3271"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Rift Chameleon"
level: "Creature 3"
size: "Small"
trait_01: "Air"
trait_02: "Beast"
trait_03: "Ethereal"
trait_04: "Uncommon"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, scent (imprecise) 30 feet"
languages: "Aklo; can't speak any language"
skills:
  - name: "Skills"
    desc: "Athletics +9, Stealth +10, Survival +8"
abilityMods: [4, 2, 3, -2, 1, 3]
abilities_top:
  - name: "Ethereal Camouflage"
    desc: "A rift chameleon can Hide, even if it doesn't have cover, but it cannot be concealed from creatures on the Ethereal Plane."
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +10; __Ref__: +9; __Will__: +8"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "25 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 1d10+4 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ tail +11 (Agile) __Damage__ 1d8+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ tongue +11 (reach 10 feet) __Damage__ tongue pull"
abilities_bot:
  - name: "Extradimensional Gullet"
    desc: "(Extradimensional) The rift chameleon's innards exist partially on the Ethereal Plane, allowing it to swallow any number of creatures, even ones larger than itself. Creatures that Escape or cut themselves free from the chameleon's stomach reappear in the Universe adjacent to the rift chameleon's position. Creatures cannot escape from the rift chameleon's gullet using teleportation effects unless those effects can also cross planar boundaries."
  - name: "Flickering Dash"
    desc: "⬻ (Occult, Teleportation)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The rift chameleon Strides twice. During this movement, it flits quickly between the Universe and the Ethereal Plane, gaining resistance 5 to physical damage."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Large, 1d12+2 bludgeoning, Rupture 10"
  - name: "Tongue Pull"
    desc: "Any creature hit by the rift chameleon's tongue is pulled adjacent to the chameleon. The creature is off-guard to the next Strike the rift chameleon makes against it this round."
sourcebook: "_Howl of the Wild_, page 146."
```

```encounter-table
name: Rift Chameleon
creatures:
  - 1: Rift Chameleon
```
