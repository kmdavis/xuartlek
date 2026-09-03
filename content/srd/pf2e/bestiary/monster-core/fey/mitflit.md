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
languages: "Sakvroth"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Diplomacy +1, Nature +3, Stealth +5, Thievery +5"
abilityMods: [-1, 3, 0, -1, 1, -1]
abilities_top:
  - name: "Self-Loathing"
    desc: "(emotion, mental) A mitflit's self-loathing makes it easy to influence. It takes a –4 penalty to its Will DC against checks to Coerce, Demoralize, Make an Impression, and Request."
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
    desc: "⬻ shortsword +8 (Agile, Finesse, versatile S) __Damage__ 1d6–1 piercing"
  - name: "Ranged"
    desc: "⬻ dart +8 (Agile, range increment 20 feet, Thrown) __Damage__ 1d4–1 piercing"
abilities_bot:
  - name: "Vengeful Anger"
    desc: "(Emotion, Mental) As long as it isn't frightened, a mitflit gains a +2 status bonus to damage rolls against a creature that has previously damaged or tormented it."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16 - __Cantrips (1st)__ Prestidigitation - __1st__ Bane - __2nd__ Speak with Animals (arthropods only; at will)"
sourcebook: "_Monster Core_, page 180."
```

```encounter-table
name: Mitflit
creatures:
  - 1: Mitflit
```
