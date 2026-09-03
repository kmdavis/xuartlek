---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bone Mother"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/ratfolk
  - pf2e/creature/trait/small
statblock: inline
name: "Bone Mother"
level: 6
source: "NPC Core"
aon_id: "creature-3669"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3669"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Bone Mother"
level: "Creature 6"
size: "Small"
trait_01: "Humanoid"
trait_02: "Ratfolk"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; low-light vision"
languages: "Common, Requian, Sakvroth, Ysoki"
skills:
  - name: "Skills"
    desc: "Deception +14, Fortune-Telling Lore +16, Intimidation +14, Medicine +13, Occultism +16, Performance +14, Religion +13, Society +12"
abilityMods: [0, 3, 0, 2, 3, 4]
abilities_top:
  - name: "Items"
    desc: "bones for fortune telling, _+1 dagger_"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +13; __Will__: +15"
hp: 80
health:
  - name: "HP"
    desc: "80"
abilities_mid:
  - name: "Rattling Bones"
    desc: "⬲ (occult, spirit)"
  - name: "Trigger"
    desc: "The bone mother or another ratfolk in their square takes damage from a melee Strike"
  - name: "Effect"
    desc: "Spirits from the bones emerge to deal 2d6 spirit damage to the attacker with a DC 24 basic Will save."
speed: "25 feet; swarming"
attacks:
  - name: "Melee"
    desc: "⬻ _dagger_ +16 (Agile, Finesse, versatile S) __Damage__ 1d4+6 piercing plus 1d10 spirit"
  - name: "Melee"
    desc: "⬻ jaws +15 (Agile, Finesse) __Damage__ 1d4+6 piercing plus 1d10 spirit"
  - name: "Ranged"
    desc: "⬻ _dagger_ +16 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+6 piercing plus 1d10 spirit"
abilities_bot:
  - name: "Swarming"
    desc: "A ysoki can end their movement in the same square as an ally that also has this ability. Only two such creatures can share the same space."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 24, attack +16 - __Cantrips (3rd)__ Daze, Detect Magic, Guidance, Light, Telekinetic Projectile - __1st__ Bless, Command, Mindlink, Sanctuary (4 slots) - __2nd__ Augury, Cleanse Affliction, Dispel Magic, Translate (4 slots) - __3rd__ Enthrall, Haste, Paralyze, Ring of Truth (4 slots)"
sourcebook: "_NPC Core_, page 211."
```

```encounter-table
name: Bone Mother
creatures:
  - 1: Bone Mother
```
