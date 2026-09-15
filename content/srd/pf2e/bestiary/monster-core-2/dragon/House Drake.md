---
noteType: pf2eMonster
aliases: "House Drake"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/tiny
statblock: inline
name: "House Drake"
level: 1
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4370"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "House Drake"
level: "Creature 1"
size: "Tiny"
trait_01: "Dragon"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], Daemonic, [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +4, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +6"
abilityMods: [1, 4, 2, 1, 3, 2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +8; __Will__: +10"
hp: 15
health:
  - name: "HP"
    desc: "15; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]"
abilities_mid:
  - name: "Ferocious Will"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]])"
  - name: "Trigger"
    desc: "The house drake succeeds at a saving throw against a magical mental effect"
  - name: "Effect"
    desc: "The house drake sends a blast of magical feedback at the effect's source, dealing 2d6 mental damage (DC 16 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Will save) to that creature. On a failed save, the creature is also [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed]] 1 for 1 round."
speed: "15 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]]) __Damage__ 1d8+1 piercing plus silver strike"
abilities_bot:
  - name: "Silver Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) The house drake breathes a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] of silver mist. Each creature within the mist must succeed at a DC 16 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied]] 2 for 1 round. The house drake can't use Silver Breath again for 1d4 rounds."
  - name: "Silver Strike"
    desc: "House drakes sharpen their jaws on silver ornamentation until they incorporate bits of silver in their teeth. Their jaws Strike counts as [[srd/pf2e/compendium/equipment/materials/Silver|silver]]. Ancient Tails Some of the oldest tales told among Varisian travelers speak of tiny dragons sent by [[srd/pf2e/compendium/deities/gods-of-the-inner-sea/Desna|Desna]] to comfort and aid her followers during a long-forgotten tyranny. With the recent rediscovery of the ancient Thassilonian empire, some suggest that these tales—and thus house drakes themselves—first appeared back in that distant age."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 17 - __1st__ [[srd/pf2e/compendium/spells/rank-1/Alarm|Alarm]], [[srd/pf2e/compendium/spells/rank-1/Soothe|Soothe]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Mist|Mist]], [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]]"
sourcebook: "_Monster Core 2_, page 137."
```

```encounter-table
name: House Drake
creatures:
  - 1: House Drake
```
