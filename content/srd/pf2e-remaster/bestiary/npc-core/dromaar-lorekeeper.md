---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dromaar Lorekeeper"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/dromaar
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/orc
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/half-orc
statblock: inline
name: "Dromaar Lorekeeper"
level: 5
source: "NPC Core"
aon_id: "creature-3664"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3664"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Dromaar Lorekeeper"
level: "Creature 5"
size: "Medium"
trait_01: "Dromaar"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Orc"
trait_05: "Half-Orc"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision"
languages: "Common, Orcish"
skills:
  - name: "Skills"
    desc: "Diplomacy +12, Occultism +11, Orc Lore +15, Performance +12, Society +13"
abilityMods: [1, 3, 0, 2, 2, 3]
abilities_top:
  - name: "Spotlight Ready"
    desc: "When performing for crowds of 10 or more, the dromaar lorekeeper gains a +2 circumstance bonus to their Performance checks."
  - name: "Items"
    desc: "Dagger, lute"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +12; __Will__: +13"
hp: 70
health:
  - name: "HP"
    desc: "70"
abilities_mid:
  - name: "Final Tale"
    desc: "(auditory, mental, occult) When the lorekeeper dies, they utter a brief but poignant final story that shakes those nearby to their core. Each creature in a 10-foot emanation must succeed at a DC 20 Will save or be paralyzed for 1 round."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +14 (Agile, Finesse, versatile S) __Damage__ 1d4+4 piercing plus 1d10 sonic"
  - name: "Melee"
    desc: "⬻ fist +14 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 piercing plus 1d10 sonic"
  - name: "Ranged"
    desc: "⬻ dagger +14 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+4 piercing plus 1d10 sonic"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 22, attack +14 - __Cantrips (3rd)__ Daze, Figment, Message, Summon Instrument, Telekinetic Projectile - __1st__ Bless, Phantasmal Minion, Ventriloquism (3 slots) - __2nd__ Laughing Fit, Noise Blast, Translate (3 slots) - __3rd__ Enthrall, Heroism (2 slots) __a__"
sourcebook: "_NPC Core_, page 207."
```

```encounter-table
name: Dromaar Lorekeeper
creatures:
  - 1: Dromaar Lorekeeper
```
