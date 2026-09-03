---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ghost Mage"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/ghost
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Ghost Mage"
level: 10
source: "Monster Core"
aon_id: "creature-3008"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3008"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ghost Mage"
level: "Creature 10"
size: "Medium"
trait_01: "Ghost"
trait_02: "Incorporeal"
trait_03: "Spirit"
trait_04: "Undead"
trait_05: "Unholy"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
languages: "Common, Draconic"
skills:
  - name: "Skills"
    desc: "Arcana +22, Intimidation +22, Stealth +21"
abilityMods: [-5, 3, 0, 6, 3, 6]
abilities_top:
  - name: "Site Bound"
    desc: ""
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +19; __Will__: +22"
hp: 135
health:
  - name: "HP"
    desc: "135 (rejuvenation, void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, precision, unconscious; __Resistances__ all damage 10 (except force, _ghost touch_, spirit, or vitality; double resistance vs. non-magical)"
abilities_mid:
  - name: "Rejuvenation"
    desc: "(divine) Completing the ghost mage's project allows it to move on to the afterlife."
speed: "fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ghostly hand +21 (Agile, Finesse, Magical) __Damage__ 2d8+12 void"
abilities_bot:
  - name: "Frightful Moan"
    desc: "⬻ (Auditory, Divine, Emotion, Fear, Mental) The ghost laments its fate, forcing each living creature within 30 feet to attempt a DC 29 Will save. On a failure, a creature becomes frightened 2 (or frightened 3 on a critical failure). On a success, a creature is temporarily immune to this ghost's frightful moan for 1 minute."
  - name: "Telekinetic Assault"
    desc: "⬺ (Divine) The ghost cries out in pain and anguish as small objects and debris fly about in a 30-foot emanation. Creatures in this area take 6d6 bludgeoning damage, with a DC 29 basic Reflex save. Building Ghosts Note that the ghost mage is built from the ground up, rather than by applying the ghost rules to a once-living creature, so its numbers don't exactly match the values listed under Creating a Ghost. This is usually the better way to go if you have the time, as it allows you to hand-craft a ghost for the situation."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 29, attack +23 - __Cantrips (5th)__ Detect Magic, Figment, Prestidigitation, Read Aura, Telekinetic Hand - __1st__ Enfeeble (×2) - __2nd__ Telekinetic Maneuver (×2) - __3rd__ Blindness, Dispel Magic, Veil of Privacy - __4th__ Suggestion, Vision of Death - __5th__ Hallucination, Howling Blizzard"
sourcebook: "_Monster Core_, page 161."
```

```encounter-table
name: Ghost Mage
creatures:
  - 1: Ghost Mage
```
