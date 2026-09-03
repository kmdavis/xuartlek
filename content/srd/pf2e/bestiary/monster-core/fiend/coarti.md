---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Coarti"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Coarti"
level: 7
source: "Monster Core"
aon_id: "creature-2907"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2907"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Coarti"
level: "Creature 7"
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; greater darkvision"
languages: "Common, Diabolic, Draconic, Empyrean; telepathy 100 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Athletics +15, Deception +17, Legal Lore +14, Religion +17"
abilityMods: [4, 6, 2, 3, 4, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 morningstar_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +13; __Ref__: +17; __Will__: +15 +1 status to all saves vs. magic"
hp: 110
health:
  - name: "HP"
    desc: "110; __Immunities__ fire; __Resistances__ physical 5 (except silver), poison 5; __Weaknesses__ holy 5 (see blood contract) Blood Contract When the coarti takes damage from their holy weakness, blood flows freely from their eyes and the contract carved into their skin. They take 1d6 persistent bleed damage and are dazzled as long as the persistent damage continues, but their Despairing Shriek recharges."
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _morningstar_ +18 (Magical, Unholy, versatile P) __Damage__ 1d6+10 bludgeoning plus 1d6 spirit"
  - name: "Melee"
    desc: "⬻ wing +17 (Agile, Unholy, versatile P) __Damage__ 1d6+7 bludgeoning plus 1d6 fire"
abilities_bot:
  - name: "Despairing Shriek"
    desc: "⬺ (Divine, Sonic, Unholy) The coarti lets out a terrible cry, dealing 4d6 sonic damage to all creatures in a 30-foot emanation with a DC 25 basic Will save. Holy creatures that fail this save are also frightened 2; this added effect has the emotion, fear, and mental traits. The coarti can't use Despairing Shriek again for 1d4 rounds."
  - name: "Wing Snap"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per turn"
  - name: "Effect"
    desc: "The coarti makes two wing Strikes, then falls if it's flying. It can't Fly until the end of its turn."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25 - __4th__ Darkness, Translocate (at will) - __Constant (5th)__ Truespeech"
  - name: "Rituals"
    desc: "DC 25 - __1st__ Diabolic Pact"
sourcebook: "_Monster Core_, page 87."
```

```encounter-table
name: Coarti
creatures:
  - 1: Coarti
```
