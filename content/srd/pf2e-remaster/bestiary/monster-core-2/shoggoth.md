---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Shoggoth"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Shoggoth"
level: 18
source: "Monster Core 2"
aon_id: "creature-4543"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4543"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Shoggoth"
level: "Creature 18"
size: "Huge"
trait_01: "Aberration"
trait_02: "Amphibious"
trait_03: "Rare"
modifier: 34
perception:
  - name: "Perception"
    desc: "Perception +34; darkvision, scent (imprecise) 60 feet, tremorsense (imprecise) 60 feet"
languages: "Aklo"
skills:
  - name: "Skills"
    desc: "Athletics +36, Intimidation +29"
abilityMods: [10, 6, 9, -3, 6, 1]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +33; __Ref__: +30; __Will__: +30 +1 status to all saves vs. magic"
hp: 275
health:
  - name: "HP"
    desc: "275 (fast healing 20); __Immunities__ bleed, blinded, controlled, critical hits, deafened, precision, sleep; __Resistances__ acid 20, cold 20, sonic 20"
abilities_mid:
  - name: "Maddening Cacophony"
    desc: "(auditory, aura, incapacitation, mental) 60 feet. A shoggoth constantly voices syllables and mutterings that mortals weren't meant to hear. A creature entering the aura or starting its turn in the aura must succeed at a DC 38 Will save or become confused for 1 round (2d4 rounds on a critical failure). A creature that succeeds at its save is temporarily immune for 24 hours."
speed: "40 feet, climb 25 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +33 (Magical, reach 30 feet) __Damage__ 4d10+18 bludgeoning plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d10+15 bludgeoning, DC 40"
  - name: "Eat Away"
    desc: "A creature that begins its turn inside the shoggoth takes 9d6 acid damage."
  - name: "Engulf"
    desc: "⬺ DC 40, 6d6 acid, Escape DC 40, Rupture 40 Tekeli-Li While a shoggoth's cacophony is an eldritch mix of sound and dangerous secrets, the phrase “tekeli-li” is the most oft-repeated cry, and these mysterious words are always discernible among their vocalizations. Sometimes, wild birds that dwell in places haunted by shoggoths cry out this strange phrase, while near other shoggoth dwellings, it can be heard on blasts of frozen wind. Attempts to translate the phrase, even via magic, have only ever met with failure, as if the words themselves resist revealing their secrets to the world."
sourcebook: "_Monster Core 2_, page 285."
```

```encounter-table
name: Shoggoth
creatures:
  - 1: Shoggoth
```
