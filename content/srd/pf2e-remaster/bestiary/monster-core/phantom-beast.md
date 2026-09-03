---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Phantom Beast"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/ethereal
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/phantom
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Phantom Beast"
level: 8
source: "Monster Core"
aon_id: "creature-3136"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3136"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Phantom Beast"
level: "Creature 8"
size: "Medium"
trait_01: "Ethereal"
trait_02: "Incorporeal"
trait_03: "Phantom"
trait_04: "Spirit"
trait_05: "Uncommon"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision"
languages: "telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Diplomacy +16, Intimidation +18, Occultism +14, Thievery +18"
abilityMods: [-5, 6, 1, 0, 4, 6]
abilities_top:
  - name: "Walk the Ethereal Line"
    desc: "⬺ The phantom walks the thin line between the Ethereal Plane and the Universe in order to exist on both planes simultaneously. They can shift back to solely the Ethereal Plane by using this ability again."
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +13; __Ref__: +18; __Will__: +16 –1 status penalty to all saves vs. death effects"
hp: 120
health:
  - name: "HP"
    desc: "120; __Immunities__ bleed, disease, paralyzed, poison, precision; __Resistances__ all damage 8 (except force, _ghost touch_, or spirit; double resistance vs. non-magical)"
abilities_mid:
  - name: "Susceptible to Death"
    desc: "Though phantoms aren't alive, neither are they undead, and they are uniquely vulnerable to the effects of death. A phantom whose Hit Points are reduced to 0 as a result of a death effect (such as from a spell like _execute_) is immediately whisked away to the River of Souls, where their soul resumes the usual path to the afterlife."
speed: "fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ phantom horn +18 (Agile, Finesse, Magical) __Damage__ 2d8+8 piercing"
abilities_bot:
  - name: "Grab Item"
    desc: "⬻ The phantom beast attempts to Steal one item of up to 1 Bulk from a creature, even if the creature is in combat, though the object still must not be one that is actively in use. If they succeed, they carry the object along with them telekinetically."
  - name: "Phantom Touch"
    desc: "(Spirit) Each time they make a Strike, a phantom can choose to deal spirit damage instead of the normal physical damage type."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 28, attack +20 - __Cantrips (4th)__ Daze, Telekinetic Projectile - __4th__ Phantom Pain, Sleep, Spiritual Armament"
sourcebook: "_Monster Core_, page 263."
```

```encounter-table
name: Phantom Beast
creatures:
  - 1: Phantom Beast
```
