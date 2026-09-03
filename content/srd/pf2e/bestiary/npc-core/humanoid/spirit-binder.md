---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Spirit Binder"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Spirit Binder"
level: 11
source: "NPC Core"
aon_id: "creature-3543"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3543"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Spirit Binder"
level: "Creature 11"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; spiritsense (imprecise) 60 feet"
languages: "Common, Necril, Shadowtongue"
skills:
  - name: "Skills"
    desc: "Diplomacy +21, Intimidation +21, Occultism +22, Spirits Lore +24"
abilityMods: [1, 3, 3, 5, 4, 6]
abilities_top:
  - name: "Spiritsense"
    desc: "(detection, occult) The spirit binder can sense the spirits of creatures, including living creatures, most non-mindless undead, and haunts within the listed range. Since spiritsense detects spiritual essence, not physical bodies, it can detect spirits projected by spells (such as _project image_) or possessing otherwise soulless objects. It can't detect soulless bodies, constructs, or objects, and like most senses, it doesn't penetrate through solid objects."
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +19; __Ref__: +19; __Will__: +24"
hp: 175
health:
  - name: "HP"
    desc: "175"
abilities_mid:
  - name: "Haunting Spirits"
    desc: "(aura, occult, spirit) 30 feet. The spirits bound by a spirit binder swirl around, lashing out at their foes. An enemy that enters or starts its turn in the aura must succeed at a DC 27 Will save or take 3d6 spirit damage and be frightened 1 (double damage and frightened 2 on a critical failure)."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ghost claw +19 (Finesse, Magical, Spirit, Unarmed) __Damage__ 2d10+6 slashing plus 2d6 spirit"
  - name: "Ranged"
    desc: "⬺ spirit pitch +19 (Magical, range increment 60 feet, Spirit) __Damage__ 3d6 spirit plus 2d6 persistent spirit"
abilities_bot:
  - name: "Spirit Scrying"
    desc: "The spirit binder's scrying spells can target or detect spirits on other planes as though the spirits were in the Universe."
  - name: "Succumb to the Void"
    desc: "⬻ (Concentrate, Occult, Void) The spirit binder taps into the more nefarious spirits of the Void, becoming something morbid and cruel. For 1d4 rounds, their resistance, aura of spirits, Strikes, and spirit spells change their damage type from spirit damage to void damage and replace their spirit trait with the void trait."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 31, attack +23 - __Cantrips (6th)__ Detect Magic, Figment, Telekinetic Hand, Telekinetic Projectile, Void Warp - __1st__ Bane, Command, Fear (3 slots) - __2nd__ Darkness, Ghostly Carrier, Peaceful Rest (3 slots) - __3rd__ Clairaudience, Ghostly Weapon, Levitate (3 slots) - __4th__ Clairvoyance, Fly, Talking Corpse (3 slots) - __5th__ Invoke Spirits, Spiritual Guardian, Wave of Despair (3 slots) - __6th__ Dominate, Spirit Blast (2 slots) - __7th__ Interplanar Teleport (to or from the Ethereal Plane only)"
sourcebook: "_NPC Core_, page 103."
```

```encounter-table
name: Spirit Binder
creatures:
  - 1: Spirit Binder
```
