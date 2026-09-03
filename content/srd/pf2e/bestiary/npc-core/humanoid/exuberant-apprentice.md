---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Exuberant Apprentice"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Exuberant Apprentice"
level: 4
source: "NPC Core"
aon_id: "creature-3591"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3591"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Exuberant Apprentice"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Academia Lore +10, Arcana +12, Library Lore +12"
abilityMods: [1, 2, 2, 4, -2, 4]
abilities_top:
  - name: "Items"
    desc: "late homework assignment, spellbook, textbooks, Writing Set"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +10; __Ref__: +10; __Will__: +8"
hp: 65
health:
  - name: "HP"
    desc: "65"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ textbook +12 __Damage__ 1d6+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +13 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+5 bludgeoning"
abilities_bot:
  - name: "Overambitious Spell"
    desc: "⬺ (arcane"
  - name: "Frequency"
    desc: "once per day)"
  - name: "Effect"
    desc: "The exuberant apprentice's teacher has told them they're not ready for this spell, but desperate times call for desperate measures. The exuberant apprentice attempts to cast _fireball_ as a 3rd-rank arcane spell but must first attempt a DC 11 flat check."
  - name: "Critical Success"
    desc: "The spell is cast flawlessly and heightened to 4th rank. The apprentice is stunned 2 from sheer shock."
  - name: "Success"
    desc: "Nothing goes wrong, and the spell is cast normally."
  - name: "Failure"
    desc: "The spell fizzles and creates only a harmless puff of smoke."
  - name: "Critical Failure"
    desc: "Academic ablaze! The apprentice takes 6d6 fire damage as the magic backfires."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 21, attack +13 - __Cantrips (2nd)__ Detect Magic, Frostbite, Prestidigitation, Read Aura, Telekinetic Hand - __1st__ Force Barrage, Grease, Gust of Wind, Phantasmal Minion - __2nd__ Acid Grip, Darkvision, Revealing Light"
sourcebook: "_NPC Core_, page 140."
```

```encounter-table
name: Exuberant Apprentice
creatures:
  - 1: Exuberant Apprentice
```
