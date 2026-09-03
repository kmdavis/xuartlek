---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mitflit"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/gremlin
  - pf2e/creature/trait/small
statblock: inline
name: "Mitflit"
level: -1
source: "Monster Core"
aon_id: "creature-3031"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3031"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Mitflit"
level: "Creature -1"
size: "Small"
trait_01: "Fey"
trait_02: "Gremlin"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +1, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +3, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +5"
abilityMods: [-1, 3, 0, -1, 1, -1]
abilities_top:
  - name: "Self-Loathing"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) A mitflit's self-loathing makes it easy to influence. It takes a –4 penalty to its Will DC against checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Coerce|Coerce]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]], and [[srd/pf2e/compendium/rules-elements/actions/player-core#Request|Request]]."
  - name: "Items"
    desc: "Dart (10), Shortsword"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +2; __Ref__: +7; __Will__: +4"
hp: 10
health:
  - name: "HP"
    desc: "10; __Weaknesses__ cold iron 2"
speed: "20 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6–1 piercing"
  - name: "Ranged"
    desc: "⬻ dart +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], range increment 20 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|Thrown]]) __Damage__ 1d4–1 piercing"
abilities_bot:
  - name: "Vengeful Anger"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) As long as it isn't [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]], a mitflit gains a +2 status bonus to damage rolls against a creature that has previously damaged or tormented it."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/prestidigitation|Prestidigitation]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/bane|Bane]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/speak-with-animals|Speak with Animals]] (arthropods only; at will)"
sourcebook: "_Monster Core_, page 180."
```

```encounter-table
name: Mitflit
creatures:
  - 1: Mitflit
```
