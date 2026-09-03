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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], Sphinx; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +17, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, Bardic Lore +19, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +16, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +16, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +18, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +17"
abilityMods: [6, 1, 3, 5, 4, 4]
abilities_top:
  - name: "Bardic Lore"
    desc: "Sphinxes are naturally curious, and their love of puzzles and mysteries leads them to gather information on a broad range of topics. Sphinxes have Bardic Lore, a special [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] skill that can be used only to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]], but on any topic."
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
    desc: "⬻ claw +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+9 slashing"
abilities_bot:
  - name: "Claw Rake"
    desc: "⬽ The sphinx rears back on their hind legs and makes two claw Strikes at the same target, using the same attack bonus as their highest melee attack. If both attacks deal damage, the target takes extra damage equal to one claw Strike."
  - name: "Pounce"
    desc: "⬻ The sphinx Strides and makes a Strike at the end of that movement. If the sphinx began this action [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], they remain hidden until after the attack."
  - name: "Riddler's Rune"
    desc: "Once per week, a Sphinx can create a magical symbol as the [[srd/pf2e/compendium/spells/rituals/rune-trap|_rune trap_]] ritual. The sphinx usually shapes it to take the form of a written riddle and sets the password to the answer. A creature that gives the wrong answer or tries to pass without answering must succeed at a DC 26 Will save or be affected by one of the following spells, chosen by the sphinx when creating the symbol: [[srd/pf2e/compendium/spells/rank-5/synaptic-pulse|_synaptic pulse_]] (5th), [[srd/pf2e/compendium/spells/rank-1/charm|_charm_]] (4th), [[srd/pf2e/compendium/spells/rank-1/fear|_fear_]] (4th), [[srd/pf2e/compendium/spells/rank-1/phantom-pain|_phantom pain_]] (4th), [[srd/pf2e/compendium/spells/rank-1/sleep|_sleep_]] (4th). The sphinx learns the identity of any creature that answers the riddle and tends to be friendly to them if they answered correctly. Sphinx Riddles Sphinxes are well known for their love of riddles, a love that often moves into the realm of obsession. A would-be foe who can answer a sphinx's favorite riddles—or better yet, can stump the sphinx with a crafty and creative riddle of their own—can often avoid combat with the creature and even secure their aid."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 27 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]] - __3rd__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-3/locate|Locate]] - __4th__ [[srd/pf2e/compendium/spells/rank-3/clairaudience|Clairaudience]] (at will), [[srd/pf2e/compendium/spells/rank-4/clairvoyance|Clairvoyance]] (at will), [[srd/pf2e/compendium/spells/rank-2/cleanse-affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-4/read-omens|Read Omens]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 319."
```

```encounter-table
name: Sphinx
creatures:
  - 1: Sphinx
```
