---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vaspercham"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/huge
statblock: inline
name: "Vaspercham"
level: 17
source: "Monster Core 2"
aon_id: "creature-4605"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4605"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Vaspercham"
level: "Creature 17"
size: "Huge"
trait_01: "Aberration"
trait_02: "Aquatic"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision, [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|_see the unseen_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +33, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +31, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +29, [[srd/pf2e/compendium/rules-elements/skills/lore|Sea Lore]] +33"
abilityMods: [8, 4, 6, 8, 5, 6]
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +31; __Ref__: +25; __Will__: +32 +1 status to all saves vs. magic"
hp: 335
health:
  - name: "HP"
    desc: "335; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 15"
abilities_mid:
  - name: "Magic-Warping Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]]) 30 feet. A vaspercham's shell distorts nearby magic. Any creature in the aura who Casts a Spell must attempt a DC 37 Will save."
  - name: "Critical Success"
    desc: "The spell is unaffected, and the caster is temporarily immune to the magic-warping aura for 1 minute."
  - name: "Success"
    desc: "The spell is unaffected, but if the spell allows a saving throw, the vaspercham gains a +1 circumstance bonus to save against it."
  - name: "Failure"
    desc: "If the spell has a target and there are one or more viable targets within its range, the spell's target changes, determined randomly by the GM. If there's no other possible target within range or the spell has no target, the spell is [[srd/pf2e/books/player-core/chapter-7-spells/casting-spells#Disrupted and Lost Spells|disrupted]]."
  - name: "Critical Failure"
    desc: "The caster instead Casts another Spell, choosing randomly from their spell repertoire, prepared spells, or available focus spells (as appropriate) and selecting any targets at random."
speed: "20 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d10+16 bludgeoning plus hallucinatory brine"
  - name: "Ranged"
    desc: "⬻ water blast +33 (Brutal, [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], range increment 100 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]]) __Damage__ 2d8+16 bludgeoning plus hallucinatory brine"
abilities_bot:
  - name: "Hallucinatory Brine"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/illusion|illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) A creature hit by the vaspercham's Strikes or Mindwarping Tide must attempt a DC 38 Fortitude save. On a failure, the creature is overwhelmed with phantasmal visions, becoming [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] for 1 round (1 minute on a critical failure)."
  - name: "Mindwarping Tide"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The vaspercham releases an effusion of noxious water from its shell. Creatures within a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] must save against the vaspercham's hallucinatory brine."
  - name: "Whipping Tentacles"
    desc: "⬺ The vaspercham makes four tentacle Strikes, each against a different target. These attacks count toward the vaspercham's multiple attack penalty, but the multiple attack penalty doesn't increase until after the vaspercham makes all of their attacks. Forbidden Armor After a devastating battle with a vaspercham, many legendary heroes have tried to forge armor or weapons from the sea beast’s magical shell, but all have failed thanks to the powerful curse that suffuses the opaline material. If one were able to dispel the curse of a vaspercham’s shell—or somehow twist the curse to their own benefit—they would be able to craft an incredible suit of _[[srd/pf2e/compendium/equipment/armor/magic-armor-3-major-resilient|+2]] [[srd/pf2e/compendium/equipment/runes/antimagic|antimagic]] [[srd/pf2e/compendium/equipment/armor/magic-armor-3-major-resilient|greater resilient]] plate mail_."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 41 - __5th__ [[srd/pf2e/compendium/spells/rank-5/control-water|Control Water]] (at will) - __6th__ [[srd/pf2e/compendium/spells/rank-6/spellwrack|Spellwrack]] (×3) - __7th__ [[srd/pf2e/compendium/spells/rank-7/regenerate|Regenerate]] - __8th__ [[srd/pf2e/compendium/spells/rank-3/lightning-bolt|Lightning Bolt]] - __9th__ [[srd/pf2e/compendium/spells/rank-4/dispelling-globe|Dispelling Globe]], [[srd/pf2e/compendium/spells/rank-5/howling-blizzard|Howling Blizzard]] - __Constant (7th)__ [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]]"
sourcebook: "_Monster Core 2_, page 343."
```

```encounter-table
name: Vaspercham
creatures:
  - 1: Vaspercham
```
