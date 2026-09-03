---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mage Killer"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Mage Killer"
level: 8
source: "NPC Core"
aon_id: "creature-3517"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3517"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mage Killer"
level: "Creature 8"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Arcana +13, Athletics +16, Stealth +18"
abilityMods: [4, 5, 2, 1, 2, 0]
abilities_top:
  - name: "Items"
    desc: "daggers (4), _+1 striking rapier_, Studded Leather Armor"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +16; __Ref__: +17; __Will__: +16"
hp: 145
health:
  - name: "HP"
    desc: "145; __Resistances__ cold 10"
abilities_mid:
  - name: "Spell Dodge"
    desc: "⬲"
  - name: "Trigger"
    desc: "The mage killer is targeted by a spell"
  - name: "Effect"
    desc: "The mage killer gains a +2 circumstance bonus to AC and saving throws against the triggering spell."
  - name: "Spell Interception"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 10 feet of the mage killer Casts a Spell"
  - name: "Effect"
    desc: "The mage killer makes a melee Strike or thrown dagger Strike against the triggering creature. If it hits, the spell is disrupted."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +20 (deadly d8, Disarm, Finesse, Magical) __Damage__ 2d6+10 piercing plus magical static"
  - name: "Melee"
    desc: "⬻ dagger +19 (Agile, Finesse, thrown 10 feet, versatile S) __Damage__ 1d4+10 piercing plus magical static"
  - name: "Melee"
    desc: "⬻ fist +19 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+10 bludgeoning plus magical static"
  - name: "Ranged"
    desc: "⬻ dagger +19 (Agile, Finesse, thrown 10 feet, versatile S) __Damage__ 1d4+10 piercing plus magical static"
abilities_bot:
  - name: "Magical Static"
    desc: "(Arcane, Mental) The mage killer's Strikes deal an additional 1d8 mental damage to a creature that has Cast (or attempted to Cast) a Spell within the last round, and on a critical hit, the creature is stupefied 1 for 1 minute."
  - name: "Shift Energy Runes"
    desc: "⬻ (Arcane, Concentrate)"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "The mage killer alters the magical countermeasures in the runes on their armor. They change their resistance to the energy type of their choice (acid, cold, electricity, fire, force, sonic, vitality, or void)."
  - name: "Sudden Charge"
    desc: "⬺ The mage killer Strides twice. If they end their movement within melee reach of at least one enemy, they can make a melee Strike against it."
sourcebook: "_NPC Core_, page 84."
```

```encounter-table
name: Mage Killer
creatures:
  - 1: Mage Killer
```
