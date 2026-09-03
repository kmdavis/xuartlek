---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Doru"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/div
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Doru"
level: 1
source: "Monster Core 2"
aon_id: "creature-4339"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4339"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Doru"
level: "Creature 1"
size: "Tiny"
trait_01: "Div"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Daemonic; telepathy (touch)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +8, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +6, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +10, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [0, 4, 1, 3, 2, 3]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +9; __Will__: +7"
hp: 20
health:
  - name: "HP"
    desc: "20; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 3, [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 3"
abilities_mid:
  - name: "Covetous of Secrets"
    desc: "Dorus have a weakness for secrets, hoarding them like a miser hoards gold. A creature can tempt a doru with some bit of obscure knowledge the doru doesn't know or thinks they don't know. Presenting the hint of the secret is a single action, which has the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|linguistic]] traits, and requires a skill check using [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]], [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]], or [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] (or some other appropriate skill determined by the GM) against the doru's Will DC. On a success, the doru is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] for as long as the presenter draws out the explanation of the secret (spending 1 action each round doing so, to a maximum of 1 minute). On a critical success, the doru is fascinated for that duration plus 1 minute more as they ponder the implications of the secret. Regardless of the outcome, the doru is temporarily immune to that creature's attempts to present them with secrets for 1 day."
speed: "15 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bite +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 1d6 piercing plus doru venom"
abilities_bot:
  - name: "Doru Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison and [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 (1 round)"
  - name: "Stage 3"
    desc: "1d6 poison and stupefied 2 (1 round) Doru Secrets Despite dorus' obsession, not all secrets capture their focus—instead, each fixates on a unique topic. Many are interested in the history of a particular mortal ancestry, while others delve into riddles, mathematical puzzles, or even local gossip."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/charm|Charm]], [[srd/pf2e/compendium/spells/rank-1/illusory-object|Illusory Object]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will; self only) - __4th__ [[srd/pf2e/compendium/spells/rank-4/read-omens|Read Omens]]"
sourcebook: "_Monster Core 2_, page 110."
```

```encounter-table
name: Doru
creatures:
  - 1: Doru
```
