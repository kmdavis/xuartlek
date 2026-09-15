---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4605"
socialImage: og-image.png
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
    desc: "+30; darkvision, [[srd/pf2e/compendium/spells/rank-2/See the Unseen|_see the unseen_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +33, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +31, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +29, [[srd/pf2e/compendium/rules-elements/skills/Lore|Sea Lore]] +33"
abilityMods: [8, 4, 6, 8, 5, 6]
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +31; __Ref__: +25; __Will__: +32 +1 status to all saves vs. magic"
hp: 335
health:
  - name: "HP"
    desc: "335; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]] 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 15"
abilities_mid:
  - name: "Magic-Warping Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]]) 30 feet. A vaspercham's shell distorts nearby magic. Any creature in the aura who Casts a Spell must attempt a DC 37 Will save."
  - name: "Critical Success"
    desc: "The spell is unaffected, and the caster is temporarily immune to the magic-warping aura for 1 minute."
  - name: "Success"
    desc: "The spell is unaffected, but if the spell allows a saving throw, the vaspercham gains a +1 circumstance bonus to save against it."
  - name: "Failure"
    desc: "If the spell has a target and there are one or more viable targets within its range, the spell's target changes, determined randomly by the GM. If there's no other possible target within range or the spell has no target, the spell is [[srd/pf2e/books/player-core/chapter-7-spells/Casting Spells#Disrupted and Lost Spells|disrupted]]."
  - name: "Critical Failure"
    desc: "The caster instead Casts another Spell, choosing randomly from their spell repertoire, prepared spells, or available focus spells (as appropriate) and selecting any targets at random."
speed: "20 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 3d10+16 bludgeoning plus hallucinatory brine"
  - name: "Ranged"
    desc: "⬻ water blast +33 (Brutal, [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], range increment 100 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]]) __Damage__ 2d8+16 bludgeoning plus hallucinatory brine"
abilities_bot:
  - name: "Hallucinatory Brine"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Illusion|illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) A creature hit by the vaspercham's Strikes or Mindwarping Tide must attempt a DC 38 Fortitude save. On a failure, the creature is overwhelmed with phantasmal visions, becoming [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]] for 1 round (1 minute on a critical failure)."
  - name: "Mindwarping Tide"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]]) The vaspercham releases an effusion of noxious water from its shell. Creatures within a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] must save against the vaspercham's hallucinatory brine."
  - name: "Whipping Tentacles"
    desc: "⬺ The vaspercham makes four tentacle Strikes, each against a different target. These attacks count toward the vaspercham's multiple attack penalty, but the multiple attack penalty doesn't increase until after the vaspercham makes all of their attacks. Forbidden Armor After a devastating battle with a vaspercham, many legendary heroes have tried to forge armor or weapons from the sea beast’s magical shell, but all have failed thanks to the powerful curse that suffuses the opaline material. If one were able to dispel the curse of a vaspercham’s shell—or somehow twist the curse to their own benefit—they would be able to craft an incredible suit of _[[srd/pf2e/compendium/equipment/armor/Magic Armor|+2]] [[srd/pf2e/compendium/equipment/runes/Antimagic|antimagic]] [[srd/pf2e/compendium/equipment/armor/Magic Armor|greater resilient]] plate mail_."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 41 - __5th__ [[srd/pf2e/compendium/spells/rank-5/Control Water|Control Water]] (at will) - __6th__ [[srd/pf2e/compendium/spells/rank-6/Spellwrack|Spellwrack]] (×3) - __7th__ [[srd/pf2e/compendium/spells/rank-7/Regenerate|Regenerate]] - __8th__ [[srd/pf2e/compendium/spells/rank-3/Lightning Bolt|Lightning Bolt]] - __9th__ [[srd/pf2e/compendium/spells/rank-4/Dispelling Globe|Dispelling Globe]], [[srd/pf2e/compendium/spells/rank-5/Howling Blizzard|Howling Blizzard]] - __Constant (7th)__ [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]]"
sourcebook: "_Monster Core 2_, page 343."
```

```encounter-table
name: Vaspercham
creatures:
  - 1: Vaspercham
```
