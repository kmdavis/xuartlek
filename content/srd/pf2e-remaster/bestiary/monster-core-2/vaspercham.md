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
    desc: "Perception +30; darkvision, _see the unseen_"
languages: "Aklo"
skills:
  - name: "Skills"
    desc: "Arcana +33, Athletics +33, Deception +31, Intimidation +29, Sea Lore +33"
abilityMods: [8, 4, 6, 8, 5, 6]
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +31; __Ref__: +25; __Will__: +32 +1 status to all saves vs. magic"
hp: 335
health:
  - name: "HP"
    desc: "335; __Resistances__ cold 10, electricity 10; __Weaknesses__ fire 15"
abilities_mid:
  - name: "Magic-Warping Aura"
    desc: "(arcane, aura) 30 feet. A vaspercham's shell distorts nearby magic. Any creature in the aura who Casts a Spell must attempt a DC 37 Will save."
  - name: "Critical Success"
    desc: "The spell is unaffected, and the caster is temporarily immune to the magic-warping aura for 1 minute."
  - name: "Success"
    desc: "The spell is unaffected, but if the spell allows a saving throw, the vaspercham gains a +1 circumstance bonus to save against it."
  - name: "Failure"
    desc: "If the spell has a target and there are one or more viable targets within its range, the spell's target changes, determined randomly by the GM. If there's no other possible target within range or the spell has no target, the spell is disrupted."
  - name: "Critical Failure"
    desc: "The caster instead Casts another Spell, choosing randomly from their spell repertoire, prepared spells, or available focus spells (as appropriate) and selecting any targets at random."
speed: "20 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +33 (Agile, magical, reach 20 feet) __Damage__ 3d10+16 bludgeoning plus hallucinatory brine"
  - name: "Ranged"
    desc: "⬻ water blast +33 (Brutal, magical, range increment 100 feet, water) __Damage__ 2d8+16 bludgeoning plus hallucinatory brine"
abilities_bot:
  - name: "Hallucinatory Brine"
    desc: "(Arcane, illusion, mental) A creature hit by the vaspercham's Strikes or Mindwarping Tide must attempt a DC 38 Fortitude save. On a failure, the creature is overwhelmed with phantasmal visions, becoming confused for 1 round (1 minute on a critical failure)."
  - name: "Mindwarping Tide"
    desc: "⬻ (Concentrate) The vaspercham releases an effusion of noxious water from its shell. Creatures within a 15-foot emanation must save against the vaspercham's hallucinatory brine."
  - name: "Whipping Tentacles"
    desc: "⬺ The vaspercham makes four tentacle Strikes, each against a different target. These attacks count toward the vaspercham's multiple attack penalty, but the multiple attack penalty doesn't increase until after the vaspercham makes all of their attacks. Forbidden Armor After a devastating battle with a vaspercham, many legendary heroes have tried to forge armor or weapons from the sea beast’s magical shell, but all have failed thanks to the powerful curse that suffuses the opaline material. If one were able to dispel the curse of a vaspercham’s shell—or somehow twist the curse to their own benefit—they would be able to craft an incredible suit of _+2 antimagic greater resilient plate mail_."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 41 - __5th__ Control Water (at will) - __6th__ Spellwrack (×3) - __7th__ Regenerate - __8th__ Lightning Bolt - __9th__ Dispelling Globe, Howling Blizzard - __Constant (7th)__ See the Unseen"
sourcebook: "_Monster Core 2_, page 343."
```

```encounter-table
name: Vaspercham
creatures:
  - 1: Vaspercham
```
