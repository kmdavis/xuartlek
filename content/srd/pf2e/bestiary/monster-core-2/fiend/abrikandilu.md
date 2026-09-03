---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Abrikandilu"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Abrikandilu"
level: 4
source: "Monster Core 2"
aon_id: "creature-4318"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4318"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Abrikandilu"
level: "Creature 4"
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +8"
abilityMods: [4, 1, 3, -2, 2, 0]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +14; __Ref__: +9; __Will__: +7"
hp: 70
health:
  - name: "HP"
    desc: "70; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 5"
abilities_mid:
  - name: "Hatred of Mirrors"
    desc: "An abrikandilu loathes the sight of their reflection. When a creature [[srd/pf2e/compendium/rules-elements/actions/player-core#Interact|Interacts]] with a mirror within sight of the wrecker demon, the demon takes a –2 penalty to Will saves against [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] checks. An abrikandilu that ends their turn adjacent to a mirror or that's attacked by a creature holding a mirror takes 1d6 mental damage (this usually leads abrikandilus to focus their efforts on destroying nearby mirrors using Wreck)."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 2d6+4 slashing"
  - name: "Melee"
    desc: "⬻ jaws +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 3d6+4 piercing plus loathsome bite"
  - name: "Ranged"
    desc: "⬻ hurled debris +11 (range increment 20 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 2d6+4 bludgeoning"
abilities_bot:
  - name: "Loathsome Bite"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) When an abrikandilu hits a creature with their jaws Strike, the creature becomes infected with the demon's self-loathing. The creature must succeed at a DC 21 Will save to avoid gaining a –1 status penalty to Charisma-based checks. This penalty is cumulative up to –3, and remains even if the wounds are healed. The penalty is reduced by 1 every 24 hours until it reaches 0."
  - name: "Wreck"
    desc: "⬻ The abrikandilu makes two claw Strikes against an unattended object or held mirror. Held mirrors use the holding character's AC. If both Strikes hit, combine their damage for the purpose of overcoming any Hardness or resistance. These Strikes don't count toward the abrikandilu's multiple attack penalty, nor does that penalty apply to these Strikes."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 20 - __2nd__ [[srd/pf2e/compendium/spells/rank-1/fear|Fear]] (×2)"
  - name: "Rituals"
    desc: "DC 20 - __1st__ [[srd/pf2e/compendium/spells/rituals/demonic-pact|Demonic Pact]]"
sourcebook: "_Monster Core 2_, page 91."
```

```encounter-table
name: Abrikandilu
creatures:
  - 1: Abrikandilu
```
