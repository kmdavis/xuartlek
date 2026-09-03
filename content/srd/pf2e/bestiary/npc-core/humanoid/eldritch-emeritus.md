---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Eldritch Emeritus"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Eldritch Emeritus"
level: 17
source: "NPC Core"
aon_id: "creature-3596"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3596"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Eldritch Emeritus"
level: "Creature 17"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 32
perception:
  - name: "Perception"
    desc: "Perception +32"
languages: "Common, Draconic; up to 6 additional languages"
skills:
  - name: "Skills"
    desc: "Academia Lore +30, Arcana +36, Intimidation +30, Nature +33, Occultism +33, Religion +33"
abilityMods: [4, 4, 4, 8, 1, -1]
abilities_top:
  - name: "Items"
    desc: "somewhat disheveled _accolade robe_, spellbook, _+2 greater striking major staff of fire_"
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +27; __Ref__: +27; __Will__: +32"
hp: 290
health:
  - name: "HP"
    desc: "290; __Resistances__ acid 10, cold 10, electricity 10, fire 10, force 10, sonic 10, vitality 10, void 10"
abilities_mid:
  - name: "Counterspell"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature casts a spell the eldritch emeritus has prepared."
  - name: "Effect"
    desc: "The emeritus expends a prepared spell to counter the triggering creature's casting of that same spell. The emeritus loses their spell slot as if they had cast the triggering spell. The emeritus then attempts to counteract the triggering spell."
  - name: "Third Contingent Sequencer"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "A creature attacks or uses a spell or ability that would affect the eldritch emeritus"
  - name: "Effect"
    desc: "A masterpiece of complex spellwork instantly takes shape, casting _fire shield_, _mislead_, and _mountain resilience_ on the eldritch emeritus, each as an 8th-rank arcane spell."
speed: "25 feet, teleport 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +31 (Magical, two-hand d8) __Damage__ 3d4+14 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +30 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+14 bludgeoning"
  - name: "Ranged"
    desc: "⬻ arcane beam +31 (Arcane, Fire, Magical) __Damage__ 6d6+10 fire"
abilities_bot:
  - name: "Didactic Arcanism"
    desc: "(Arcane, Magical)"
  - name: "Requirement"
    desc: "The eldritch emeritus has seen a creature Cast a Spell of 7th rank or lower during the previous round, that spell takes between one and three actions to cast, and that spell is on the arcane spell list"
  - name: "Effect"
    desc: "The eldritch emeritus mastered that spell 30 years ago, and is happy to show how a real master does it. The emeritus Casts the same Spell but heightened to 8th rank. Didactic Arcanism uses the same number of actions as the original spell took to cast."
  - name: "Steady Spellcasting"
    desc: "If a reaction would disrupt the eldritch emeritus's spellcasting action, the eldritch emeritus attempts a DC 15 flat check. On a success, the action isn't disrupted."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 38, attack +30 - __Cantrips (9th)__ Detect Magic, Light, Prestidigitation, Sigil, Telekinetic Hand - __1st__ Fleet Step (x2), Sure Strike - __2nd__ Gecko Grip, Translate, Water Walk - __3rd__ Earthbind, Haste, Locate - __4th__ Creation, Dispel Magic, Fly - __5th__ Banishment, Howling Blizzard, Slither - __6th__ Disintegrate, Teleport, Wall of Force - __7th__ Chain Lightning (×2), Project Image - __8th__ Earthquake, Quandary (×2) - __9th__ Detonate Magic, Falling Stars - __Constant (9th)__ Energy Aegis"
sourcebook: "_NPC Core_, page 143."
```

```encounter-table
name: Eldritch Emeritus
creatures:
  - 1: Eldritch Emeritus
```
