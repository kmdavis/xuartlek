---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dibrasgorth"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Dibrasgorth"
level: 13
source: "Monster Core 2"
aon_id: "creature-4331"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4331"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Dibrasgorth"
level: "Creature 13"
size: "Gargantuan"
trait_01: "Aberration"
trait_02: "Amphibious"
trait_03: "Uncommon"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision 120 feet, planar sight 120 feet, _see the unseen_"
languages: "Chthonian, Common, Diabolic, Draconic, Empyrean"
skills:
  - name: "Skills"
    desc: "Acrobatics +18, Arcana +20, Athletics +25, Nature +17, Occultism +20, Religion +17, Stealth +20, Survival +19"
abilityMods: [8, 1, 4, 5, 2, 0]
abilities_top:
  - name: "Planar Sight"
    desc: "(occult) The eyes at the end of their tentacles allow a dibrasgorth to see into planes coterminous with the one it is currently on at the listed range. For instance, if they're in the Universe, they can see into the Ethereal Plane and the Netherworld."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +20; __Will__: +23"
hp: 250
health:
  - name: "HP"
    desc: "250; __Immunities__ death effects, petrification, polymorph; __Resistances__ acid 15, cold 15, mental 15"
abilities_mid:
  - name: "Warped Space"
    desc: "(aura, occult) 100 feet. The dibrasgorth's presence distorts the fabric of space. Any other creature who uses a teleportation effect or spell within the aura must attempt a DC 33 Fortitude save or become sickened 2."
speed: "20 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +27 (Magical, reach 20 feet) __Damage__ 3d10+16 piercing plus draining bite"
  - name: "Melee"
    desc: "⬻ tentacle +27 (Agile, magical, reach 20 feet) __Damage__ 3d8+16 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Breath of Phantasms"
    desc: "⬺ (Inhaled, mental, poison) The dibrasgorth exhales a 60-foot cone of noxious gas. Each creature in the area takes 7d6 poison damage (DC 30 basic Fortitude save). On a failure, the creature is also confused for 1 round (or 2 rounds on a critical failure)."
  - name: "Drag Through Dimensions"
    desc: "⬻ (Occult, teleportation)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The dibrasgorth has a creature grabbed or restrained with a tentacle"
  - name: "Effect"
    desc: "The dibrasgorth's tentacle whips through coterminous planes as it smashes the creature it is holding against the ground and other natural features in each plane before returning to this plane. The creature takes 5d8 bludgeoning damage (DC 30 basic Reflex save). A creature who fails the save is also stupefied 1 for 1 round and sickened 1 by the rapid planar travel."
  - name: "Draining Bite"
    desc: "(Occult) A dibrasgorth feeds on the spirits of its victims. A creature that is damaged by the dibrasgorth's jaws Strike must attempt a DC 30 Fortitude save or become drained 1 (drained 2 on a critical failure). In addition, the dibrasgorth gains 10 temporary Hit Points that last for 1 minute if the creature fails or critically fails the save."
  - name: "Transdimensional Tentacles"
    desc: "(Occult) The dibrasgorth can worm its tentacles through nearby planes to attack. While in the Universe, its tentacle Strikes ignore all cover from objects unless those objects exist on both the Universe and either the Netherworld or the Ethereal Plane, or the objects have the extradimensional trait. The Myth Of Black Magga Varisian locals who live near the Storval Deep, an enormous freshwater lake on the Storval Plateau, tell tales of Black Magga, a powerful and unholy dibrasgorth rumored to be older than the gods. They say that terrible storms presage her appearance near the lake's surface, and that those who see her form and live are cursed to be unable to completely describe her, with black blood welling in their mouth if they make the attempt."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 33 - __Cantrips (7th)__ Daze - __4th__ Nightmare, Suggestion - __5th__ Banishment, Synaptic Pulse - __6th__ Dominate, Repulsion - __7th__ Interplanar Teleport - __Constant (5th)__ See the Unseen"
sourcebook: "_Monster Core 2_, page 104."
```

```encounter-table
name: Dibrasgorth
creatures:
  - 1: Dibrasgorth
```
