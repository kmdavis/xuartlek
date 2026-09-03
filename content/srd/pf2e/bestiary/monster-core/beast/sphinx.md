---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sphinx"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Sphinx"
level: 8
source: "Monster Core"
aon_id: "creature-3205"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3205"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sphinx"
level: "Creature 8"
size: "Large"
trait_01: "Beast"
trait_02: "Humanoid"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision"
languages: "Common, Draconic, Sphinx; _truespeech_"
skills:
  - name: "Skills"
    desc: "Arcana +17, Athletics +18, Bardic Lore +19, Deception +16, Diplomacy +16, Intimidation +18, Occultism +17"
abilityMods: [6, 1, 3, 5, 4, 4]
abilities_top:
  - name: "Bardic Lore"
    desc: "Sphinxes are naturally curious, and their love of puzzles and mysteries leads them to gather information on a broad range of topics. Sphinxes have Bardic Lore, a special Lore skill that can be used only to Recall Knowledge, but on any topic."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +14; __Will__: +19"
hp: 135
health:
  - name: "HP"
    desc: "135"
speed: "35 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +20 (Agile) __Damage__ 2d6+9 slashing"
abilities_bot:
  - name: "Claw Rake"
    desc: "⬽ The sphinx rears back on their hind legs and makes two claw Strikes at the same target, using the same attack bonus as their highest melee attack. If both attacks deal damage, the target takes extra damage equal to one claw Strike."
  - name: "Pounce"
    desc: "⬻ The sphinx Strides and makes a Strike at the end of that movement. If the sphinx began this action hidden, they remain hidden until after the attack."
  - name: "Riddler's Rune"
    desc: "Once per week, a Sphinx can create a magical symbol as the _rune trap_ ritual. The sphinx usually shapes it to take the form of a written riddle and sets the password to the answer. A creature that gives the wrong answer or tries to pass without answering must succeed at a DC 26 Will save or be affected by one of the following spells, chosen by the sphinx when creating the symbol: _synaptic pulse_ (5th), _charm_ (4th), _fear_ (4th), _phantom pain_ (4th), _sleep_ (4th). The sphinx learns the identity of any creature that answers the riddle and tends to be friendly to them if they answered correctly. Sphinx Riddles Sphinxes are well known for their love of riddles, a love that often moves into the realm of obsession. A would-be foe who can answer a sphinx's favorite riddles—or better yet, can stump the sphinx with a crafty and creative riddle of their own—can often avoid combat with the creature and even secure their aid."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 27 - __Cantrips (4th)__ Detect Magic - __2nd__ See the Unseen - __3rd__ Dispel Magic, Locate - __4th__ Clairaudience (at will), Clairvoyance (at will), Cleanse Affliction, Read Omens - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core_, page 319."
```

```encounter-table
name: Sphinx
creatures:
  - 1: Sphinx
```
