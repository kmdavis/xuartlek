---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Karkadann"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Karkadann"
level: 7
source: "Howl of the Wild"
aon_id: "creature-3318"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3318"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Karkadann"
level: "Creature 7"
size: "Large"
trait_01: "Beast"
trait_02: "Fey"
trait_03: "Holy"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision, scent (imprecise) 30 feet"
languages: "Common, Fey"
skills:
  - name: "Skills"
    desc: "Athletics +17, Diplomacy +13, Intimidation +15, Medicine +14, Survival +14"
abilityMods: [6, 3, 6, 0, 3, 4]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +17; __Ref__: +14; __Will__: +14"
hp: 120
health:
  - name: "HP"
    desc: "120; __Immunities__ poison"
abilities_mid:
  - name: "Fearless Rush"
    desc: "⬲"
  - name: "Trigger"
    desc: "The karkadann becomes frightened"
  - name: "Effect"
    desc: "The karkadann reduces their frightened value by 1 (to a minimum of 0). The karkadann then Strides toward an enemy."
speed: "45 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +17 (Holy, Magical) __Damage__ 2d10+8 piercing and ghost touch"
  - name: "Melee"
    desc: "⬻ hoof +17 (Holy, Magical) __Damage__ 2d6+8 bludgeoning and ghost touch"
abilities_bot:
  - name: "Ghost Touch"
    desc: "A karkadann's Strikes have the effects of a _ghost touch_ property rune."
  - name: "Impaling Charge"
    desc: "⬺ The karkadann Strides twice, then Strikes with their horn. If the Strike hits, it also deals 1d10 persistent bleed damage."
  - name: "Trample"
    desc: "⬽ Medium or smaller, hoof, DC 25"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 25 - __Cantrips (4th)__ Light - __1st__ Cleanse Cuisine (×3) - __3rd__ Cleanse Affliction (×2)"
sourcebook: "_Howl of the Wild_, page 190."
```

```encounter-table
name: Karkadann
creatures:
  - 1: Karkadann
```
