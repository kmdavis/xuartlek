---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2907"
socialImage: og-image.png
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
    desc: "+17; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; telepathy 100 feet, [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +17, Legal Lore +14, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +17"
abilityMods: [4, 6, 2, 3, 4, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/weapons/club/Morningstar|morningstar]]_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +13; __Ref__: +17; __Will__: +15 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 110
health:
  - name: "HP"
    desc: "110; __Immunities__ fire; __Resistances__ physical 5 (except silver), [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 5; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 5 (see blood contract) Blood Contract When the coarti takes damage from their holy weakness, blood flows freely from their eyes and the contract carved into their skin. They take 1d6 persistent bleed damage and are [[srd/pf2e/compendium/rules-elements/Conditions#Dazzled|dazzled]] as long as the persistent damage continues, but their Despairing Shriek recharges."
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _morningstar_ +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 1d6+10 bludgeoning plus 1d6 spirit"
  - name: "Melee"
    desc: "⬻ wing +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 1d6+7 bludgeoning plus 1d6 fire"
abilities_bot:
  - name: "Despairing Shriek"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|Sonic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) The coarti lets out a terrible cry, dealing 4d6 sonic damage to all creatures in a 30-foot emanation with a DC 25 basic Will save. [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]] creatures that fail this save are also [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened 2]]; this added effect has the [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], and [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] traits. The coarti can't use Despairing Shriek again for 1d4 rounds."
  - name: "Wing Snap"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per turn"
  - name: "Effect"
    desc: "The coarti makes two wing Strikes, then falls if it's flying. It can't Fly until the end of its turn."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25 - __4th__ [[srd/pf2e/compendium/spells/rank-2/Darkness|Darkness]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
  - name: "Rituals"
    desc: "DC 25 - __1st__ [[srd/pf2e/compendium/spells/rituals/Diabolic Pact|Diabolic Pact]]"
sourcebook: "_Monster Core_, page 87."
```

```encounter-table
name: Coarti
creatures:
  - 1: Coarti
```
