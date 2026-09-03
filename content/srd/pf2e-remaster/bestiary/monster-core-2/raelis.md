---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Raelis"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/azata
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Raelis"
level: 11
source: "Monster Core 2"
aon_id: "creature-4094"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4094"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Raelis"
level: "Creature 11"
size: "Large"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
languages: "Common, Diabolic, Draconic, Empyrean; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Arcana +19, Athletics +19, Deception +20, Occultism +19, Performance +22, Religion +20, Society +21, Stealth +19"
abilityMods: [6, 6, 5, 4, 3, 5]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +21; __Ref__: +24; __Will__: +18"
hp: 200
health:
  - name: "HP"
    desc: "200; __Weaknesses__ cold iron 10, unholy 10"
speed: "40 feet, fly 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +23 (Agile, Finesse, Holy, Magical) __Damage__ 2d6+9 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) The raelis can take on the appearance of any Small or Medium humanoid, or any Medium or smaller animal. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but might change the damage type their Strikes deal."
  - name: "Recount Epic"
    desc: "⬺ (Auditory, Divine, Mental) The raelis recounts a tale to inspire their allies to heroic feats. For the next minute, all allied creatures who heard the epic gain a +1 circumstance bonus to Acrobatics, Athletics, and Performance checks."
  - name: "Siphon Scroll"
    desc: "⬺ (Divine) The raelis Casts a Spell from a scroll within 60 feet that they've read with Word Caller; this scroll must be divine. If this spell has the holy or vitality trait, they Cast it as one spell rank higher. This expends the scroll as normal."
  - name: "Word Caller"
    desc: "⬻ (Concentrate, Divine) The raelis senses the presence of words around them within 60 feet, reading up to 100 pages of nonmagical writing or automatically succeeding at a Recall Knowledge to identify 1 magical scroll."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30, attack +22 - __Cantrips (6th)__ Detect Magic, Divine Lance, Figment, Haunting Hymn, Read Aura, Telekinetic Projectile - __1st__ Bless - __3rd__ Enthrall, Heroism, Lightning Bolt - __4th__ Outcast's Curse, Unfettered Movement - __5th__ Illusory Scene, Temporary Glyph, Translocate - __6th__ Vibrant Pattern, Zealous Conviction - __Constant (4th)__ Unfettered Movement, Veil of Privacy - __Constant (5th)__ Truespeech"
  - name: "Rituals"
    desc: "DC 30 - __3rd__ Rune Trap (doesn't require secondary casters)"
sourcebook: "_Monster Core 2_, page 51."
```

```encounter-table
name: Raelis
creatures:
  - 1: Raelis
```
