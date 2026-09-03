---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lamia"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Lamia"
level: 6
source: "Monster Core"
aon_id: "creature-3077"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3077"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lamia"
level: "Creature 6"
size: "Large"
trait_01: "Beast"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision"
languages: "Chthonian, Common"
skills:
  - name: "Skills"
    desc: "Athletics +16, Cult Lore +11, Deception +15, Diplomacy +11, Intimidation +13, Stealth +15, Survival +11"
abilityMods: [6, 3, 2, 1, 3, 3]
abilities_top:
  - name: "Items"
    desc: "Javelin (2), _+1 spear_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +12; __Ref__: +15; __Will__: +15"
hp: 95
health:
  - name: "HP"
    desc: "95"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _spear_ +17 __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ tail +16 (Agile) __Damage__ 1d6+10 bludgeoning plus Grab"
  - name: "Ranged"
    desc: "⬻ _spear_ +14 (thrown 10 feet) __Damage__ 1d6+10 piercing"
  - name: "Ranged"
    desc: "⬻ javelin +13 (thrown 30 feet) __Damage__ 1d6+10 piercing"
abilities_bot:
  - name: "Lamia's Caress"
    desc: "⬺ (Curse, Mental, Occult) The lamia touches a creature, who must succeed at a DC 23 Will save or become stupefied 1. If the target fails additional saves against this ability, the condition value increases by 1 (to a maximum of stupefied 4). This condition value decreases by 1 every 24 hours."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25 - __1st__ Illusory Disguise (at will), Illusory Object (at will), Ventriloquism (at will) - __2nd__ Blur, Humanoid Form (at will) - __3rd__ Sleep - __4th__ Charm (×3), Suggestion"
sourcebook: "_Monster Core_, page 214."
```

```encounter-table
name: Lamia
creatures:
  - 1: Lamia
```
