---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kithangian"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Kithangian"
level: 9
source: "Monster Core 2"
other_sources: "Gatewalkers (Hardcover)"
aon_id: "creature-4320"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4320"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Kithangian"
level: "Creature 9"
size: "Large"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision"
languages: "Chthonian, Draconic, Empyrean; _speak with animals_, telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Athletics +18, Intimidation +20, Nature +21, Stealth +16"
abilityMods: [6, 3, 5, -2, 4, 3]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +20; __Ref__: +15; __Will__: +19 +1 status to all saves vs. magic"
hp: 180
health:
  - name: "HP"
    desc: "180; __Weaknesses__ cold iron 10, holy 10"
abilities_mid:
  - name: "Animal Kindness"
    desc: "Vulnerability Kithangians find kindness to animals revolting. The first time each round that a kithangian sees someone heal or otherwise provide aid to a creature that has the animal trait, the kithangian takes 3d6 mental damage."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pincer +21 (Magical, reach 10 feet, unholy) __Damage__ 2d12+9 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ stinger +21 (Agile, magical, reach 10 feet, unholy) __Damage__ 2d8+9 piercing plus kithangian venom"
abilities_bot:
  - name: "Divine Rituals"
    desc: "DC 25 - __1st__ Demonic Pact"
  - name: "Animal Killer"
    desc: "A kithangian's melee Strikes deal an additional 2d6 precision damage to animals."
  - name: "Change Shape"
    desc: "⬻ (Concentrate, divine, polymorph) The kithangian transforms into a Medium or Large animal. This doesn't affect their statistics, but it may change the damage type of their Strikes."
  - name: "Kithangian Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 poison damage (2 rounds)"
  - name: "Stage 2"
    desc: "2d6 poison damage and sickened 1 (2 rounds)"
  - name: "Stage 3"
    desc: "3d6 poison damage and sickened 2 (2 rounds)"
  - name: "Rasping Tongues"
    desc: "⬻ (Attack)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The kithangian has a creature grabbed or restrained in one or both pincers"
  - name: "Effect"
    desc: "Barbed tongues slither out of the faces in the kithangian's pincers. The tongues burrow into grabbed creatures and inject their minds with haunting psychic screams. Each grabbed creature takes 2d8 piercing damage and 2d8 mental damage. A creature can try to resist the mental damage by attempting a DC 25 basic Will save. Demon Hunters Reclaimers of the Sarkoris Scar who follow the Green Faith consider kithangians particularly heinous foes. They take grim satisfaction in hunting and slaying such demons, viewing their extermination as just vengeance for the evils these demons visit upon wildlife. Demon Hunters Reclaimers of the Sarkoris Scar who follow the Green Faith consider kithangians particularly heinous foes. They take grim satisfaction in hunting and slaying such demons, viewing their extermination as just vengeance for the evils these demons visit upon wildlife."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25 - __1st__ Command (at will; animals only) - __3rd__ Paralyze (×2) - __4th__ Fly, Translocate - __Constant (4th)__ Speak with Animals"
sourcebook: "_Monster Core 2_, page 92."
```

```encounter-table
name: Kithangian
creatures:
  - 1: Kithangian
```
