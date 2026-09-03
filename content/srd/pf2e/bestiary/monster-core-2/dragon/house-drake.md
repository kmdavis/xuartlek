---
obsidianUIMode: preview
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
aon_id: "creature-4370"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4370"
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
    desc: "Perception +8; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Daemonic, [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6"
abilityMods: [1, 4, 2, 1, 3, 2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +8; __Will__: +10"
hp: 15
health:
  - name: "HP"
    desc: "15; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Ferocious Will"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Trigger"
    desc: "The house drake succeeds at a saving throw against a magical mental effect"
  - name: "Effect"
    desc: "The house drake sends a blast of magical feedback at the effect's source, dealing 2d6 mental damage (DC 16 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Will save) to that creature. On a failed save, the creature is also [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 for 1 round."
speed: "15 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d8+1 piercing plus silver strike"
abilities_bot:
  - name: "Silver Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) The house drake breathes a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] of silver mist. Each creature within the mist must succeed at a DC 16 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 2 for 1 round. The house drake can't use Silver Breath again for 1d4 rounds."
  - name: "Silver Strike"
    desc: "House drakes sharpen their jaws on silver ornamentation until they incorporate bits of silver in their teeth. Their jaws Strike counts as [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]]. Ancient Tails Some of the oldest tales told among Varisian travelers speak of tiny dragons sent by Desna to comfort and aid her followers during a long-forgotten tyranny. With the recent rediscovery of the ancient Thassilonian empire, some suggest that these tales—and thus house drakes themselves—first appeared back in that distant age."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 17 - __1st__ [[srd/pf2e/compendium/spells/rank-1/alarm|Alarm]], [[srd/pf2e/compendium/spells/rank-1/soothe|Soothe]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/mist|Mist]], [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]]"
sourcebook: "_Monster Core 2_, page 137."
```

```encounter-table
name: House Drake
creatures:
  - 1: House Drake
```
